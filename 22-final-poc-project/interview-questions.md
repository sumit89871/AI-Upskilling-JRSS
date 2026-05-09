# Final POC Interview Questions

## Question 1: What did you build?

Short answer:

I built an AI QA Knowledge Assistant and Test Case Generator.

Expanded answer:

The POC lets a user ask questions about local requirement notes and generate starter QA test cases from a requirement. The user interacts through a Streamlit UI. The UI calls a FastAPI backend. Pydantic validates request data. A workflow retrieves relevant local context, calls a helper tool, generates mock LLM output, and returns structured JSON.

Project example:

The project folder is `ai-engineer-poc-qa-assistant`. The backend exposes `/ask` and `/generate-test-cases`. The local knowledge base is `data/requirements_notes.txt`.

Common wrong answer:

```text
I built a chatbot.
```

Why it is weak:

It does not explain the QA use case, API design, validation, retrieval, tools, workflow, or deployment awareness.

## Question 2: Explain your POC in two minutes.

Short answer:

It is a mock-first AI QA assistant that uses Streamlit, FastAPI, Pydantic, local RAG, MCP-style tools, a LangGraph-style workflow, Docker, and Kubernetes basics.

Expanded answer:

The user enters a question or requirement in Streamlit. Streamlit sends a REST request to FastAPI. Pydantic validates the input. A LangGraph-style workflow controls the steps. RAG retrieves context from local requirement notes. An MCP-style tool provides helper test data such as users and status codes. A mock LLM generates deterministic output. FastAPI returns structured JSON and Streamlit displays it.

Project example:

For `/generate-test-cases`, the request body contains `requirement`. The response contains generated test cases, context used, and `mode: mock`.

Common wrong answer:

```text
It uses AI to generate test cases.
```

Why it is weak:

It is too shallow for an interview because it does not explain how the system works.

## Question 3: Why did you use FastAPI?

Short answer:

I used FastAPI to expose the Python AI workflow as REST endpoints.

Expanded answer:

FastAPI lets other clients call Python logic over HTTP. In this POC, the Streamlit UI does not directly import backend functions. It sends requests to endpoints such as `/ask` and `/generate-test-cases`. FastAPI also gives automatic Swagger documentation at `/docs`, which makes the POC easy to test and demo.

Project example:

`backend/main.py` creates the FastAPI app and defines routes with decorators such as `@app.post("/generate-test-cases")`.

Common wrong answer:

```text
FastAPI is used to make the UI.
```

Correction:

FastAPI is the backend API layer. Streamlit is the UI layer.

## Question 4: Why did you use Pydantic?

Short answer:

I used Pydantic to validate request and response data.

Expanded answer:

Pydantic protects the backend from invalid input. For example, `Field(min_length=1)` prevents an empty requirement from reaching the workflow. It also documents the expected schema, which helps FastAPI generate useful API docs.

Project example:

`backend/models.py` defines `AskRequest`, `TestCaseRequest`, `TestCase`, and `TestCaseResponse`.

Common wrong answer:

```text
Pydantic is just for creating classes.
```

Correction:

Pydantic classes validate data. A normal Python class does not automatically validate request bodies.

## Question 5: Why did you use REST endpoints?

Short answer:

REST endpoints give the UI and other clients a clean way to call the backend.

Expanded answer:

An endpoint is a URL plus an HTTP method. For example, `POST /generate-test-cases` accepts a JSON request and returns a JSON response. This makes the backend usable from Streamlit, Swagger UI, PowerShell, Postman, or another service.

Project example:

Streamlit sends:

```text
POST http://127.0.0.1:8000/generate-test-cases
```

Common wrong answer:

```text
The frontend calls the Python function directly.
```

Correction:

The frontend sends an HTTP request to the endpoint. FastAPI then runs the matching Python function.

## Question 6: Why did you use RAG?

Short answer:

I used RAG so the assistant can answer using project-specific requirement notes.

Expanded answer:

RAG stands for Retrieval-Augmented Generation. It retrieves relevant context first and then uses that context during answer generation. This is useful because the model or mock generator should not rely only on general knowledge. It should use the local notes for the current project.

Project example:

`rag/rag_service.py` loads `data/requirements_notes.txt`, splits it into chunks, and returns matching lines.

