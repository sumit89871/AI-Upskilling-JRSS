# Course Roadmap

This roadmap gives the safest order for a beginner. Each phase builds the vocabulary and implementation skill needed for the next phase.

## Phase 1: Setup and Python Foundation

### 1. Environment Setup

Learn how to install tools, open a terminal, create a virtual environment, install packages, store API keys safely, and run Python files.

Why first: if your setup is broken, every later topic becomes frustrating.

### 2. Python Beginner to Advanced

Learn Python syntax, data types, functions, files, exceptions, classes, JSON, requests, type hints, dataclasses, and pytest basics.

Why second: FastAPI, LangChain, MCP, LangGraph, and agents are all Python projects.

### 3. Python for GenAI/Agentic AI

Learn JSON-heavy Python, nested data, structured responses, retry logic, logging, environment variables, async basics, prompt templates, tool calling concepts, and simple agent loops.

Why third: GenAI code is mostly Python code that sends, receives, validates, and routes structured data.

## Phase 2: API and Backend Foundation

### 4. Git

Learn `init`, `status`, `add`, `commit`, `branch`, `switch`, `clone`, `pull`, `push`, and conflict basics.

Why here: every lab and POC should be version-controlled.

### 5. REST API Fundamentals

Learn client/server, endpoints, URLs, methods, headers, request body, response body, JSON, status codes, authentication, bearer tokens, and curl.

Why here: LLM APIs, FastAPI apps, MCP clients, and deployment health checks use API concepts.

### 6. FastAPI

Learn how to create Python APIs with route decorators, Pydantic models, request bodies, path/query parameters, headers, errors, Swagger UI, and testing.

Why here: AI Engineers often expose AI functionality as APIs.

### 7. Pydantic

Learn validation, schemas, nested models, optional fields, defaults, `model_dump`, `model_validate`, structured GenAI output, FastAPI integration, and agent state models.

Why here: AI systems fail when data shape is unclear.

## Phase 3: GenAI Foundation

### 8. LLM Fundamentals

Learn models, prompts, completions, tokens, context windows, embeddings, attention, transformers, hallucination, grounding, RAG, inference, local models, hosted models, open models, and closed models.

Why here: implementation becomes easier when you know what the model can and cannot do.

### 9. Prompt Engineering

Learn instruction prompts, zero-shot, one-shot, few-shot, structured prompting, JSON prompting, RAG templates, agent system prompts, evaluation prompts, and common prompt mistakes.

Why here: prompts are part of application design, not decoration.

### 10. OpenAI/Gemini APIs

Learn API keys, environment variables, SDK installation, request structure, messages, response parsing, error handling, rate limits, retries, Gemini basics, OpenAI basics, wrappers, and mock fallback.

Why here: most POCs need optional real LLM integration.

## Phase 4: RAG and Agentic Systems

### 11. RAG with LangChain and Vector DB

Learn documents, chunking, metadata, embeddings, vector databases, ChromaDB, retrievers, generators, reranking basics, LangChain basics, and RAG evaluation.

Why here: enterprise AI often needs answers grounded in private documents.

### 12. MCP and FastMCP

Learn MCP servers, clients, tools, resources, prompts, FastMCP decorators, tool schemas, and manual testing.

Why here: MCP is a practical way to expose tools and context to AI systems.

### 13. LangGraph

Learn graph, node, edge, state, reducer, checkpointing, conditional edges, retry nodes, human approval nodes, and supervisor workflow basics.

Why here: many agent workflows need controlled state, not a single prompt call.

### 14. Agents and Multi-Agent Systems

Learn LLM vs agent, tool-using agents, planner/executor/reviewer patterns, supervisor agents, handoffs, memory, AutoGen awareness, CrewAI awareness, PydanticAI awareness, and when not to use agents.

Why here: agents are useful only when a workflow needs planning, tools, memory, or review.

## Phase 5: Deployment and Labs

### 15. Ollama/Hugging Face/Local Models

Learn local models, Ollama pull/run, calling Ollama from Python, Hugging Face Hub, tokenizers, pipelines, vLLM awareness, Docker awareness, and hardware limits.

### 16. Docker

Learn images, containers, Dockerfiles, build, run, ports, environment variables, volumes, Compose, FastAPI containerization, RAG containerization, and common errors.

### 17. Kubernetes

Learn clusters, nodes, pods, deployments, services, configmaps, secrets, namespaces, minikube, kubectl, YAML, logs, scaling, and cleanup.

### 18. Streamlit

Learn simple demo UI creation, text input, buttons, output display, FastAPI backend calls, and GenAI demo flow.

### 19. Langflow

Learn visual flow builder concepts, nodes, edges, prompt nodes, LLM nodes, retrievers, RAG flows, and limitations.

### 20. MCP Context Forge

Learn the concept of MCP tool/context registries, local model plus MCP tools, lab architecture, limitations, and troubleshooting.

## Phase 6: Enterprise and Final Prep

### 21. IBM AI Engineer Awareness

Learn AI Engineer role expectations, watsonx awareness, ICA awareness, Agent Studio awareness, MCP in enterprise AI, SME-led sessions, POC demos, security, auditability, explainability, logging, and API governance.

### 22. Final POC Project

Build the AI QA Knowledge Assistant + Test Case Generator with FastAPI, Pydantic, RAG, optional LLM APIs, FastMCP, LangGraph, Docker, Kubernetes, Streamlit, and Git-ready structure.

### 23. Mettl Prep

Practice Python MCQs, output questions, coding tasks, API/FastAPI, Git, Docker, Kubernetes, LLM, prompting, RAG, MCP, and LangGraph screening questions.

### 24. Interview Prep

Prepare concise explanations for role fit, project discussion, POC architecture, challenges, productionization, security, monitoring, and stand-and-deliver demo.

## How To Pace Yourself

If you have limited time:

- Day 1-3: setup, Python basics, Git
- Day 4-6: REST, FastAPI, Pydantic
- Day 7-9: LLMs, prompts, API integration
- Day 10-14: RAG, MCP, LangGraph
- Day 15-18: Docker, Kubernetes, Streamlit
- Day 19-21: final POC, Mettl revision, interview scripts

Do not skip hands-on practice. Interview confidence comes from having run code and fixed errors.

