# Python Mini Project

## Project goal

Build a small Python script that prepares QA-style data for an AI application.

Beginner goal:

Practice variables, lists, dictionaries, functions, loops, and JSON-like output.

## Suggested project

Create a file:

```text
mini-project/test_case_builder.py
```

Code:

```python
def build_test_case(title, priority):
    return {
        "title": title,
        "priority": priority,
        "type": "functional"
    }


test_cases = []
test_cases.append(build_test_case("Valid login", "P1"))
test_cases.append(build_test_case("Invalid password", "P2"))

for test_case in test_cases:
    print(test_case)
```

## How to run

Command:

```powershell
python test_case_builder.py
```

Where to run:

Run from:

```text
02-python-beginner-to-advanced/mini-project/
```

Expected output:

```text
{'title': 'Valid login', 'priority': 'P1', 'type': 'functional'}
{'title': 'Invalid password', 'priority': 'P2', 'type': 'functional'}
```

## What each part teaches

- function creates reusable logic
- dictionary stores one test case
- list stores many test cases
- `append` adds to the list
- loop prints each item

## Common mistakes

- Forgetting to return the dictionary from the function.
- Using dot access on a dictionary.
- Running the command from the wrong folder.

## AI Engineer connection

This pattern appears later in generated test case JSON, FastAPI responses, Pydantic models, and LLM structured output.
