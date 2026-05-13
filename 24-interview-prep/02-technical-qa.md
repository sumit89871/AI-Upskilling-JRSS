# Technical Interview Q&A

## Python Q&A

### Question: What is the difference between `print` and `return`?

Short answer:

`print` displays output. `return` sends a value back to the caller.

Expanded explanation:

`print()` is useful for showing something in the terminal. `return` is used inside a function when another part of the code needs the result.

Real project example:

In a helper function that builds a prompt, I return the prompt string so the FastAPI endpoint or LangGraph node can use it.

Common wrong answer:

"They both do the same thing."

When to say this in interview:

Use when asked Python basics or debugging function behavior.

### Question: What is a dictionary and where did you use it?

Short answer:

A dictionary stores key-value pairs.

Expanded explanation:

Dictionaries are useful for JSON-like data, API responses, model outputs, and agent state.

Real project example:

LangGraph-style state can be represented as `{"query": "...", "context": [], "answer": None}`.

Common wrong answer:

"Dictionary is only for words and meanings."

When to say this in interview:

Use when asked about Python data structures or JSON handling.

### Question: Why use exceptions?

Short answer:

Exceptions handle errors without crashing the app unexpectedly.

Expanded explanation:

Instead of letting a failure stop the program, code can catch specific errors and return a useful response or retry safely.

Real project example:

When parsing LLM JSON output, I would catch parsing or validation errors and return a clear failure message.

Common wrong answer:

"Use `except` for every error and ignore it."

When to say this in interview:

Use when asked about robust Python code.

## REST API Q&A

### Question: What is a REST API?

Short answer:

A REST API lets clients communicate with a server using HTTP methods and resources.

Expanded explanation:

Clients send requests to endpoints. The server processes the request and returns a response, often JSON.

Real project example:

The POC can expose `/health`, `/ask-context`, and `/generate-test-cases` endpoints.

Common wrong answer:

"REST API is only a URL."

When to say this in interview:

Use when asked backend fundamentals.

### Question: GET vs POST?

Short answer:

GET usually reads data. POST usually submits data.

Expanded explanation:

GET is used for retrieval. POST is used when the client sends a body, such as a prompt or requirement, for the server to process.

Real project example:

`GET /health` checks service status. `POST /generate-test-cases` sends a requirement and receives generated tests.

Common wrong answer:

"GET and POST are the same."

When to say this in interview:

Use when explaining API design decisions.

### Question: Path parameter vs query parameter?

Short answer:

A path parameter is part of the route. A query parameter comes after `?`.

Expanded explanation:

Path parameters identify a resource, such as `/users/10`. Query parameters filter or modify a request, such as `/search?q=rag`.

Real project example:

`/documents/{doc_id}` can identify a document. `/search?query=login` can search documents.

Common wrong answer:

"Both are request bodies."

When to say this in interview:

Use when asked REST API details.

## FastAPI Q&A

### Question: What is FastAPI?

Short answer:

FastAPI is a Python framework for building APIs.

Expanded explanation:

It supports route decorators, automatic docs, request validation with Pydantic, async endpoints, and JSON responses.

Real project example:

I use FastAPI to expose AI assistant endpoints for asking questions and generating test cases.

Common wrong answer:

"FastAPI is the web server."

When to say this in interview:

Use when discussing backend implementation. Uvicorn is commonly the server that runs the FastAPI app.

### Question: What does `@app.get("/health")` do?

Short answer:

It registers a GET endpoint at `/health`.

Expanded explanation:

The decorator tells FastAPI to call the function below it when a GET request comes to `/health`.

Real project example:

The POC uses a health endpoint to verify the backend is running.

Common wrong answer:

"It starts the server."

When to say this in interview:

Use when asked to explain FastAPI syntax.

### Question: Why use Pydantic with FastAPI?

Short answer:

Pydantic validates request and response data.

Expanded explanation:

FastAPI uses Pydantic models to check JSON fields and types before endpoint logic runs.

Real project example:

`GenerateTestCaseRequest` can require a `requirement` string before the LLM workflow starts.

Common wrong answer:

"Pydantic is only for documentation."

When to say this in interview:

Use when asked about input validation.

## Git Q&A

### Question: What is Git?

Short answer:

Git is a version control system that tracks changes in files.

Expanded explanation:

It lets developers save snapshots, compare versions, work on branches, and collaborate safely.

Real project example:

I would commit changes after adding a FastAPI endpoint or Dockerfile.

Common wrong answer:

"Git and GitHub are the same."

When to say this in interview:

Use when asked about team workflow.

### Question: `git add` vs `git commit`?

Short answer:

