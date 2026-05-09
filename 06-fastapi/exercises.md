# FastAPI Exercises

These exercises are designed for beginners. Do not only make the endpoint work. After each exercise, explain the request flow in simple words.

Use this mental model:

```text
Client sends request -> Uvicorn receives it -> FastAPI matches route -> Python function runs -> response becomes JSON -> client receives response
```

## Exercise 1: Create And Run A Health Endpoint

### Task

Create a FastAPI app with:

```text
GET /health
```

It should return:

```json
{"status":"ok"}
```

### Practice File

Use a practice folder inside this module, for example:

```text
06-fastapi/practice/main.py
```

Do not create files outside `06-fastapi/`.

### Expected Code

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}
```

### Expected Commands

Command:

```powershell
cd 06-fastapi\practice
```

Where to run:

Run this from the course root folder.

What each part means:

- `cd` changes the current terminal folder
- `06-fastapi\practice` is the folder containing your practice `main.py`

Command:

```powershell
uvicorn main:app --reload
```

Where to run:

Run this from the folder that contains `main.py`.

What each part means:

- `uvicorn` starts the local server
- `main` means `main.py`
- `app` means the FastAPI object named `app`
- `--reload` restarts the server when code changes

### Expected Terminal Output

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

### Expected Browser Output

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

### Hints

- `app = FastAPI()` must exist before `@app.get(...)`.
- The route decorator must be directly above the function.
- Return a dictionary, not a printed string.

### Self-Check

Can you explain:

- where `app` comes from?
- what `FastAPI()` creates?
- what `@app.get("/health")` connects?
- why the browser receives JSON even though Python returned a dictionary?

### Solution Outline

1. Import `FastAPI`.
2. Create `app = FastAPI()`.
3. Add `@app.get("/health")`.
4. Define `health()`.
5. Return `{"status": "ok"}`.
6. Run `uvicorn main:app --reload`.
7. Test `/health`.

### Common Mistake

Running:

```powershell
uvicorn app:main --reload
```

This is wrong for this file because:

- the file is `main.py`
- the FastAPI object is `app`
- correct syntax is `main:app`

## Exercise 2: Add A Query Parameter

### Task

Create:

```text
GET /model-info?name=mock-llm
```

It should return the model name and mock mode.

### Expected Code

```python
@app.get("/model-info")
def model_info(name: str = "mock-llm"):
    return {"model": name, "mode": "mock"}
```

### Expected Commands

Command:

```powershell
uvicorn main:app --reload
```

Where to run:

Run this from the folder containing your `main.py`.

Expected browser URL:

```text
http://127.0.0.1:8000/model-info?name=mock-qa-model
```

### Expected Output

```json
{"model":"mock-qa-model","mode":"mock"}
```

If you omit the query parameter:

```text
http://127.0.0.1:8000/model-info
```

Expected output:

```json
{"model":"mock-llm","mode":"mock"}
```

### Hints

- Query parameters are function parameters that are not inside the route path.
- `name: str = "mock-llm"` gives a default value.

### Self-Check

Can you explain why `name` is a query parameter and not a path parameter?

### Solution Outline

1. Add the route decorator `@app.get("/model-info")`.
2. Add `name: str = "mock-llm"` as a function parameter.
3. Return a dictionary containing `name`.
4. Test with and without `?name=...`.

### Common Mistake

Writing:

```python
@app.get("/model-info/{name}")
```

This creates a path parameter. It is not wrong in general, but it does not match the task because the task asks for `?name=...`.

## Exercise 3: Add A Path Parameter

### Task

Create:

```text
GET /requirements/10
```

It should return:

```json
{"requirement_id":10}
```

### Expected Code

```python
@app.get("/requirements/{requirement_id}")
def get_requirement(requirement_id: int):
    return {"requirement_id": requirement_id}
```

### Expected Commands

Command:

```powershell
uvicorn main:app --reload
```

Test URL:

```text
http://127.0.0.1:8000/requirements/10
```

### Expected Output

```json
{"requirement_id":10}
```

### Hints

- The name inside `{}` should match the function parameter name.
- `requirement_id: int` tells FastAPI to convert the URL text into an integer.

### Self-Check

What should happen if you open:

```text
http://127.0.0.1:8000/requirements/abc
```

Expected answer:

FastAPI should return a validation error because `abc` is not an integer.

### Solution Outline

1. Add `@app.get("/requirements/{requirement_id}")`.
2. Add `requirement_id: int` to the function.
3. Return the ID in a dictionary.
4. Test with a number.
5. Test with text to observe validation.

### Common Mistake

Using different names:

```python
@app.get("/requirements/{id}")
def get_requirement(requirement_id: int):
    return {"requirement_id": requirement_id}
