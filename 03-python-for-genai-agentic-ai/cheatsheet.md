# Python For GenAI Cheatsheet

## Nested Dictionary Access

```python
answer = response["result"]["answer"]
```

## Safe Dictionary Access

```python
answer = response.get("result", {}).get("answer", "No answer")
```

## State Dictionary

```python
state = {
    "query": "Generate test cases",
    "steps": [],
    "final_answer": None,
}
```

## Update State

```python
state["steps"].append("retrieved_context")
state["final_answer"] = "Done"
```

## Prompt Template

```python
template = "Answer using this context: {context}\nQuestion: {question}"
prompt = template.format(context="notes", question="What is RAG?")
```

## Mock LLM Client

```python
class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return f"Mock answer for: {prompt}"
```

## Environment Variable

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

## Retry Skeleton

```python
for attempt in range(1, 4):
    try:
        result = call_api()
        break
    except RuntimeError:
        result = None
```

## Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Starting workflow")
```

## Tool Function

```python
def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}
```

## Agent Loop Guard

```python
max_steps = 5
step_count = 0

while step_count < max_steps:
    step_count += 1
```

Always use a stop condition.

