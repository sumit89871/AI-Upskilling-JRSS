# Pydantic Interview Questions

Use these answers for AI Engineer JRSS screening, Mettl-style questions, POC discussion, and interviews.

## 1. What is Pydantic?

Short answer:

Pydantic is a Python library for validating data using type hints.

Expanded answer:

Pydantic lets you define the expected shape of data using Python classes. It checks whether incoming dictionaries or JSON-like data contain the required fields and correct types. If the data is valid, it returns a clean model object. If invalid, it raises a validation error.

Project example:

In a FastAPI `/generate-test-cases` endpoint, Pydantic can validate that the request contains a non-empty requirement before the app calls an LLM.

Common wrong answer:

"Pydantic is only for FastAPI."

Why this is wrong:

FastAPI uses Pydantic heavily, but Pydantic can also validate GenAI output, RAG responses, MCP tool payloads, LangGraph state, and plain Python dictionaries.

## 2. What is `BaseModel`?

Short answer:

`BaseModel` is the parent class that gives a Pydantic model validation behavior.

Expanded answer:

When your class inherits from `BaseModel`, Pydantic adds features such as `model_validate`, `model_dump`, field validation, and clear validation errors.

Project example:

```python
class AskRequest(BaseModel):
    question: str
```

This creates a request model for an `/ask` API endpoint.

Common wrong answer:

"BaseModel is just for documentation."

Why this is wrong:

`BaseModel` gives runtime validation behavior. Without it, the class is not a Pydantic model.

## 3. What is a field in Pydantic?

Short answer:

A field is one named value inside a Pydantic model.

Expanded answer:

In `question: str`, `question` is the field name and `str` is the expected type. Fields define what data the model expects.

Project example:

```python
class PromptRequest(BaseModel):
    prompt: str
    max_tokens: int = 300
```

Here `prompt` and `max_tokens` are fields.

Common wrong answer:

"A field is the same as a function."

Why this is wrong:

A field stores data. A function performs behavior.

## 4. What is the difference between type hints and validation?

Short answer:

Type hints describe expected types. Pydantic performs runtime validation.

Expanded answer:

Normal Python type hints help readers and tools, but Python usually does not enforce them at runtime. Pydantic checks actual input data when you validate or create a model.

Project example:

If an API receives `{"age": "thirty"}` for `age: int`, Pydantic can reject it before the app uses it.

Common wrong answer:

"Python type hints automatically stop wrong data."

Why this is wrong:

Type hints alone do not reliably block wrong runtime values in normal Python.

## 5. What is `model_validate`?

Short answer:

`model_validate` validates input data and returns a Pydantic model object if valid.

Expanded answer:

Use it when you have raw data, usually a dictionary, and want to check if it matches the model.

Project example:

```python
request = PromptRequest.model_validate({"prompt": "Explain RAG"})
```

After this, `request.prompt` can be used safely.

Common wrong answer:

"model_validate converts a model object to a dictionary."

Why this is wrong:

That is `model_dump`. `model_validate` validates raw input and creates a model object.

## 6. What is `model_dump`?

Short answer:

`model_dump` converts a Pydantic model object into a dictionary.

Expanded answer:

After validation, your app may need dictionary data for JSON responses, logging, or passing data to another system. `model_dump()` gives a normal Python dictionary.

Project example:

```python
data = request.model_dump()
```

Common wrong answer:

"model_dump validates input data."

Why this is wrong:

`model_dump` converts an existing model object. It does not validate raw dictionaries.

## 7. What is the difference between required and optional fields?

Short answer:

A required field must be provided. An optional field can be omitted or set to `None` when defined with a default.

Expanded answer:

`name: str` is required because it has no default. `email: str | None = None` is optional because it allows `None` and has a default value.

Project example:

```python
class UserProfile(BaseModel):
    name: str
    email: str | None = None
```

Common wrong answer:

"`str | None` always means the field is not required."

Why this is incomplete:

Without `= None`, the field may still be required even though it can accept `None`.

## 8. What is a default value?

Short answer:

A default value is used when the input does not provide that field.

Expanded answer:

Defaults make models easier to use because callers only provide values that must change.

Project example:

```python
class PromptRequest(BaseModel):
    prompt: str
    model: str = "mock-llm"
    max_tokens: int = 300
```

If the input only has `prompt`, Pydantic fills `model` and `max_tokens`.

Common wrong answer:

"Default value means the field cannot be changed."

Why this is wrong:

The caller can still provide another valid value. The default is only used when the field is missing.

## 9. What is `Field`?

Short answer:

