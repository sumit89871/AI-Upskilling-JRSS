# Implementation: LLM Client Pattern

This implementation is intentionally beginner-friendly and mock-first.

It does not require real OpenAI or Gemini keys to run the main example.

## 1. What this implementation demonstrates

This folder demonstrates the wrapper/client pattern:

```text
app code -> get_llm_client() -> selected client -> generate(prompt) -> response text
```

Current behavior:

- `llm_client.py` selects the client.
- The selected client is currently `MockLLMClient`.
- Mock mode returns predictable local text.
- OpenAI and Gemini files are safe placeholder examples for missing-key behavior.

## 2. File list

### `llm_client.py`

What it is for:

This file is the provider selector. It decides which LLM client object the app should use.

Current beginner behavior:

It reads `USE_MOCK_LLM` and safely returns `MockLLMClient()`.

Important code:

```python
client = get_llm_client()
print(client.generate("Generate test cases for login"))
```

Meaning:

- `get_llm_client()` creates/selects a client object.
- `client` stores that object.
- `client.generate(...)` calls the client's `generate` method.
- The prompt string is the input.
- `print(...)` displays the returned answer.

### `mock_llm_client.py`

What it is for:

This file defines the no-key fallback client.

Important code:

```python
class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return f"Mock LLM response for: {prompt}"
```

Meaning:

- `MockLLMClient` is our class.
- `generate` is our method.
- `prompt` is input text.
- The method returns predictable mock text.

### `example_openai_call.py`

What it is for:

This file shows safe OpenAI key checking without hardcoding a key.

Current behavior:

- reads `OPENAI_API_KEY`
- if missing, returns a safe message
- does not perform a real provider call yet

Expected missing-key output:

```text
OPENAI_API_KEY not found. Use mock mode.
```

### `example_gemini_call.py`

What it is for:

This file shows safe Gemini key checking without hardcoding a key.

Current behavior:

- reads `GEMINI_API_KEY`
- if missing, returns a safe message
- does not perform a real provider call yet

Expected missing-key output:

```text
GEMINI_API_KEY not found. Use mock mode.
```

### `.env.example`

What it is for:

This file documents the environment variables the module may use.

Content:

```text
OPENAI_API_KEY=replace_with_your_key
GEMINI_API_KEY=replace_with_your_key
USE_MOCK_LLM=true
```

Important:

This file contains placeholders only. Do not put real secrets in `.env.example`.

### `requirements.txt`

What it is for:

This file lists optional packages:

```text
python-dotenv
openai
google-genai
```

Meaning:

- `python-dotenv` can load local `.env` files.
- `openai` is the OpenAI SDK package.
- `google-genai` is the Gemini SDK package used by this module.

## 3. Setup steps

### Step 1: Move into the implementation folder

Command:

```powershell
cd .\ai-engineer-jrss-reskilling-course\10-openai-gemini-api-python\implementation
```

Where to run:

Run from workspace root:

```text
C:\Users\Sumit\Desktop\AI_Test_Engineer_JRSS
```

What each part means:

- `cd` means change directory.
- The path moves into this module's implementation folder.

Expected output:

PowerShell usually prints no output. The prompt path should change.

How to verify:

```powershell
Get-Location
```

Expected verification:

The printed path should end with:

```text
10-openai-gemini-api-python\implementation
```

Common beginner mistake:

Running `python llm_client.py` from the wrong folder and getting an import error.

### Step 2: Install optional requirements

Command:

```powershell
pip install -r requirements.txt
```

Where to run:

Run inside:

```text
10-openai-gemini-api-python/implementation/
```

When to run:

Run after activating your virtual environment.

What each part means:

- `pip` installs Python packages.
- `install` means add packages.
- `-r` means read from a requirements file.
- `requirements.txt` is the package list.

Expected output:

```text
Successfully installed ...
```

How to verify:

```powershell
pip show openai
pip show google-genai
```

Expected verification:

You should see package name, version, and location.

Common beginner mistake:

Installing packages globally instead of inside the project's `.venv`.

## 4. How to create `.env`

Do not edit `.env.example` with real keys.

Create a local `.env` file if you want local configuration.

Example `.env` content:

```text
OPENAI_API_KEY=replace_with_real_key_only_if_available
GEMINI_API_KEY=replace_with_real_key_only_if_available
USE_MOCK_LLM=true
```

Important:

- `.env` should stay local.
- `.env` should not be committed.
- Real keys should not appear in screenshots or notes.

## 5. Run mock mode

Command:

```powershell
python llm_client.py
```

Where to run:

Run inside:

```text
10-openai-gemini-api-python/implementation/
```

What each part means:

- `python` runs Python.
- `llm_client.py` is the local selector file.

Expected output:

```text
Mock LLM response for: Generate test cases for login
```

How to verify:

If you see the prompt text inside the mock response, the selector and mock client worked.

Common error:

```text
ModuleNotFoundError: No module named 'mock_llm_client'
```

Likely cause:

You ran the command from the wrong folder.

Fix:

Move into the `implementation/` folder and rerun.

## 6. Run provider placeholder mode

These files are safe placeholders. They check for missing keys and return clear messages.

Command:

```powershell
python example_openai_call.py
```

Expected output without key:

```text
OPENAI_API_KEY not found. Use mock mode.
```

Command:

```powershell
python example_gemini_call.py
```

Expected output without key:

```text
GEMINI_API_KEY not found. Use mock mode.
```

Common beginner mistake:

Thinking these files already make real provider calls. They currently teach safe key checking and placeholder behavior.

## 7. How real provider mode would be added later

Real provider mode would usually require:

- installing provider SDKs
- reading the API key from environment variables
- creating a provider-specific client
- sending prompt/messages
- parsing the provider response
- handling errors, timeouts, and rate limits

Beginner-safe design:

```text
FastAPI/RAG/LangGraph code -> client.generate(prompt)
provider-specific SDK details -> hidden inside OpenAIClient or GeminiClient
```

Do not put real provider SDK code directly into every route or workflow node.

## 8. Common errors

### `ModuleNotFoundError`

Meaning:

Python cannot find a module you imported.

Likely cause:

Wrong folder, missing package, or incorrect import path.

### Missing API key

Meaning:

Environment variable such as `OPENAI_API_KEY` or `GEMINI_API_KEY` is not set.

Safe behavior:

Return a clear message or use mock mode.

### Package not found

Meaning:

`pip show openai` or `pip show google-genai` does not show package details.

Likely cause:

Package was not installed in the active environment.

### Real provider call fails

Possible causes:

- invalid key
- no internet
- rate limit
- timeout
- provider SDK change
- wrong model/provider configuration

## 9. How this connects to the final POC

The final POC can use the same pattern:

```text
Streamlit UI -> FastAPI endpoint -> RAG/LangGraph workflow -> LLM wrapper -> mock/OpenAI/Gemini -> structured response
```

Why this matters:

- mock mode keeps the demo runnable without paid keys
- wrapper keeps provider code isolated
- FastAPI route stays clean
- RAG and LangGraph can reuse the same `client.generate(prompt)` idea
- interview explanation becomes simpler and more professional

## 10. Beginner self-check

Before moving on, confirm you can answer:

- What is `MockLLMClient`?
- Where does `client` come from?
- What does `generate` mean in this implementation?
- What does the prompt string do?
- What does the method return?
- What happens if API keys are missing?
- Why is mock mode the default?
- Why should OpenAI/Gemini SDK code be isolated behind a wrapper?
