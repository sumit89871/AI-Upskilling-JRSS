# Final POC Cheatsheet

## Core Flow

```text
User -> Streamlit -> FastAPI -> Pydantic -> Workflow -> RAG -> Tool -> Mock LLM -> JSON -> UI
```

Meaning:

The request starts in the UI, goes to the backend, is validated, moves through the workflow, retrieves context, calls helper data, generates a response, and returns JSON.

Be careful:

Do not explain the POC as "I just used an LLM." The value is the full application flow.

## Project Folder

```text
22-final-poc-project/ai-engineer-poc-qa-assistant
```

Meaning:

This is the folder where backend, frontend, RAG, workflow, Docker, and Kubernetes files live.

When to use:

Run backend, frontend, Docker, and most commands from this folder.

Be careful:

Running commands from the wrong folder causes import errors.

## Create Virtual Environment

```powershell
python -m venv .venv
```

Meaning:

Creates an isolated Python environment.

When to use:

Run once before installing dependencies.

Be careful:

Create it inside the POC project folder.

## Activate Virtual Environment

```powershell
.\.venv\Scripts\Activate.ps1
```

Meaning:

Activates the local Python environment in PowerShell.

When to use:

Run before `pip`, `uvicorn`, or `streamlit`.

Be careful:

If PowerShell blocks scripts, you may need to adjust execution policy in your local environment.

## Install Dependencies

```powershell
pip install -r requirements.txt
```

Meaning:

Installs packages listed in `requirements.txt`.

When to use:

Run after activating `.venv`.

Be careful:

Do not install dependencies globally if the virtual environment is not active.

## Run Backend

```powershell
uvicorn backend.main:app --reload
```

Meaning:

Starts the FastAPI backend.

When to use:

Run before using `/docs`, `/health`, or Streamlit.

Example URL:

```text
http://127.0.0.1:8000/docs
```

Be careful:

`backend.main:app` means folder `backend`, file `main.py`, object `app`.

## Run Frontend

```powershell
streamlit run frontend/app.py
```

Meaning:

Starts the browser UI.

When to use:

Run in a second terminal after the backend is running.

Example URL:

```text
http://localhost:8501
```

Be careful:

Streamlit calls FastAPI. If FastAPI is off, the UI cannot get a response.

## Health Endpoint

```text
GET /health
```

Meaning:

Checks whether the backend is alive.

Example response:

```json
{"status": "ok"}
```

Be careful:

Health only proves the server is running. It does not prove RAG or workflow logic works.

## Ask Endpoint

```text
POST /ask
```

Meaning:

Answers a question using local context.

Example body:

```json
{
  "question": "What should be tested for login?"
}
```

Be careful:

The field name must be `question`.

## Generate Test Cases Endpoint

```text
POST /generate-test-cases
```

Meaning:

Generates starter test cases from a requirement.

Example body:

```json
{
  "requirement": "User can reset password"
}
```

Be careful:

The field name must be `requirement`.

## Pydantic Model

```python
class TestCaseRequest(BaseModel):
    requirement: str = Field(min_length=1)
```

Meaning:

Defines the expected request body and rejects empty requirements.

When to use:

Use for request and response validation in FastAPI apps.

Be careful:

A dictionary stores data. A Pydantic model validates data.

## REST Endpoint vs Function

REST endpoint:

```text
POST /generate-test-cases
```

Function:

```python
def generate_test_cases(request: TestCaseRequest) -> dict:
```

Meaning:

The endpoint is the URL clients call. The function is the Python code FastAPI runs.

Be careful:

Beginners often say the browser calls the function directly. It calls the endpoint.

## RAG

```text
Retrieve context first, then generate using that context.
```

Meaning:

RAG lets the assistant use project-specific documents at request time.

When to use:

Use when answers should be grounded in files, docs, tickets, or knowledge bases.

Be careful:

RAG is not fine-tuning. It does not retrain the model.

## Local Documents

```text
data/requirements_notes.txt
```

Meaning:

Small local knowledge base for the demo.

When to use:

Edit this file to change what the assistant can retrieve.

Be careful:

This is not a production document store.

## Mock LLM

```text
mode: mock
```

Meaning:

The app returns predictable generated output without calling a real model.

When to use:

Use for local demos, debugging, and architecture validation.

Be careful:

Mock output proves the flow, not real model quality.

## Optional Real LLM

```text
Replace the generator step with a provider client.
```

Meaning:

OpenAI, Gemini, Ollama, or another provider can be added later.

When to use:

Add after the mock flow works end to end.

Be careful:

Do not hardcode API keys.

## MCP-Style Tool

```text
mcp_tools/test_data_tools.py
```

Meaning:

Provides controlled helper functions for the workflow.

When to use:

Use when the assistant needs reliable external or computed data.

Be careful:

A tool should do a clear, limited job.

## LangGraph-Style Workflow

```text
understand_query -> retrieve -> generate -> review
```

Meaning:

Runs the AI flow in controlled steps.

When to use:

Use when one request needs multiple stages and shared state.

Be careful:

State is the data carried between steps. It is not the same as a single local variable inside one function.

## Docker

```powershell
docker compose up --build
```

Meaning:

Builds and runs the backend container using `docker-compose.yml`.

When to use:

Use after the local Python flow works.

Be careful:

This compose file runs the backend service, not the full Streamlit UI.

## Kubernetes/minikube

```powershell
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Meaning:

Creates a backend Deployment and Service in Kubernetes.

When to use:

Use for local Kubernetes practice with minikube.

Be careful:

Kubernetes YAML here shows basics, not full production readiness.

## `.env`

```text
USE_MOCK_LLM=true
BACKEND_URL=http://127.0.0.1:8000
```

Meaning:

Stores configuration outside source code.

When to use:

Use for local settings and provider configuration.

Be careful:

Never commit real API keys.

## Common Errors

`ModuleNotFoundError: No module named 'backend'`

Meaning:

Usually running from the wrong folder.

Fix:

Run from `ai-engineer-poc-qa-assistant`.

`422 Unprocessable Entity`

Meaning:

Pydantic rejected the request body.

Fix:

Send the correct JSON field with non-empty text.

`Connection refused`

Meaning:

The backend is not running or the URL is wrong.

Fix:

Start FastAPI and verify `http://127.0.0.1:8000/health`.
