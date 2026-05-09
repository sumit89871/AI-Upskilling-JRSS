# OpenAI And Gemini Integration Patterns

## 1. What this topic is

This topic explains the practical pattern for connecting your Python app to OpenAI, Gemini, or mock mode without spreading provider-specific code everywhere.

Important phrase:

```text
provider-specific code
```

Provider-specific code means code that only works for one provider.

Example:

- OpenAI SDK code is OpenAI-specific.
- Gemini SDK code is Gemini-specific.
- Ollama local HTTP code is Ollama-specific.
- Mock client code is local practice code.

If every FastAPI route, RAG function, and LangGraph node directly uses provider-specific code, your app becomes hard to change.

## 2. The most important beginner idea

Your application should call your own simple interface, not random provider SDK code everywhere.

Beginner mental model:

```text
User prompt -> our app wrapper -> selected provider client -> hosted LLM API -> response -> parsed answer
```

The app should be able to say:

```python
response = client.generate("Generate test cases for login")
```

without caring whether `client` is:

- a mock client
- an OpenAI client
- a Gemini client
- a future Ollama client

This is why the wrapper pattern exists.

## 3. What problem a wrapper solves

A wrapper is your own small layer around provider details.

Simple meaning:

```text
wrapper = your code that gives the rest of the app one simple way to call different providers
```

Problem without wrapper:

```text
FastAPI route contains OpenAI code
RAG function contains Gemini code
LangGraph node contains different provider code
Tests cannot run without real keys
Changing provider requires edits everywhere
```

Better with wrapper:

```text
FastAPI route -> client.generate(prompt)
RAG function -> client.generate(prompt)
LangGraph node -> client.generate(prompt)
Only the client implementation knows provider details
```

The wrapper solves:

- provider switching
- mock fallback
- easier testing
- safer secret handling
- cleaner app logic
- simpler final POC explanation

## 4. What `client.generate("prompt")` means

Look at this beginner example:

```python
client = MockLLMClient()
response = client.generate("Generate test cases for login")
print(response)
```

Read it in this order:

```text
MockLLMClient -> client -> generate(...) -> response -> print(...)
```

Meaning:

- `MockLLMClient` is our class.
- `client = MockLLMClient()` creates an object from that class.
- `client` is the variable name storing that object.
- `.generate(...)` calls a method on the object.
- `"Generate test cases for login"` is the prompt string.
- `response` stores the returned answer.
- `print(response)` displays the answer in the terminal.

Important:

`generate` is not automatically from OpenAI or Gemini in this example.

`generate` is a method we define in our own class so the rest of the app has a consistent way to request output.

## 5. Detailed mock client example

File name:

`mock_llm_client.py`

Folder path:

`10-openai-gemini-api-python/implementation/mock_llm_client.py`

What this file is for:

This file creates a local fake LLM client. It lets the learner run the app without API keys, internet, billing, or provider SDK setup.

Full code:

```python
class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return f"Mock LLM response for: {prompt}"
```

Line-by-line explanation:

- `class MockLLMClient:` creates a class named `MockLLMClient`.
- A class is a blueprint for creating objects.
- `def generate(self, prompt: str) -> str:` creates a method named `generate`.
- A method is a function that belongs to a class/object.
- `self` means the current object.
- `prompt: str` means the method expects `prompt` to be text.
- `-> str` means the method should return text.
- `return f"Mock LLM response for: {prompt}"` sends text back to the caller.
- `f"..."` is an f-string.
- `{prompt}` inserts the prompt value into the returned text.

What learner creates manually:

- the file
- the class name
- the `generate` method
- the returned mock response format

What Python gives automatically:

- object creation through `MockLLMClient()`
- method calling through `client.generate(...)`
- passing the current object as `self`

## 6. Running the mock client through the selector

File name:

`llm_client.py`

Folder path:

`10-openai-gemini-api-python/implementation/llm_client.py`

Important code:

```python
import os

from mock_llm_client import MockLLMClient


def get_llm_client():
    use_mock = os.getenv("USE_MOCK_LLM", "true").lower() == "true"
    if use_mock:
        return MockLLMClient()
    return MockLLMClient()


if __name__ == "__main__":
    client = get_llm_client()
    print(client.generate("Generate test cases for login"))
```

Line-by-line explanation:

- `import os` imports Python's operating-system helper module.
- `from mock_llm_client import MockLLMClient` imports our mock class from another file.
- `def get_llm_client():` creates a function that chooses which client to use.
- `os.getenv("USE_MOCK_LLM", "true")` reads the environment variable named `USE_MOCK_LLM`.
- The second value `"true"` is the default if the environment variable is missing.
- `.lower()` converts text such as `"TRUE"` to `"true"`.
- `== "true"` checks whether mock mode is enabled.
- `if use_mock:` means if mock mode is true, run the next indented line.
- `return MockLLMClient()` creates and returns a mock client object.
- The second `return MockLLMClient()` is currently a safe fallback so the beginner app still runs.
- `if __name__ == "__main__":` runs the block only when this file is executed directly.
- `client = get_llm_client()` stores the selected client object.
- `client.generate(...)` calls the `generate` method on that selected client.
- `print(...)` displays the returned answer.

Run command:

```powershell
python llm_client.py
```

Where to run:

Run from:

```text
10-openai-gemini-api-python/implementation/
```

When to run:

Run this when you want to test that the wrapper pattern works locally.

Command explanation:

- `python` starts the Python interpreter.
- `llm_client.py` is the file to execute.

Expected output:

