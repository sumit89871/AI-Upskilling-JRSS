# Pydantic Overview

## 1. What Pydantic is

Pydantic is a Python library for validating data using classes and type hints.

Simple meaning:

```text
Pydantic checks whether incoming data matches the shape your code expects.
```

Example:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
```

This model says:

```text
A valid User must have:
- name as text
- age as integer
```

Pydantic is not only for FastAPI. FastAPI uses it heavily, but you can also use Pydantic in normal Python scripts, GenAI output validation, RAG response validation, MCP tool payloads, and agent state.

## 2. The most important beginner idea

Type hints alone do not validate runtime data in normal Python.

Example:

```python
def greet(name: str) -> str:
    return "Hello " + name
```

The `name: str` type hint tells readers and tools that `name` should be a string.

But normal Python does not automatically block this at runtime:

```python
greet(123)
```

Pydantic is different because it validates real input data when you create or validate a model.

Beginner memory:

```text
Type hint = expected type
Pydantic validation = actual runtime check
```

## 3. Why validation matters

Validation matters because real applications receive data from outside your code.

Examples:

- user sends JSON to a FastAPI endpoint
- LLM returns structured JSON
- RAG pipeline returns answer and sources
- agent workflow passes state between nodes
- MCP tool receives input from an AI client

Your app should not blindly trust incoming data.

Bad flow:

```text
raw input -> app logic -> crash later
```

Better flow:

```text
raw input -> validation -> clean object -> safe app logic
```

## 4. Why AI/API apps need structured data

AI apps often need data that has a predictable shape.

Example structured test case output:

```json
{
  "title": "Valid login",
  "priority": "P1",
  "expected_result": "Dashboard opens"
}
```

This is easier to use than free text because your app can display it in a table, save it as JSON, return it from FastAPI, or pass it to a reviewer node.

If an LLM returns:

```text
Here are some tests, maybe valid login and invalid password...
```

That may be readable by a human, but difficult for code to reliably parse.

Pydantic helps check that structured output really has the fields your app expects.

## 5. Beginner mental model

Use this mental model:

```text
Raw input data -> Pydantic model -> validation -> clean Python object -> safe app logic / API response / structured AI output
```

Expanded:

```text
dictionary or JSON-like data
    -> model describes expected shape
    -> Pydantic checks fields and types
    -> valid data becomes a model object
    -> invalid data raises a validation error
```

## 6. BaseModel

`BaseModel` is the parent class that gives your class Pydantic behavior.

Example:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
```

Syntax breakdown:

- `from pydantic import BaseModel` imports `BaseModel` from the installed `pydantic` package.
- `class` creates a class.
- `User` is the model class name chosen by the developer.
- `(BaseModel)` means `User` inherits from Pydantic's `BaseModel`.
- `:` starts the indented class body.

### BaseModel inheritance

Inheritance means one class receives behavior from another class.

Here:

```text
User inherits from BaseModel
```

That means `User` gets Pydantic features such as:

- validation
- `model_validate`
- `model_dump`
- error reporting
- typed field handling

If you forget `(BaseModel)`, your class becomes a normal Python class and Pydantic validation will not happen.

## 7. Class fields

Inside a Pydantic model, fields describe expected data.

Example:

```python
class User(BaseModel):
    name: str
    age: int
```

Field meaning:

- `name` is a field.
- `str` means the value should be text.
- `age` is a field.
- `int` means the value should be an integer.

Class field syntax:

```text
field_name: type
```

The colon `:` means:

```text
this field is expected to have this type
```

This is different from assignment.

Assignment uses `=`.

Example:

```python
model: str = "mock-llm"
```

This means:

- field name is `model`
- expected type is `str`
- default value is `"mock-llm"`

## 8. Required fields

A field is required when it has no default value.

Example:

```python
class User(BaseModel):
    name: str
    age: int
```

Both `name` and `age` are required.

Valid:

```python
User.model_validate({"name": "Asha", "age": 30})
```

Invalid:

```python
User.model_validate({"name": "Asha"})
```

