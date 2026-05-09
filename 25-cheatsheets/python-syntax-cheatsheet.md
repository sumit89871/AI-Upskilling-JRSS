# Python Syntax Cheatsheet

## Variable

Syntax: `name = "Asha"`

Meaning: Store a value in a name.

Use when: You need to reuse a value later.

Example: `role = "qa"`

Be careful: `=` assigns. `==` compares.

## Function

Syntax:

```python
def add(a, b):
    return a + b
```

Meaning: Create reusable code that accepts inputs and returns output.

Use when: Logic is repeated or needs a clear name.

Example: `build_prompt(requirement)`

Be careful: `print` displays; `return` sends value back.

## List

Syntax: `items = ["api", "rag"]`

Meaning: Ordered collection of values.

Use when: You need many values in sequence.

Example: `test_cases = ["valid login", "invalid password"]`

Be careful: Index starts at `0`.

## Dictionary

Syntax: `data = {"status": "ok"}`

Meaning: Key-value data.

Use when: Working with JSON-like API or model data.

Example: `data["status"]`

Be careful: Missing key with bracket access raises `KeyError`.

## Class

Syntax:

```python
class User:
    pass
```

Meaning: Blueprint for objects.

Use when: Grouping data and behavior.

Example: Pydantic models use classes.

Be careful: `class User(BaseModel)` gives Pydantic validation; plain `class User` does not.

## Try/Except

Syntax:

```python
try:
    value = data["answer"]
except KeyError:
    value = None
```

Meaning: Handle expected errors safely.

Use when: Parsing external input or model output.

Be careful: Do not catch all errors and silently ignore them.
