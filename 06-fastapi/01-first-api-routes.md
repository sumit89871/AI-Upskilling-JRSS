# First API And Routes

## 1. What A Route Is

A route connects an HTTP method and URL path to a Python function.

Simple meaning:

```text
Route = if this request comes in, run this function
```

Example:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Plain English:

```text
GET /health -> health() -> {"status": "ok"}
```

The route is the public API access point. The function is the Python code behind that access point.

## 2. The Most Important Beginner Idea

The decorator connects the web world to the Python world.

Without this line:

```python
@app.get("/health")
```

the function below it is only a normal Python function.

With that line, FastAPI registers the function as an endpoint handler. That means FastAPI stores this rule:

```text
When a GET request comes to /health, call health().
```

## 3. Where `app` Comes From

Before you can write routes, you need the FastAPI app object:

```python
from fastapi import FastAPI

app = FastAPI()
```

Breakdown:

- `from fastapi import FastAPI` imports the FastAPI class
- `FastAPI()` creates a FastAPI application object
- `app =` stores that object in a variable named `app`
- route decorators such as `@app.get(...)` are called on this `app` object

The route decorator does not come from nowhere. It is a method on the FastAPI app object.

## 4. What `@app.get("/health")` Means

Code:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Read the decorator in this order:

```text
@ -> decorator syntax
app -> FastAPI application object
.get -> register a GET route
("/health") -> URL path for this route
```

Read the full block as:

```text
Register a GET endpoint at /health.
When that endpoint is called, run the health function.
Return the dictionary as JSON.
```

## 5. What A Decorator Means Here

A Python decorator wraps or modifies a function.

In FastAPI beginner terms, a route decorator registers the function below it as a route handler.

You do not need advanced decorator theory yet. For this module, remember:

```text
@app.get("/health") attaches API route behavior to health().
```

Common mistake:

```python
app.get("/health")
def health():
    return {"status": "ok"}
```

This is wrong because the `@` is missing. FastAPI will not treat the next function as the route handler.

## 6. GET Route

GET is usually used to read information.

Example:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Use GET for:

- health checks
- reading model information
- reading one item by ID
- search or filter requests with query parameters

Expected request:

```text
GET http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

## 7. Route Function

The route function is the function FastAPI calls after a request matches.

Example:

```python
def health():
    return {"status": "ok"}
```

Line-by-line:

- `def` defines a function
- `health` is the function name
- `()` means there are no inputs for this function
- `return` sends data back
- `{"status": "ok"}` is a Python dictionary

In normal Python, a function runs only when another line calls it:

```python
health()
```

In FastAPI, the matching HTTP request triggers the function:

```text
GET /health triggers health()
```

## 8. Dictionary To JSON

Most beginner FastAPI endpoints return dictionaries:

```python
return {"status": "ok"}
```

FastAPI converts this Python dictionary to JSON automatically.

Developer writes:

```python
{"status": "ok"}
```

Client receives:

```json
{"status":"ok"}
```

This automatic conversion is one reason FastAPI is beginner-friendly. You focus on returning Python data structures. FastAPI handles the HTTP JSON response.

## 9. Path Parameter

A path parameter is a value inside the URL path.

Code:

```python
@app.get("/requirements/{requirement_id}")
def get_requirement(requirement_id: int):
    return {"requirement_id": requirement_id}
```

Request:

```text
GET /requirements/10
```

Meaning:

```text
requirement_id = 10
```

Syntax breakdown:

- `"/requirements/{requirement_id}"` declares a variable part of the path
- `{requirement_id}` must match the function parameter name
- `requirement_id: int` tells FastAPI to convert the value to an integer
- `return {"requirement_id": requirement_id}` returns the parsed value

Expected response:

```json
{"requirement_id":10}
```

Common mistake:

```python
@app.get("/requirements/{id}")
def get_requirement(requirement_id: int):
    return {"requirement_id": requirement_id}
```

The path uses `{id}`, but the function expects `requirement_id`. The names should match unless you intentionally use advanced patterns.

## 10. Query Parameter

A query parameter comes after `?` in the URL.

Code:

```python
@app.get("/model-info")
def model_info(name: str = "mock-llm"):
    return {"model": name, "mode": "mock"}