Why invalid:

`age` is missing.

## 9. Optional fields

An optional field may be missing or may be `None`.

Example:

```python
class UserProfile(BaseModel):
    name: str
    email: str | None = None
```

Syntax breakdown:

- `email` is the field name.
- `str | None` means the value can be a string or `None`.
- `= None` gives a default value of `None`.
- Because there is a default, the caller can skip the field.

Important beginner warning:

```python
email: str | None
```

This allows `email` to be a string or `None`, but it may still be required because there is no default value.

For a truly optional field in beginner code, use:

```python
email: str | None = None
```

## 10. Default values

A default value is used when the caller does not provide that field.

Example:

```python
class PromptRequest(BaseModel):
    prompt: str
    model: str = "mock-llm"
    max_tokens: int = 300
```

Input:

```python
{"prompt": "Explain RAG"}
```

Result:

```python
{
    "prompt": "Explain RAG",
    "model": "mock-llm",
    "max_tokens": 300
}
```

### Default value vs missing value

Missing value means the input did not include the field.

Default value means Pydantic can fill it automatically.

If a required field is missing, validation fails.

If a default field is missing, Pydantic uses the default.

## 11. Nested models

A nested model is a Pydantic model inside another Pydantic model.

Example:

```python
class TestCase(BaseModel):
    title: str
    priority: str


class TestCaseResponse(BaseModel):
    requirement: str
    test_cases: list[TestCase]
```

This means:

- `TestCase` describes one test case.
- `TestCaseResponse` describes the full response.
- `test_cases: list[TestCase]` means `test_cases` must be a list.
- every item in the list must match the `TestCase` model.

## 12. List of objects

Syntax:

```python
test_cases: list[TestCase]
```

Read it slowly:

```text
test_cases -> is expected to be -> a list -> where each item is a TestCase
```

Valid:

```python
{
    "test_cases": [
        {"title": "Valid login", "priority": "P1"},
        {"title": "Invalid password", "priority": "P2"}
    ]
}
```

Invalid:

```python
{
    "test_cases": {"title": "Valid login", "priority": "P1"}
}
```

Why invalid:

The model expects a list, but the input gives a single dictionary.

## 13. Validation errors

A validation error happens when input does not match the model.

Example:

```python
User.model_validate({"name": "Asha", "age": "thirty"})
```

Possible error message:

```text
1 validation error for User
age
  Input should be a valid integer, unable to parse string as an integer
```

Output meaning:

- `1 validation error for User` means one field failed validation.
- `age` identifies the field with the problem.
- `Input should be a valid integer` explains what Pydantic expected.
- `unable to parse string as an integer` explains why `"thirty"` failed.

### Validation error vs Python exception

A validation error is a specific kind of Python exception raised by Pydantic.

It is still an exception, but it is more informative than a random crash later.

Example:

```python
from pydantic import ValidationError

try:
    User.model_validate({"name": "Asha", "age": "thirty"})
except ValidationError as error:
    print(error)
```

## 14. model_validate

`model_validate` checks raw input and returns a Pydantic model object if valid.

Example:

```python
user = User.model_validate({"name": "Asha", "age": 30})
```

Syntax breakdown:

- `User` is the Pydantic model class.
- `.model_validate(...)` calls Pydantic validation.
- `{...}` is the raw dictionary input.
- `user` stores the validated model object.

After validation:

```python
print(user.name)
print(user.age)
```

## 15. model_dump

`model_dump` converts a Pydantic model object back to a normal Python dictionary.

Example:

```python
data = user.model_dump()
```

Syntax breakdown:

- `user` is a Pydantic model object.
- `.model_dump()` converts it to a dictionary.
- `data` stores the dictionary.

Use `model_dump()` when:

- returning JSON-like data
- passing data to another function
- logging validated data
- preparing structured output for API response

## 16. Pydantic model vs Python dictionary

| Concept | Meaning | Example access |
|---|---|---|
| Python dictionary | Raw key-value data | `data["name"]` |
| Pydantic model | Validated object with fields | `user.name` |

