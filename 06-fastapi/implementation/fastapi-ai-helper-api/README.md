# fastapi-ai-helper-api

## 1. Project Goal

This project is a beginner FastAPI backend for a mock AI helper API.

It does not call a real LLM yet. Instead, it teaches the backend shape that later AI systems use:

```text
Client sends request -> Uvicorn receives it -> FastAPI matches route -> route function runs -> response becomes JSON
```

The API includes:

- `GET /health`
- `POST /summarize`
- `POST /generate-test-case`
- `POST /ask-context`

## 2. Project Files

Folder:

```text
06-fastapi/implementation/fastapi-ai-helper-api/
```

Files:

```text
main.py
requirements.txt
.env.example
README.md
```

### `main.py`

What it is:

The main FastAPI application file.

What it contains:

- imports
- `app = FastAPI(...)`
- Pydantic request models
- route decorators
- route functions
- mock AI responses

Why it matters:

This is the file Uvicorn loads when you run:

```powershell
uvicorn main:app --reload
```

### `requirements.txt`

What it is:

A list of Python packages needed by this project.

Current contents:

```text
fastapi
uvicorn
pydantic
```

Why it matters:

Instead of installing packages one by one, you can install the project dependencies with:

```powershell
pip install -r requirements.txt
```

### `.env.example`

What it is:

A safe example environment configuration file.

Current contents:

```text
APP_ENV=local
USE_MOCK_LLM=true
```

Why it matters:

Real projects often use environment variables for settings and secrets. This example uses safe placeholder values only.

Important:

This project does not require a real API key.

### `README.md`

What it is:

The file you are reading now.

Why it matters:

It explains how the project works, how to run it, what output to expect, and how to fix common beginner errors.

## 3. `main.py` Explained

Current code:

```python
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="FastAPI AI Helper API")


class TextRequest(BaseModel):
    text: str


class RequirementRequest(BaseModel):
    requirement: str


class ContextQuestionRequest(BaseModel):
    question: str
    context: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/summarize")
def summarize(request: TextRequest) -> dict:
    summary = request.text[:120]
    return {"summary": summary, "mode": "mock"}


@app.post("/generate-test-case")
def generate_test_case(request: RequirementRequest) -> dict:
    return {
        "requirement": request.requirement,
        "test_cases": [
            {"title": "Valid scenario", "expected_result": "System accepts valid input"},
            {"title": "Invalid scenario", "expected_result": "System rejects invalid input"},
        ],
        "mode": "mock",
    }


@app.post("/ask-context")
def ask_context(request: ContextQuestionRequest) -> dict:
    return {
        "question": request.question,
        "answer": f"Mock answer based on provided context: {request.context[:80]}",
    }
```

Line-by-line meaning:

- `from fastapi import FastAPI` imports the FastAPI class.
- `from pydantic import BaseModel` imports the base class for request validation models.
- `app = FastAPI(title="FastAPI AI Helper API")` creates the app object and gives Swagger UI a title.
- `class TextRequest(BaseModel)` defines the expected request body for `/summarize`.
- `text: str` means the JSON body must contain a string field named `text`.
- `class RequirementRequest(BaseModel)` defines the request body for `/generate-test-case`.
- `requirement: str` means the body must contain a string field named `requirement`.
- `class ContextQuestionRequest(BaseModel)` defines the request body for `/ask-context`.
- `question: str` and `context: str` require both fields.
- `@app.get("/health")` registers a GET endpoint.
- `def health() -> dict:` defines the function for `/health`.
- `return {"status": "ok"}` returns a Python dictionary that FastAPI converts to JSON.
- `@app.post("/summarize")` registers a POST endpoint.
- `request: TextRequest` tells FastAPI to validate the body with `TextRequest`.
- `request.text[:120]` uses the first 120 characters as a mock summary.
- `@app.post("/generate-test-case")` registers a POST endpoint for requirement input.
- `request.requirement` reads the validated requirement field.
- `@app.post("/ask-context")` registers a mock context Q&A endpoint.
- `request.context[:80]` uses a short slice of context for the mock answer.

What learner writes manually:

- the models
- the routes
- the functions
- the mock response logic

What FastAPI gives automatically:

- route matching
- request body parsing
- Pydantic validation
- JSON conversion
- Swagger UI
- validation error responses

## 4. Install Dependencies

Command:

```powershell
python -m venv .venv
```

Where to run:

Run this inside:

```text
06-fastapi/implementation/fastapi-ai-helper-api/
```

When to run:

Run once when setting up the project environment.

What each part means:

- `python` runs Python
- `-m` runs a Python module as a command
- `venv` is Python's virtual environment module
- `.venv` is the folder where the environment is created

Expected output:

Usually no long success message appears. A `.venv` folder should be created.

How to verify:

Run:

```powershell
Get-ChildItem -Force
```

You should see `.venv`.

Common beginner mistake:

Running this command from the wrong folder creates `.venv` in the wrong place.

Command:

```powershell
.\.venv\Scripts\Activate.ps1
```

Where to run:

Run from the project folder that contains `.venv`.

When to run:

Run before installing dependencies or starting the app.

What each part means:

- `.\.venv` points to the virtual environment folder
- `Scripts\Activate.ps1` is the PowerShell activation script

Expected output:

Your prompt may show `(.venv)`.

Common beginner mistake:

If PowerShell blocks the script, you may see an execution policy message. In that case, use your course environment setup guidance for PowerShell script activation.

Command:

```powershell
pip install -r requirements.txt
```

Where to run:

Run from:

```text
06-fastapi/implementation/fastapi-ai-helper-api/
```

When to run:

Run after activating the virtual environment.

What each part means:

- `pip` installs Python packages
- `install` tells pip to install packages
- `-r` means read package names from a file
- `requirements.txt` is the dependency list

Expected output:

```text
Successfully installed fastapi uvicorn pydantic ...
```

How to verify:

Run:

```powershell
pip show fastapi
```

Expected verification:

```text
Name: fastapi
Version: ...
Location: ...
```

Common beginner mistake:

Installing dependencies before activating `.venv`, then running the app with a different Python environment.

## 5. Run The App

Command:

```powershell
uvicorn main:app --reload
```

Where to run:

Run from:

```text
06-fastapi/implementation/fastapi-ai-helper-api/
```

When to run:

Run after dependencies are installed.

What each part means:

- `uvicorn` starts the local web server
- `main` means `main.py`
- `app` means the FastAPI object named `app`
- `--reload` restarts the server when code changes

Expected terminal output:

```text
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

The exact log prefix may vary, but the important parts are:

- server URL is shown
- application startup completes
- terminal stays running

Common beginner mistake:

Closing the terminal stops the server.

## 6. Expected Browser And API Output

### Health Check

Open:

```text
http://127.0.0.1:8000/health
```

Expected output:

```json
{"status":"ok"}
```

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

Expected output:

You should see the FastAPI AI Helper API documentation with:

- `GET /health`
- `POST /summarize`
- `POST /generate-test-case`
- `POST /ask-context`

### Summarize

In Swagger UI, test `POST /summarize`.

Request body:

```json
{
  "text": "FastAPI turns Python functions into API endpoints and automatically returns JSON."
}
```

Expected response:

```json
{
  "summary": "FastAPI turns Python functions into API endpoints and automatically returns JSON.",
  "mode": "mock"
}
```

### Generate Test Case

Request body:

```json
{
  "requirement": "User can login with valid credentials"
}
```

Expected response:

```json
{
  "requirement": "User can login with valid credentials",
  "test_cases": [
    {
      "title": "Valid scenario",
      "expected_result": "System accepts valid input"
    },
    {
      "title": "Invalid scenario",
      "expected_result": "System rejects invalid input"
    }
  ],
  "mode": "mock"
}
```

### Ask Context

Request body:

```json
{
  "question": "What is FastAPI?",
  "context": "FastAPI is a Python framework for building APIs."
}
```

Expected response:

```json
{
  "question": "What is FastAPI?",
  "answer": "Mock answer based on provided context: FastAPI is a Python framework for building APIs."
}
```

## 7. Common Errors And Fixes

### Error: `No module named 'fastapi'`

Meaning:

FastAPI is not installed in the active Python environment.

Fix:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Error: `Could not import module "main"`

Meaning:

Uvicorn cannot find `main.py` from the current folder.

Fix:

Run:

```powershell
cd 06-fastapi\implementation\fastapi-ai-helper-api
uvicorn main:app --reload
```

### Error: `Attribute "app" not found`

Meaning:

Uvicorn found `main.py`, but it could not find an object named `app`.

Fix:

Check that `main.py` contains:

```python
app = FastAPI(title="FastAPI AI Helper API")
```

### Error: `422 Unprocessable Entity`

Meaning:

The request did not match the expected Pydantic model.

Example cause:

Sending:

```json
{"text": "login"}
```

to `/generate-test-case`, which expects:

```json
{"requirement": "login"}
```

Fix:

Read the `detail` field in the error response and send the required field names.

### Error: Port Already In Use

Meaning:

Another server is already using port `8000`.

Fix:

Stop the other server, or run this app on another port:

```powershell
uvicorn main:app --reload --port 8001
```

Then open:

```text
http://127.0.0.1:8001/docs
```

## 8. What To Explain In A Demo

In a demo or interview, explain the project like this:

```text
This is a mock AI helper backend built with FastAPI. Uvicorn runs the app object from main.py. FastAPI maps endpoints such as /summarize and /generate-test-case to Python functions. Pydantic models validate the JSON request bodies. The functions return Python dictionaries, and FastAPI converts them into JSON responses. Swagger UI at /docs lets us test the API interactively.
```
