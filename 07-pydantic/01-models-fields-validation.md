# Models, Fields, and Validation

## 1. What a Pydantic model is

A Pydantic model is a Python class that describes the expected shape of data.

Example:

```python
class PromptRequest(BaseModel):
    prompt: str
    temperature: float = 0.2
```

This model says:

- `prompt` is required and must be text
- `temperature` should be a decimal number
- if `temperature` is missing, use `0.2`

## 2. What a field is

A field is one named value inside a model.

In this model:

```python
class PromptRequest(BaseModel):
    prompt: str
    model: str = "mock-llm"
    max_tokens: int = 300
```

Fields are:

- `prompt`
- `model`
- `max_tokens`

Each field has:

- a name
- a type
- optionally a default value
- optionally validation rules

## 3. The most important beginner idea

Required field means:

```text
The caller must provide this value.
```

Default field means:

```text
The caller may skip this value, and Pydantic will use the default.
```

Optional field means:

```text
The value may be None, and usually the caller may skip it when a default is provided.
```

These are related but not identical.

## 4. Why fields and validation matter

LLM and API calls often need configuration:

- prompt
- model name
- temperature
- max token limit
- mock mode
- user question
- RAG source list
- generated test cases

If these values are missing or wrong, the app may:

- call the wrong model
- send an empty prompt
- crash during API response generation
- produce malformed structured output
- fail in a later LangGraph node

Pydantic catches many of these issues early.

## 5. Beginner mental model

```text
Model = form design
Field = one question on the form
Validation = checking the filled form
Default value = answer used if user leaves field blank
Validation error = clear explanation of what is wrong
```

## 6. Full code example

File:

```text
07-pydantic/practice/prompt_request.py
```

What this file is for:

It demonstrates required fields, default values, `Field` rules, and validation error handling.

Full code:

```python
from pydantic import BaseModel, Field, ValidationError


class PromptRequest(BaseModel):
    prompt: str = Field(min_length=1)
    model: str = "mock-llm"
    temperature: float = 0.2
    max_tokens: int = 300


valid_request = PromptRequest.model_validate({
    "prompt": "Generate test cases for login"
})

print(valid_request.model_dump())

try:
    PromptRequest.model_validate({"prompt": ""})
except ValidationError as error:
    print("Validation failed")
    print(error)
```

## 7. Import syntax breakdown

```python
from pydantic import BaseModel, Field, ValidationError
```

Read it slowly:

```text
from pydantic -> import -> BaseModel, Field, ValidationError
```

Meaning:

- `from` tells Python where to import from.
- `pydantic` is the package name.
- `import` means bring names into this file.
- `BaseModel` is used to create Pydantic model classes.
- `Field` adds field-level validation rules and metadata.
- `ValidationError` is the error type Pydantic raises when validation fails.

## 8. Class and BaseModel breakdown

```python
class PromptRequest(BaseModel):
```

Meaning:

- `class` creates a class.
- `PromptRequest` is the model class name.
- `(BaseModel)` means this class inherits Pydantic validation behavior.
- `:` starts the indented class body.

What the developer creates manually:

- the class name
- the field names
- the field types
- the field rules

What Pydantic provides:

- validation logic
- `model_validate`
- `model_dump`
- validation error messages

## 9. Field rule breakdown

```python
prompt: str = Field(min_length=1)
```

Meaning:

- `prompt` is the field name.
- `:` separates the field name from the type hint.
- `str` means the value should be text.
- `=` assigns a field configuration.
- `Field(...)` is a Pydantic helper for field rules.
- `min_length=1` means the string must contain at least one character.

Valid:

```python
{"prompt": "Generate test cases"}
```

Invalid:

```python
{"prompt": ""}
```

Why invalid:

The string is empty, so it has length `0`, not at least `1`.

## 10. Default values

```python
model: str = "mock-llm"
temperature: float = 0.2
max_tokens: int = 300
```

Meaning:

- `model` should be a string, defaulting to `"mock-llm"`.
- `temperature` should be a float, defaulting to `0.2`.
- `max_tokens` should be an integer, defaulting to `300`.

Input:

```python
{"prompt": "Generate test cases for login"}
```

Validated output:

```python
{
    "prompt": "Generate test cases for login",
    "model": "mock-llm",
    "temperature": 0.2,
    "max_tokens": 300
}
```

## 11. Required field vs default field

Required field:

```python
prompt: str
```

The caller must provide `prompt`.

Default field:

```python
max_tokens: int = 300
```

The caller may skip `max_tokens`.

Pydantic will fill `300`.

Common mistake:

Thinking every field with a type hint is optional. It is not. A field without a default is usually required.

## 12. Optional field

Sometimes a field may be intentionally missing.

