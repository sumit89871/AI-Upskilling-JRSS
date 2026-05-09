# Final POC Overview

## 1. What It Is

The final POC is an AI QA Knowledge Assistant + Test Case Generator.

It is a small AI Engineer project that helps a user ask questions about requirement notes and generate starter QA test cases.

POC name:

```text
ai-engineer-poc-qa-assistant
```

Core use case:

```text
Read requirement notes -> answer questions -> generate test scenarios and API test ideas
```

The project is designed for a beginner demo. It should be understandable, runnable, and explainable in an interview.

## 2. The Most Important Beginner Idea

This POC is not one big AI script.

It is an application made from small pieces.

Beginner mental model:

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

Each part has one job. That makes the project easier to debug and easier to explain.

## 3. What Problem It Solves

QA teams often receive requirement notes, user stories, acceptance criteria, API behavior, and defect examples.

Before testing, they need to answer questions like:

- What does this feature do?
- What positive scenarios should be tested?
- What negative scenarios should be tested?
- What API status codes are relevant?
- What data should be used for test execution?

This POC creates a first draft. It does not replace a QA engineer. It helps the QA engineer move faster.

## 4. Why It Is A Good Reskilling POC

An AI Engineer role is usually not only about prompt writing.

A practical AI Engineer needs to connect:

- backend APIs
- validation
- documents
- retrieval
- LLM calls or mock LLM calls
- tool calls
- workflow control
- UI
- packaging and deployment basics

This POC touches all of those areas without becoming too large.

Interview framing:

```text
I built a local-first AI assistant for QA. It uses FastAPI for the backend, Pydantic for validation, local RAG for context, an MCP-style tool for helper data, a LangGraph-style workflow for step control, Streamlit for the UI, and Docker/Kubernetes files to show deployment awareness.
```

## 5. High-Level Architecture

Architecture in plain text:

```text
Streamlit frontend
  calls
FastAPI backend
  validates with
Pydantic models
  runs
LangGraph-style workflow
  retrieves from
Local documents using RAG
  calls
MCP-style helper tools
  generates with
Mock LLM by default
  returns
Structured JSON response
```

The real project uses a simple workflow implementation in Python. It is called LangGraph-style because it teaches the same idea: a workflow has state, steps, and a controlled order.

## 6. Component Roles

### FastAPI Backend

FastAPI exposes the application as HTTP endpoints.

The backend has routes such as:

```text
GET /health
POST /ask
POST /generate-test-cases
```

Beginner meaning:

```text
The backend is the part that receives requests, runs Python logic, and returns JSON.
```

### Pydantic Validation

Pydantic models define what valid input and output should look like.

Example:

```python
class TestCaseRequest(BaseModel):
    requirement: str = Field(min_length=1)
```

Read this line slowly:

- `class TestCaseRequest` creates a model named `TestCaseRequest`
- `BaseModel` gives validation behavior from Pydantic
- `requirement: str` means the field must be text
- `Field(min_length=1)` means empty text is not allowed

If a user sends an empty requirement, FastAPI and Pydantic return a validation error before the workflow runs.

### REST Endpoint

A REST endpoint is a URL that another program can call.

Example:

```text
POST /generate-test-cases
```

Beginner meaning:

```text
The UI does not directly run Python functions. It sends an HTTP request to an endpoint, and the backend decides which function handles that request.
```

### RAG

RAG means Retrieval-Augmented Generation.

In this POC, retrieval means the app searches local requirement notes for useful lines. Generation means the mock LLM-style step uses that context to create an answer or test cases.

Important:

```text
RAG is not training the model.
```

RAG gives the model or mock generator relevant information at request time.

### Local Documents

The local knowledge base is stored in:

```text
data/requirements_notes.txt
```

This keeps the POC simple. A beginner can open the file, change the notes, restart or rerun the request, and see how retrieved context changes.

### Mock LLM

The mock LLM is the default output generator.

It does not call OpenAI, Gemini, or any paid provider.

Why this matters:

- no API key needed
- no billing risk
- no network dependency
- predictable demo output
- easier debugging

