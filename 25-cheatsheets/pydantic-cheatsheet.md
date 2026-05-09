# Pydantic Cheatsheet

## BaseModel

Syntax:

```python
class AskRequest(BaseModel):
    question: str
```

Meaning: Define validated data shape.

Use when: Validating API body, LLM output, or agent state.

Example: `AskRequest.model_validate(data)`

Be careful: Without `(BaseModel)`, validation methods are missing.

## Optional Field

Syntax: `answer: str | None = None`

Meaning: String or `None`, can be omitted.

Use when: Value is filled later.

Example: agent state before final answer.

Be careful: `str | None` without `= None` may still be required.

## model_validate

Syntax: `obj = Model.model_validate(data)`

Meaning: Validate raw dictionary and create model object.

Use when: Data comes from API, JSON, or LLM.

Be careful: Raises `ValidationError` if invalid.

## model_dump

Syntax: `data = obj.model_dump()`

Meaning: Convert model object to dictionary.

Use when: Returning JSON-like response.

Be careful: It does not validate raw input.
