# Python Coding and Output Practice

## Output Question 1: List indexing

Code:

```python
items = ["python", "fastapi", "rag"]
print(items[1])
```

Expected answer:

```text
fastapi
```

Explanation:

Python list indexes start at `0`. `items[0]` is `"python"`, `items[1]` is `"fastapi"`.

Common mistake:

Thinking index `1` means the first item.

## Output Question 2: Dictionary update

Code:

```python
state = {"step": "start"}
state["step"] = "done"
state["status"] = "ok"
print(state)
```

Expected answer:

```text
{'step': 'done', 'status': 'ok'}
```

Explanation:

`state["step"] = "done"` updates an existing key. `state["status"] = "ok"` adds a new key.

Common mistake:

Thinking dictionary fields are fixed after creation.

## Output Question 3: Loop accumulation

Code:

```python
total = 0
for number in [1, 2, 3]:
    total = total + number
print(total)
```

Expected answer:

```text
6
```

Explanation:

The loop adds `1`, then `2`, then `3` to `total`.

Common mistake:

Only adding the last number and answering `3`.

## Output Question 4: Mutable list parameter

Code:

```python
def add_step(steps):
    steps.append("review")

workflow = ["analyze", "generate"]
add_step(workflow)
print(workflow)
```

Expected answer:

```text
['analyze', 'generate', 'review']
```

Explanation:

Lists are mutable. The function receives a reference to the same list and appends to it.

Common mistake:

Thinking the function changes only a private copy.

## Output Question 5: Return inside function

Code:

```python
def classify(score):
    if score >= 80:
        return "high"
    return "normal"

print(classify(90))
```

Expected answer:

```text
high
```

Explanation:

When `score` is `90`, the `if` condition is true. The function returns `"high"` and stops.

Common mistake:

Thinking Python continues to the second return after the first return.

## Coding Question 1: Count positive numbers

Question:

Write a function that counts how many numbers in a list are greater than `0`.

Expected answer:

```python
def count_positive(numbers):
    count = 0
    for number in numbers:
        if number > 0:
            count = count + 1
    return count
```

Example:

```python
print(count_positive([-1, 0, 2, 5]))
```

Expected output:

```text
2
```

Explanation:

Only `2` and `5` are greater than `0`.

Common mistake:

Counting `0` as positive. In this question, positive means greater than `0`.

## Coding Question 2: Validate API response shape

Question:

Write a function that checks whether a dictionary has both `status` and `data` keys.

Expected answer:

```python
def has_required_keys(response):
    return "status" in response and "data" in response
```

Example:

```python
print(has_required_keys({"status": "ok", "data": []}))
print(has_required_keys({"status": "ok"}))
```

Expected output:

```text
True
False
```

Explanation:

The first dictionary has both keys. The second dictionary is missing `data`.

Common mistake:

Checking values instead of checking whether keys exist.

## Coding Question 3: Build prompt from template

Question:

Fill a prompt template with a requirement.

Expected answer:

```python
def build_prompt(requirement):
    template = "Generate test cases for this requirement: {requirement}"
    return template.format(requirement=requirement)
```

Example:

```python
print(build_prompt("User can login"))
```

Expected output:

```text
Generate test cases for this requirement: User can login
```

Explanation:

`.format(requirement=requirement)` replaces `{requirement}` with the function input.

Common mistake:

Returning the template without filling the placeholder.

## Coding Question 4: Extract titles

Question:

Given a list of test case dictionaries, return only their titles.

Expected answer:

```python
def get_titles(test_cases):
    titles = []
    for test_case in test_cases:
        titles.append(test_case["title"])
    return titles
```

Example:

```python
cases = [{"title": "Valid login"}, {"title": "Invalid password"}]
print(get_titles(cases))
```

Expected output:

```text
['Valid login', 'Invalid password']
```

Explanation:

The loop reads each dictionary and appends the value under `"title"`.

Common mistake:

Writing `test_case.title`. Dictionaries use bracket access, not dot access.
