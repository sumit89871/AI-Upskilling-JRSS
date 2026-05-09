# OpenAI/Gemini Cheatsheet

Use this after reading the detailed notes. It is concise, but it should still remind you what each command or pattern means.

## Hosted LLM API

Meaning:

Your Python app sends input to a provider-hosted model and receives a generated response.

When to use:

Use when your app needs model output without running a large model locally.

Example:

```text
FastAPI endpoint -> LLM wrapper -> OpenAI/Gemini/mock -> answer
```

Be careful:

Hosted providers may require API keys, internet access, billing, and rate-limit handling.

## API key

Meaning:

A secret credential used to authenticate provider API calls.

When to use:

Use when real provider mode is enabled.

Example:

```text
OPENAI_API_KEY=replace_with_your_key
```

Be careful:

Never hardcode real keys in Python files or commit `.env`.

## Environment variable

Meaning:

A named value your running program can read.

When to use:

Use for API keys, provider selection, model names, and mock-mode flags.

Example:

```python
api_key = os.getenv("OPENAI_API_KEY")
```

Be careful:

If the variable is missing, `os.getenv(...)` returns `None` unless you provide a default.

## Install packages

Command:

```powershell
pip install -r requirements.txt
```

Meaning:

Install packages listed in `requirements.txt`.

When to use:

Use after activating `.venv` and moving into `10-openai-gemini-api-python/implementation/`.

Example:

```powershell
pip install -r requirements.txt
```

Expected output:

```text
Successfully installed ...
```

Be careful:

Running this outside the active virtual environment may install packages in the wrong place.

## Verify packages

Command:

```powershell
pip show openai
pip show google-genai
```

Meaning:

Show installed package information.

When to use:

Use after installing requirements.

Example output:

```text
Name: openai
Version: ...
Location: ...
```

Be careful:

No output or "not found" means the package is not installed in the current environment.

## Run mock mode

Command:

```powershell
python llm_client.py
```

Meaning:

Run the local client selector and call the mock client.

When to use:

Use before real provider mode to confirm the wrapper works.

Expected output:

```text
Mock LLM response for: Generate test cases for login
```

Be careful:

Run from `10-openai-gemini-api-python/implementation/`.

## Mock client pattern

Syntax:

```python
client = MockLLMClient()
response = client.generate("Generate test cases for login")
print(response)
```

Meaning:

Create a mock client object, call its `generate` method with a prompt, store the returned text, and print it.

When to use:

Use for local learning, tests, and demos without real keys.

Be careful:

`generate` is our method in the mock example, not automatically a provider SDK method.

## Wrapper pattern

Meaning:

Your app calls one simple method such as `client.generate(prompt)` while provider-specific code stays inside client classes.

When to use:

Use when the app may support mock, OpenAI, Gemini, or another provider.

Example:

```python
answer = client.generate(prompt)
```

Be careful:

Do not put provider SDK code directly into every FastAPI route, RAG function, or LangGraph node.

## System and user messages

Syntax:

```python
messages = [
    {"role": "system", "content": "You are a QA assistant."},
    {"role": "user", "content": "Generate test cases."},
]
```

Meaning:

System message sets behavior. User message contains the task.

When to use:

Use with chat-style model APIs.

Be careful:

Do not put secrets or private keys inside prompts/messages.

## Response parsing

Meaning:

Extract the useful answer from the provider's returned response object.

When to use:

Use after calling a real provider SDK.

Example:

```python
parsed_answer = response_text
```

Be careful:

Different providers return different response structures. Keep parsing inside provider-specific client classes.
