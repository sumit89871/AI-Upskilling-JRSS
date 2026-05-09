# OpenAI/Gemini API Exercises

Use these exercises after reading `00-overview.md` and `01-openai-gemini-patterns.md`.

The goal is not to call a paid API immediately. The goal is to understand the safe integration pattern first.

## Exercise 1: Explain the `.env.example` file

Task:

Open `10-openai-gemini-api-python/implementation/.env.example` and explain every line.

Expected file content:

```text
OPENAI_API_KEY=replace_with_your_key
GEMINI_API_KEY=replace_with_your_key
USE_MOCK_LLM=true
```

Expected explanation:

- `OPENAI_API_KEY` is the variable name for an OpenAI key.
- `GEMINI_API_KEY` is the variable name for a Gemini key.
- `USE_MOCK_LLM=true` means the app should use mock mode by default.
- The values are placeholders, not real secrets.

Expected output:

No command output is required. The learner should be able to explain why `.env.example` is safe to commit and `.env` is not.

Hints:

- Focus on the difference between an API key and an environment variable.
- Remember that `.env.example` documents required names.

Self-check:

Can you explain why real API keys should not be written in Python files?

Solution outline:

Write a short note in your own words explaining each variable and why mock mode is default.

Common mistake:

Putting a real key into `.env.example`.

## Exercise 2: Run mock mode

Task:

Run the existing mock-first client selector.

Expected command:

```powershell
python llm_client.py
```

Where to run:

Run from:

```text
10-openai-gemini-api-python/implementation/
```

Command explanation:

- `python` runs the Python interpreter.
- `llm_client.py` is the file that selects the LLM client and calls `generate`.

Expected output:

```text
Mock LLM response for: Generate test cases for login
```

Hints:

- If you see an import error, check that you are inside the `implementation/` folder.
- The current selector returns `MockLLMClient()` safely.

Self-check:

Can you explain where `client` comes from in `llm_client.py`?

Solution outline:

- `get_llm_client()` returns a `MockLLMClient` object.
- `client` stores that object.
- `client.generate(...)` calls the mock client's method.

Common mistake:

Thinking `client` comes from OpenAI or Gemini. In this exercise, `client` comes from our own `MockLLMClient` class.

## Exercise 3: Decode `client.generate("Generate test cases for login")`

Task:

Explain this line slowly:

```python
response = client.generate("Generate test cases for login")
```

Expected explanation:

- `response` is a variable.
- `client` is an object.
- `.generate(...)` is a method on that object.
- `"Generate test cases for login"` is the prompt string.
- The method returns text.
- The returned text is stored in `response`.

Expected output:

If printed, the mock response should look like:

```text
Mock LLM response for: Generate test cases for login
```

Hints:

- Read the line left to right.
- Ask: where was `client` created?
- Ask: which class defines `generate`?

Self-check:

Can you identify whether `generate` is our method or a provider SDK method in the mock example?

Solution outline:

In the mock example, `generate` is defined manually inside `MockLLMClient`.

Common mistake:

Assuming every method named `generate` comes from a provider SDK.

## Exercise 4: Install optional requirements

Task:

Install optional packages from `requirements.txt`.

Expected command:

```powershell
pip install -r requirements.txt
```

Where to run:

Run from:

```text
10-openai-gemini-api-python/implementation/
```

When to run:

Run after activating the project virtual environment.

Command explanation:

- `pip` installs Python packages.
- `install` means add packages.
- `-r` means read package names from a file.
- `requirements.txt` contains `python-dotenv`, `openai`, and `google-genai`.

Expected output:

```text
Successfully installed ...
```

How to verify:

```powershell
pip show openai
pip show google-genai
```

Expected verification output:

```text
Name: openai
Version: ...
Location: ...
```

Hints:

- If the command fails because of internet or package index access, continue learning with mock mode.
- The course should not require paid API access for beginner practice.

Self-check:

Can you explain why package installation should happen inside `.venv`?

Solution outline:

Install dependencies in an isolated environment so this project does not affect other Python projects.

Common mistake:

Installing packages globally and then wondering why VS Code or Python cannot import them inside the project.

## Exercise 5: Run missing-key provider examples

Task:

Run the placeholder OpenAI and Gemini examples without setting real keys.

Expected commands:

```powershell
python example_openai_call.py
python example_gemini_call.py
```

Where to run:

Run from:

```text
10-openai-gemini-api-python/implementation/
```

Command explanation:

- `python example_openai_call.py` runs the OpenAI placeholder file.
- `python example_gemini_call.py` runs the Gemini placeholder file.
- These examples read environment variables and return safe missing-key messages.

Expected output:

```text
OPENAI_API_KEY not found. Use mock mode.
GEMINI_API_KEY not found. Use mock mode.
```

Hints:

- These files intentionally do not contain real provider calls yet.
- The purpose is to teach safe missing-key behavior.

Self-check:

Can you explain why missing-key behavior is better than a crash?

Solution outline:

The app should fail safely and clearly. In a POC, mock mode lets the demo continue without exposing secrets or requiring paid keys.

Common mistake:

Editing the Python file and pasting a real API key directly into it.

## Exercise 6: Design a provider selector

Task:

Write pseudocode that chooses between mock, OpenAI, and Gemini.

Expected code idea:

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

Expected output:

No terminal output is required. The expected result is a clear provider selection design.

Hints:

- Do not implement real provider calls yet.
- Focus on how the rest of the app can still call `client.generate(prompt)`.

Self-check:

Can you explain why all clients should have the same `generate(prompt)` method?

Solution outline:

The same method name lets FastAPI, RAG, and LangGraph call the client without knowing which provider is selected.

Common mistake:

Making each provider use a different method name, forcing the rest of the app to know provider details.

## Exercise 7: Explain system and user roles

Task:

Explain this message list:

```python
messages = [
    {"role": "system", "content": "You are a QA assistant."},
    {"role": "user", "content": "Generate test cases for login."},
]
```

Expected explanation:

- `messages` is a list.
- Each item is a dictionary.
- The system message sets behavior.
- The user message contains the task.
- `content` stores the actual text.

Expected output:

No command output is required. The learner should be able to explain the structure.

Hints:

- Compare system role to "rules for the assistant".
- Compare user role to "the current request".

Self-check:

Can you explain why the system role should not contain private API keys?

Solution outline:

System prompts are sent to the model provider. Secrets should never be included in prompts.

Common mistake:

Putting configuration secrets inside prompt text.
