# Python Exercises

## Exercise 1: Variables and output

Task:

Create variables for `name`, `role`, and `experience_months`, then print a sentence.

Expected code:

```python
name = "Asha"
role = "QA Analyst"
experience_months = 6

print(f"{name} is a {role} with {experience_months} months experience.")
```

Expected output:

```text
Asha is a QA Analyst with 6 months experience.
```

Hint:

Use an f-string to insert variable values into text.

Self-check:

Can you explain what each variable stores?

Common mistake:

Putting variable names inside quotes, which prints the name instead of the value.

## Exercise 2: List and loop

Task:

Print each test type from a list.

Expected code:

```python
test_types = ["positive", "negative", "edge"]

for test_type in test_types:
    print(test_type)
```

Expected output:

```text
positive
negative
edge
```

Hint:

The loop variable `test_type` receives one list item at a time.

Common mistake:

Trying to access the whole list when the task asks for each item.

## Exercise 3: Dictionary access

Task:

Create an API response dictionary and print its status.

Expected code:

```python
response = {"status": "ok", "data": [1, 2, 3]}
print(response["status"])
```

Expected output:

```text
ok
```

Hint:

Dictionaries use key access with square brackets.

Common mistake:

Writing `response.status`. That is not normal dictionary access.

## Exercise 4: Function with return

Task:

Write a function that builds a prompt from a requirement.

Expected code:

```python
def build_prompt(requirement):
    return f"Generate test cases for: {requirement}"


prompt = build_prompt("User can login")
print(prompt)
```

Expected output:

```text
Generate test cases for: User can login
```

Hint:

Use `return` so another part of code can reuse the prompt.

Common mistake:

Only printing inside the function and then expecting a returned value.

## Exercise 5: Exception handling

Task:

Safely read a missing dictionary key.

Expected code:

```python
data = {"answer": "RAG retrieves context."}

try:
    print(data["source"])
except KeyError:
    print("source is missing")
```

Expected output:

```text
source is missing
```

Hint:

`KeyError` happens when a dictionary key does not exist.

Common mistake:

Catching every exception with a blank `except` and hiding the real problem.

## Exercise 6: Class and object

Task:

Create a simple `TestCase` class.

Expected code:

```python
class TestCase:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority


case = TestCase("Valid login", "P1")
print(case.title)
print(case.priority)
```

Expected output:

```text
Valid login
P1
```

Hint:

`self.title` stores data inside the object.

Common mistake:

Forgetting `self` in instance methods.

## Exercise 7: JSON handling

Task:

Convert a dictionary to JSON string.

Expected code:

```python
import json

data = {"question": "What is MCP?", "mode": "mock"}
json_text = json.dumps(data)
print(json_text)
```

Expected output:

```text
{"question": "What is MCP?", "mode": "mock"}
```

Hint:

`json.dumps` means dump dictionary to string.

Common mistake:

Confusing `json.dumps` with `json.loads`. `loads` reads JSON string into Python data.