Common wrong answer:

```text
RAG trains the model on my documents.
```

Correction:

RAG retrieves documents at request time. It does not train or fine-tune the model.

## Question 7: Why did you use local documents?

Short answer:

Local documents make the POC easy to run and easy to understand.

Expanded answer:

Instead of requiring a database, storage account, or vector service, the POC uses a simple text file as the knowledge base. This makes it beginner-friendly. A learner can open the file, edit requirement notes, and see how retrieval changes.

Project example:

The local document is `data/requirements_notes.txt`.

Common wrong answer:

```text
Local documents are production-ready storage.
```

Correction:

Local files are good for a demo. Production would usually use a document store, vector database, permission model, and indexing pipeline.

## Question 8: Why did you use a mock LLM?

Short answer:

I used a mock LLM so the POC runs without API keys, cost, or network dependency.

Expanded answer:

Mock mode proves the architecture first. It lets me test the UI, API, validation, retrieval, tools, and workflow before adding provider complexity. This is useful in interviews because the demo is predictable and does not fail due to API quota or internet issues.

Project example:

The `/generate-test-cases` response includes:

```text
mode: mock
```

Common wrong answer:

```text
Mock mode means the project is not AI-related.
```

Correction:

Mock mode is a development and demo strategy. The architecture still shows where a real LLM client would be integrated.

## Question 9: How would you add a real LLM?

Short answer:

I would replace the mock generation step with a provider client while keeping the API contract stable.

Expanded answer:

The clean approach is to keep Streamlit, FastAPI, Pydantic models, retrieval, and workflow structure the same. Only the generation step should call OpenAI, Gemini, Ollama, or another approved model provider. Secrets should come from environment variables or a secret manager, not from source code.

Project example:

The replacement would happen around the `generate` step in `graph/workflow.py`.

Common wrong answer:

```text
I would rewrite the whole app for OpenAI.
```

Correction:

A good design isolates provider-specific code so the rest of the app does not need major rewrites.

## Question 10: Why did you use MCP or MCP-style tools?

Short answer:

I used MCP-style tools to show how an AI workflow can call controlled helper functions.

Expanded answer:

A tool is useful when the assistant needs reliable data or an action that should not be guessed by the LLM. In this POC, helper functions return test user data and API status codes. In a real MCP server, these tools could be exposed through FastMCP and called by compatible clients.

Project example:

`mcp_tools/test_data_tools.py` contains `get_test_user` and `get_api_test_data`.

Common wrong answer:

```text
MCP is the same as RAG.
```

Correction:

RAG retrieves context from documents. MCP tools expose controlled functions or resources.

## Question 11: Why did you use LangGraph or a LangGraph-style workflow?

Short answer:

I used a workflow pattern to control the steps of the AI process.

Expanded answer:

LangGraph is useful when an AI application needs state and multiple steps. This POC uses a beginner-friendly workflow with functions for understanding, retrieval, generation, and review. The main concept is that data moves through a controlled sequence instead of being hidden inside one large function.

Project example:

`graph/workflow.py` creates a `state` dictionary and passes it through `understand_query`, `retrieve`, `generate`, and `review`.

Common wrong answer:

```text
LangGraph is only for chatbots.
```

Correction:

LangGraph-style workflows can be used for many multi-step AI processes, including QA generation.

## Question 12: Why did you use Streamlit?

Short answer:

I used Streamlit to make the POC easy to demo in a browser.

Expanded answer:

Streamlit lets a learner create a simple UI quickly with Python. For this POC, the UI has tabs for asking the knowledge base and generating test cases. It calls the backend through HTTP and displays JSON responses.

Project example:

`frontend/app.py` calls `BACKEND_URL` and posts JSON to FastAPI.

Common wrong answer:

```text
Streamlit is the backend.
```

Correction:

Streamlit is the frontend demo layer. FastAPI is the backend.

## Question 13: Why did you include Docker?

Short answer:

Docker shows how the backend can be packaged and run consistently.

Expanded answer:

The Dockerfile defines the backend runtime: start from Python, copy dependencies, install packages, copy code, and run Uvicorn. This helps explain the difference between running code directly on a laptop and running it inside a container.

Project example:

The Dockerfile starts the backend with:

```text
uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

Common wrong answer:

```text
Docker is the same as Kubernetes.
```

Correction:

Docker packages and runs containers. Kubernetes manages containers across a cluster.

## Question 14: Why did you include Kubernetes/minikube files?

Short answer:

They show basic deployment awareness.

Expanded answer:

The Kubernetes YAML includes a Deployment and Service. The Deployment describes how to run the backend container. The Service exposes it inside or outside the cluster. minikube can run this locally for practice.

Project example:

The files are in `k8s/deployment.yaml` and `k8s/service.yaml`.

Common wrong answer:

```text
Kubernetes files mean this is production-ready.
```

Correction:

These files show foundational knowledge. Production would need secrets, config management, resource limits, ingress, monitoring, scaling, and security policies.

## Question 15: What is the role of `.env`?

Short answer:

`.env` stores configuration outside source code.

Expanded answer:

Configuration values such as `USE_MOCK_LLM`, `BACKEND_URL`, or provider API keys should not be hardcoded. Local development can use a `.env` file or environment variables. Real secrets should not be committed to Git.

Project example:

The frontend reads `BACKEND_URL` from the environment and defaults to `http://127.0.0.1:8000`.

Common wrong answer:

```text
.env is where I should commit API keys.
```

Correction:

Never commit real secrets. Use placeholders or `.env.example` for documentation.

## Question 16: What is the role of `requirements.txt`?

Short answer:

It lists the Python packages needed to run the project.

Expanded answer:

When another person clones or opens the project, they need a repeatable way to install dependencies. `pip install -r requirements.txt` reads the file and installs packages such as FastAPI, Uvicorn, Pydantic, Streamlit, and requests.

Project example:

The project cannot run the backend without FastAPI and Uvicorn.

Common wrong answer:

```text
requirements.txt contains my project code.
```

Correction:

It contains dependency names, not application logic.

## Question 17: How would you productionize this POC?

Short answer:

I would add real model integration, stronger retrieval, authentication, secrets management, observability, automated tests, and deployment hardening.

Expanded answer:

For production, I would replace simple keyword retrieval with embeddings and a vector database, add a real LLM client, implement authentication and authorization, use a secret manager, add logging and metrics, write automated tests, add CI/CD, scan containers, and configure Kubernetes properly.

Project example:

The current `rag/rag_service.py` is simple and local. A production version might use a vector database with document indexing and access controls.

Common wrong answer:

```text
I would only add a better prompt.
```

Correction:

Productionization includes reliability, security, monitoring, deployment, testing, and data governance.

## Question 18: How would you secure it?

Short answer:

I would protect the API, secrets, data, logs, and model/tool usage.

Expanded answer:

Security improvements include authentication, authorization, HTTPS, input validation, rate limiting, secret management, safe logging, dependency scanning, container scanning, prompt injection checks, and access controls for documents.

Project example:

The current POC validates input with Pydantic but does not include authentication. That is acceptable for a local demo, not for production.

Common wrong answer:

```text
It is secure because it runs locally.
```

Correction:

Local demo scope reduces exposure, but production security still needs explicit controls.

## Question 19: How would you monitor it?

Short answer:

I would monitor requests, errors, latency, retrieval quality, tool calls, and model usage.

Expanded answer:

Monitoring should show how many requests are coming in, which endpoints fail, how long responses take, whether retrieval returns useful context, whether tool calls fail, and how much LLM usage costs. Logs should avoid secrets and sensitive data.

Project example:

For `/generate-test-cases`, useful metrics include request count, validation failures, workflow errors, and response time.

Common wrong answer:

```text
I would only look at terminal output.
```

Correction:

Terminal output is fine for a demo. Production needs structured logs, metrics, traces, dashboards, and alerts.

## Question 20: What is the biggest limitation of this POC?

Short answer:

The biggest limitation is that it uses simple local retrieval and mock generation.

Expanded answer:

That is acceptable for a beginner POC because the goal is to prove architecture and flow. It does not yet prove real LLM quality, semantic retrieval, authentication, production deployment, or enterprise monitoring.

Project example:

`retrieve_context` uses keyword matching, not embeddings.

Common wrong answer:

```text
There are no limitations.
```

Correction:

A strong interview answer should honestly explain scope and next improvements.
