# Pydantic Cheatsheet

Use this after studying the module. It is concise, but each item includes meaning, use case, example, and caution.

## 1. Basic model

Syntax:

```python
from pydantic import BaseModel


class Request(BaseModel):
    text: str
```

Meaning:

Create a Pydantic model where `text` is a required string.

When to use:

Use when you need to validate a dictionary, FastAPI request body, LLM output, or agent state.

Example:

```python
request = Request.model_validate({"text": "hello"})
```

Be careful:

Without `(BaseModel)`, Pydantic validation will not happen.

## 2. BaseModel inheritance

Syntax:

```python
class User(BaseModel):
```

Meaning:

`User` inherits validation behavior from Pydantic's `BaseModel`.

When to use:

Use for every Pydantic model class.

Example:

```python
class AskRequest(BaseModel):
    question: str
```

Be careful:

`class User:` is a normal Python class. It does not get Pydantic methods like `model_validate`.

## 3. Required field

Syntax:

```python
name: str
```

Meaning:

The caller must provide `name`, and it should be a string.

When to use:

Use for values your app cannot work without.

Example:

```python
class User(BaseModel):
    name: str
```

Be careful:

A type hint without a default does not create an empty value. It usually means required.

## 4. Default value

Syntax:

```python
max_tokens: int = 300
```

Meaning:

If caller does not provide `max_tokens`, Pydantic uses `300`.

When to use:

Use for safe defaults such as mock model name, token limit, or flags.

Example:

```python
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 300
```

Be careful:

The default value should match the declared type.

## 5. Optional field

Syntax:

```python
style: str | None = None
```

Meaning:

`style` can be a string or `None`, and the caller can omit it.

When to use:

Use when a value may be filled later or may not be available.

Example:

```python
class SummaryRequest(BaseModel):
    text: str
    style: str | None = None
```

Be careful:

`str | None` without `= None` may still be required.

## 6. Field rule

Syntax:

```python
from pydantic import Field

prompt: str = Field(min_length=1)
```

Meaning:

The string must have at least one character.

When to use:

Use when simple type checking is not enough.

Example:

```python
class PromptRequest(BaseModel):
    prompt: str = Field(min_length=1)
```

Be careful:

`prompt: str` allows empty string. Use `Field(min_length=1)` to reject it.

## 7. Validate dictionary

Syntax:

```python
item = Request.model_validate({"text": "hello"})
```

Meaning:

Validate a raw dictionary and return a Pydantic model object.

When to use:

Use when data comes from JSON, API request, LLM output, file, or another system.

Example:

```python
user = User.model_validate({"name": "Asha", "age": 30})
```

Be careful:

If validation fails, Pydantic raises a `ValidationError`.

## 8. Dump to dictionary

Syntax:

```python
data = item.model_dump()
```

Meaning:

Convert a Pydantic model object back to a normal dictionary.

When to use:

Use when returning JSON-like responses, logging, or passing data to another function.

Example:

```python
print(user.model_dump())
```

Be careful:

`model_dump()` does not validate raw input. It converts an already-created model object.

## 9. ValidationError

Syntax:

```python
from pydantic import ValidationError

try:
    Request.model_validate({"text": ""})
except ValidationError as error:
    print(error)
```

Meaning:

Catch validation failure and print the details.

When to use:

Use when you want controlled error handling in scripts, clients, or workflows.

Example:

```python
except ValidationError as error:
    print("Validation failed")
```

Be careful:

Do not hide validation errors without logging or returning useful feedback.

## 10. Nested model

Syntax:

```python
class TestCase(BaseModel):
    title: str


class Response(BaseModel):
    test_cases: list[TestCase]
```

Meaning:

`Response` contains a list of structured `TestCase` objects.

When to use:

Use when data has layers, such as RAG answers with sources or generated test cases.

Example:

```python
response.test_cases[0].title
```

Be careful:

If a field says `list[TestCase]`, input must be a list, not a single dictionary.

## 11. list[ModelName]

Syntax:

```python
sources: list[Source]
```

Meaning:

`sources` must be a list, and each item must match the `Source` model.

When to use:

Use for repeated structured items.

Example:

```python
class RagAnswer(BaseModel):
    sources: list[Source]
```

Be careful:

`list[str]` is for plain text items. `list[Source]` is for structured objects.

## 12. Pydantic with FastAPI

Syntax:

```python
class AskRequest(BaseModel):
    question: str
```

Meaning:

FastAPI can use this model to validate JSON request bodies.

When to use:

Use for API endpoint input and response structure.

Example:

```python
@app.post("/ask")
def ask(request: AskRequest):
    return {"question": request.question}
```

Be careful:

If the client sends wrong JSON, FastAPI may return `422` before your function runs.

## 13. Pydantic with GenAI output

Syntax:

```python
class GeneratedTestCase(BaseModel):
    title: str
    expected_result: str
```

Meaning:

Describe the structure your app expects from an LLM.

When to use:

Use before displaying, saving, or passing LLM output to another workflow step.

Example:

```python
GeneratedTestCase.model_validate(llm_json)
```

Be careful:

Pydantic validates output. It does not guarantee the LLM will produce correct business content.

## 14. Pydantic with agent state

Syntax:

```python
class AgentState(BaseModel):
    query: str
    answer: str | None = None
```

Meaning:

Describe the data an agent workflow carries.

When to use:

Use when you want clear state shape for LangGraph or agent workflows.

Example:

```python
state = AgentState.model_validate({"query": "Generate tests"})
```

Be careful:

Design state keys consistently. Later nodes depend on those names.