`git add` stages changes. `git commit` saves staged changes into history.

Expanded explanation:

Staging is preparation. Commit is the saved snapshot.

Real project example:

After editing `main.py`, run `git add main.py`, then `git commit -m "Add health endpoint"`.

Common wrong answer:

"git add saves the final version."

When to say this in interview:

Use for command behavior questions.

## Docker Q&A

### Question: Image vs container?

Short answer:

An image is the packaged template. A container is a running instance of that image.

Expanded explanation:

Dockerfile builds an image. Docker run starts a container from the image.

Real project example:

The POC FastAPI app can be packaged into an image and run as a container.

Common wrong answer:

"Image and container are the same."

When to say this in interview:

Use when asked deployment basics.

### Question: Why Docker for AI apps?

Short answer:

Docker makes app runtime consistent across machines.

Expanded explanation:

It packages code, dependencies, and runtime setup so the FastAPI app can run similarly on a laptop, server, or deployment environment.

Real project example:

The POC can run FastAPI in a container with environment variables for provider mode.

Common wrong answer:

"Docker is only for databases."

When to say this in interview:

Use when discussing deployment.

## Kubernetes Q&A

### Question: Pod vs deployment?

Short answer:

A pod runs containers. A deployment manages pods and replicas.

Expanded explanation:

Kubernetes schedules pods. Deployments ensure the desired number of pods are running and support rolling updates.

Real project example:

A FastAPI container can run inside a pod managed by a deployment.

Common wrong answer:

"Deployment and pod are identical."

When to say this in interview:

Use when asked Kubernetes basics.

### Question: Service vs deployment?

Short answer:

A deployment manages pods. A service provides stable network access to pods.

Expanded explanation:

Pods can change IPs. A service gives a stable endpoint to reach them.

Real project example:

The POC backend deployment runs pods, and a service exposes the backend inside minikube.

Common wrong answer:

"Service creates Docker images."

When to say this in interview:

Use when explaining Kubernetes access.

## LLM Q&A

### Question: What is an LLM?

Short answer:

An LLM is a model that takes text input and generates text output.

Expanded explanation:

It processes tokens and predicts likely next tokens based on the prompt and context.

Real project example:

The POC uses an LLM or mock LLM to generate test cases from requirements.

Common wrong answer:

"An LLM is the full app."

When to say this in interview:

Use when asked GenAI fundamentals.

### Question: What is hallucination?

Short answer:

Hallucination is confident but unsupported or wrong model output.

Expanded explanation:

It can happen when the model lacks reliable context or guesses facts.

Real project example:

If the model invents a login lockout rule not present in the requirement notes, that is hallucination.

Common wrong answer:

"Hallucination is only spelling mistake."

When to say this in interview:

Use when discussing risk and grounding.

## Prompt Engineering Q&A

### Question: What is prompt engineering?

Short answer:

Prompt engineering is designing clear instructions so the model returns useful controlled output.

Expanded explanation:

Good prompts include instruction, context, constraints, examples, and output format.

Real project example:

The POC uses a prompt that asks for test cases in a fixed JSON schema.

Common wrong answer:

"Prompt engineering is just asking questions."

When to say this in interview:

Use when asked how you control LLM output.

## RAG Q&A

### Question: What is RAG?

Short answer:

RAG retrieves relevant context before generating an answer.

Expanded explanation:

The app searches documents, adds relevant chunks to the prompt, and asks the model to answer using that context.

Real project example:

The POC answers questions from local requirement notes using a RAG-style flow.

Common wrong answer:

"RAG trains the model permanently."

When to say this in interview:

Use when asked about grounding or private knowledge.

## MCP Q&A

### Question: What is MCP?

Short answer:

MCP is a protocol for connecting AI clients to tools, resources, and prompts.

Expanded explanation:

An MCP server exposes capabilities. An MCP client discovers and calls them.

Real project example:

The POC can expose a test data helper as an MCP-style tool.

Common wrong answer:

"MCP is the model."

When to say this in interview:

Use when asked about agent tool integration.

## LangGraph Q&A

### Question: What is LangGraph?

Short answer:

LangGraph helps build controlled stateful AI workflows.

Expanded explanation:

It uses state, nodes, edges, conditional routing, and checkpointing to manage multi-step workflows.

Real project example:

The POC workflow can run understand query, retrieve context, generate answer, review, and final response as graph steps.

Common wrong answer:

"LangGraph is just multiple prompts."

When to say this in interview:

Use when explaining workflow orchestration.

## Agentic AI Q&A

### Question: What is an AI agent?

Short answer:

An AI agent is a workflow that can use model reasoning, state, tools, and decisions to complete a task.

