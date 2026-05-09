# Pydantic Exercises

These exercises are written for beginners. Each one includes the task, expected code or command, expected output, hints, self-checks, solution outline, and common mistake.

## Exercise 1: Create a basic model

### Task

Create a model named `UserRequest` with:

- `name: str`
- `role: str`

### Starting file

Create this file:

```text
07-pydantic/practice/user_request.py
```

### Expected code

```python
from pydantic import BaseModel


class UserRequest(BaseModel):
    name: str
    role: str


user = UserRequest.model_validate({"name": "Asha", "role": "qa"})
print(user.model_dump())
```

### Expected command

```powershell
python .\practice\user_request.py
```

Where to run:

```text
07-pydantic/
```

Command explanation:

- `python` runs the Python interpreter.
- `.\practice\user_request.py` is the path to your practice file.
- `.\` means start from the current folder.

### Expected output

```text
{'name': 'Asha', 'role': 'qa'}
```

### Hint

Do not forget `(BaseModel)` after the class name.

### Self-check

What does `model_validate` do?

Expected answer:

It checks the input dictionary and returns a validated Pydantic model object if the data is valid.

### Solution outline

1. Import `BaseModel`.
2. Create `UserRequest(BaseModel)`.
3. Add two required fields.
4. Validate a dictionary.
5. Print `model_dump()`.

### Common mistake

Writing:

```python
class UserRequest:
```

This creates a normal Python class, not a Pydantic model.

## Exercise 2: Required field validation

### Task

Use the same `UserRequest` model and validate bad input that is missing `role`.

### Expected code

```python
from pydantic import BaseModel, ValidationError


class UserRequest(BaseModel):
    name: str
    role: str


try:
    UserRequest.model_validate({"name": "Asha"})
except ValidationError as error:
    print("Validation failed")
    print(error)
```

### Expected command

```powershell
python .\practice\user_request.py
```

### Expected output

```text
Validation failed
1 validation error for UserRequest
role
  Field required
```

Exact wording may vary by Pydantic version.

### Hint

A field with no default value is required.

### Self-check

Why did `name` pass but `role` fail?

### Solution outline

`name` was present in the input dictionary. `role` was required but missing.

### Common mistake

Thinking `role: str` creates a default empty string. It does not.

## Exercise 3: Defaults and optional fields

### Task

Create `SummaryRequest` with:

- `text: str`
- `max_words: int = 100`
- `style: str | None = None`

### Expected code

```python
from pydantic import BaseModel


class SummaryRequest(BaseModel):
    text: str
    max_words: int = 100
    style: str | None = None


request = SummaryRequest.model_validate({"text": "hello"})
print(request.model_dump())
```

### Expected output

```text
{'text': 'hello', 'max_words': 100, 'style': None}
```

### Hint

`str | None = None` means the field can be a string, can be `None`, and can be omitted.

### Self-check

What is the difference between `max_words` and `style`?

Expected answer:

`max_words` has a default integer value. `style` has a default `None` value and allows either string or `None`.

### Solution outline

1. Create the model.
2. Give defaults to `max_words` and `style`.
3. Validate input with only `text`.
4. Confirm Pydantic fills missing default fields.

### Common mistake

Writing:

```python
style: str | None
```

without `= None`. This allows `None` but may still make the field required.

## Exercise 4: Field rule for empty prompt

### Task

Create `PromptRequest` where `prompt` cannot be empty.

### Expected code

```python
from pydantic import BaseModel, Field, ValidationError


class PromptRequest(BaseModel):
    prompt: str = Field(min_length=1)


try:
    PromptRequest.model_validate({"prompt": ""})
except ValidationError as error:
    print("Validation failed")
    print(error)
```

### Expected output

```text
Validation failed
1 validation error for PromptRequest
prompt
  String should have at least 1 character
