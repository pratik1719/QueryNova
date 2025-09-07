# QueryNova

**An AI-powered research assistant that generates structured research summaries using web search, Wikipedia, and advanced LLMs.**

---

## Overview

QueryNova leverages **Groq’s LLM (`llama-3.3-70b-versatile`)** to provide:

* Intelligent research summaries.
* Automated web and Wikipedia searches.
* Structured outputs with topic, summary, sources, and tools used.
* Optional saving of all research outputs to a text file.

QueryNova is perfect for students, researchers, and anyone looking to automate research tasks efficiently.

---

## Features

* **Multi-tool integration**: DuckDuckGo + Wikipedia + custom save tool.
* **Structured output**: Pydantic model ensures clean JSON-like responses.
* **Single-entry file saving**: Collects all intermediate results and saves once per query.
* **Configurable via `.env`**: Keep your Groq API key safe.

---

## Project Structure

```
QueryNova/
├── main.py              # Entry point
├── tools.py             # Custom tools: search, Wikipedia, save
├── .env                 # Groq API key (ignored in git)
├── requirements.txt     # Dependencies
├── research_output.txt  # Saved research outputs (ignored in git)
└── README.md            # Project documentation
```

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/QueryNova.git
cd QueryNova
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root with your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

> **Note:** `.env` is in `.gitignore` so it won’t be pushed to GitHub.

### 5. Run QueryNova

```bash
python3 main.py
```

* Enter your research query, e.g., `How do I get an entry level job at Netflix?`
* The assistant will search, summarize, and optionally save results.

---

## Example Output

Console summary:

```
--- Research Summary ---
Topic: Getting an entry level job at Netflix
Summary: To get an entry level job at Netflix, research the company, apply through official channels, and prepare for the interview process. Relevant skills, education, and teamwork skills are important.
Sources: Netflix website, Indeed.com, Glassdoor.com
Tools used: search, wikipedia, save_text_to_file
```

Saved in `research_output.txt` with timestamp for reference.

---

## Dependencies

* `langchain`
* `langchain-groq`
* `langchain-anthropic` (optional if Anthropic models are used)
* `langchain-openai` (optional if OpenAI models are used)
* `pydantic`
* `python-dotenv`
* `ddgs` (for DuckDuckGo search)

Install via:

```bash
pip install -r requirements.txt
```

---

## Security / Best Practices

* Keep `.env` secret.
* `venv/` and `research_output.txt` are ignored in Git.
* Do not commit API keys or sensitive data.

---



