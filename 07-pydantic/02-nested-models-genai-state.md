# Nested Models, GenAI Output, and Agent State

## 1. What a nested model is

A nested model is a Pydantic model inside another Pydantic model.

Simple meaning:

```text
Nested model = structured data inside structured data
```

Example:

```text
TestCaseResponse
  -> requirement
  -> list of test cases
       -> each test case has title, type, priority, expected_result
```

This matters because real API and AI responses are rarely one flat value.

## 2. The most important beginner idea

Real GenAI output should often be structured before your app uses it.

Free text is easy for humans to read but hard for code to trust.

Structured output is easier to:

- display in UI
- return from FastAPI
- save as JSON
- pass into a LangGraph review node
- validate before using

Pydantic lets you describe that structure and reject bad output.

## 3. Why nested models matter

Suppose an AI assistant generates test cases.

Weak free-text output:

```text
Test valid login, invalid password, and locked account.
```

Better structured output:

```json
{
  "requirement": "User can login",
  "test_cases": [
    {
      "title": "Valid login",
      "type": "positive",
      "priority": "P1",
      "expected_result": "Dashboard opens"
    }
  ]
}
```

The second format is easier to validate, display, store, and review.

## 4. Beginner mental model

```text
Outer model = full response
Inner model = one repeated item
list[InnerModel] = many items of that shape
```

For test cases:

```text
TestCase = one test case
TestCaseResponse = full response containing many TestCase objects
```

## 5. Full code example

File:

```text
07-pydantic/practice/test_case_response.py
```

What this file is for:

It demonstrates nested models and `list[TestCase]`.

Full code:

```python
from pydantic import BaseModel


class TestCase(BaseModel):
    title: str
    type: str
    priority: str
    expected_result: str


class TestCaseResponse(BaseModel):
    requirement: str
    test_cases: list[TestCase]
    mode: str = "mock"


response = TestCaseResponse.model_validate({
    "requirement": "User can login",
    "test_cases": [
        {
            "title": "Valid login",
            "type": "positive",
            "priority": "P1",
            "expected_result": "Dashboard opens",
        }
    ],
})

print(response.test_cases[0].title)
print(response.model_dump())
```

## 6. Inner model explanation

```python
class TestCase(BaseModel):
    title: str
    type: str
    priority: str
    expected_result: str
```

Meaning:

- `class TestCase(BaseModel):` creates a Pydantic model named `TestCase`.
- `title: str` means each test case must have a title string.
- `type: str` means each test case must have a type string, such as `"positive"` or `"negative"`.
- `priority: str` means each test case must have a priority string, such as `"P1"`.
- `expected_result: str` means each test case must explain the expected result.

This model describes one test case only.

## 7. Outer model explanation

```python
class TestCaseResponse(BaseModel):
    requirement: str
    test_cases: list[TestCase]
    mode: str = "mock"
```

Meaning:

- `TestCaseResponse` describes the full response.
- `requirement: str` stores the requirement being tested.
- `test_cases: list[TestCase]` stores many test case objects.
- `mode: str = "mock"` gives a default value if the input does not include `mode`.

## 8. list[ModelName] syntax

```python
test_cases: list[TestCase]
```

Read it slowly:

```text
test_cases -> should be -> a list -> where each item matches TestCase
```

Valid:

```python
[
    {
        "title": "Valid login",
        "type": "positive",
        "priority": "P1",
        "expected_result": "Dashboard opens"
    }
]
```

Invalid:

```python
{
    "title": "Valid login",
    "type": "positive",
    "priority": "P1",
    "expected_result": "Dashboard opens"
}
```

Why invalid:

The model expects a list of test cases, but this is only one dictionary.

## 9. Accessing nested data

```python
print(response.test_cases[0].title)
```

Read it slowly:

```text
response -> test_cases -> first item -> title
```

Meaning:

- `response` is the outer Pydantic model object.
- `.test_cases` gets the list of test case objects.
- `[0]` gets the first item in the list.
- `.title` gets the title field from that first test case.

Important:

Python list indexes start at `0`.

So `[0]` means first item, not zero items.

## 10. How to run this example

Command:

```powershell
python .\practice\test_case_response.py
```

Where to run:

Run this from:

```text
07-pydantic/
```

What each part means:

- `python` runs Python.
- `.\practice\test_case_response.py` points to the nested model example.
- `.\` means start from the current folder.
- `practice` is the folder containing the file.

Expected output:

```text
Valid login
{'requirement': 'User can login', 'test_cases': [{'title': 'Valid login', 'type': 'positive', 'priority': 'P1', 'expected_result': 'Dashboard opens'}], 'mode': 'mock'}
```

Output explanation:

- `Valid login` comes from `response.test_cases[0].title`.
- The dictionary output comes from `response.model_dump()`.
- `mode` appears even though the input did not include it because the model has a default value.

## 11. Validation error example

Bad input:

```python
TestCaseResponse.model_validate({
    "requirement": "User can login",
    "test_cases": {
        "title": "Valid login",
        "type": "positive",
        "priority": "P1",
        "expected_result": "Dashboard opens"
    }
})
```

Possible output:

```text
1 validation error for TestCaseResponse
test_cases
  Input should be a valid list
