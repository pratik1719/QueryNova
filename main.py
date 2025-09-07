import os
from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool, collected_outputs

# Load API key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env!")

os.environ["GROQ_API_KEY"] = groq_api_key

# Structured response model
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that helps generate research summaries.
            Answer the user query and use necessary tools.
            Wrap the output in this format and provide no other text:\n{format_instructions}
            """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [search_tool, wiki_tool, save_tool]

# Initialize agent
agent = create_tool_calling_agent(
    llm=ChatGroq(
        model="llama-3.3-70b-versatile",
        api_key=groq_api_key,
        temperature=0.7,
        max_tokens=512
    ),
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run query
query = input("What can I help you research? ")

# Clear previous outputs
collected_outputs.clear()

raw_response = agent_executor.invoke({"query": query})

# Parse structured response
try:
    structured_response = parser.parse(raw_response.get("output")[0]["text"])
    
    # Print clean summary
    print("\n--- Research Summary ---")
    print(f"Topic: {structured_response.topic}")
    print(f"Summary: {structured_response.summary}")
    print(f"Sources: {', '.join(structured_response.sources)}")
    print(f"Tools used: {', '.join(structured_response.tools_used)}")
    
except Exception as e:
    print("Error parsing response:", e)
    print("Raw Response -", raw_response)
