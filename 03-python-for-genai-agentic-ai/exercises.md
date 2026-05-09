# Python For GenAI Exercises

## Exercise 1: Nested Response Parsing

Create a dictionary:

```python
response = {
    "result": {
        "answer": "Use FastAPI for backend APIs",
        "sources": ["fastapi.md", "rest-api.md"]
    }
}
```

Print:

- answer
- first source

## Exercise 2: Structured Output

Create a Python dictionary that represents generated test cases:

- `summary`
- `test_cases`
- each test case should have `title`, `type`, `priority`, and `expected_result`

## Exercise 3: State Updates

Create state:

```python
state = {"query": "Explain MCP", "steps": [], "answer": None}
```

Update it through three fake steps:

- `analyzed_query`
- `selected_tool`
- `generated_answer`

## Exercise 4: Mock LLM Client

Create a class:

```python
class MockLLMClient:
    def generate(self, prompt):
        return "Mock answer for: " + prompt
```

Call it with a prompt about RAG.

## Exercise 5: Retry Logic

Write a function that fails for the first two attempts and succeeds on the third attempt.

Use a loop and `try/except`.

## Exercise 6: Tool Function

Create:

```python
def get_test_user(role):
    ...
```

Return username and password in a dictionary.

Use the tool result in a prompt.

## Exercise 7: Agent Loop

Create a loop that:

- starts with a user goal
- increments `step_count`
- adds step names to state
- stops after `3` steps
- sets `final_answer`

Add a max step count so it cannot run forever.

