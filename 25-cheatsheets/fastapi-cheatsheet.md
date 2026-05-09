# FastAPI Cheatsheet

## App Object

Syntax: `app = FastAPI()`

Meaning: Create the FastAPI application object.

Use when: Starting a backend API.

Example: Uvicorn runs `main:app`.

Be careful: `app` is a variable name, not magic.

## GET Route

Syntax:

```python
@app.get("/health")
def health():
    return {"status": "ok"}
```

Meaning: Register a GET endpoint at `/health`.

Use when: Reading data or checking status.

Example: health check endpoint.

Be careful: Decorator registers the route; it does not start the server.

## POST Route

Syntax:

```python
@app.post("/ask")
def ask(request: AskRequest):
    return {"answer": "mock"}
```

Meaning: Accept submitted data.

Use when: Client sends JSON body.

Example: generate test cases from requirement.

Be careful: Invalid body may return `422` before function runs.

## Uvicorn

Command: `uvicorn main:app --reload`

Meaning: Run `app` object from `main.py`.

Use when: Starting local FastAPI app.

Example: open Swagger UI at `/docs`.

Be careful: Run from the folder containing `main.py`.
