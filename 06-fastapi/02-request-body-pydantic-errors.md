# Request Body, Pydantic, And Errors

## 1. What A Request Body Is

A request body is data sent from the client to the server as part of an HTTP request.

In FastAPI, request bodies are usually JSON.

Example request body:

```json
{
  "text": "FastAPI is useful for AI backend APIs."
}
```

This is different from a path parameter or query parameter.

Comparison:

```text
/requirements/10              -> path parameter
/search?topic=rag             -> query parameter
{"text": "hello"}             -> request body
```

## 2. The Most Important Beginner Idea

FastAPI does not guess your request body shape.

You define the expected shape with a Pydantic model:

```python
class TextRequest(BaseModel):
    text: str
```

This tells FastAPI:

```text
The JSON request body must have a field named text, and text must be a string.
```

If the request is valid, your route function runs.

If the request is invalid, FastAPI returns a validation error before your route function runs.

## 3. Why Request Bodies Matter For AI Apps

AI endpoints often need more than a short value in the URL.

Examples:

- text to summarize
- a requirement to turn into test cases
- a question plus context
- a prompt plus settings
- document metadata

These values belong in a JSON request body because they are structured input.

Example:

```json
{
  "question": "What is FastAPI?",
  "context": "FastAPI is a Python framework for APIs."
}
```

The backend can validate this input before calling any mock AI logic, LLM, RAG pipeline, or agent workflow.

## 4. Beginner Mental Model

Request body flow:

```text
Client sends JSON -> FastAPI receives request -> Pydantic checks shape -> route function runs -> function returns response body
```

If validation fails:

```text
Client sends wrong JSON -> Pydantic detects problem -> FastAPI returns 422 -> route function does not run
```

## 5. Full Code Example

File name:

```text
main.py
```

Folder path:

```text
06-fastapi/implementation/fastapi-ai-helper-api/main.py
```

What this file is for:

This file creates FastAPI endpoints that accept JSON bodies and return mock AI responses.

Small example:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
def summarize(request: TextRequest):
    summary = request.text[:120]
    return {"summary": summary, "mode": "mock"}
```

## 6. Line-By-Line Explanation

```python
from fastapi import FastAPI
```

Imports the FastAPI class so you can create the app object.

```python
from pydantic import BaseModel
```

Imports `BaseModel`, the parent class used to create validation models.

```python
app = FastAPI()
```

Creates the FastAPI application object.

```python
class TextRequest(BaseModel):
    text: str
```

Creates a Pydantic model.

Decode it:

- `class` creates a class
- `TextRequest` is the model name
- `(BaseModel)` gives the class Pydantic validation behavior
- `text: str` says the request body must contain `text` as a string

```python
@app.post("/summarize")
```

Registers a POST endpoint at `/summarize`.

```python
def summarize(request: TextRequest):
```

Defines the route function. The parameter `request: TextRequest` tells FastAPI to read the JSON request body and validate it with the `TextRequest` model.

```python
summary = request.text[:120]
```

Reads the validated `text` field and takes the first 120 characters.

```python
return {"summary": summary, "mode": "mock"}
```

Returns a Python dictionary. FastAPI converts it to a JSON response body.

## 7. What Learner Creates Manually

You create:

- Pydantic model class
- endpoint decorator
- endpoint function
- function parameter
- response dictionary
- mock AI logic

## 8. What FastAPI And Pydantic Give Automatically

FastAPI and Pydantic automatically:

- read the JSON body
- check required fields
- check field types
- create a request object
- block invalid requests
- return `422` validation errors
- convert response dictionaries to JSON
- show request schemas in Swagger UI

## 9. POST Request Body Example

Endpoint:

```text
POST /summarize
```

Expected request body:

```json
{
  "text": "FastAPI is useful for AI backend APIs."
}
```

Expected response body:

```json
{
  "summary": "FastAPI is useful for AI backend APIs.",
  "mode": "mock"
}
```

Request body:

```text
client -> server
```

Response body:

```text
server -> client
```

## 10. Pydantic Model vs Dictionary

A dictionary stores actual data:

```python
{"text": "hello"}
```

A Pydantic model defines and validates the expected shape:

```python
class TextRequest(BaseModel):
    text: str
