# Beginner Glossary

## API

Simple meaning:

An API is a way for one software system to communicate with another software system.

Example:

Your Streamlit UI sends a request to a FastAPI backend.

Where used:

REST APIs, FastAPI, OpenAI/Gemini API calls, final POC endpoints.

## REST

Simple meaning:

REST is a common style for designing web APIs using HTTP methods and resources.

Example:

`GET /health` checks whether an API is running.

Where used:

REST API fundamentals, FastAPI, POC backend.

## Endpoint

Simple meaning:

An endpoint is a specific API path that a client can call.

Example:

`/generate-test-cases` can be an endpoint that accepts a requirement and returns test cases.

Where used:

FastAPI routes, REST APIs, final POC.

## JSON

Simple meaning:

JSON is a text format for structured data using key-value pairs and lists.

Example:

```json
{"question": "What is RAG?"}
```

Where used:

API request bodies, model responses, Pydantic validation, structured GenAI output.

## Schema

Simple meaning:

A schema describes the expected shape of data.

Example:

`question` must be a string and `sources` must be a list.

Where used:

Pydantic, FastAPI, MCP tool input/output, JSON output prompts.

## Validation

Simple meaning:

Validation checks whether data matches expected rules before the app uses it.

Example:

Pydantic rejects a request missing the required `question` field.

Where used:

Pydantic, FastAPI, structured LLM output, final POC.

## Model

Simple meaning:

In AI, a model is the system that processes input and produces output.

Example:

An LLM generates test cases from a prompt.

Where used:

LLM fundamentals, OpenAI/Gemini, Ollama, Hugging Face.

## LLM

Simple meaning:

An LLM is a large language model that takes text input and generates text output.

Example:

Prompt: `Summarize this requirement.`

Where used:

Prompt engineering, GenAI API calls, RAG, agents.

## Token

Simple meaning:

A token is a small text unit processed by a language model.

Example:

A word may be one token or split into multiple tokens.

Where used:

LLM context window, model cost, max tokens, prompt design.

## Embedding

Simple meaning:

An embedding is a list of numbers representing text meaning.

Example:

`"password reset"` becomes a vector such as `[0.12, -0.44, ...]`.

Where used:

RAG, vector databases, similarity search.

## Vector

Simple meaning:

A vector is a list of numbers.

Example:

An embedding vector stores meaning numerically.

Where used:

Embeddings, vector databases, ChromaDB, FAISS.

## RAG

Simple meaning:

RAG retrieves relevant context before asking the model to answer.

Example:

Question -> retrieve requirement chunks -> prompt model with context -> answer.

Where used:

RAG module, final POC knowledge assistant.

## Retriever

Simple meaning:

A retriever finds relevant documents or chunks for a question.

Example:

Retriever finds login requirement notes for a login question.

Where used:

LangChain, vector databases, RAG pipelines.

## MCP

Simple meaning:

MCP is a protocol that lets AI clients discover and use tools, resources, and prompts.

Example:

An AI agent calls a test data helper tool through MCP.

Where used:

FastMCP, agents, enterprise tool integration.

## Tool

Simple meaning:

A tool is an action an AI system can call through controlled code.

Example:

`get_test_user("admin")` returns demo test data.

Where used:

MCP, agents, LangGraph workflows.

## Agent

Simple meaning:

An agent is an AI workflow that can use state, tools, and decisions to complete a task.

Example:

A QA agent retrieves context, generates tests, reviews output, and returns a final answer.

Where used:

Agentic AI, MCP, LangGraph, final POC.

## State

Simple meaning:

State is shared workflow data carried between steps.

Example:

`{"query": "...", "context": [], "answer": None}`

Where used:

LangGraph, agent workflows, final POC.

## Node

Simple meaning:

A node is one workflow step in a graph.

Example:

`retrieve_context` can be a node.

Where used:

LangGraph workflows.

## Edge

Simple meaning:

An edge connects one workflow step to the next.

Example:

`retrieve_context -> generate_answer`

Where used:

LangGraph graph design.

## Checkpoint

Simple meaning:

A checkpoint is saved workflow progress.

Example:

Save state after retrieving context so generation can retry later.

Where used:

LangGraph, long-running workflows, human approval flows.

## Container

Simple meaning:

A container is a running instance of a packaged application image.

Example:

A FastAPI backend runs inside a Docker container.

Where used:

Docker, Kubernetes deployment.

## Image

Simple meaning:

An image is a packaged template used to create containers.

Example:

Build a FastAPI Docker image, then run a container from it.

Where used:

Docker basics, deployment.

## Pod

Simple meaning:

A pod is the smallest deployable unit in Kubernetes and usually runs one or more containers.

Example:

A FastAPI container runs inside a pod.

Where used:

Kubernetes basics.

## Deployment

Simple meaning:

A Kubernetes Deployment manages pod replicas and updates.

Example:

Deployment keeps two FastAPI pods running.

Where used:

Kubernetes deployment files.

## Service

Simple meaning:

A Kubernetes Service gives stable network access to pods.

Example:

Service exposes the FastAPI backend inside minikube.

Where used:

Kubernetes networking.
