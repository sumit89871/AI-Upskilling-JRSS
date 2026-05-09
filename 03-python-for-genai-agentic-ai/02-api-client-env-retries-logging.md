# API Client Pattern, Environment Variables, Retries, And Logging

## 1. What it is

An API client is a small layer of Python code that hides the details of calling an external service.

Environment variables store configuration outside the source code.

Retry logic repeats an operation when the failure may be temporary.

Logging records what happened while the app ran.

## 2. The most important beginner idea

Do not spread API-calling code everywhere.

Instead, put provider-specific logic in one client class or function:

```text
app code -> LLM client -> OpenAI/Gemini/Ollama/mock provider
```

This keeps the rest of the app clean. Your FastAPI route, RAG pipeline, or LangGraph node can call `client.generate(prompt)` without caring which provider is behind it.

## 3. Why it matters

LLM APIs can fail because of missing API keys, invalid requests, network problems, rate limits, timeouts, or service outages.

Good client code makes these problems easier to debug and safer to demo.

Bad pattern:

```text
route function directly calls provider SDK with hardcoded key
```

Better pattern:

```text
route function -> client.generate() -> client handles provider, retries, logs, fallback
```

## 4. Beginner mental model

```text
read config -> build request -> call provider -> retry temporary failure -> parse response -> return safe result
```

Environment variables:

```text
.env file -> loaded into environment -> Python reads value -> client uses value
```

Logging:

```text
important event -> log message -> terminal/file shows what happened
```

## 5. API client pattern

```python
class LLMClient:
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class MockLLMClient(LLMClient):
    def generate(self, prompt: str) -> str:
        return f"Mock answer for: {prompt}"
```

Syntax breakdown:

- `class LLMClient:` creates a base class.
- `def generate(self, prompt: str) -> str:` defines the method every client should provide.
- `raise NotImplementedError` intentionally fails if the method is not implemented.
- `class MockLLMClient(LLMClient):` creates a child class.
- Parentheses mean `MockLLMClient` inherits from `LLMClient`.
- The child class provides the real `generate` behavior.

Why this helps:

You can later create `OpenAIClient`, `GeminiClient`, or `OllamaClient` with the same `.generate(...)` method.

## 6. Environment variables

Example `.env` value:

```text
OPENAI_API_KEY=your_placeholder_key_here
USE_MOCK_LLM=true
```

Important rule:

Never hardcode real API keys in Python files.

Read environment values in Python:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

Syntax breakdown:

- `import os` loads Python's operating-system helper module.
- `os.getenv(...)` reads an environment variable.
- `"OPENAI_API_KEY"` is the variable name.
- If the variable does not exist, `api_key` becomes `None`.

Common beginner confusion:

`.env` does not automatically load into Python in every setup. You often need `python-dotenv` or your framework/deployment platform to load it.

## 7. Retry and logging example

File name: `retry_logging.py`

Exact folder path: `03-python-for-genai-agentic-ai/practice/retry_logging.py`

Full code:

```python
import logging

logging.basicConfig(level=logging.INFO)


def unreliable_call(attempt):
    if attempt < 3:
        raise RuntimeError("Temporary failure")
    return "Success"


def call_with_retry(max_attempts):
    for attempt in range(1, max_attempts + 1):
        try:
            logging.info("Attempt %s", attempt)
            return unreliable_call(attempt)
        except RuntimeError as error:
            logging.warning("Call failed: %s", error)
    return "Failed after retries"


print(call_with_retry(3))
```

What this file is for:

It simulates a temporary failure and shows how retry logic can recover.

Important lines:

- `import logging` loads Python's logging module.
- `logging.basicConfig(level=logging.INFO)` enables info-level logs.
- `range(1, max_attempts + 1)` creates attempt numbers starting at `1`.
- `try` runs risky code.
- `except RuntimeError as error` catches the simulated failure.
- `logging.warning(...)` records a warning without crashing.
- `return unreliable_call(attempt)` returns immediately if the call succeeds.

Run from the module folder:

```powershell
python .\practice\retry_logging.py
```

Command explanation:

- `python` runs Python.
- `.\practice\retry_logging.py` points to the script.
- This example uses only Python's standard library.

Expected output:

```text
INFO:root:Attempt 1
WARNING:root:Call failed: Temporary failure
INFO:root:Attempt 2
WARNING:root:Call failed: Temporary failure
INFO:root:Attempt 3
Success
```

The exact log prefix may vary, but you should see two failed attempts and then `Success`.

How to verify:

Change `call_with_retry(3)` to `call_with_retry(2)`. The final output should become:

```text
Failed after retries
```

## 8. Retry rules

Retry temporary failures:

- timeout
- rate limit
- temporary network problem
- service unavailable

Do not blindly retry permanent failures:

- missing API key
- invalid request body
- unsupported model name
- broken code

Always use a max retry count. Never create infinite retries.

## 9. Logging safety

Good logs:

```text
INFO Calling LLM provider
WARNING Request timed out on attempt 2
ERROR Missing OPENAI_API_KEY
```

Bad logs:

```text
OPENAI_API_KEY=real-secret-value
```

Never print real secrets in logs, screenshots, commits, or demo recordings.

## 10. Common mistakes

- Hardcoding API keys.
- Retrying every error.
- Retrying forever without a limit.
- Printing secrets in logs.
- Logging too little to debug a failure.
- Returning provider-specific objects directly to the UI.
- Not providing a mock fallback for demo mode.

## 11. Where used in AI Engineer work

- OpenAI/Gemini clients
- Ollama local clients
- RAG document loaders
- vector DB calls
- FastAPI service logs
- LangGraph retry nodes
- MCP tool error handling
- final POC demo resilience