```

Request:

```text
GET /model-info?name=mock-qa-model
```

Meaning:

```text
name = mock-qa-model
```

Syntax breakdown:

- `/model-info` is the route path
- `?name=mock-qa-model` is the query string
- `name: str = "mock-llm"` defines a query parameter with a default value
- if the client does not send `name`, FastAPI uses `"mock-llm"`

Expected response:

```json
{"model":"mock-qa-model","mode":"mock"}
```

If you open:

```text
http://127.0.0.1:8000/model-info
```

Expected response:

```json
{"model":"mock-llm","mode":"mock"}
```

## 11. Path Parameter vs Query Parameter

Use a path parameter when the value identifies a specific resource.

Examples:

```text
/requirements/10
/users/42
/documents/abc123
```

Use a query parameter when the value filters, searches, sorts, or changes options.

Examples:

```text
/requirements?priority=P1
/search?topic=rag
/model-info?name=mock-llm
```

Beginner memory:

```text
Path parameter = which thing?
Query parameter = what option/filter?
```

## 12. GET vs POST

GET is usually for reading data.

POST is usually for sending data to be processed.

FastAPI examples:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

```python
@app.post("/summarize")
def summarize(request: TextRequest):
    return {"summary": request.text[:120]}
```

For AI work:

- `GET /health` checks if the backend is running
- `POST /summarize` sends text to be summarized
- `POST /ask-context` sends question and context
- `POST /generate-test-case` sends a requirement to process

## 13. Full Small Example

File name:

```text
main.py
```

Folder path:

```text
06-fastapi/implementation/fastapi-ai-helper-api/main.py
```

What this file is for:

This file defines a FastAPI app and route functions for a mock AI helper backend.

Example code:

```python
from fastapi import FastAPI

app = FastAPI(title="AI Helper")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/model-info")
def model_info(name: str = "mock-llm"):
    return {"model": name, "mode": "mock"}

@app.get("/requirements/{requirement_id}")
def get_requirement(requirement_id: int):
    return {"requirement_id": requirement_id}
```

What learner creates manually:

- the import
- `app = FastAPI(...)`
- route decorators
- route functions
- return dictionaries

What FastAPI gives automatically:

- route matching
- query parameter parsing
- path parameter parsing
- type conversion
- validation errors
- JSON response conversion
- Swagger UI

## 14. How To Run

Command:

```powershell
uvicorn main:app --reload
```

Where to run:

Run it from the folder containing `main.py`.

For this project:

```powershell
cd 06-fastapi\implementation\fastapi-ai-helper-api
uvicorn main:app --reload
```

When to run:

Run it after installing dependencies and after saving `main.py`.

What each part means:

- `uvicorn` starts the server
- `main` means `main.py`
- `app` means the FastAPI object named `app`
- `--reload` restarts automatically when files change

Expected terminal output:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

How to verify:

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI should list your routes.

## 15. Common Mistakes

- Forgetting the `@` before `app.get`.
- Running Uvicorn from a folder that does not contain `main.py`.
- Writing `uvicorn app:main` when the file is `main.py` and the object is `app`.
- Returning printed text instead of returning a value.
- Confusing path parameters with query parameters.
- Sending `/requirements/abc` when `requirement_id` is typed as `int`.
- Thinking FastAPI writes your route functions automatically.
- Defining two functions with the same name and confusing yourself while debugging.

## 16. Similar Concepts Beginners Confuse

Route vs function:

```text
route = HTTP method plus URL path
function = Python code that runs for the route
```

FastAPI vs Uvicorn:

```text
FastAPI defines the app.
Uvicorn runs the app.
```

Dictionary vs JSON:

```text
dictionary = Python data inside your function
JSON = HTTP response format sent to the client
```

Endpoint vs URL:

```text
endpoint = API route definition
URL = full address used to call it
```

## 17. Quick Practice

Create these routes:

```text
GET /health
GET /version
GET /requirements/{requirement_id}
GET /search?topic=rag
```

For each route, write:

- route decorator
- function name
- expected URL
- expected JSON response
- whether it uses no parameter, path parameter, or query parameter

## 18. Where Used In AI Engineer Work

Routes appear in:

- final POC backend
- RAG question-answering API
- LLM summarization API
- test generation API
- Docker and Kubernetes health checks
- Playwright API tests
- interview architecture explanations
