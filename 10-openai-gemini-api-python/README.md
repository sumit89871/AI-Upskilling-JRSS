# 10 OpenAI And Gemini API From Python

## 1. What this module is

This module teaches how a Python application can call hosted LLM APIs such as OpenAI and Gemini.

Hosted LLM API means:

```text
Your Python app sends a request over the internet -> provider runs the model on its servers -> provider sends a response back
```

In this module, the learner starts with mock mode first. Mock mode means the code returns a fake but predictable response without using a real API key, internet call, or paid provider.

This is important because a beginner should first understand the app structure before dealing with provider accounts, billing, rate limits, and SDK details.

## 2. Why it matters

AI Engineer work is often integration work.

You usually do not train a large model from scratch. You connect an application to a model provider safely and reliably.

That means you must understand:

- what a provider is
- what an SDK is
- what an API key is
- why API keys must not be hardcoded
- how requests and responses work
- how prompts/messages are sent
- how to parse the provider response
- how to handle missing keys, timeouts, rate limits, and temporary failures
- why application code should not depend directly on one provider everywhere

## 3. What the learner should finish knowing

After this module, the learner should be able to explain and use:

- hosted LLM APIs
- OpenAI vs Gemini at a beginner integration level
- provider vs model vs application
- SDK vs REST API
- API key vs environment variable
- request vs response
- prompt vs message list
- system role vs user role
- mock mode vs real provider mode
- wrapper/client pattern
- `client.generate("prompt")`
- response parsing
- retry, timeout, and rate-limit basics
- safe `.env.example` placeholders
- how this module connects to FastAPI, RAG, LangGraph, and the final POC

## 4. Study order

1. `00-overview.md`
2. `01-openai-gemini-patterns.md`
3. `implementation/README.md`
4. `exercises.md`
5. `cheatsheet.md`
6. `interview-questions.md`

## 5. File list

Current module files:

- `README.md`: this module guide.
- `00-overview.md`: beginner explanation of hosted APIs, keys, messages, mock mode, and provider mode.
- `01-openai-gemini-patterns.md`: wrapper/client pattern, provider-specific code, response parsing, retries, and rate limits.
- `exercises.md`: hands-on practice tasks with expected outputs, hints, and self-checks.
- `cheatsheet.md`: quick but meaningful command/syntax reference.
- `interview-questions.md`: interview answers with short answer, expanded answer, project example, and common wrong answer.
- `implementation/README.md`: how the implementation files work and how to run them.
- `implementation/llm_client.py`: provider selector that currently returns mock client behavior.
- `implementation/mock_llm_client.py`: simple no-key fallback client.
- `implementation/example_openai_call.py`: placeholder OpenAI example with safe missing-key behavior.
- `implementation/example_gemini_call.py`: placeholder Gemini example with safe missing-key behavior.
- `implementation/.env.example`: safe placeholder environment variables.
- `implementation/requirements.txt`: optional package list.

## 6. Practical scope

This module is local-first and mock-first.

Required:

- understand the integration pattern
- run mock mode
- explain where `client` comes from
- explain what `generate` means
- understand why wrapper code exists
- avoid hardcoded secrets

Optional:

- install provider SDKs
- add real OpenAI or Gemini calls later
- use real keys locally through `.env`

## 7. What not to over-focus on

Do not start by memorizing every provider SDK method.

Provider SDKs can change over time. The stable beginner skill is understanding the integration pattern:

```text
prompt -> wrapper -> selected client -> provider/mock -> response -> parsed answer
```

Do not hardcode real API keys.

Do not build the final POC so that it breaks when no paid API key exists.

## 8. How this helps in AI Engineer JRSS / Mettl / POC / interview

This module prepares the learner to:

- explain hosted model integration
- build a mock-first final POC
- connect FastAPI endpoints to an LLM client
- use RAG context as prompt input
- call the same wrapper from LangGraph nodes
- discuss API key safety and productionization
- answer interview questions about OpenAI/Gemini integration without sounding like they only copied SDK code
