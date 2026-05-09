# 22 Final POC Project

## 1. What This Module Is

This module is the final proof-of-concept project for the course.

POC name:

```text
ai-engineer-poc-qa-assistant
```

POC use case:

```text
AI QA Knowledge Assistant + Test Case Generator
```

The project shows how an AI Engineer can connect a user interface, an API backend, validation models, retrieval logic, a tool layer, a workflow layer, and deployment files into one small runnable demo.

This is not meant to be a large production system. It is a beginner-demo-ready project that proves you understand how the parts of an AI application fit together.

## 2. What The Project Does

The POC helps a QA learner or QA engineer do two things:

- ask questions about local requirement notes
- generate simple test cases from a requirement

Example user question:

```text
What should be tested for password reset?
```

Example requirement:

```text
User should be able to reset password using a registered email address.
```

The application reads local notes from the `data/` folder, finds relevant context, uses a mock LLM-style generator, adds helper data from a tool function, and returns structured output through FastAPI and Streamlit.

## 3. Why This Is A Good AI Engineer Reskilling POC

This POC is useful because it is small enough to understand but broad enough to discuss in an interview.

It demonstrates:

- Python backend programming
- REST API design
- Pydantic request and response validation
- local RAG thinking
- mock LLM mode before paid provider integration
- MCP-style tool integration
- LangGraph-style workflow thinking
- Streamlit demo UI
- Docker packaging awareness
- Kubernetes/minikube deployment awareness
- `.env` configuration awareness
- clear demo and interview explanation

The important interview point is this:

```text
I did not only call an LLM. I built an end-to-end AI application flow around the LLM.
```

## 4. Architecture Mental Model

Read this flow slowly:

```text
User enters question
  -> Streamlit UI sends request
  -> FastAPI receives request
  -> LangGraph controls workflow
  -> RAG retrieves context
  -> MCP tool provides helper data
  -> LLM/mock LLM generates answer
  -> FastAPI returns response
  -> UI displays result
```

Beginner meaning:

- Streamlit is the screen the user sees.
- FastAPI is the backend service that receives requests.
- Pydantic checks whether the request body is valid.
- RAG finds useful information from local documents.
- The MCP-style tool provides controlled helper data.
- The LangGraph-style workflow decides the order of steps.
- The mock LLM creates deterministic demo output without an API key.
- FastAPI sends JSON back.
- Streamlit displays that JSON in the browser.

## 5. Study Order

Use this order:

1. `00-poc-overview.md`
2. `01-architecture-and-demo-script.md`
3. `ai-engineer-poc-qa-assistant/README.md`
4. `ai-engineer-poc-qa-assistant/DEMO_GUIDE.md`
5. `exercises.md`
6. `cheatsheet.md`
7. `interview-questions.md`

## 6. Project Folder

Main project folder:

```text
22-final-poc-project/ai-engineer-poc-qa-assistant/
```

High-level structure:

```text
ai-engineer-poc-qa-assistant/
  backend/          FastAPI app and Pydantic models
  frontend/         Streamlit UI
  rag/              local document retrieval helper
  mcp_tools/        MCP-style helper tool functions
  graph/            workflow steps
  data/             local requirement notes
  k8s/              Kubernetes/minikube YAML
  Dockerfile        backend container recipe
  docker-compose.yml
  requirements.txt
  README.md
  DEMO_GUIDE.md
```

## 7. What Each Major Part Proves

FastAPI proves that you can expose Python logic as a web API.

Pydantic proves that you can validate request and response data instead of trusting random user input.

REST endpoints prove that your application can be called by a UI, a browser, `curl`, Postman, or another service.

RAG proves that the assistant can use project-specific documents instead of answering only from general model knowledge.

Local documents prove that the POC can run without a database or cloud storage.

Mock LLM proves that the architecture works without paid keys, network dependency, or provider setup.

Optional real LLM integration proves how the mock generator could later be replaced with OpenAI, Gemini, Ollama, or another provider.

FastMCP/MCP-style tools prove that the assistant can call controlled helper functions instead of guessing all information.

LangGraph-style workflow proves that the app has a step-by-step process rather than one unclear prompt call.

Streamlit proves that the POC can be demonstrated visually.

Docker proves that the backend can be packaged consistently.

Kubernetes/minikube proves basic deployment awareness.

`.env` proves that configuration should be separated from code.

`requirements.txt` proves that dependencies are explicit and reinstallable.

## 8. Mock First, Real LLM Later

The default project uses mock output.

That is intentional.

For a beginner POC, the first goal is to prove:

- the backend starts
- endpoints work
- request validation works
- retrieval works
- workflow steps run
- UI can call the API
- output is understandable

After that works, a real LLM can be added as an optional improvement.

Common beginner mistake:

```text
Starting with real API keys before the local architecture works.
```

Better approach:

```text
Make the mock workflow reliable first, then replace only the generator step.
```

## 9. How To Run

Detailed commands are in:

```text
ai-engineer-poc-qa-assistant/README.md
```

Short version:

```powershell
cd 22-final-poc-project/ai-engineer-poc-qa-assistant
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

In another terminal:

```powershell
cd 22-final-poc-project/ai-engineer-poc-qa-assistant
.\.venv\Scripts\Activate.ps1
streamlit run frontend/app.py
```

Expected local URLs:

```text
FastAPI docs: http://127.0.0.1:8000/docs
Streamlit UI: http://localhost:8501
```

## 10. Two-Minute Demo Script

Problem:

```text
QA teams often receive requirements and need to quickly understand what to test. Manually reading notes and drafting test cases takes time.
```

Solution:

```text
I built an AI QA Knowledge Assistant and Test Case Generator. It reads local requirement notes, answers questions, and generates starter test cases.
```

Architecture:

```text
The user enters a question in Streamlit. Streamlit sends a REST request to FastAPI. Pydantic validates the input. A LangGraph-style workflow controls the steps. RAG retrieves relevant local context. An MCP-style tool provides helper test data. A mock LLM creates the answer. FastAPI returns JSON and the UI displays it.
```

Live flow:

```text
I open the Streamlit UI, enter a requirement, click Generate, and show the returned test cases and context used.
```

Business value:

```text
This reduces the time needed to create first-draft QA coverage and helps teams ask questions against project notes.
```

Technical value:

```text
The POC demonstrates API design, validation, RAG, tool integration, workflow orchestration, mock-first LLM design, UI integration, and container/deployment awareness.
```

## 11. Common Errors

Error:

```text
ModuleNotFoundError: No module named 'backend'
```

Likely cause:

```text
The command was run from the wrong folder.
```

Fix:

```powershell
cd 22-final-poc-project/ai-engineer-poc-qa-assistant
uvicorn backend.main:app --reload
```

Error:

```text
Connection refused in Streamlit
```

Likely cause:

```text
The FastAPI backend is not running.
```

Fix:

```text
Start the backend first, then refresh the Streamlit UI.
```

Error:

```text
422 Unprocessable Entity
```

Likely cause:

```text
Pydantic rejected an empty or invalid request body.
```

Fix:

```text
Enter a non-empty question or requirement.
```

## 12. Remaining Learning Goal

By the end of this module, you should be able to run the POC and explain it in plain English:

```text
I built a mock-first AI QA assistant that uses FastAPI, Pydantic, local RAG, a tool layer, a workflow layer, Streamlit, Docker, and Kubernetes basics.
```
