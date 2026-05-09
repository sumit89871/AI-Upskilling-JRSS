# Python Interview Questions

## What is a variable?

Short answer:

A variable is a name that stores a value.

Expanded explanation:

Python uses variables to keep data that can be reused or changed later.

Project example:

`requirement = "User can login"` stores text used to build a prompt.

Common wrong answer:

"A variable is fixed forever."

When to say this in interview:

Use for Python basics.

## List vs tuple?

Short answer:

A list is mutable. A tuple is immutable.

Expanded explanation:

Mutable means it can be changed after creation. Immutable means it cannot be changed directly.

Project example:

Use a list for test cases because new test cases may be appended.

Common wrong answer:

"They are exactly the same."

When to say this in interview:

Use for data structure comparison questions.

## Dictionary vs JSON?

Short answer:

A dictionary is a Python data structure. JSON is a text data format.

Expanded explanation:

They look similar, but JSON is text used for data exchange. Python dictionaries are in-memory objects.

Project example:

FastAPI receives JSON and Python code works with dictionaries or Pydantic models.

Common wrong answer:

"JSON and dictionary are always the same."

When to say this in interview:

Use when discussing APIs.

## Function vs method?

Short answer:

A function is standalone code. A method belongs to an object or class.

Expanded explanation:

`build_prompt()` can be a function. `user.model_dump()` is a method called on a Pydantic object.

Project example:

`model_dump()` converts a Pydantic object to a dictionary.

Common wrong answer:

"Function and method are never related."

When to say this in interview:

Use for OOP and framework code questions.

## What is exception handling?

Short answer:

Exception handling lets code respond to errors safely.

Expanded explanation:

Use `try/except` when an expected operation may fail, such as reading missing keys or parsing invalid JSON.

Project example:

Catch JSON parsing errors from model output and return a useful validation message.

Common wrong answer:

"Catch every error and ignore it."

When to say this in interview:

Use when discussing robust code.

## What are type hints?

Short answer:

Type hints describe expected input and output types.

Expanded explanation:

They help readers and tools understand code. They are not the same as runtime validation.

Project example:

`def generate(prompt: str) -> str:` says prompt and response should be strings.

Common wrong answer:

"Type hints always block wrong values at runtime."

When to say this in interview:

Use when discussing Python readability or Pydantic.