```text
Mock LLM response for: Generate test cases for login
```

How to verify:

If the output includes your prompt text, the selector created a client and called its `generate` method successfully.

Common beginner mistake:

Running the command from the wrong folder can cause:

```text
ModuleNotFoundError: No module named 'mock_llm_client'
```

Fix:

Run the command from the `implementation/` folder, or adjust imports and module paths later when building a larger project.

## 7. How mock, OpenAI, and Gemini clients can share the same method

The key idea is consistent method name.

Example:

```python
class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return f"Mock answer for: {prompt}"


class OpenAIClient:
    def generate(self, prompt: str) -> str:
        return "OpenAI answer would be parsed here"


class GeminiClient:
    def generate(self, prompt: str) -> str:
        return "Gemini answer would be parsed here"
```

All three classes have:

```python
generate(self, prompt: str) -> str
```

That means the rest of the app can call:

```python
answer = client.generate(prompt)
```

without changing the route, RAG function, or LangGraph node.

The object stored in `client` decides which implementation runs.

Beginner memory:

```text
same method name -> different class implementation -> same app code can call it
```

## 8. Provider selection using environment variables

Provider selection means choosing which client your app should use.

Example environment values:

```text
USE_MOCK_LLM=true
LLM_PROVIDER=openai
OPENAI_API_KEY=replace_with_your_key
GEMINI_API_KEY=replace_with_your_key
```

Beginner selector idea:

```python
provider = os.getenv("LLM_PROVIDER", "mock")

if provider == "mock":
    client = MockLLMClient()
elif provider == "openai":
    client = OpenAIClient()
elif provider == "gemini":
    client = GeminiClient()
else:
    client = MockLLMClient()
```

Syntax breakdown:

- `provider` stores the selected provider name.
- `os.getenv("LLM_PROVIDER", "mock")` reads an environment variable and uses `"mock"` if missing.
- `if`, `elif`, and `else` choose one path.
- `MockLLMClient()`, `OpenAIClient()`, and `GeminiClient()` create client objects.

Why this is useful:

The same app can run locally with mock mode and later run with a real provider when keys are available.

## 9. Response parsing

Response parsing means extracting the useful answer from whatever the provider returns.

Mock client response is simple:

```python
"Mock LLM response for: Generate test cases for login"
```

Real provider responses are often nested objects.

Beginner mental model:

```text
provider response object -> find answer field -> return plain text or structured JSON
```

Why parsing matters:

Your app usually does not want to return the entire provider object to the UI. It wants the useful answer.

Example:

```python
parsed_answer = response_text
return parsed_answer
```

In a real OpenAI/Gemini client, `response_text` would come from the provider SDK response structure.

Common mistake:

Assuming every provider returns the answer in the same field. They do not.

That is another reason to keep provider parsing inside provider-specific client classes.

## 10. Timeout, retry logic, and rate limits

Timeout means:

```text
do not wait forever for an API call
```

Retry means:

```text
try again when a failure may be temporary
```

Rate limit means:

```text
provider allows only a certain number of requests/tokens in a time window
```

Retry pattern:

```python
for attempt in range(3):
    try:
        answer = client.generate(prompt)
        break
    except Exception as error:
        print(f"Attempt {attempt + 1} failed: {error}")
```

Syntax breakdown:

- `for attempt in range(3):` runs up to three attempts.
- `try:` starts code that may fail.
- `answer = client.generate(prompt)` calls the LLM client.
- `break` exits the loop after success.
- `except Exception as error:` catches an error and stores it in `error`.
- `attempt + 1` prints human-friendly attempt numbers starting from 1.

Important beginner warning:

Do not retry forever. Always use a limit.

Do not retry missing API key errors as if they are temporary. A missing key requires configuration, not retry.

## 11. Expected outputs

Mock mode expected output:

```text
Mock LLM response for: Generate test cases for login
```

Missing OpenAI key placeholder output:

```text
OPENAI_API_KEY not found. Use mock mode.
```

Missing Gemini key placeholder output:

```text
GEMINI_API_KEY not found. Use mock mode.
```

These outputs are intentionally safe. They teach the app to fail clearly instead of exposing secrets or crashing.

## 12. Common beginner mistakes

- Thinking `client` is automatically created by OpenAI or Gemini.
- Thinking `generate` is always a provider SDK method.
- Hardcoding real API keys.
- Committing `.env`.
- Mixing OpenAI code directly inside FastAPI routes.
- Returning the full provider object instead of parsed text.
- Not handling missing API keys.
- Retrying permanent errors.
- Forgetting that real provider mode may cost money.
- Not using mock mode for tests and demos.

## 13. Similar concepts beginners confuse

### Provider code vs app code

Provider code talks to OpenAI, Gemini, or another model service.

App code handles your business flow such as FastAPI route, RAG prompt, or LangGraph node.

### Client vs provider

Client is the Python object your app uses.

Provider is the external service/company.

### Method vs function

`generate` is a method when it belongs to an object such as `client`.

A standalone function is called without an object.

### Mock response vs real response

Mock response is predictable local text.

Real response comes from the provider and may vary.

### Parsing vs generating

Generating means the model creates output.

Parsing means your code extracts the useful part from the returned response.

## 14. Where used in AI Engineer work

This pattern appears in:

- FastAPI `/ask` or `/generate-test-cases` endpoints
- RAG generator step
- LangGraph generation node
- Streamlit demo backend call
- final POC mock-first design
- production code where provider switching may be needed
- interview explanations about clean architecture and secret safety
