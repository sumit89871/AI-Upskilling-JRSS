# OpenAI And Gemini API Integration Overview

## 1. What hosted LLM APIs are

A hosted LLM API is a service where another company runs the model on its servers, and your application calls that model over the internet.

Simple meaning:

```text
Your Python app -> internet request -> provider's LLM service -> model response -> your Python app
```

You do not download or train the large model yourself. You send input text to the provider, the provider runs the model, and you receive output.

Examples of hosted LLM providers:

- OpenAI
- Google Gemini
- Anthropic
- Azure-hosted model services
- other cloud or enterprise model platforms

This module focuses on OpenAI and Gemini at beginner integration level.

## 2. The most important beginner idea

OpenAI or Gemini is not your whole application.

Your app still controls:

- user input
- prompt construction
- API key loading
- provider selection
- request sending
- response parsing
- error handling
- fallback to mock mode
- final output returned to FastAPI, RAG, LangGraph, or Streamlit

Beginner mental model:

```text
Model provider = outside service
Your app = code that decides what to send, how to send it, and what to do with the result
```

If you understand this separation, the rest of the module becomes easier.

## 3. OpenAI vs Gemini in this course

OpenAI and Gemini are treated as provider options.

Provider means:

```text
the company/service that gives access to a model API
```

Model means:

```text
the AI system that generates the answer
```

Application means:

```text
your Python code, FastAPI backend, RAG pipeline, LangGraph workflow, or Streamlit demo
```

Comparison:

| Term | Simple meaning | Example |
| --- | --- | --- |
| Provider | Company/service exposing the API | OpenAI, Gemini |
| Model | AI system that generates text | a chat or generation model |
| Application | Your project code | final QA assistant POC |

In this course, do not depend on one provider too early. Learn the common pattern first.

## 4. SDK vs REST API

REST API means the provider exposes HTTP endpoints that can be called over the internet.

SDK means a Python package that makes those API calls easier.

Mental model:

```text
REST API = provider's HTTP interface
SDK = Python helper library that calls that interface for you
```

Example:

- `openai` package is an SDK for OpenAI.
- `google-genai` package is an SDK for Gemini-style usage in this module.
- Behind the SDK, HTTP requests still happen.

Why SDKs are useful:

- less manual HTTP code
- easier authentication
- easier request objects
- easier response handling

Why you still need to understand APIs:

- SDK calls can fail
- responses must be parsed
- rate limits still apply
- API keys must still be protected

## 5. API key vs environment variable

An API key is a secret value that proves your app is allowed to call a provider.

Environment variable is a safe way to provide configuration to your app without hardcoding it in source code.

Comparison:

| Concept | Meaning |
| --- | --- |
| API key | Secret credential from provider |
| Environment variable | Named value available to your running program |
| `.env` file | Local file that can store environment values for development |
| `.env.example` | Safe placeholder file that shows required variable names |

Bad:

```python
api_key = "real-secret-key"
```

Why this is bad:

- the key may be committed to Git
- someone else may copy it
- it may appear in screenshots
- it may be reused without permission

Better:

```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```

Syntax breakdown:

- `import os` loads Python's operating-system helper module.
- `os.getenv(...)` reads an environment variable.
- `"OPENAI_API_KEY"` is the name of the variable to read.
- If the variable is missing, Python returns `None`.

## 6. Request vs response

Request means what your application sends to the provider.

Response means what the provider sends back.

Mental model:

```text
request = question/instruction/config sent out
response = answer/data/error returned back
```

Example request data:

```python
prompt = "Generate test cases for login"
```

Example response text:

```text
1. Verify valid user can log in.
2. Verify invalid password is rejected.
3. Verify locked account cannot log in.
```

In real SDK calls, the response may be an object or nested dictionary-like structure. Response parsing means extracting the useful answer from that returned structure.

## 7. Prompt vs message

A prompt is the input instruction text sent to a model.

Example prompt:

```text
Generate test cases for login.
```

Many chat APIs use messages instead of one plain prompt.

Example messages:

