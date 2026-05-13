# Final Rapid Revision

Use this file in the last 60 to 90 minutes before a screening.

## Python

Remember:

- `=` assigns a value.
- `==` compares values.
- Lists are mutable.
- Dictionaries use key access such as `data["key"]`.
- Missing dictionary key with bracket access raises `KeyError`.
- A function without `return` returns `None`.
- `print()` displays output; `return` sends a value back to caller.

Common traps:

- list index starts at `0`
- `append()` changes the list
- type hints do not guarantee runtime validation
- dictionary dot access usually does not work

## REST API and FastAPI

Remember:

- API means software communication interface.
- GET usually reads data.
- POST usually submits data.
- Path parameter is part of URL path: `/users/{id}`.
- Query parameter comes after `?`: `/search?q=rag`.
- Request body is usually JSON sent with POST/PUT/PATCH.
- FastAPI uses Pydantic for request validation.
- `422` often means validation failed.
- `@app.get("/health")` registers a GET route.

Common traps:

- endpoint function may not run if request validation fails
- Uvicorn runs the FastAPI app; FastAPI defines the app
- Swagger UI is docs/testing UI, not the backend itself

## Git

Remember:

- Git is local version control.
- GitHub is remote hosting/collaboration platform.
- `git status` shows current worktree state.
- `git add .` stages changes.
- `git commit -m "message"` saves staged changes locally.
- `git push` uploads commits to remote.
- Commit is not the same as push.

Common traps:

- forgetting to stage before commit
- committing `.env` or `.venv`
- thinking `git add` saves history

## Docker

Remember:

- Dockerfile is the recipe.
- Image is the packaged template.
- Container is a running instance of an image.
- Port mapping `8000:8000` means host port to container port.
- Environment variables pass config into containers.
- Volumes persist or share files.

Common traps:

- image vs container confusion
- app runs in container but port is not mapped
- expecting container changes to persist without volume

## Podman

Remember:

- Podman is a container tool similar in command shape to Docker.
- Common awareness commands are `podman build -t app-name .` and `podman run -p 8000:8000 app-name`.
- Enterprises may use Podman in Linux/container environments.
- For beginner interviews, connect Podman to shared container concepts: image, container, build, run, port mapping, logs.

Common traps:

- saying Podman is Kubernetes
- claiming deep Podman experience if you only practiced Docker
- forgetting that `8000:8000` means host port to container port

## Kubernetes

Remember:

- Cluster contains nodes.
- Node runs workloads.
- Pod is smallest deployable unit.
- Deployment manages replicas and rollout of pods.
- Service gives stable access to pods.
- ConfigMap stores non-sensitive config.
- Secret stores sensitive config.
- `kubectl logs` checks logs.
- `kubectl get pods` checks pod status.

Common traps:

- pod vs deployment
- service vs deployment
- ConfigMap vs Secret
- YAML indentation errors

## LLM and Prompt Engineering

Remember:

- Prompt is input.
- Response/completion is output.
- Token is model text unit, not always a word.
- Context window is model working space for one request.
- Temperature controls randomness.
- Low temperature is safer for JSON and classification.
- Hallucination is confident unsupported output.
- Grounding means answer based on trusted context.

Prompt structure:

```text
Instruction + context + constraints + examples + output format
```

Common traps:

- trusting fluent output without validation
- asking for JSON but not validating it
- using high temperature for strict output

## RAG

Remember:

```text
Question -> retrieve context -> add context to prompt -> model answers using context
```

Key terms:

- document
- chunk
- embedding
- vector database
- similarity search
- retriever
- generator
- source citation

Common traps:

- RAG does not train the model permanently
- embedding is not final answer
- irrelevant chunks cause weak answers

## MCP

Remember:

```text
Python function -> exposed as MCP tool -> MCP server advertises tool -> client calls tool
```

Key terms:

- MCP server exposes tools/resources/prompts
- MCP client discovers and calls them
- tool performs action
- resource provides readable context
- prompt provides reusable instruction

Common traps:

- MCP is not the model
- tool and resource are not the same

## LangGraph

Remember:

```text
State carries data -> node reads state -> node updates state -> edge routes next node
```

Key terms:

- graph is workflow map
- node is workflow step
- edge connects nodes
- conditional edge branches based on state
- checkpoint saves progress

Common traps:

- node vs Kubernetes node
- state vs local variable
- checkpoint vs final answer

## A2A and Enterprise Agent Awareness

Remember:

- A2A means agent-to-agent communication.
- A2A is not the same as MCP.
- MCP connects AI systems to tools/resources/prompts.
- Supervisor pattern uses a controller to route work between agents.
- Agent Studio / Agentic Studio should be discussed as enterprise agent tooling awareness unless you have official details.
- IBM BOB is a program/PPT-specific IBM ecosystem term; do not invent internal details.
- Claim only credentials or badges you have actually completed.

Safe interview wording:

```text
I understand this as part of the enterprise AI ecosystem from the program material. I would validate exact internal usage from official IBM resources and avoid guessing.
```

## Final screening mindset

If a question asks "what is this used for?", answer with purpose.

If a question shows code, trace it line by line.

If a question compares two terms, define both and state the difference.

If unsure, eliminate options that belong to the wrong domain.
