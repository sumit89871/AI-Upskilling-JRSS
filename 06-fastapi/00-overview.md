# FastAPI Overview

## 1. What FastAPI Is

FastAPI is a Python framework for building web APIs.

That definition is correct, but a beginner needs more than that.

Simple meaning:

```text
FastAPI lets a Python function respond to an HTTP request.
```

Example:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Plain English:

```text
When a client sends GET /health, run the health function and send back JSON.
```

FastAPI is the framework. It gives your Python project web API behavior such as routing, request parsing, validation, JSON responses, and Swagger UI.

## 2. Why FastAPI Is Useful For AI Engineers

AI Engineers often build logic that starts as normal Python:

```text
take text -> call model or mock model -> return answer
```

That is useful for learning, but another system cannot easily call it unless you expose it through an interface.

FastAPI gives you that interface.

Examples:

```text
POST /summarize
POST /ask-context
POST /generate-test-case
GET /health
```

In a final AI POC, the backend may look like this:

```text
Streamlit UI -> FastAPI endpoint -> RAG or LLM workflow -> JSON response -> UI displays answer
```

FastAPI is especially useful because it works naturally with Pydantic. Pydantic lets you describe the expected request body shape and lets FastAPI validate incoming JSON before your AI logic runs.

## 3. API Backend Mental Model

An API backend is a program that waits for requests and sends responses.

It is not a normal script that starts, prints something, and exits. A backend keeps running.

Normal script mental model:

```text
run file -> code executes -> program exits
```

FastAPI backend mental model:

```text
start server -> server waits -> client sends request -> matching function runs -> response returns -> server keeps waiting
```

The most important FastAPI flow:

```text
Client sends request -> Uvicorn receives it -> FastAPI matches route -> Python function runs -> response becomes JSON -> client receives response
```

Example with `/health`:

```text
Browser sends GET /health
Uvicorn receives the HTTP request
FastAPI checks registered routes
FastAPI finds @app.get("/health")
FastAPI calls health()
health() returns {"status": "ok"}
FastAPI converts the dictionary to JSON
Browser receives {"status":"ok"}
```

## 4. Where `app` Comes From

You create `app` manually in your Python file.

Code:

```python
from fastapi import FastAPI

app = FastAPI()
```

Read this in order:

```text
from fastapi import FastAPI -> bring the FastAPI class into this file
app = FastAPI() -> create one FastAPI application object and store it in app
```

`app` is just a variable name, but it is a very important variable. It points to the FastAPI application object.

Uvicorn later loads this object when you run:

```powershell
uvicorn main:app --reload
```

If your object was named `api` instead:

```python
api = FastAPI()
```

then your command would need to be:

```powershell
uvicorn main:api --reload
```

Beginner memory:

```text
app is the object Uvicorn runs.
FastAPI() creates that object.
```

## 5. What `FastAPI()` Creates

`FastAPI()` creates an application object.

That object stores the API configuration and route registrations. When you write route decorators such as `@app.get("/health")`, you are attaching endpoint information to this application object.

The object remembers things like:

- which paths exist
- which HTTP methods are allowed
- which Python function handles each route
- what request body models exist
- what schemas should appear in Swagger UI

FastAPI does not create your endpoint functions automatically. You write those functions. FastAPI stores the connection between the web request and your function.

## 6. What A Route Decorator Means

Code:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

The line `@app.get("/health")` is a decorator.

A decorator is syntax that attaches extra behavior to the function below it. In FastAPI, route decorators register route functions.

Read this line slowly:

```text
@ -> this is a decorator line
app -> use the FastAPI application object
.get -> register a GET endpoint
("/health") -> for the /health URL path
def health(): -> this function should run when that request matches
```

Plain English:

```text
Connect GET /health to the health() Python function.
```

Without the decorator, `health()` is just a normal Python function. With the decorator, FastAPI knows it is an API endpoint handler.

## 7. Route Function

A route function is the Python function FastAPI calls when a matching request arrives.

Example:

```python
def health():
    return {"status": "ok"}
```

This is normal Python syntax:

- `def` starts a function definition
- `health` is the function name
- `()` means this function has no parameters
- `return` sends a value back to the caller
- `{"status": "ok"}` is a Python dictionary