```

Use the same name in the path and function parameter.

## Exercise 4: Add A POST Endpoint With Pydantic

### Task

Create:

```text
POST /generate-test-case
```

The endpoint should accept this request body:

```json
{"requirement": "User can login"}
```

It should return generated mock test cases.

### Expected Code

```python
from pydantic import BaseModel

class TestCaseRequest(BaseModel):
    requirement: str

@app.post("/generate-test-case")
def generate_test_case(request: TestCaseRequest):
    return {
        "requirement": request.requirement,
        "test_cases": [
            {"title": "Valid scenario", "expected_result": "System accepts valid input"},
            {"title": "Invalid scenario", "expected_result": "System rejects invalid input"},
        ],
        "mode": "mock",
    }
```

### Expected Commands

Command:

```powershell
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Use the `POST /generate-test-case` section and click:

```text
Try it out -> Execute
```

### Expected Request

```json
{
  "requirement": "User can login"
}
```

### Expected Output

```json
{
  "requirement": "User can login",
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

### Hints

- POST endpoints commonly accept request bodies.
- The Pydantic model must inherit from `BaseModel`.
- Use `request.requirement` to access the field.

### Self-Check

Can you explain what happens before the route function runs?

Expected answer:

FastAPI reads the JSON body and Pydantic validates that it contains `requirement` as a string.

### Solution Outline

1. Import `BaseModel`.
2. Create `TestCaseRequest`.
3. Add a POST route decorator.
4. Type the function parameter as `TestCaseRequest`.
5. Return mock test cases.
6. Test valid JSON.
7. Test invalid JSON.

### Common Mistake

Sending:

```json
{"text": "User can login"}
```

This causes a validation error because the model expects `requirement`, not `text`.

## Exercise 5: Observe A Validation Error

### Task

Use Swagger UI to send invalid JSON to `POST /generate-test-case`.

### Expected Invalid Request

```json
{
  "wrong_field": "User can login"
}
```

### Expected Output

The exact response may vary by FastAPI/Pydantic version, but it should show a `422` validation error and mention that `requirement` is missing.

Example:

```json
{
  "detail": [
    {
      "loc": ["body", "requirement"],
      "msg": "Field required"
    }
  ]
}
```

### Hints

- Do not fix the request immediately.
- Read the error first.
- Find `loc` and `msg`.

### Self-Check

Did the route function run?

Expected answer:

No. FastAPI returned the validation error before calling the function.

### Solution Outline

1. Start the server.
2. Open `/docs`.
3. Open `POST /generate-test-case`.
4. Send a body with the wrong field.
5. Read the `422` response.
6. Replace the wrong field with `requirement`.
7. Confirm the endpoint works.

### Common Mistake

Ignoring the response body and only noticing "it failed." FastAPI validation errors usually tell you exactly which field is missing or invalid.

## Exercise 6: Add A Context Q&A Endpoint

### Task

Create:

```text
POST /ask-context
```

It should accept:

```json
{
  "question": "What is FastAPI?",
  "context": "FastAPI is a Python framework for APIs."
}
```

### Expected Code

```python
class ContextQuestionRequest(BaseModel):
    question: str
    context: str

@app.post("/ask-context")
def ask_context(request: ContextQuestionRequest):
    return {
        "question": request.question,
        "answer": f"Mock answer based on provided context: {request.context[:80]}",
    }
```

### Expected Commands

Command:

```powershell
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

### Expected Output

```json
{
  "question": "What is FastAPI?",
  "answer": "Mock answer based on provided context: FastAPI is a Python framework for APIs."
}
```

### Hints

- The request model needs two fields.
- Access them as `request.question` and `request.context`.
- This is a mock RAG-style endpoint shape.

### Self-Check

Why is POST better than GET for this endpoint?

Expected answer:

Because the question and context are structured input and can become too long for a clean URL.

### Solution Outline

1. Create `ContextQuestionRequest`.
2. Add `question: str`.
3. Add `context: str`.
4. Create `POST /ask-context`.
5. Return a mock answer.
6. Test through Swagger UI.

### Common Mistake

Trying to pass the context as a query parameter:

```text
/ask-context?question=...&context=...
```

That becomes messy for long text. Use a JSON request body.
