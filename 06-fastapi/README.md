# 06 FastAPI

## 1. What This Module Is

This module teaches FastAPI from the point of view of a complete beginner who is learning how Python code becomes a web API.

FastAPI is a Python framework for building HTTP APIs. In simple words, it lets you write Python functions and expose them as endpoints that another program can call.

Example endpoint names:

```text
GET /health
POST /summarize
POST /generate-test-case
POST /ask-context
```

These are not just function names. They are public API doors. A browser, frontend, test script, Streamlit app, or another backend can send a request to one of these doors and receive a response.

## 2. Why AI Engineers Need FastAPI

Most AI work does not stay inside one Python notebook forever.

At first, you may write:

```text
prompt -> Python function -> printed answer
```

But a useful AI system usually needs this shape:

```text
Client -> FastAPI backend -> AI workflow -> JSON response
```

The client could be:

- a Streamlit UI
- a React frontend
- a Playwright API test
- another backend service
- a Docker/Kubernetes health checker
- a final POC demo script

FastAPI is useful because it gives you a clean backend layer around AI logic. You can expose summarization, RAG question-answering, test case generation, agent workflows, and health checks as APIs.

## 3. Main Beginner Mental Model

Keep this full request flow in your head:

```text
Client sends request -> Uvicorn receives it -> FastAPI matches route -> Python function runs -> response becomes JSON -> client receives response
```

Each piece has a different job:

- client sends the HTTP request
- Uvicorn is the local web server process
- FastAPI is the framework that knows your routes
- route decorator connects URL path to Python function
- route function contains your Python logic
- returned Python data is converted to JSON

This is the foundation for the whole module.

## 4. What You Will Learn

By the end of this module, you should be able to explain and use:

- what FastAPI is
- what Uvicorn is
- where `app` comes from
- what `FastAPI()` creates
- why `app = FastAPI()` matters
- what `@app.get("/health")` means
- what a decorator means in this context
- how a route function becomes an endpoint
- request and response basics
- automatic JSON conversion
- `main:app` syntax
- `--reload`
- Swagger UI at `/docs`
- GET vs POST
- path parameter vs query parameter
- request body vs response body
- Pydantic request models
- basic validation errors
- where FastAPI appears in the final POC

## 5. Study Order

Read the files in this order:

1. `00-overview.md`
2. `01-first-api-routes.md`
3. `02-request-body-pydantic-errors.md`
4. `implementation/fastapi-ai-helper-api/README.md`
5. `exercises.md`
6. `cheatsheet.md`
7. `interview-questions.md`

Do not start by memorizing commands. First understand the flow:

```text
request -> route match -> function call -> JSON response
```

Then the commands become easier.

## 6. Module Files

- `README.md`: this module guide and learning path.
- `00-overview.md`: beginner explanation of FastAPI, app object, Uvicorn, request flow, Swagger UI, JSON conversion, GET/POST, parameters, bodies, Pydantic, and errors.
- `01-first-api-routes.md`: route decorators, route functions, GET endpoints, path parameters, query parameters, and syntax decoding.
- `02-request-body-pydantic-errors.md`: POST request bodies, Pydantic models, validation, response bodies, and error handling basics.
- `exercises.md`: hands-on practice with task, commands, expected output, hints, self-checks, solution outline, and common mistakes.
- `cheatsheet.md`: compact command and syntax reference with meaning, use case, example, and caution notes.
- `interview-questions.md`: interview answers with short answer, expanded answer, project example, and common wrong answer.
- `implementation/fastapi-ai-helper-api/README.md`: runnable project instructions and troubleshooting.
- `implementation/fastapi-ai-helper-api/main.py`: mock AI helper backend.
- `implementation/fastapi-ai-helper-api/requirements.txt`: Python packages needed by the project.
- `implementation/fastapi-ai-helper-api/.env.example`: safe example configuration values.

## 7. Practical Scope

This module uses a mock AI backend.

That means the endpoints return fixed or simple Python-generated responses instead of calling a real LLM provider. This is intentional. Before adding OpenAI, Gemini, LangChain, RAG, MCP, Docker, or Kubernetes, you must be comfortable with:

- running a local API
- sending a request
- receiving JSON
- validating request bodies
- reading Swagger UI
- debugging common server startup errors

## 8. What FastAPI Gives Automatically

FastAPI gives you a lot of behavior after you write a small amount of code:

- route registration through decorators
- path parameter parsing
- query parameter parsing
- request body parsing
- Pydantic validation
- JSON response conversion
- OpenAPI schema generation
- Swagger UI at `/docs`
- validation error responses such as `422`

## 9. What You Still Write Manually

FastAPI does not write your business logic for you.

You still create:

- `main.py`
- the `app` object
- endpoint paths
- route functions
- request models
- returned response data
- AI workflow logic
- error decisions for your application

Beginner memory:

```text
FastAPI gives the web framework behavior.
You write the application behavior.
```

## 10. How This Helps In JRSS, Mettl, POC, And Interviews

For JRSS labs, FastAPI helps you build runnable backend endpoints.

For Mettl screening, FastAPI questions often test:

- decorators
- HTTP methods
- request body validation
- path and query parameters
- server command syntax

For the final POC, FastAPI becomes the backend between the UI and AI logic:

```text
Streamlit UI -> FastAPI API -> RAG/LLM/helper logic -> JSON response
```

For interviews, you should be able to explain this clearly:

```text
A client sends an HTTP request. Uvicorn receives it. FastAPI matches the method and path to a route function. The function runs Python logic and returns data. FastAPI converts the data to JSON and sends it back.
```