```

Meaning:

- Pydantic found a problem in `test_cases`.
- The model expected a list.
- The input provided a dictionary.

Another bad input:

```python
{
    "requirement": "User can login",
    "test_cases": [
        {
            "title": "Valid login",
            "type": "positive"
        }
    ]
}
```

Possible issue:

```text
priority
  Field required
expected_result
  Field required
```

Meaning:

Each item in `test_cases` must follow the `TestCase` model.

## 12. Nested model vs dictionary

A nested dictionary is raw data.

A nested Pydantic model validates the raw data and gives object-style access.

Raw dictionary:

```python
data["test_cases"][0]["title"]
```

Pydantic model:

```python
response.test_cases[0].title
```

Both can access the value, but Pydantic adds validation before your app trusts it.

## 13. List of strings vs list of objects

List of strings:

```python
tags: list[str]
```

Example:

```python
["login", "smoke", "positive"]
```

List of objects:

```python
test_cases: list[TestCase]
```

Example:

```python
[
    {"title": "Valid login", "priority": "P1"},
    {"title": "Invalid password", "priority": "P2"}
]
```

Use `list[str]` when each item is only text.

Use `list[ModelName]` when each item has multiple fields.

## 14. Pydantic for GenAI structured output

When an LLM returns structured data, validate it before using it.

Example model:

```python
class GeneratedTestCase(BaseModel):
    title: str
    steps: list[str]
    expected_result: str
```

Why:

- LLMs may omit fields.
- LLMs may return one object instead of a list.
- LLMs may return extra explanation text.
- LLMs may return wrong field names.

Pydantic does not make the LLM perfect. It checks whether the output is usable by your application.

## 15. Pydantic for RAG answer with sources

RAG answers often need sources.

Example:

```python
class Source(BaseModel):
    file_name: str
    chunk_text: str


class RagAnswer(BaseModel):
    question: str
    answer: str
    sources: list[Source]
```

Meaning:

- `Source` describes one retrieved source.
- `RagAnswer` describes the complete RAG response.
- `sources: list[Source]` means every source must have `file_name` and `chunk_text`.

Why useful:

The frontend can show the answer and source citations in a predictable way.

## 16. Pydantic for agent state

Agent workflows pass state across steps.

Example:

```python
class AgentState(BaseModel):
    query: str
    steps: list[str] = []
    answer: str | None = None
    errors: list[str] = []
```

Meaning:

- `query` is required.
- `steps` stores workflow steps completed so far.
- `answer` may be missing until the final node.
- `errors` stores problems that happened during the workflow.

Beginner caution:

For more advanced production code, mutable defaults like `[]` need careful handling. Pydantic handles model defaults better than plain Python dataclasses in many cases, but the beginner focus here is understanding the state shape.

## 17. Pydantic with FastAPI response models

FastAPI can use Pydantic models for responses too.

Example:

```python
class TestCaseResponse(BaseModel):
    requirement: str
    test_cases: list[TestCase]
```

Endpoint idea:

```python
@app.post("/generate-test-cases")
def generate_test_cases() -> TestCaseResponse:
    ...
```

This helps document and control the API response shape.

## 18. What learner creates vs what frameworks provide

Learner creates:

- model class names
- field names
- field types
- nested model relationships
- default values
- validation handling

Pydantic provides:

- field validation
- nested validation
- readable validation errors
- conversion to model object
- conversion back to dictionary

FastAPI provides:

- automatic request body validation using Pydantic
- automatic `422` response when request validation fails
- API docs based on Pydantic schemas

## 19. Common mistakes

- Sending a dictionary where `list[TestCase]` expects a list.
- Missing required fields inside nested objects.
- Accessing `response.test_cases.title` instead of `response.test_cases[0].title`.
- Forgetting that list indexes start at `0`.
- Using free-form LLM text where structured data is needed.
- Creating separate models with inconsistent field names.
- Thinking Pydantic fixes bad LLM output automatically. It validates and rejects; your app must decide what to do next.

## 20. Quick practice

Create:

- `Source` model with `file_name` and `chunk_text`
- `RagAnswer` model with `question`, `answer`, and `sources: list[Source]`

Validate:

```python
{
    "question": "What is RAG?",
    "answer": "RAG retrieves relevant context before answering.",
    "sources": [
        {
            "file_name": "rag-notes.md",
            "chunk_text": "RAG means retrieval augmented generation."
        }
    ]
}
```

Expected first source file:

```text
rag-notes.md
```

## 21. Where used in AI Engineer work

Nested models appear in:

- FastAPI request and response models
- generated test case responses
- structured LLM output
- RAG answers with sources
- LangGraph state
- MCP tool schemas
- final POC API contracts
- interview discussions about safe AI app design
