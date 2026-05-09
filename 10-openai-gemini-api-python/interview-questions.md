# OpenAI/Gemini API Interview Questions

## 1. What is a hosted LLM API?

Short answer:

A hosted LLM API lets your app call a model running on a provider's servers.

Expanded answer:

Instead of running a large model on your laptop, your Python app sends a request to a provider such as OpenAI or Gemini. The provider runs the model and returns a response. Your app still handles prompts, keys, request building, response parsing, errors, and fallback behavior.

Project example:

In the final POC, a FastAPI endpoint can call an LLM wrapper. The wrapper may use mock mode locally or a hosted provider if keys are available.

Common wrong answer:

"The API is the model."

This is incomplete. The API is the interface used to call the provider service. The model is the AI system behind that service.

## 2. What is an API key?

Short answer:

An API key is a secret credential used to authenticate API calls.

Expanded answer:

Providers use API keys to identify and authorize your application. If the key is missing, invalid, or leaked, real provider calls may fail or become unsafe. API keys should be read from environment variables, not hardcoded in Python files.

Project example:

The implementation uses `OPENAI_API_KEY` and `GEMINI_API_KEY` names in `.env.example` as placeholders.

Common wrong answer:

"An API key is just a variable."

It may be stored in a variable at runtime, but the key itself is a secret credential.

## 3. Why use environment variables?

Short answer:

Environment variables keep secrets and configuration outside source code.

Expanded answer:

Environment variables let the same code run in different modes without editing Python files. For example, local development can use `USE_MOCK_LLM=true`, while a secured environment can provide real provider keys.

Project example:

`llm_client.py` reads `USE_MOCK_LLM` to decide whether to use mock behavior.

Common wrong answer:

"Environment variables are only for API keys."

They are also useful for provider selection, model names, feature flags, file paths, and deployment settings.

## 4. What is the difference between a provider, a model, and an application?

Short answer:

Provider is the service/company, model is the AI system, and application is your code that uses it.

Expanded answer:

OpenAI or Gemini is the provider. A specific LLM is the model. Your FastAPI/RAG/Streamlit/POC code is the application. The application sends requests to the provider and uses the model response.

Project example:

The final QA assistant is the application. It may call OpenAI or Gemini through a wrapper.

Common wrong answer:

"OpenAI is my app's model."

OpenAI is usually the provider. The model is the AI system accessed through that provider.

## 5. What is an SDK?

Short answer:

An SDK is a Python package that helps your code call a provider API.

Expanded answer:

An SDK gives ready-made classes and functions so you do not manually write every HTTP request. However, you still need to understand authentication, request data, response parsing, errors, and rate limits.

Project example:

`requirements.txt` lists `openai` and `google-genai` as optional SDK packages.

Common wrong answer:

"The SDK replaces the API."

The SDK helps call the API. It does not remove the provider API behind it.

## 6. What is a wrapper and why use one?

Short answer:

A wrapper is your own layer that hides provider-specific details behind a simple method such as `generate(prompt)`.

Expanded answer:

Without a wrapper, OpenAI or Gemini-specific code may spread across FastAPI routes, RAG functions, and LangGraph nodes. With a wrapper, the rest of the app calls one interface, while provider details stay inside client classes.

Project example:

The app can call `client.generate(prompt)` whether `client` is a mock client, OpenAI client, or Gemini client.

Common wrong answer:

"A wrapper is just extra code."

It is extra structure, but it solves provider switching, testing, fallback, and maintainability problems.

## 7. What does `client.generate("Generate test cases for login")` mean?

Short answer:

It calls the `generate` method on the `client` object and passes a prompt string.

Expanded answer:

`client` is an object created from a class such as `MockLLMClient`. `generate` is a method defined on that class. The string is the prompt input. The method returns an answer, which can be stored in a variable or printed.

Project example:

In `llm_client.py`, `client = get_llm_client()` creates/selects a client, then `client.generate(...)` gets the mock answer.

Common wrong answer:

"`generate` is from OpenAI."

In the mock example, `generate` is our own method. A real provider client may use SDK-specific methods internally, but the wrapper exposes our consistent `generate` method.

## 8. What should happen if no API key exists?

Short answer:

The app should use mock fallback or fail with a clear safe error.

Expanded answer:

Missing API key is a configuration issue. The app should not crash with an unclear traceback, and it should never ask the learner to paste keys into source code. For beginner POCs, mock mode is the safest default.

Project example:

`example_openai_call.py` returns `OPENAI_API_KEY not found. Use mock mode.`

Common wrong answer:

"Just hardcode the key temporarily."

This is unsafe and can leak secrets.

## 9. What is response parsing?

Short answer:

Response parsing means extracting the useful answer from the provider response.

Expanded answer:

Provider SDKs often return objects or nested structures, not just plain strings. Your client code should extract the actual answer text or JSON your app needs. Parsing should stay inside provider-specific client classes.

Project example:

In the final POC, the backend should return a clean structured response, not a raw provider object.

Common wrong answer:

"Parsing means the model generates text."

Generating is what the model does. Parsing is what your code does after receiving the response.

## 10. What are rate limits?

Short answer:

Rate limits are provider rules that restrict how many requests or tokens you can use in a time period.

Expanded answer:

Providers use rate limits to protect services and control usage. If your app sends too many requests too quickly, provider calls may fail temporarily. Good clients handle this with clear errors, retries, backoff, or user-friendly messages.

Project example:

A final POC should avoid uncontrolled loops that call the LLM repeatedly without limits.

Common wrong answer:

"Rate limit means the model is down."

Rate limiting usually means you exceeded an allowed usage threshold, not necessarily that the provider is unavailable.

## 11. Why use mock mode first?

Short answer:

Mock mode lets the app run safely without real keys, cost, internet, or provider setup.

Expanded answer:

Mock mode helps beginners build and test application flow first. It makes outputs predictable and avoids billing or secret risks. After the app architecture works, real provider integration can be added as an optional upgrade.

Project example:

The final POC can demonstrate FastAPI, RAG, MCP-style tools, LangGraph-style workflow, and Streamlit UI even without paid LLM access.

Common wrong answer:

"Mock mode is useless because it is not real AI."

Mock mode is an engineering technique. It validates the integration path before adding real provider behavior.

## 12. How does this module connect to RAG and LangGraph?

Short answer:

RAG and LangGraph can call the same LLM wrapper to generate answers.

Expanded answer:

In RAG, retrieved context is placed into a prompt and sent through the wrapper. In LangGraph, a generation node can call the wrapper and store the result in state. The wrapper keeps provider details out of the RAG and graph logic.

Project example:

The final POC can use one `client.generate(prompt)` call inside the generation step.

Common wrong answer:

"RAG and LangGraph each need separate provider code."

They can share the same wrapper pattern.