Dictionary example:

```python
data = {"name": "Asha", "age": 30}
print(data["name"])
```

Pydantic model example:

```python
user = User.model_validate(data)
print(user.name)
```

Beginner mistake:

Trying to access a dictionary with dot syntax:

```python
data.name
```

That fails because dictionaries use bracket access.

## 17. Pydantic with FastAPI

FastAPI uses Pydantic models to validate request bodies.

Example:

```python
class AskRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(request: AskRequest):
    return {"answer": f"You asked: {request.question}"}
```

What happens automatically:

- FastAPI reads the JSON request body.
- FastAPI validates it using `AskRequest`.
- If valid, your function receives a Pydantic object.
- If invalid, FastAPI returns a `422` validation response.

What the developer creates manually:

- the `AskRequest` model
- field names
- field types
- endpoint function logic

## 18. Pydantic with GenAI structured output

LLM output can be unpredictable.

If your app asks an LLM to return test cases, you may want this structure:

```python
class TestCase(BaseModel):
    title: str
    priority: str
    expected_result: str
```

After receiving JSON-like output from a model, validate it before using it.

Why:

- prevent missing fields
- detect wrong types
- avoid UI crashes
- avoid passing bad data to the next agent step

## 19. Pydantic with agent state

Agent workflows pass state between steps.

Example:

```python
class AgentState(BaseModel):
    query: str
    retrieved_context: list[str] = []
    draft_answer: str | None = None
    final_answer: str | None = None
```

This helps describe what the agent workflow expects to carry.

Use Pydantic for agent state when you want clearer structure and validation.

## 20. Full code example

File:

```text
07-pydantic/practice/user_model.py
```

What this file is for:

It demonstrates validating a dictionary using a Pydantic model.

Full code:

```python
from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


user = User.model_validate({"name": "Asha", "age": 30})

print(user.name)
print(user.age)
print(user.model_dump())
```

Line explanation:

- `from pydantic import BaseModel` imports the Pydantic base class.
- `class User(BaseModel):` creates a Pydantic model class named `User`.
- `name: str` says `name` is required and should be text.
- `age: int` says `age` is required and should be an integer.
- `User.model_validate(...)` validates the input dictionary.
- `user` stores the validated model object.
- `user.name` reads the `name` field from the model object.
- `user.age` reads the `age` field.
- `user.model_dump()` converts the model object into a dictionary.

## 21. How to run it

Command:

```powershell
python .\practice\user_model.py
```

Where to run:

Run this from:

```text
07-pydantic/
```

What each part means:

- `python` runs the Python interpreter.
- `.\practice\user_model.py` is the path to the example file.
- `.\` means "start from the current folder" in PowerShell.
- `practice` is the folder containing the file.
- `user_model.py` is the Python file to execute.

Expected output:

```text
Asha
30
{'name': 'Asha', 'age': 30}
```

How to verify:

You should see the name, age, and dictionary output.

Common error:

```text
ModuleNotFoundError: No module named 'pydantic'
```

Meaning:

Pydantic is not installed in the current Python environment.

Fix:

Install it in your active environment:

```powershell
pip install pydantic
```

Command explanation:

- `pip` installs Python packages.
- `install` tells pip to add a package.
- `pydantic` is the package name.

Expected output:

```text
Successfully installed pydantic-...
```

## 22. Common mistakes

- Forgetting `(BaseModel)` after the class name.
- Thinking type hints alone validate runtime data.
- Confusing `model_validate` and `model_dump`.
- Writing `str | None` but forgetting `= None` for a field that should be optional.
- Accessing a dictionary with dot syntax.
- Accessing a Pydantic object with dictionary syntax without understanding the difference.
- Sending a single dictionary where `list[ModelName]` expects a list.

## 23. Where used in AI Engineer work

Pydantic appears in:

- FastAPI request bodies
- FastAPI response models
- structured GenAI output
- RAG answers with source citations
- MCP tool input and output schemas
- LangGraph state models
- final POC API contracts
- interview questions about validation and type hints