```python
messages = [
    {"role": "system", "content": "You are a QA assistant."},
    {"role": "user", "content": "Generate test cases for login."},
]
```

Syntax breakdown:

- `messages` is a Python list.
- Square brackets `[]` create the list.
- Each item is a dictionary.
- Curly braces `{}` create each dictionary.
- `"role"` tells the model who is speaking.
- `"content"` stores the actual text.
- `"system"` sets behavior or rules.
- `"user"` contains the user's request.

Simple memory:

```text
system role = behavior instruction
user role = task request
```

## 8. Mock mode vs real provider mode

Mock mode means your app returns a fake predictable answer.

Real provider mode means your app calls OpenAI, Gemini, or another hosted provider.

Comparison:

| Mode | Uses real API key? | Uses internet? | Costs money? | Best for |
| --- | --- | --- | --- | --- |
| Mock mode | No | No | No | learning, tests, demos |
| Real provider mode | Yes | Usually yes | Usually yes | real model behavior |

Why mock mode first:

- beginner can run the project immediately
- no billing risk
- no secret-handling risk
- app architecture can be built before provider details
- tests become predictable

Mock mode is not fake in a bad way. It is a safe engineering technique.

## 9. How this connects to FastAPI, RAG, LangGraph, and final POC

FastAPI:

```text
HTTP request -> FastAPI endpoint -> LLM wrapper -> mock/OpenAI/Gemini -> JSON response
```

RAG:

```text
user question -> retrieve context -> build prompt with context -> LLM wrapper -> answer
```

LangGraph:

```text
state -> generation node -> LLM wrapper -> update state with answer
```

Final POC:

```text
Streamlit UI -> FastAPI backend -> RAG/context -> LangGraph workflow -> LLM wrapper -> structured QA output
```

The wrapper from this module becomes the safe middle layer between your application and model providers.

## 10. Install command

Run this only inside an activated virtual environment for this module or project:

```powershell
pip install -r requirements.txt
```

Where to run:

Run from:

```text
10-openai-gemini-api-python/implementation/
```

When to run:

Run when you want to install optional SDK packages for this implementation folder.

What each part means:

- `pip` installs Python packages.
- `install` tells pip to install packages.
- `-r` means read package names from a requirements file.
- `requirements.txt` contains package names such as `python-dotenv`, `openai`, and `google-genai`.

Expected output:

```text
Successfully installed ...
```

How to verify:

```powershell
pip show openai
pip show google-genai
```

Command explanation:

- `pip show openai` displays installed package information for the OpenAI SDK.
- `pip show google-genai` displays installed package information for the Gemini SDK package used in this module.

Expected verification output:

```text
Name: openai
Version: ...
Location: ...
```

Common beginner mistake:

Installing packages before activating `.venv` can install them into the wrong Python environment.

## 11. Common mistakes

- Hardcoding real API keys.
- Committing `.env`.
- Assuming SDK means no need to understand requests and responses.
- Assuming provider response shape never changes.
- Building the app so it fails completely when no key exists.
- Printing secrets in logs.
- Mixing OpenAI-specific or Gemini-specific code throughout the whole app.
- Forgetting timeout and retry strategy.

## 12. Similar concepts beginners confuse

### Provider vs model

Provider is the service/company.

Model is the AI system that generates output.

### SDK vs API

SDK is a Python package.

API is the service interface being called.

### API key vs environment variable

API key is the secret.

Environment variable is how your app receives the secret safely.

### Prompt vs messages

Prompt is usually one instruction string.

Messages are structured role-based inputs used by chat-style APIs.

### Mock client vs real client

Mock client returns predictable local output.

Real client calls a provider and must handle keys, network, cost, rate limits, and errors.

## 13. Where used in AI Engineer work

Hosted LLM API integration appears in:

- FastAPI AI endpoints
- RAG answer generation
- LangGraph generation nodes
- Streamlit AI demos
- final POC test case generation
- enterprise model-provider integration
- interview questions about secrets, providers, SDKs, and fallback design