`Field` adds validation rules or metadata to a model field.

Expanded answer:

Type hints check broad types. `Field` can add rules such as minimum length or numeric limits.

Project example:

```python
prompt: str = Field(min_length=1)
```

This rejects an empty prompt.

Common wrong answer:

"Field is only for comments."

Why this is wrong:

`Field` can enforce validation constraints.

## 10. What is a validation error?

Short answer:

A validation error is raised when input does not match the Pydantic model.

Expanded answer:

Pydantic validation errors usually identify the model, field, and reason for failure. This is better than letting bad data crash the app later.

Project example:

If `age: int` receives `"thirty"`, Pydantic reports that `age` should be a valid integer.

Common wrong answer:

"Validation error means the Python file cannot run."

Why this is wrong:

The file can run, but the specific input failed validation.

## 11. What is a nested model?

Short answer:

A nested model is a Pydantic model inside another Pydantic model.

Expanded answer:

Nested models are useful when data has layers, such as a response containing many test cases, or a RAG answer containing many sources.

Project example:

```python
class TestCase(BaseModel):
    title: str


class TestCaseResponse(BaseModel):
    test_cases: list[TestCase]
```

Common wrong answer:

"Nested model means one long dictionary without validation."

Why this is wrong:

Nested Pydantic models validate each layer of the structure.

## 12. What does `list[TestCase]` mean?

Short answer:

It means the field must be a list, and each item must match the `TestCase` model.

Expanded answer:

This is used when a response contains multiple structured items of the same shape.

Project example:

Generated test cases from an LLM can be validated as:

```python
test_cases: list[TestCase]
```

Common wrong answer:

"It means one TestCase object."

Why this is wrong:

The `list[...]` part means many items, even if the list contains only one item.

## 13. How does Pydantic connect to FastAPI?

Short answer:

FastAPI uses Pydantic models to validate request bodies and structure responses.

Expanded answer:

When a FastAPI endpoint has a Pydantic model parameter, FastAPI reads the JSON body, validates it, and passes a model object to the function. If validation fails, FastAPI returns a `422` response.

Project example:

```python
@app.post("/ask")
def ask(request: AskRequest):
    return {"question": request.question}
```

Common wrong answer:

"FastAPI validation happens after my function runs."

Why this is wrong:

Request body validation happens before the endpoint function runs.

## 14. How does Pydantic help GenAI structured output?

Short answer:

It validates structured LLM output before the application uses it.

Expanded answer:

LLMs may return missing fields, wrong field names, or the wrong shape. Pydantic can check whether the output matches the expected model before the app displays, stores, or passes it to another step.

Project example:

Validate LLM-generated test cases with `TestCaseResponse` before returning them from the API.

Common wrong answer:

"Pydantic guarantees the LLM answer is factually correct."

Why this is wrong:

Pydantic validates structure, not truth. The answer can be well-structured but still factually wrong.

## 15. How does Pydantic help agent state?

Short answer:

It gives agent state a clear shape and validates the data carried between workflow steps.

Expanded answer:

Agent workflows pass state between nodes. If state keys or types are inconsistent, later nodes may fail. A Pydantic model can document and validate expected state.

Project example:

```python
class AgentState(BaseModel):
    query: str
    retrieved_context: list[str] = []
    final_answer: str | None = None
```

Common wrong answer:

"Agent state does not need validation."

Why this is weak:

State bugs are common in agent workflows. Validation helps catch shape problems earlier.

## 16. Scenario: FastAPI returns 422. How can Pydantic be involved?

Short answer:

The request body likely did not match the expected Pydantic model.

Expanded answer:

The client may have sent a missing field, wrong field name, wrong type, or invalid value. FastAPI validates request data using Pydantic before the endpoint function runs.

Project example:

If `AskRequest` expects `question: str` but the client sends `{ "query": "..." }`, FastAPI may return `422`.

Common wrong answer:

"422 always means server crash."

Why this is wrong:

`422` usually means the request was understood but validation failed.

## 17. Why use Pydantic instead of only manual if checks?

Short answer:

Pydantic handles common structure and type validation consistently, while manual checks are better for business-specific rules.

Expanded answer:

You can write manual `if` checks, but they become repetitive. Pydantic gives a standard way to validate fields, types, nested objects, and defaults. You can still add manual business rules when needed.

Project example:

Use Pydantic to check `expected_status` is an integer. Use manual business logic to check whether that status code is allowed for a specific API.

Common wrong answer:

"Pydantic removes all need for manual validation."

Why this is wrong:

Pydantic helps with data shape and type validation. Business rules may still need custom logic.
