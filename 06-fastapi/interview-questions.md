# FastAPI Interview Questions

## 1. What is FastAPI?

Short answer:

FastAPI is a Python framework for building HTTP APIs.

Expanded answer:

FastAPI lets Python functions handle web requests and return responses, usually JSON. It provides route decorators, request parsing, Pydantic validation, automatic JSON conversion, and Swagger UI documentation.

Project example:

In the final POC, FastAPI can expose endpoints such as `POST /ask-context` and `POST /generate-test-case` so a Streamlit UI or test script can call AI functionality.

Common wrong answer:

FastAPI is only a server. The server process is usually Uvicorn. FastAPI defines the API application.

## 2. What is Uvicorn?

Short answer:

Uvicorn is the ASGI server that runs the FastAPI app.

Expanded answer:

FastAPI defines routes and application behavior. Uvicorn starts a web server process, receives HTTP requests, loads the FastAPI `app` object, and passes requests into the app.

Project example:

```powershell
uvicorn main:app --reload
```

This command runs the `app` object from `main.py`.

Common wrong answer:

Uvicorn and FastAPI are the same thing.

## 3. What does `app = FastAPI()` do?

Short answer:

It creates the FastAPI application object.

Expanded answer:

The app object stores route registrations, configuration, schema information, and the behavior Uvicorn loads when the server starts. Route decorators such as `@app.get(...)` are attached to this object.

Project example:

In `implementation/fastapi-ai-helper-api/main.py`, Uvicorn runs the object created by:

```python
app = FastAPI(title="FastAPI AI Helper API")
```

Common wrong answer:

`app` is created automatically by Uvicorn. You create it manually in Python.

## 4. What does `@app.get("/health")` mean?

Short answer:

It registers a GET endpoint at `/health` and connects it to the function below.

Expanded answer:

`@app.get("/health")` is a route decorator. `app` is the FastAPI application object, `.get` means register a GET route, and `"/health"` is the URL path. When a client sends `GET /health`, FastAPI calls the decorated function.

Project example:

```python
@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
```

Common wrong answer:

It calls the function immediately when the file loads. Actually, it registers the route. The function runs when a matching request arrives.

## 5. What is a route function?

Short answer:

A route function is the Python function that runs when a matching API request arrives.

Expanded answer:

The route decorator defines the HTTP method and path. The function below contains the Python logic. FastAPI calls that function when the request method and path match.

Project example:

`summarize(request: TextRequest)` is the function behind `POST /summarize`.

Common wrong answer:

The route and the function are the same thing. The route is the web access point; the function is the code that handles it.

## 6. What does `main:app` mean in `uvicorn main:app --reload`?

Short answer:

`main` means `main.py`, and `app` means the FastAPI object inside that file.

Expanded answer:

Uvicorn needs to know which Python module and which application object to load. The colon separates the module name from the object name.

Project example:

If the file is `main.py` and it contains `app = FastAPI()`, then `main:app` is correct.

Common wrong answer:

`main:app` is a URL path. It is not a URL path. It is Uvicorn's module-and-object syntax.

## 7. What does `--reload` do?

Short answer:

It restarts the server automatically when code changes.

Expanded answer:

`--reload` is useful during local development because you can edit `main.py`, save the file, and Uvicorn reloads the app. It is not the main concept of FastAPI itself; it is a Uvicorn development option.

Project example:

Use it while building the mock AI helper API:

```powershell
uvicorn main:app --reload
```

Common wrong answer:

`--reload` fixes code errors automatically. It only restarts the server; syntax or import errors still need to be fixed.

## 8. What is Swagger UI?

Short answer:

Swagger UI is FastAPI's automatically generated interactive API documentation at `/docs`.

Expanded answer:

FastAPI reads your routes, type hints, and Pydantic models to generate an OpenAPI schema. Swagger UI displays that schema in the browser and lets you test endpoints.

Project example:

Open:

```text
http://127.0.0.1:8000/docs
```

Then test `POST /generate-test-case` with a JSON body.

Common wrong answer:

Swagger UI is a separate frontend you must manually build. FastAPI generates it automatically.

## 9. What is the difference between GET and POST?

Short answer:

GET usually reads data. POST usually sends data for processing or creation.

Expanded answer:

GET requests commonly use path or query parameters. POST requests commonly include a JSON request body. AI APIs often use POST because prompts, questions, context, and requirements are structured input.

Project example:

`GET /health` checks whether the service is running. `POST /summarize` sends text to summarize.

Common wrong answer:

GET and POST are interchangeable. They have different HTTP semantics and different common usage patterns.

## 10. Path parameter vs query parameter?

Short answer:

A path parameter is part of the URL path. A query parameter appears after `?`.

Expanded answer:

Use a path parameter to identify a specific resource, such as `/requirements/10`. Use a query parameter for filters or options, such as `/search?topic=rag`.

Project example:

```python
@app.get("/requirements/{requirement_id}")
def get_requirement(requirement_id: int):
    return {"requirement_id": requirement_id}
```

```python
@app.get("/model-info")
def model_info(name: str = "mock-llm"):
    return {"model": name}
```

Common wrong answer:

All values should go in the path. Filters and optional values usually belong in query parameters.

## 11. Request body vs response body?

Short answer:

Request body is data sent by the client. Response body is data sent back by the server.

Expanded answer:

In FastAPI, POST endpoints often accept JSON request bodies validated by Pydantic. Route functions return Python data, and FastAPI converts it into a JSON response body.

Project example:

Request body:

```json
{"requirement": "User can login"}
```

Response body:

```json
{"requirement": "User can login", "test_cases": []}
```

Common wrong answer:

The request body and response body are the same thing. They move in opposite directions.

## 12. How does FastAPI convert dictionaries to JSON?

Short answer:

FastAPI automatically serializes returned Python data into JSON responses.

Expanded answer:

If a route function returns a dictionary, FastAPI converts it into a JSON response that an HTTP client can read. The developer writes Python data; FastAPI handles the HTTP response formatting.

Project example:

```python
return {"status": "ok"}
```

Client receives:

```json
{"status":"ok"}
```

Common wrong answer:

You must manually call `json.dumps()` for every response. For normal FastAPI responses, you usually return dictionaries or Pydantic models directly.

## 13. How does FastAPI validate request bodies?

Short answer:

FastAPI validates request bodies using Pydantic models.

Expanded answer:

You define a class that inherits from `BaseModel`. FastAPI reads the incoming JSON body, checks it against the model fields and types, and passes a validated object to the route function.

Project example:

```python
class RequirementRequest(BaseModel):
    requirement: str

@app.post("/generate-test-case")
def generate_test_case(request: RequirementRequest):
    return {"requirement": request.requirement}
```

Common wrong answer:

FastAPI accepts any JSON by default and your function must manually validate everything. If you use Pydantic models correctly, FastAPI validates before the function runs.

## 14. What is a `422` error in FastAPI?

Short answer:

It usually means request validation failed.

Expanded answer:

FastAPI returns `422 Unprocessable Entity` when the request shape or type does not match what the route expects. This can happen with missing body fields, wrong field types, invalid path parameters, or invalid query parameters.

Project example:

If `RequirementRequest` expects `requirement` and the client sends `{"text": "login"}`, FastAPI returns a validation error.

Common wrong answer:

`422` always means the server crashed. It usually means the client request did not match the expected schema.

## 15. Why use Pydantic models instead of normal dictionaries?

Short answer:

Pydantic models define and validate the expected data shape.

Expanded answer:

A dictionary stores data, but it does not enforce required fields or types by itself. A Pydantic model tells FastAPI what fields are required and what type each field should be.

Project example:

`ContextQuestionRequest` requires both `question` and `context` before the mock Q&A endpoint runs.

Common wrong answer:

Pydantic models and dictionaries are the same. They are related, but a model adds structure and validation.

## 16. Why is FastAPI useful for AI apps?

Short answer:

It exposes AI workflows as clean, validated HTTP APIs.

Expanded answer:

AI logic often needs to be called by UIs, test tools, schedulers, or other services. FastAPI wraps that logic in endpoints, validates input with Pydantic, and returns JSON responses.

Project example:

The final POC can use FastAPI as the backend for RAG, summarization, and test case generation.

Common wrong answer:

FastAPI itself is the AI model. FastAPI is the API framework around the AI logic.

## 17. Scenario: Uvicorn says it cannot import `main`. What do you check?

Short answer:

Check the current folder, file name, and `main:app` syntax.

Expanded answer:

`uvicorn main:app --reload` expects a file named `main.py` in the current folder and an object named `app` inside it. If either part is different, the command must change.

Project example:

If you run from the course root instead of `06-fastapi/implementation/fastapi-ai-helper-api`, Uvicorn may not find `main.py`.

Common wrong answer:

Reinstall FastAPI immediately. The problem is often the folder or object name, not the package.

## 18. Scenario: Endpoint works in Swagger UI but not from another client. What do you check?

Short answer:

Check URL, method, request body shape, headers, server status, and logs.

Expanded answer:

Swagger UI uses the schema FastAPI generated. Another client may be sending the wrong method, wrong path, missing JSON body, wrong field name, or wrong content type.

Project example:

The endpoint expects:

```json
{"requirement": "User can login"}
```

but a client sends:

```json
{"text": "User can login"}
```

Common wrong answer:

FastAPI is broken because another client failed. First compare the successful Swagger request with the failing client request.
