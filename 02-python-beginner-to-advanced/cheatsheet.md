# Python Beginner Cheatsheet

## Variable

Syntax: `role = "qa"`

Meaning: Store a value in a name.

Use when: You need to reuse data.

Be careful: `=` assigns, `==` compares.

## List

Syntax: `items = ["api", "rag"]`

Meaning: Ordered collection.

Use when: You have many values.

Be careful: Index starts at `0`.

## Dictionary

Syntax: `data = {"status": "ok"}`

Meaning: Key-value data.

Use when: Working with JSON/API/model responses.

Be careful: Missing key with `data["key"]` raises `KeyError`.

## Function

Syntax:

```python
def add(a, b):
    return a + b
```

Meaning: Reusable block of code.

Use when: Logic has a clear task.

Be careful: `return` and `print` are different.

## Class

Syntax:

```python
class User:
    def __init__(self, name):
        self.name = name
```

Meaning: Blueprint for objects.

Use when: Grouping related data and behavior.

Be careful: `self` refers to the current object.

## Try/Except

Syntax:

```python
try:
    value = data["x"]
except KeyError:
    value = None
```

Meaning: Handle expected errors safely.

Use when: Data may be missing or external input may fail.

Be careful: Do not silently hide all errors.

## Type Hints

Syntax: `def ask(question: str) -> str:`

Meaning: Describes expected input and output types.

Use when: Making code easier to read.

Be careful: Type hints alone are not runtime validation.