Expanded explanation:

Unlike a simple LLM call, an agent may decide whether to call a tool, retrieve context, ask for clarification, or route to another step.

Real project example:

A QA assistant agent may retrieve context, call a test data tool, generate test cases, and review the output.

Common wrong answer:

"Every chatbot is an agent."

When to say this in interview:

Use when asked about agentic AI or multi-agent systems.

### Question: What is A2A?

Short answer:

A2A means agent-to-agent communication.

Expanded explanation:

In a multi-agent system, one agent may ask another agent for help, hand off a specialized task, or receive a structured result from another agent. A2A should be controlled and logged in enterprise systems because uncontrolled agent communication can become hard to debug.

Real project example:

In a larger version of the QA assistant POC, a Requirement Analyst Agent could ask an API Test Agent for API test ideas, then pass the result to a Reviewer Agent.

Common wrong answer:

"A2A is the same as MCP."

When to say this in interview:

Use when the interviewer asks about multi-agent systems, agent collaboration, or PPT-specific agentic AI terms.

### Question: What is the difference between MCP and A2A?

Short answer:

MCP connects AI clients to tools/resources/prompts. A2A is communication between agents.

Expanded explanation:

An agent may use MCP to call a test data tool. The same agent may use A2A to ask another specialist agent to review generated test cases. MCP is tool integration. A2A is agent collaboration.

Real project example:

The POC uses MCP-style tools for controlled test data lookup. A future multi-agent version could add A2A between analyst, generator, and reviewer agents.

Common wrong answer:

"Both are just APIs."

When to say this in interview:

Use when asked to compare terms from agentic AI architecture.

## Podman Q&A

### Question: What is Podman?

Short answer:

Podman is a container tool that can build and run containers with command patterns similar to Docker.

Expanded explanation:

Docker and Podman share key beginner concepts: image, container, build, run, port mapping, environment variables, and logs. Podman is often discussed in Linux or enterprise environments. If you practiced Docker, explain that Podman knowledge transfers at the concept level, while exact operational details depend on the environment.

Real project example:

A FastAPI POC with a Dockerfile could be built with `podman build -t qa-assistant .` and run with `podman run -p 8000:8000 qa-assistant` in a Podman-based setup.

Common wrong answer:

"Podman is the same as Kubernetes."

When to say this in interview:

Use when deployment tools from the reskilling plan are mentioned.

## IBM Ecosystem Awareness Q&A

### Question: What is IBM BOB?

Short answer:

IBM BOB is mentioned in the reskilling material as an IBM ecosystem item. Exact details should be validated from official IBM resources.

Expanded explanation:

Do not invent internal functionality if you have not been given official documentation or tool access. A safe answer is to acknowledge the term, explain that it belongs to the IBM enablement/platform context, and connect your readiness to the broader engineering skills: integration, governance, RAG, tools, APIs, and POC delivery.

Real project example:

My course POC does not claim IBM BOB integration. It demonstrates transferable AI Engineer skills: FastAPI integration, Pydantic validation, RAG-style grounding, MCP-style tool usage, LangGraph-style workflow, Docker awareness, and demo explanation.

Common wrong answer:

"IBM BOB definitely has these features..." without official source.

When to say this in interview:

Use if asked about internal IBM ecosystem terms from the PPT.

### Question: What is Agent Studio or Agentic Studio?

Short answer:

It is enterprise agent tooling awareness for building or configuring agentic AI workflows.

Expanded explanation:

At beginner/interview level, connect it to concepts you understand: agent workflows, tools, prompts, state, governance, and deployment. Avoid claiming exact internal product details unless you have used official resources.

Real project example:

My POC simulates the core engineering ideas with FastAPI, RAG, MCP-style tools, LangGraph-style stateful flow, and Streamlit UI.

Common wrong answer:

"Agent Studio means only prompt writing."

When to say this in interview:

Use when asked how enterprise tools relate to your local POC.

### Question: How should you discuss IBM credentials or badges?

Short answer:

Claim only credentials you completed. If still preparing, say you are preparing.

Expanded explanation:

Credential awareness means you understand the expected learning path and topics. It does not mean you should overclaim completion. You can say you are preparing for watsonx, GenAI, Agentic AI, hyperscaler AI, or ISV AI expectations and can demonstrate the underlying technical skills.

Real project example:

I can say: "I am preparing through this AI Engineer course and POC. The project demonstrates APIs, RAG, tool usage, agents, deployment awareness, and enterprise constraints."

Common wrong answer:

"I am certified" without having completed the badge or credential.

When to say this in interview:

Use if the interviewer asks about badges, credentials, or certification status.