Example:

```python
class UserProfile(BaseModel):
    name: str
    email: str | None = None
```

Syntax breakdown:

- `email` is the field name.
- `str | None` means the value can be a string or `None`.
- `= None` means if the caller skips `email`, use `None`.

Valid:

```python
UserProfile.model_validate({"name": "Asha"})
```

Result:

```python
{"name": "Asha", "email": None}
```

Common beginner trap:

```python
email: str | None
```

This allows `None`, but without `= None`, the field may still be required.

## 13. model_validate

```python
valid_request = PromptRequest.model_validate({
    "prompt": "Generate test cases for login"
})
```

Meaning:

- `PromptRequest` is the model class.
- `.model_validate(...)` asks Pydantic to validate raw data.
- `{...}` is a Python dictionary.
- `valid_request` receives the validated Pydantic object.

After this line, you can access:

```python
valid_request.prompt
valid_request.model
valid_request.temperature
valid_request.max_tokens
```

## 14. model_dump

```python
print(valid_request.model_dump())
```

Meaning:

- `valid_request` is a Pydantic model object.
- `.model_dump()` converts it into a dictionary.
- `print(...)` displays the dictionary in the terminal.

Use `model_dump()` when:

- returning data from an API
- logging validated data
- passing the result to another function
- comparing expected and actual output in tests

## 15. try/except and ValidationError

```python
try:
    PromptRequest.model_validate({"prompt": ""})
except ValidationError as error:
    print("Validation failed")
    print(error)
```

Meaning:

- `try` starts code that may fail.
- `PromptRequest.model_validate(...)` attempts validation.
- `except ValidationError as error` catches Pydantic validation failures.
- `error` stores the validation error object.
- `print(error)` displays the validation details.

Validation error is still a Python exception, but it is a specific and useful one.

## 16. How to run this example

Command:

```powershell
python .\practice\prompt_request.py
```

Where to run:

Run from:

```text
07-pydantic/
```

When to run:

Run after Pydantic is installed in your active Python environment.

What each part means:

- `python` runs the Python interpreter.
- `.\practice\prompt_request.py` points to the example file.
- `.\` means the path starts from the current folder.
- `practice` is the folder containing the file.

Expected output:

```text
{'prompt': 'Generate test cases for login', 'model': 'mock-llm', 'temperature': 0.2, 'max_tokens': 300}
Validation failed
1 validation error for PromptRequest
prompt
  String should have at least 1 character
```

Your exact Pydantic wording may vary slightly by version.

How to verify:

- The first line should show default values filled.
- The second section should show validation failed for empty `prompt`.

Common error:

```text
ModuleNotFoundError: No module named 'pydantic'
```

Fix:

```powershell
pip install pydantic
```

Command explanation:

- `pip` installs Python packages.
- `install` tells pip to install a package.
- `pydantic` is the package name.

## 17. Validation error vs later app crash

Without validation:

```text
bad input enters app -> LLM call fails -> confusing error later
```

With validation:

```text
bad input enters app -> Pydantic rejects it -> clear error near the boundary
```

This is especially important in AI apps because LLM calls can be slow, expensive, and harder to debug.

## 18. Similar concepts beginners confuse

### Required vs optional

Required means caller must provide it.

Optional means the field can be skipped or be `None` when a default is provided.

### Default value vs optional value

Default value means Pydantic fills a missing field.

Optional value means `None` is allowed.

### Type hint vs validation

Type hint describes expected type.

Pydantic validates actual input data.

### `Field(...)` vs normal default

Normal default:

```python
max_tokens: int = 300
```

Field rule:

```python
prompt: str = Field(min_length=1)
```

`Field` can enforce constraints.

## 19. Common mistakes

- Forgetting `(BaseModel)` after class name.
- Writing `email: str | None` but forgetting `= None`.
- Thinking `Field(min_length=1)` is only documentation.
- Using a default value of the wrong type.
- Catching every exception instead of specifically handling `ValidationError`.
- Calling `model_dump()` before validation.
- Misspelling field names in input data.

## 20. Quick practice

Create `ApiTestRequest` with:

- `endpoint: str`
- `method: str`
- `expected_status: int = 200`
- `auth_required: bool = False`

Validate this:

```python
{
    "endpoint": "/login",
    "method": "POST"
}
```

Expected `model_dump()`:

```python
{
    "endpoint": "/login",
    "method": "POST",
    "expected_status": 200,
    "auth_required": False
}
```

## 21. Where used in AI Engineer work

You use models, fields, and validation for:

- FastAPI request models
- FastAPI response models
- LLM generation parameter validation
- structured JSON output validation
- agent state validation
- RAG answer schemas
- API test case schemas
- final POC endpoint contracts