In normal Python, you would call it manually:

```python
health()
```

In FastAPI, the client request causes FastAPI to call it:

```text
GET /health -> FastAPI calls health()
```

## 8. Request And Response

A request is what the client sends to the API.

It may contain:

- HTTP method such as GET or POST
- URL path such as `/health`
- query parameters such as `?name=mock-llm`
- path parameters such as `/requirements/10`
- request body JSON such as `{"text": "hello"}`
- headers such as content type or authorization

A response is what the API sends back.

It usually contains:

- status code such as `200`, `404`, or `422`
- response body such as JSON
- headers

Beginner memory:

```text
request = client to server
response = server to client
```

## 9. Automatic JSON Conversion

In your route function, you often return a Python dictionary:

```python
return {"status": "ok"}
```

Python dictionary:

```text
{"status": "ok"}
```

JSON response:

```json
{"status":"ok"}
```

They look similar, but they are not the same thing.

A Python dictionary is a Python data structure inside your program. JSON is a text format sent over HTTP so other systems can understand the response.

FastAPI automatically converts common Python return values into JSON responses:

- dictionary -> JSON object
- list -> JSON array
- string/number/boolean -> JSON-compatible value
- Pydantic model -> JSON object

What you write manually:

```python
return {"summary": "FastAPI is useful"}
```

What FastAPI does automatically:

```text
convert Python dictionary into HTTP JSON response
```

## 10. Uvicorn

FastAPI defines your API, but it does not run the web server process by itself.

Uvicorn is the server that runs the FastAPI app locally.

FastAPI vs Uvicorn:

```text
FastAPI = framework used to define routes and API behavior
Uvicorn = server process that receives HTTP requests and runs the app
```

You usually run:

```powershell
uvicorn main:app --reload
```

The server then waits at a local URL such as:

```text
http://127.0.0.1:8000
```

## 11. What `main:app` Means

The syntax `main:app` is one of the most common beginner confusion points.

Command:

```powershell
uvicorn main:app --reload
```

Meaning:

- `uvicorn` starts the server
- `main` means find a file named `main.py`
- `:` separates the file/module name from the object name
- `app` means find a variable named `app` inside `main.py`
- `--reload` means restart automatically when code changes

If your file is:

```text
main.py
```

and inside it you have:

```python
app = FastAPI()
```

then `main:app` is correct.

If your file is `server.py`, then the command would be:

```powershell
uvicorn server:app --reload
```

If your object is named `api`, then the command would be:

```powershell
uvicorn main:api --reload
```

## 12. What `--reload` Does

`--reload` is a development convenience.

It tells Uvicorn:

```text
Watch the code files. If they change, stop and restart the app automatically.
```

Use it while learning and developing locally.

Be careful:

- it is useful for local development
- it should not be treated as the main production setting
- if you have a syntax error, the reload may fail until you fix the code

## 13. Swagger UI

Swagger UI is an interactive API documentation page generated automatically by FastAPI.

Open:

```text
http://127.0.0.1:8000/docs
```

You can use it to:

- see available endpoints
- see required request bodies
- test GET and POST requests
- view response schemas
- observe validation errors

You do not manually build this page. FastAPI generates it from your routes, type hints, and Pydantic models.

What you write:

```python
class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: TextRequest):
    return {"summary": request.text[:50]}
```

What FastAPI generates:

```text
/docs page showing POST /summarize and the expected JSON body shape
```

## 14. GET vs POST

GET is usually used to read or fetch data.

Example:

```text
GET /health
GET /model-info?name=mock-llm
```

POST is usually used to send data for processing or creation.

Example:

```text
POST /summarize
POST /generate-test-case
```

Beginner comparison:

```text
GET = ask for information
POST = send information to be processed
```

In AI APIs, POST is common because prompts, context, requirements, and documents are often too large or too structured to put in a URL.

## 15. Path Parameter vs Query Parameter

A path parameter is part of the URL path.

Example:

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

A query parameter comes after `?`.

Example:

```python
@app.get("/model-info")
def model_info(name: str = "mock-llm"):
    return {"model": name}
```

Request:

```text
GET /model-info?name=mock-qa-model
```

Meaning:

```text
name = mock-qa-model
```

Simple rule:

```text
Path parameter identifies a specific thing.
Query parameter filters or provides options.
```

## 16. Request Body vs Response Body

Request body is data sent by the client to the server.

Example request body:

```json
{
  "text": "FastAPI is useful for AI backends."
}
```

Response body is data sent by the server back to the client.

Example response body:

```json
{
  "summary": "FastAPI is useful for AI backends."
}
```

In FastAPI, request bodies are common with POST endpoints:

```python
@app.post("/summarize")
def summarize(request: TextRequest):
    return {"summary": request.text[:120]}
```

## 17. Pydantic Model In FastAPI

Pydantic models define the expected shape of data.

Code:

```python
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str
```

Read this slowly:

- `class` creates a class
- `TextRequest` is the model name
- `(BaseModel)` gives it Pydantic validation behavior
- `text: str` means the JSON body must contain `text` as a string

Use it in an endpoint:

```python
@app.post("/summarize")
def summarize(request: TextRequest):
    return {"summary": request.text[:120]}
```

Meaning:

```text
FastAPI reads the incoming JSON body, validates it as TextRequest, then gives the route function a request object.
```

If the client sends:

```json
{"text": "hello"}
```

the function can access:

```python
request.text
```

If the client sends:

```json
{"wrong": "hello"}
```

FastAPI returns a validation error before your function runs.

## 18. Error Handling Basics

FastAPI gives automatic validation errors.

Common example:

```text
422 Unprocessable Entity
```

This often means:

- required field is missing
- field has the wrong type
- path parameter could not be converted
- request body JSON does not match the Pydantic model

Example error:

```json
{
  "detail": [
    {
      "loc": ["body", "text"],
      "msg": "Field required"
    }
  ]
}
```

Meaning:

- `detail` contains the error list
- `body` says the problem is in the request body
- `text` says the missing field is named `text`
- `Field required` says the client did not send it

You can also raise your own errors later with `HTTPException`, for example when a requested item does not exist. This module focuses first on validation and beginner request flow.

## 19. Full First Example

File name:

```text
main.py
```

Folder path:

```text
06-fastapi/implementation/fastapi-ai-helper-api/main.py
```

What this file is for:

This file creates a small FastAPI app with mock AI helper endpoints.

Small version:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

Line-by-line explanation:

- `from fastapi import FastAPI` imports the FastAPI class from the installed package
- `app = FastAPI()` creates the application object
- `@app.get("/health")` registers a GET endpoint for `/health`
- `def health():` defines the function FastAPI will call
- `return {"status": "ok"}` returns a Python dictionary
- FastAPI converts that dictionary into JSON automatically

What learner creates manually:

- the `main.py` file
- the `app` variable
- the route decorator
- the route function
- the returned dictionary

What the framework gives automatically:

- route registration behavior
- request handling
- JSON conversion
- Swagger UI
- OpenAPI schema

## 20. How To Run

Command:

```powershell
uvicorn main:app --reload
```

Where to run:

Run it from the folder that contains `main.py`:

```powershell
cd 06-fastapi\implementation\fastapi-ai-helper-api
uvicorn main:app --reload
```

When to run:

Run it after dependencies are installed and you want to start the local API.

What each part means:

- `uvicorn` starts the local web server
- `main` means `main.py`
- `app` means the FastAPI object named `app`
- `--reload` restarts the server after code changes

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

How to verify:

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

Open:

```text
http://127.0.0.1:8000/docs
```

Expected result:

Swagger UI should show the registered endpoints.

Common beginner mistake:

Running `uvicorn main:app --reload` from the wrong folder. Uvicorn then cannot find `main.py`.

## 21. Where FastAPI Appears In The Final POC

In the final POC, FastAPI is the backend layer.

Likely flow:

```text
User enters question in Streamlit
Streamlit sends POST request to FastAPI
FastAPI validates request body with Pydantic
FastAPI route function calls RAG or mock AI helper
AI helper returns answer
FastAPI sends JSON response
Streamlit displays answer
```

This module prepares you to explain and build that backend layer clearly.
