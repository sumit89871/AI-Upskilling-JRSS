# AI Engineer POC QA Assistant

## 1. Project Goal

This project is a beginner-friendly final POC:

```text
AI QA Knowledge Assistant + Test Case Generator
```

It helps a user:

- ask questions about local requirement notes
- generate starter QA test cases from a requirement
- see how an AI Engineer connects UI, API, validation, retrieval, tools, workflow, and deployment basics

The default mode is mock mode. No paid LLM key is required.

## 2. Beginner Mental Model

```text
User enters question
  -> Streamlit UI sends request
  -> FastAPI receives request
  -> Pydantic validates request
  -> LangGraph-style workflow controls steps
  -> RAG retrieves local context
  -> MCP-style tool provides helper data
  -> mock LLM generates answer/test cases
  -> FastAPI returns JSON
  -> Streamlit displays result
```

This is the explanation to remember for demos and interviews.

## 3. Project Structure

```text
ai-engineer-poc-qa-assistant/
  backend/
    main.py              FastAPI app and REST endpoints
    models.py            Pydantic request and response models

  frontend/
    app.py               Streamlit browser UI

  rag/
    rag_service.py       Loads local notes and retrieves matching context

  mcp_tools/
    test_data_tools.py   MCP-style helper tool functions

  graph/
    workflow.py          LangGraph-style workflow steps

  data/
    requirements_notes.txt

  k8s/
    deployment.yaml      Kubernetes Deployment example
    service.yaml         Kubernetes Service example

  Dockerfile             Backend container recipe
  docker-compose.yml     Local backend container runner
  requirements.txt       Python dependency list
  .env.example           Example environment configuration
  DEMO_GUIDE.md          Demo and presentation guide
  README.md              This file
```

## 4. What Each Part Does

`backend/main.py`

Creates the FastAPI app and exposes:

- `GET /health`
- `POST /ask`
- `POST /generate-test-cases`

`backend/models.py`

Defines request and response schemas using Pydantic. It rejects empty input before the workflow runs.

`rag/rag_service.py`

Loads `data/requirements_notes.txt`, splits it into lines, and returns lines that match words from the user query.

`mcp_tools/test_data_tools.py`

Provides controlled helper data such as a demo user and API status codes.

`graph/workflow.py`

Runs a step-by-step workflow:

```text
understand_query -> retrieve -> generate -> review
```

`frontend/app.py`

Creates a Streamlit UI with two tabs:

- Ask Knowledge Base
- Generate Test Cases

`Dockerfile`

Packages the backend into a container.

`k8s/`

Shows how the backend could be deployed with Kubernetes/minikube basics.

## 5. Setup

Where to run:

Run these commands from:

```text
22-final-poc-project/ai-engineer-poc-qa-assistant
```

Command:

```powershell
python -m venv .venv
```

What each part means:

- `python` runs Python
- `-m` runs a Python module as a command
- `venv` is Python's virtual environment module
- `.venv` is the folder created for the environment

Expected output:

Usually no long success message appears.

How to verify:

```powershell
Get-ChildItem -Force
```

You should see `.venv`.

Command:

```powershell
.\.venv\Scripts\Activate.ps1
```

What it means:

This activates the local environment in PowerShell.

Expected output:

The terminal prompt usually starts with:

```text
(.venv)
```

Command:

```powershell
pip install -r requirements.txt
```

What each part means:

- `pip` installs Python packages
- `install` means install packages
- `-r` means read package names from a file
- `requirements.txt` is the dependency list

Expected output:

```text
Successfully installed ...
```

How to verify:

```powershell
pip show fastapi
pip show streamlit
```

## 6. Run The Backend

Command:

```powershell
uvicorn backend.main:app --reload
```

Where to run:

Run from:

```text
22-final-poc-project/ai-engineer-poc-qa-assistant
```

What each part means:

- `uvicorn` runs the FastAPI app
- `backend.main` means `main.py` inside the `backend` folder
- `app` is the FastAPI object in that file
- `--reload` restarts the server when code changes

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

How to verify:

Open:

```text
http://127.0.0.1:8000/docs
```

or:

```text
http://127.0.0.1:8000/health
```

Expected health response:

```json
{
  "status": "ok"
}
```

Common error:

```text
ModuleNotFoundError: No module named 'backend'
```

Fix:

Run the command from the POC project folder, not from the course root.

## 7. Run The Frontend

Open a second terminal.

Commands:

```powershell
cd 22-final-poc-project/ai-engineer-poc-qa-assistant
.\.venv\Scripts\Activate.ps1
streamlit run frontend/app.py
```

What each part means:

- `streamlit` runs the Streamlit command-line tool
- `run` starts a Streamlit app
- `frontend/app.py` is the UI file

Expected output:

```text
Local URL: http://localhost:8501
```

How to verify:

Open the URL and confirm that the page title is:

```text
AI QA Knowledge Assistant
```

Common error:

```text
Connection refused
```

Likely cause:

FastAPI is not running.

Fix:

Start the backend first with `uvicorn backend.main:app --reload`.

## 8. Test The API Directly

Health:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/health
```

Expected output:

```json
{
  "status": "ok"
}
```

Ask:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/ask -Method Post -ContentType "application/json" -Body '{"question":"What should be tested for login?"}'
```

Expected output:

```text
The response includes question, answer, and context_used.
```

Generate test cases:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/generate-test-cases -Method Post -ContentType "application/json" -Body '{"requirement":"User can reset password using registered email"}'
```

Expected output:

```text
The response includes requirement, test_cases, context_used, and mode.
```

## 9. Pydantic Validation Example

Try this invalid request:

```powershell
Invoke-RestMethod -Uri http://127.0.0.1:8000/generate-test-cases -Method Post -ContentType "application/json" -Body '{"requirement":""}'
```

Expected behavior:

FastAPI returns a validation error.

Why:

`backend/models.py` has this rule:

```python
requirement: str = Field(min_length=1)
```

Meaning:

The field must be a string and must contain at least one character.

## 10. Docker Run

Command:

```powershell
docker compose up --build
```

Where to run:

Run from:

```text
22-final-poc-project/ai-engineer-poc-qa-assistant
```

What each part means:

- `docker` runs Docker
- `compose` uses `docker-compose.yml`
- `up` starts the service
- `--build` rebuilds the image before starting

Expected output:

```text
backend service starts and listens on port 8000
```

How to verify:

Open:

```text
http://127.0.0.1:8000/health
```

Be careful:

The Docker setup starts the backend container. The Streamlit UI is still normally run locally with `streamlit run frontend/app.py`.

## 11. Kubernetes/minikube Run

Use this only after the local and Docker flows make sense.

Typical commands:

```powershell
minikube start
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl get pods
kubectl get services
```

What each command means:

- `minikube start` starts a local Kubernetes cluster
- `kubectl apply -f ...` creates or updates resources from YAML
- `kubectl get pods` shows running application pods
- `kubectl get services` shows exposed services

Expected output:

```text
ai-qa-assistant pod eventually shows Running
ai-qa-assistant-service appears as a NodePort service
```

Common beginner note:

The YAML uses image `ai-qa-assistant:latest`. With minikube, local image handling may require building inside minikube's Docker environment or loading the image into minikube.

## 12. `.env` Role

`.env` files hold configuration values.

Example:

```text
USE_MOCK_LLM=true
BACKEND_URL=http://127.0.0.1:8000
```

In this project:

- mock mode is the default idea
- Streamlit reads `BACKEND_URL` if it is set
- real provider keys would be optional future configuration

Important:

```text
Do not commit real API keys.
```

## 13. Optional Real LLM Role

A real LLM is optional.

The clean upgrade path is:

1. Keep `/ask` and `/generate-test-cases` the same.
2. Keep Pydantic request and response models stable.
3. Keep retrieval and workflow steps.
4. Replace mock generation with a provider client.
5. Read provider configuration from environment variables.
6. Add tests and error handling around model calls.

Do not start with this. First make the mock POC reliable.

## 14. Common Errors And Fixes

Error:

```text
ModuleNotFoundError: No module named 'backend'
```

Fix:

Run from `ai-engineer-poc-qa-assistant`.

Error:

```text
422 Unprocessable Entity
```

Fix:

Send the required JSON field with non-empty text.

Error:

```text
Streamlit cannot connect to backend
```

Fix:

Start FastAPI and verify `/health`.

Error:

```text
Port 8000 is already in use
```

Fix:

Stop the other backend process or run Uvicorn on another port:

```powershell
uvicorn backend.main:app --reload --port 8001
```

Then set `BACKEND_URL` for Streamlit:

```powershell
$env:BACKEND_URL="http://127.0.0.1:8001"
streamlit run frontend/app.py
```

## 15. Demo Checklist

Before presenting:

- install dependencies
- start backend
- verify `/health`
- open `/docs`
- start Streamlit
- ask one knowledge-base question
- generate test cases for one requirement
- explain the JSON response
- explain mock mode
- explain how real LLM integration would be added
- explain production security and monitoring improvements

## 16. Short Interview Summary

```text
I built a mock-first AI QA Knowledge Assistant and Test Case Generator. It uses Streamlit as the UI, FastAPI as the backend, Pydantic for validation, local RAG over requirement notes, MCP-style helper tools, and a LangGraph-style workflow. It returns structured JSON and includes Docker and Kubernetes files to show deployment awareness. The current version runs locally without paid API keys, and the production path would add real LLM integration, vector retrieval, authentication, secrets management, monitoring, and automated tests.
```