```

FastAPI uses the model to decide whether the incoming dictionary-like JSON is acceptable.

Beginner memory:

```text
JSON body = data the client sends
Pydantic model = rules for that data
request object = validated data inside Python
```

## 11. Accessing Request Body Data

After validation, FastAPI gives your function a Pydantic object.

Code:

```python
def summarize(request: TextRequest):
    return {"summary": request.text}
```

`request.text` means:

```text
read the text field from the validated request object
```

Common mistake:

```python
return {"summary": text}
```

This is wrong because there is no variable named `text`. The value is inside `request.text`.

## 12. Multiple Body Fields

Example:

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

Expected request:

```json
{
  "question": "What is FastAPI?",
  "context": "FastAPI is a Python framework used to build APIs."
}
```

Expected response:

```json
{
  "question": "What is FastAPI?",
  "answer": "Mock answer based on provided context: FastAPI is a Python framework used to build APIs."
}
```

## 13. Default Values

Pydantic models can include defaults:

```python
class TestCaseRequest(BaseModel):
    requirement: str
    priority: str = "P3"
```

Meaning:

- `requirement` is required
- `priority` is optional
- if the client does not send `priority`, Pydantic uses `"P3"`

Request:

```json
{
  "requirement": "User can login"
}
```

Inside Python:

```text
request.priority is "P3"
```

## 14. Validation Error Example

Model:

```python
class TextRequest(BaseModel):
    text: str
```

Invalid request:

```json
{
  "wrong": "hello"
}
```

Possible FastAPI response:

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "text"],
      "msg": "Field required"
    }
  ]
}
```

How to read it:

- `detail` is the list of validation problems
- `body` means the problem is in the request body
- `text` means the missing field is named `text`
- `Field required` means the client did not send a required field

## 15. Path And Query Validation Errors

FastAPI also validates path and query parameters.

Example:

```python
@app.get("/requirements/{requirement_id}")
def get_requirement(requirement_id: int):
    return {"requirement_id": requirement_id}
```

Valid:

```text
/requirements/10
```

Invalid:

```text
/requirements/abc
```

Because `abc` cannot be converted to an integer, FastAPI returns a validation error.

## 16. Error Handling Basics With `HTTPException`

Validation errors are automatic. Application errors are your decision.

Example:

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/requirements/{requirement_id}")
def get_requirement(requirement_id: int):
    if requirement_id <= 0:
        raise HTTPException(status_code=400, detail="requirement_id must be positive")
    return {"requirement_id": requirement_id}
```

Meaning:

- FastAPI validates that `requirement_id` is an integer
- your code checks whether it is positive
- `HTTPException` sends a controlled error response

Expected invalid response for `/requirements/0`:

```json
{
  "detail": "requirement_id must be positive"
}
```

## 17. How To Run

Command:

```powershell
uvicorn main:app --reload
```

Where to run:

Run from the folder that contains `main.py`:

```powershell
cd 06-fastapi\implementation\fastapi-ai-helper-api
uvicorn main:app --reload
```

What each part means:

- `uvicorn` starts the server
- `main` means `main.py`
- `app` means the FastAPI object named `app`
- `--reload` restarts the server when code changes

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

Use Swagger UI to test POST endpoints with valid and invalid JSON.

## 18. Common Mistakes

- Forgetting `from pydantic import BaseModel`.
- Creating a model class but not inheriting from `BaseModel`.
- Sending the wrong field name.
- Sending a string when the model expects a number.
- Trying to read `request["text"]` when using a Pydantic object instead of `request.text`.
- Expecting a GET request to have a request body.
- Thinking type hints alone validate data. Pydantic performs the runtime validation.
- Ignoring the `422` response details.

## 19. Similar Concepts Beginners Confuse

Request body vs response body:

```text
request body = client sends data to server
response body = server sends data to client
```

Pydantic model vs dictionary:

```text
Pydantic model = validation rules and object shape
dictionary = actual key-value data
```

Validation error vs application error:

```text
validation error = request did not match expected shape
application error = your code decided the request cannot be processed
```

POST body vs query parameter:

```text
POST body = structured data, often JSON
query parameter = small option/filter in URL
```

## 20. Where Used In AI Engineer Work

Pydantic request bodies are used for:

- LLM prompt input
- summarization requests
- RAG question and context input
- test case generation requests
- agent workflow input
- tool execution parameters
- API validation in POCs
- interview explanations about reliable backend design
