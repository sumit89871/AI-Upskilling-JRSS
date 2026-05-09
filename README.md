# AI Engineer JRSS Reskilling Course

This repository is a beginner-to-interview-ready self-study course for the target role:

**AI Engineer / Technical Consultant AI Integration**

The course is designed for learners preparing for:

- AI Engineer reskilling programs
- Mettl-style technical screening
- programming assessments
- SME-led technical labs
- POC demos
- interview-style technical discussions

The goal is practical readiness, not academic theory. Every module explains what to build, why it matters, how the syntax works, how to run examples, and where the topic appears in real AI engineering work.

## Who This Is For

Use this course if you are starting from a beginner level and need a structured path into Python, APIs, GenAI, RAG, MCP, LangGraph, agents, deployment, and final POC delivery.

You do not need to know everything before starting. The notes explain beginner assumptions directly.

## What You Will Learn

By the end, you should be comfortable with:

- Python programming from basics to practical advanced usage
- Python patterns used in GenAI and agentic AI
- REST APIs and FastAPI
- Pydantic validation and structured output
- LLM fundamentals and prompt engineering
- OpenAI and Gemini API usage from Python
- RAG, embeddings, vector databases, and LangChain basics
- MCP and FastMCP tool servers
- LangGraph stateful workflows
- agents and multi-agent systems
- local models with Ollama and Hugging Face basics
- Docker and Kubernetes basics
- Streamlit demo apps
- final POC preparation and interview explanation

## Recommended Study Order

Follow [00-course-roadmap.md](./00-course-roadmap.md).

Do not jump directly to agents or RAG if Python, REST APIs, and Pydantic are weak. Most GenAI bugs are normal programming bugs hidden behind AI terminology.

## Repository Structure

```text
ai-engineer-jrss-reskilling-course/
  README.md
  00-course-roadmap.md
  01-environment-setup/
  02-python-beginner-to-advanced/
  03-python-for-genai-agentic-ai/
  04-git-version-control/
  05-rest-api-fundamentals/
  06-fastapi/
  07-pydantic/
  08-llm-fundamentals/
  09-prompt-engineering/
  10-openai-gemini-api-python/
  11-rag-langchain-vector-db/
  12-mcp-fastmcp/
  13-langgraph-stateful-agents/
  14-agents-multi-agent-systems/
  15-local-models-ollama-huggingface/
  16-docker-basics/
  17-kubernetes-basics/
  18-streamlit-app-lab/
  19-langflow-basics/
  20-mcp-context-forge-local-model/
  21-ibm-ai-engineer-awareness/
  22-final-poc-project/
  23-mettl-screening-prep/
  24-interview-prep/
  25-cheatsheets/
  26-practice-tracker/
  27-glossary/
```

The first generation step creates the root files and modules `01` to `03`. Later generation steps should continue from module `04` in order.

## How To Use This Course

1. Read each module README first.
2. Study topic files in the given order.
3. Run the examples locally.
4. Complete exercises before reading interview questions.
5. Maintain your own notes on mistakes and commands.
6. Build the final POC only after finishing the foundation modules.

## Command Explanation Standard

Whenever a command appears, the notes explain the parts.

Example:

```powershell
python -m venv .venv
```

- `python` runs the Python interpreter.
- `-m` means run a Python module as a command.
- `venv` is the built-in module that creates virtual environments.
- `.venv` is the folder where the environment files are created.

## Code Explanation Standard

Whenever code appears, the course explains:

- file name
- where to create the file
- full code
- important lines
- how to run it
- expected output
- common errors
- how it connects to AI Engineer work

## Important Rules

- Never hardcode real API keys.
- Prefer mock LLM examples first.
- Learn local-only execution before cloud or production deployment.
- Keep projects Git-ready from the beginning.
- Treat every error message as debugging practice.

