from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

# Collector for all tool outputs per query
collected_outputs = []

# Save tool (saves all collected outputs at once)
def save_wrapper(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    combined_text = "\n\n".join(collected_outputs)
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{combined_text}\n\n"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_text_to_file",
    func=save_wrapper,
    description="Saves all research tool outputs to a text file."
)

# DuckDuckGo search
search = DuckDuckGoSearchRun()
def search_wrapper(query: str) -> str:
    result = search.run(query)
    collected_outputs.append(f"Search Result:\n{result}")
    return result

search_tool = Tool(
    name="search",
    func=search_wrapper,
    description="Search the web for information"
)

# Wikipedia search
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)
def wiki_wrapper(query: str) -> str:
    result = wiki.run(query)
    collected_outputs.append(f"Wikipedia Result:\n{result}")
    return result

wiki_tool = Tool(
    name="wikipedia",
    func=wiki_wrapper,
    description="Query Wikipedia for relevant information"
)
