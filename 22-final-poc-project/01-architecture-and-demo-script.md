# POC Architecture And Demo Script

## 1. Architecture In One Line

```text
User enters question -> Streamlit UI sends request -> FastAPI receives request -> LangGraph controls workflow -> RAG retrieves context -> MCP tool provides helper data -> LLM/mock LLM generates answer -> FastAPI returns response -> UI displays result
```

This line is the main mental model for the whole POC.

## 2. Architecture With Responsibilities

```text
User
  -> Streamlit frontend
      job: collect question or requirement from the user

  -> FastAPI backend
      job: expose REST endpoints and run backend logic

  -> Pydantic models
      job: validate request body and response shape

  -> LangGraph-style workflow
      job: control the order of steps and carry state

  -> RAG helper
      job: retrieve relevant lines from local documents

  -> MCP-style tool
      job: provide controlled helper data for generated tests

  -> Mock LLM
      job: generate predictable demo output without an API key

  -> JSON response
      job: return structured data to UI or API client
```

## 3. Request Flow For `/ask`

Endpoint:

```text
POST /ask
```

What happens:

1. User types a question in Streamlit.
2. Streamlit sends JSON to FastAPI.
3. FastAPI maps the request to the `ask` function.
4. Pydantic checks that `question` exists and is not empty.
5. The retrieval helper searches `data/requirements_notes.txt`.
6. The backend returns a mock answer and the context used.

Example request:

```json
{
  "question": "What should be tested for login?"
}
```

Expected response shape:

```json
{
  "question": "What should be tested for login?",
  "answer": "Mock answer based on context: ...",
  "context_used": [
    "Relevant note from local file"
  ]
}
```

## 4. Request Flow For `/generate-test-cases`

Endpoint:

```text
POST /generate-test-cases
```

What happens:

1. User types a requirement in Streamlit.
2. Streamlit sends JSON to FastAPI.
3. FastAPI validates the body with `TestCaseRequest`.
4. The workflow creates a state dictionary.
5. The workflow runs `understand_query`.
6. The workflow runs `retrieve` and gets context from local notes.
7. The workflow runs `generate` and calls helper tool functions.
8. The workflow runs `review`.
9. FastAPI returns a `TestCaseResponse`.

Expected response shape:

```json
{
  "requirement": "User can reset password",
  "test_cases": [
    {
      "title": "Valid requirement scenario",
      "type": "positive",
      "priority": "P1",
      "expected_result": "System accepts valid input..."
    },
    {
      "title": "Invalid requirement scenario",
      "type": "negative",
      "priority": "P2",
      "expected_result": "System rejects invalid input..."
    }
  ],
  "context_used": [
    "Relevant note from local file"
  ],
  "mode": "mock"
}
```

## 5. LangGraph Workflow Mental Model

LangGraph-style thinking means:

```text
state + nodes + edges/order = workflow
```

In this beginner POC:

- `state` is a Python dictionary
- each node is a Python function
- the edge/order is the list of functions in `run_workflow`

Current workflow order:

```text
understand_query -> retrieve -> generate -> review
```

Beginner explanation:

```text
The workflow carries information from one step to the next. The retrieve step adds context. The generate step adds test cases. The review step marks the result as reviewed.
```

## 6. RAG Mental Model

RAG means:

```text
retrieve useful context first, then generate an answer using that context
```

In this POC:

- the documents are local text notes
- the retriever splits notes into lines
- the retriever searches for matching words
- the generator uses the returned lines as context

This is intentionally simple. A production system might use embeddings and a vector database, but this beginner version makes the retrieval behavior visible.

## 7. MCP Tool Mental Model

An MCP-style tool is a controlled helper function that the AI workflow can use.

In this POC, the tool functions provide:

- demo test user data
- expected API status code data

Why this matters:

```text
Instead of asking the LLM to invent every detail, the workflow can call a known function that returns trusted helper data.
```

## 8. Demo Script: Two Minutes

Use this exact order.

Problem:

```text
QA teams often need to understand requirements and produce test coverage quickly. Manually reading notes and creating first-draft cases takes time.
```

Solution:

```text
I built an AI QA Knowledge Assistant and Test Case Generator. It answers questions from local requirement notes and generates starter positive and negative test cases.
```

Architecture:

```text
The user enters a question in Streamlit. Streamlit sends a REST request to FastAPI. Pydantic validates the input. A LangGraph-style workflow controls the steps. RAG retrieves context from local notes. An MCP-style tool provides helper data such as users and status codes. A mock LLM generates deterministic output. FastAPI returns JSON and the UI displays it.
```

Live flow:

```text
I start the backend, open the API docs, check /health, then open Streamlit. I enter a password reset requirement, click Generate, and show the generated test cases plus the context used.
```

Business value:

```text
The value is faster first-draft QA analysis. A QA engineer still reviews and improves the output, but the assistant reduces blank-page time.
```

Technical value:

```text
The value is that the system is not just a prompt. It shows backend API design, validation, retrieval, tool use, workflow orchestration, UI integration, container packaging, and deployment awareness.
```

## 9. Stand-And-Deliver Explanation

Use this when presenting without touching the keyboard:

```text
This POC is an AI QA Knowledge Assistant and Test Case Generator. The user enters a question or requirement in a Streamlit UI. Streamlit calls a FastAPI backend through REST endpoints. Pydantic validates the input so empty or malformed requests are rejected early. The backend runs a LangGraph-style workflow: understand the request, retrieve context from local requirement notes, call an MCP-style helper tool, generate mock LLM output, and review the result. The response comes back as structured JSON. The project runs locally without paid API keys, and Docker plus Kubernetes files show how the backend could later be packaged and deployed.
```

## 10. Productionization Talking Points

If asked how to make it production-ready, say:

- replace simple keyword retrieval with embeddings and a vector database
- replace mock LLM with a provider client or approved local model
- add authentication and authorization
- store secrets in a secret manager, not in code
- add request logging, error logging, metrics, and traces
- add automated tests for endpoints, workflow, retrieval, and UI behavior
- add rate limiting and input size limits
- add CI/CD and container scanning
- use Kubernetes Secrets and ConfigMaps
- review privacy, compliance, and data retention requirements

## 11. Security Talking Points

Beginner-safe security explanation:

```text
This demo does not hardcode real API keys. In production I would not store secrets in source code. I would validate inputs, authenticate users, restrict who can call endpoints, avoid logging sensitive prompts or outputs, scan dependencies, and monitor unusual usage.
```

## 12. Common Demo Problems

Problem:

```text
Streamlit shows a connection error.
```

Likely cause:

```text
FastAPI is not running, or BACKEND_URL points to the wrong address.
```

Problem:

```text
FastAPI returns 422.
```

Likely cause:

```text
The request body is empty or the field name is wrong.
```

Problem:

```text
The response looks too simple.
```

Explanation:

```text
That is expected. This is a mock-first POC. The goal is to demonstrate architecture and integration before adding model complexity.
```