```

### Hint

Use `Field(min_length=1)`.

### Self-check

Why is an empty prompt dangerous in an LLM app?

Expected answer:

The app may call the model with no meaningful instruction, causing poor output or wasted cost.

### Solution outline

Use Pydantic to reject empty prompt values at the boundary.

### Common mistake

Thinking `prompt: str` rejects empty strings. It does not. Empty string is still a string.

## Exercise 5: Nested test case response

### Task

Create:

- `TestCase`
- `TestCaseResponse`

`TestCaseResponse` should contain:

```python
test_cases: list[TestCase]
```

### Expected code

```python
from pydantic import BaseModel


class TestCase(BaseModel):
    title: str
    priority: str


class TestCaseResponse(BaseModel):
    requirement: str
    test_cases: list[TestCase]


response = TestCaseResponse.model_validate({
    "requirement": "User can login",
    "test_cases": [
        {"title": "Valid login", "priority": "P1"}
    ]
})

print(response.test_cases[0].title)
```

### Expected output

```text
Valid login
```

### Hint

Use `[0]` to access the first item in a list.

### Self-check

Why do we use `list[TestCase]` instead of `list[str]`?

Expected answer:

Each test case has multiple fields, so each item should be a structured object, not plain text.

### Common mistake

Writing:

```python
response.test_cases.title
```

This is wrong because `test_cases` is a list. You must choose an item first.

## Exercise 6: Bad nested data validation

### Task

Pass a dictionary where `list[TestCase]` expects a list.

### Expected bad input

```python
{
    "requirement": "User can login",
    "test_cases": {"title": "Valid login", "priority": "P1"}
}
```

### Expected result

You should see a validation error similar to:

```text
test_cases
  Input should be a valid list
```

### Hint

If the model says `list[TestCase]`, the input must use square brackets:

```python
"test_cases": [
    {"title": "Valid login", "priority": "P1"}
]
```

### Self-check

Why is this error better than allowing the app to continue?

Expected answer:

The app can stop early and report the shape problem instead of crashing later when it tries to loop over test cases.

### Common mistake

Confusing one object with a list containing one object.

## Exercise 7: Pydantic for RAG answer

### Task

Create a model for a RAG answer with sources.

Each source should have:

- `file_name`
- `chunk_text`

The answer should have:

- `question`
- `answer`
- `sources`

### Expected code

```python
from pydantic import BaseModel


class Source(BaseModel):
    file_name: str
    chunk_text: str


class RagAnswer(BaseModel):
    question: str
    answer: str
    sources: list[Source]


rag_answer = RagAnswer.model_validate({
    "question": "What is RAG?",
    "answer": "RAG retrieves relevant context before answering.",
    "sources": [
        {
            "file_name": "rag-notes.md",
            "chunk_text": "RAG means retrieval augmented generation."
        }
    ]
})

print(rag_answer.sources[0].file_name)
```

### Expected output

```text
rag-notes.md
```

### Hint

This is the same pattern as `TestCaseResponse`, but with `Source` items.

### Self-check

Where would this appear in an AI Engineer POC?

Expected answer:

In a RAG API response where the app returns an answer plus supporting source chunks.

### Common mistake

Returning only `answer` without `sources`, which makes grounding and explainability weaker.

## Exercise 8: Pydantic for agent state

### Task

Create an `AgentState` model.

Fields:

- `query: str`
- `steps: list[str] = []`
- `draft_answer: str | None = None`
- `final_answer: str | None = None`

### Expected code

```python
from pydantic import BaseModel


class AgentState(BaseModel):
    query: str
    steps: list[str] = []
    draft_answer: str | None = None
    final_answer: str | None = None


state = AgentState.model_validate({"query": "Generate login tests"})
print(state.model_dump())
```

### Expected output

```text
{'query': 'Generate login tests', 'steps': [], 'draft_answer': None, 'final_answer': None}
```

### Hint

Use defaults for values that are filled later in the workflow.

### Self-check

Which field is required?

Expected answer:

`query` is required because it has no default value.

### Common mistake

Making `draft_answer` required even though it is not available until a later node.