### Optional Real LLM

A real LLM can be added later by replacing the generator step.

Production-like idea:

```text
Keep the workflow and API contract stable. Swap only the model client.
```

### FastMCP Tool Server Role

MCP means Model Context Protocol. FastMCP is a Python-friendly way to expose tools to AI applications.

This POC uses MCP-style tool functions in:

```text
mcp_tools/test_data_tools.py
```

The current tool layer is intentionally simple. It teaches the idea that an AI workflow can call controlled helper functions, such as getting a test user or API status data.

### LangGraph Workflow Role

LangGraph is used in AI applications to create stateful workflows.

This POC uses a beginner-friendly workflow file:

```text
graph/workflow.py
```

The workflow runs steps in order:

```text
understand_query -> retrieve_context -> generate -> review
```

Beginner meaning:

```text
Instead of one unclear function doing everything, the workflow shows the exact stages of thinking and generation.
```

### Streamlit UI

Streamlit creates the browser demo.

It lets the user type a question or requirement and see the JSON response.

This is useful because interviews and demos are easier when the audience can see the flow without using only terminal commands.

### Docker

Docker packages the backend into a container.

Beginner mental model:

```text
Dockerfile = recipe
image = packaged application
container = running copy of the image
```

### Kubernetes/minikube

Kubernetes runs containers in a cluster.

minikube is a local Kubernetes cluster for practice.

This POC includes basic YAML to show:

- a Deployment for running the backend container
- a Service for exposing the backend

This is deployment awareness, not full production readiness.

### `.env`

`.env` files store configuration values outside code.

Example values:

```text
USE_MOCK_LLM=true
BACKEND_URL=http://127.0.0.1:8000
```

Do not commit real secrets.

### `requirements.txt`

`requirements.txt` lists Python packages needed by the project.

Example:

```text
fastapi
uvicorn
pydantic
streamlit
requests
```

Beginner meaning:

```text
If another learner gets the project, they can install the same dependencies with pip install -r requirements.txt.
```

## 7. What Is Local-Only vs Production-Like

Local-only:

- text file knowledge base
- mock LLM
- simple keyword retrieval
- no authentication
- no database
- no observability stack

Production-like:

- API boundary
- request validation
- structured responses
- workflow stages
- tool integration pattern
- Dockerfile
- Kubernetes YAML
- environment-based configuration

## 8. Expected Demo Output

For `GET /health`, expected response:

```json
{
  "status": "ok"
}
```

For `POST /generate-test-cases`, expected response shape:

```json
{
  "requirement": "User can reset password",
  "test_cases": [
    {
      "title": "Valid requirement scenario",
      "type": "positive",
      "priority": "P1",
      "expected_result": "System accepts valid input..."
    }
  ],
  "context_used": [
    "Relevant line from local notes"
  ],
  "mode": "mock"
}
```

The exact context depends on the words in the request and the content of `data/requirements_notes.txt`.

## 9. Common Mistakes

Mistake:

```text
Thinking RAG means the model has been trained.
```

Correction:

```text
RAG retrieves relevant context and passes it into the generation step. It does not change model weights.
```

Mistake:

```text
Running uvicorn from the wrong folder.
```

Correction:

```text
Run uvicorn from ai-engineer-poc-qa-assistant, where backend/ exists.
```

Mistake:

```text
Trying to use a real LLM before the mock flow works.
```

Correction:

```text
First prove the API, validation, retrieval, workflow, and UI.
```

## 10. Stand-And-Deliver Explanation

Use this version when speaking:

```text
This is my final AI Engineer POC. I built an AI QA Knowledge Assistant and Test Case Generator. A user enters a question or requirement in Streamlit. The UI sends a REST request to FastAPI. Pydantic validates the request. A workflow controls the steps: understand the request, retrieve local context, call a helper tool, generate mock LLM output, and return structured JSON. The project uses a mock LLM by default so it runs without paid API keys. Docker and Kubernetes files show how the backend could be packaged and deployed. In production, I would add authentication, real LLM integration, a vector database, better monitoring, secrets management, and automated tests.
```
