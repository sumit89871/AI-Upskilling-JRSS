# JSON, Structured Output, And State

## 1. What it is

JSON is the common text format used by APIs and GenAI apps to exchange structured data.

Structured output means the model response follows a predictable shape instead of returning random free text.

State is the data a workflow keeps while it runs.

Example state:

```python
state = {
    "user_query": "Generate API tests for login",
    "retrieved_context": [],
    "draft_answer": None,
    "final_answer": None,
}
```

## 2. The most important beginner idea

Free text is easy for humans to read but hard for applications to trust.

Structured output is easier to validate, display, save, test, and pass to the next workflow step.

Agents need state because one step often depends on what happened in previous steps.

## 3. Beginner mental model

Structured output:

```text
model response -> known keys -> application can safely use values
```

State:

```text
workflow starts -> state dictionary created -> each step reads/writes state -> final result returned
```

Nested data:

```text
dictionary -> key -> dictionary/list -> key/index -> final value
```

## 4. How nested structured output works

```python
model_response = {
    "task": "generate_test_cases",
    "result": {
        "test_cases": [
            {"title": "Valid login", "priority": "P1"},
            {"title": "Invalid password", "priority": "P2"},
        ]
    },
}

title = model_response["result"]["test_cases"][0]["title"]
print(title)
```

Syntax breakdown:

- `model_response` is a dictionary.
- `"result"` is a key inside the outer dictionary.
- `"test_cases"` is a key inside the nested result dictionary.
- `[0]` means the first item in the list.
- `"title"` is a key inside the first test case dictionary.

Expected output:

```text
Valid login
```

Why this matters:

OpenAI/Gemini responses, RAG results, MCP tool outputs, and LangGraph state often use nested dictionaries and lists.

## 5. State dictionary

```python
state = {
    "query": "Create test cases for login API",
    "steps_completed": [],
    "final_answer": None,
}
```

Syntax breakdown:

- `state` is a dictionary.
- `"query"` stores the user request.
- `"steps_completed"` starts as an empty list.
- `[]` means no completed steps yet.
- `"final_answer": None` means the workflow does not have an answer yet.
- `None` is Python's value for "nothing here yet".

Update state:

```python
state["steps_completed"].append("analyzed_query")
state["final_answer"] = {"summary": "Generated two test cases"}
```

What happens:

- `.append(...)` adds one item to the existing list.
- `state["final_answer"] = ...` replaces `None` with a dictionary.

## 6. Small example

File name: `state_example.py`

Exact folder path: `03-python-for-genai-agentic-ai/practice/state_example.py`

Full code:

```python
state = {
    "query": "Create test cases for login API",
    "steps_completed": [],
    "final_answer": None,
}

state["steps_completed"].append("analyzed_query")
state["steps_completed"].append("generated_test_cases")
state["final_answer"] = {
    "summary": "Generated two test cases",
    "test_cases": ["valid login", "invalid password"],
}

print(state["steps_completed"])
print(state["final_answer"]["summary"])
```

What this file is for:

It shows how an agent or workflow can remember what happened between steps.

What you created manually:

- the state keys
- the step names
- the final answer shape

What Python gives automatically:

- dictionary storage
- list append behavior
- nested dictionary access

Run from the module folder:

```powershell
python .\practice\state_example.py
```

Command explanation:

- `python` runs Python.
- `.\practice\state_example.py` points to the file.
- This script runs locally and does not call an LLM.

Expected output:

```text
['analyzed_query', 'generated_test_cases']
Generated two test cases
```

How to verify:

The first output should show two completed steps. The second output should show the nested summary value.

## 7. Similar concepts beginners confuse

### Dictionary vs JSON

A dictionary is a Python object. JSON is text used for storage or API transfer.

### State vs final answer

State contains all working data during the workflow. Final answer is only the output returned at the end.

### `None` vs empty string

`None` means no value exists yet. `""` means a text value exists, but it is empty.

### List access vs dictionary access

Use `[0]` for a list item by position. Use `["key"]` for a dictionary value by key.

## 8. Common mistakes

- Assuming nested keys always exist.
- Mixing list and dictionary access syntax.
- Using free-form model output when the app expects structured JSON.
- Forgetting to initialize state before updating it.
- Replacing a list with a string by accident.
- Using `None` without checking for it before nested access.

## 9. Quick practice

Create state for a RAG workflow with these keys:

- `question`
- `documents`
- `retrieved_chunks`
- `answer`
- `errors`

Then update it after each fake step:

- add two document names
- add one retrieved chunk
- set an answer
- print the final answer

Expected result:

You should be able to explain which state values are created at the start and which are filled later.

## 10. Where used in AI Engineer work

- FastAPI JSON responses
- Pydantic structured output
- RAG source citations
- LangGraph state
- MCP tool inputs and outputs
- agent memory and workflow tracking
- POC final response format
