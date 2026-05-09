# POC Demo Guide

## 1. Demo Goal

The goal of the demo is to show that this is an end-to-end AI Engineer POC, not only a prompt.

You should prove:

- the backend runs
- the UI runs
- a user can ask a question
- a user can generate test cases
- the response uses local context
- the output is structured
- the mock-first design is intentional
- the architecture can be explained clearly

## 2. Before The Demo

Start in:

```text
22-final-poc-project/ai-engineer-poc-qa-assistant
```

Prepare two terminals.

Terminal 1 runs FastAPI:

```powershell
.\.venv\Scripts\Activate.ps1
uvicorn backend.main:app --reload
```

Terminal 2 runs Streamlit:

```powershell
.\.venv\Scripts\Activate.ps1
streamlit run frontend/app.py
```

Open these URLs:

```text
FastAPI docs: http://127.0.0.1:8000/docs
Streamlit UI: http://localhost:8501
Health check: http://127.0.0.1:8000/health
```

## 3. Live Demo Flow

Step 1:

Show `/health`.

Say:

```text
This confirms the FastAPI backend is running.
```

Step 2:

Show `/docs`.

Say:

```text
FastAPI automatically documents the REST endpoints. The main endpoints are /ask and /generate-test-cases.
```

Step 3:

Open Streamlit.

Say:

```text
This is the simple demo UI. It sends HTTP requests to the FastAPI backend.
```

Step 4:

In Ask Knowledge Base, enter:

```text
What should be tested for login?
```

Say:

```text
The backend retrieves local context from the requirement notes and returns a mock answer with the context used.
```

Step 5:

In Generate Test Cases, enter:

```text
User can reset password using registered email
```

Say:

```text
The workflow retrieves context, calls helper tool data, generates positive and negative test cases, and returns structured JSON.
```

Step 6:

Point to `mode: mock`.

Say:

```text
Mock mode is intentional. It lets the POC run without paid API keys and proves the architecture before adding provider complexity.
```

## 4. Two-Minute Script

Problem:

```text
QA teams often need to understand requirements and create first-draft test coverage quickly. Doing that manually from notes can take time.
```

Solution:

```text
I built an AI QA Knowledge Assistant and Test Case Generator. It answers questions from local requirement notes and creates starter test cases.
```

Architecture:

```text
The user enters a question in Streamlit. Streamlit sends a REST request to FastAPI. Pydantic validates the input. A LangGraph-style workflow controls the flow. RAG retrieves local context. An MCP-style tool provides helper data. A mock LLM generates the answer. FastAPI returns JSON and Streamlit displays it.
```

Live flow:

```text
I check /health, open the API docs, then use Streamlit to ask a question and generate test cases from a password reset requirement.
```

Business value:

```text
The business value is faster QA analysis and faster first-draft test coverage.
```

Technical value:

```text
The technical value is that the POC demonstrates API design, validation, RAG, tool integration, workflow orchestration, UI integration, Docker, and Kubernetes awareness.
```

## 5. Stand-And-Deliver Version

Use this if you are asked to explain without running the app:

```text
This POC is an AI QA Knowledge Assistant and Test Case Generator. The user enters a question or requirement in Streamlit. Streamlit calls FastAPI through REST endpoints. Pydantic validates the input. A LangGraph-style workflow controls the steps: understand the request, retrieve context, call a helper tool, generate mock output, and review the result. RAG retrieves relevant lines from local requirement notes. The MCP-style tool provides controlled helper data like users and status codes. The backend returns structured JSON. Docker and Kubernetes files show how the backend could be packaged and deployed. In production I would add authentication, real LLM integration, vector search, secrets management, monitoring, and automated tests.
```

## 6. Expected Output To Show

Health output:

```json
{
  "status": "ok"
}
```

Generate test cases output should include:

```text
requirement
test_cases
context_used
mode
```

Each test case should include:

```text
title
type
priority
expected_result
```

## 7. Common Demo Recovery

If Streamlit shows a backend connection error:

```text
Check that FastAPI is still running on port 8000.
```

If FastAPI returns 422:

```text
Enter a non-empty question or requirement.
```

If the audience asks why the answer is simple:

```text
This is mock-first. The demo is proving architecture and integration. A real LLM can replace the generator step later.
```

If asked whether this is production-ready:

```text
No. It is a POC. Production would require authentication, secrets management, provider integration, monitoring, tests, scaling, and stronger retrieval.
```
