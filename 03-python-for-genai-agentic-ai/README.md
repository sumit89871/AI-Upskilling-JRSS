# 03 Python For GenAI And Agentic AI

## 1. What This Module Is

This module teaches Python patterns that appear repeatedly in GenAI, RAG, tool-calling, MCP, LangGraph, and agentic AI projects.

It assumes you know basic Python syntax from module 02.

## 2. Why It Matters

GenAI code is usually not magic. It is Python code that:

- builds prompts
- sends JSON to a model or API
- receives JSON-like responses
- extracts useful fields
- retries failed calls
- logs what happened
- tracks state across steps
- exposes Python functions as tools

## 3. What The Learner Should Finish Knowing

You should be able to:

- work with nested dictionaries and lists
- parse model-like responses
- design structured output
- use environment variables
- create a simple API client pattern
- understand retry logic
- use basic logging
- understand `async` and `await`
- understand streaming response basics
- create prompt templates
- explain tool/function calling
- build a simple agent loop
- use a state dictionary

## 4. Study Order

1. [00-overview.md](./00-overview.md)
2. [01-json-structured-output-state.md](./01-json-structured-output-state.md)
3. [02-api-client-env-retries-logging.md](./02-api-client-env-retries-logging.md)
4. [03-async-streaming-prompts-tools-agent-loop.md](./03-async-streaming-prompts-tools-agent-loop.md)
5. [exercises.md](./exercises.md)
6. [cheatsheet.md](./cheatsheet.md)
7. [interview-questions.md](./interview-questions.md)

## 5. File List

- `README.md`: module guide
- `00-overview.md`: GenAI Python mental model
- `01-json-structured-output-state.md`: nested data, structured output, state
- `02-api-client-env-retries-logging.md`: API clients, env vars, retries, logging
- `03-async-streaming-prompts-tools-agent-loop.md`: async, streaming, tools, agent loop
- `exercises.md`: hands-on tasks
- `cheatsheet.md`: revision commands and patterns
- `interview-questions.md`: Q&A for screening and interviews
- `implementation/mock_llm_client.py`: runnable mock LLM client
- `implementation/simple_agent_loop.py`: runnable simple agent loop
- `mini-project/README.md`: mini project guide

## 6. Practical Scope

This module uses mock LLM behavior first. That means examples run without paid API keys.

Real OpenAI, Gemini, and Ollama integration comes later.

## 7. What Not To Over-Focus On

Do not over-focus on agent frameworks yet.

First understand:

- data shape
- state
- tool function
- loop
- stop condition
- error handling

Frameworks are easier after these ideas are clear.

## 8. How This Helps In AI Engineer JRS / Mettl / POC / Interview

- **JRS labs**: you can understand GenAI Python examples.
- **Mettl**: you can answer JSON, function, error handling, and API pattern questions.
- **POC**: you can build mock-first AI demos.
- **Interview**: you can explain what agents, tools, and state mean without vague language.

