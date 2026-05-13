# 16 Docker Basics

## 1. What This Module Is

This module teaches Docker from beginner level.

Docker packages an application with the files, dependencies, runtime, and startup command it needs so the application can run more consistently across machines.

Simple meaning:

```text
Docker helps reduce "it works on my machine" problems.
```

The core Docker mental model is:

```text
Dockerfile -> image -> container -> running app
```

## 2. The "Works On My Machine" Problem

Beginners often build an app that works locally but fails somewhere else.

Common reasons:

- different Python version
- missing package
- wrong package version
- environment variable missing
- wrong startup command
- port already in use
- operating system differences
- dependency installed globally on one laptop but not another

Example:

```text
Your laptop has FastAPI installed.
Your friend's laptop does not.
Your app works for you but fails for them.
```

Docker reduces this by packaging the app setup into an image. Another machine can run a container from that image instead of manually recreating every setup step.

## 3. Why It Matters For AI Engineers

AI Engineer POCs often include:

- FastAPI backend
- Streamlit UI
- RAG packages
- vector database client
- LLM provider configuration
- environment variables
- model server connection

Without Docker, every machine must recreate the setup manually. With Docker, the application can be packaged with a clear recipe.

Docker does not remove all deployment work, but it makes the application more repeatable.

## 4. What You Should Finish Knowing

After this module, you should understand:

- Docker
- image
- container
- Dockerfile
- build
- run
- port mapping
- environment variables
- volumes
- Docker Compose
- Podman awareness
- container logs
- containerizing FastAPI
- common Docker errors

You should also be able to explain:

```text
Dockerfile -> image -> container -> running app
```

## 5. Study Order

1. `00-overview.md`
2. `01-dockerfile-run-compose.md`
3. `implementation/fastapi-docker-example/README.md`
4. `exercises.md`
5. `cheatsheet.md`
6. `interview-questions.md`

## 6. File List

- `README.md`: module guide.
- `00-overview.md`: Docker mental model, image vs container, build/run flow, ports, env vars, volumes, logs, and common errors.
- `01-dockerfile-run-compose.md`: Dockerfile syntax, Docker Compose syntax, and line-by-line FastAPI containerization explanation.
- `implementation/fastapi-docker-example/README.md`: runnable FastAPI Docker example instructions.
- `implementation/fastapi-docker-example/main.py`: minimal FastAPI app.
- `implementation/fastapi-docker-example/requirements.txt`: Python dependencies.
- `implementation/fastapi-docker-example/Dockerfile`: image recipe.
- `implementation/fastapi-docker-example/docker-compose.yml`: Compose service definition.
- `exercises.md`: Docker practice tasks with expected commands, outputs, hints, self-checks, solution outlines, and common mistakes.
- `cheatsheet.md`: practical command reference.
- `interview-questions.md`: Docker interview Q&A.

## 7. Practical Scope

This module focuses on local Docker usage for a FastAPI-style app.

It prepares you for Kubernetes, because Kubernetes usually runs container images. First understand Docker packaging locally. Then Kubernetes will make more sense.

## 8. What Docker Gives Automatically

Docker gives:

- image build process
- isolated container runtime
- container logs
- basic networking and port publishing
- environment variable injection
- volume mounting
- Compose service startup

## 9. What You Still Create Manually

You still write:

- application code
- `requirements.txt`
- `Dockerfile`
- startup command
- port mapping
- environment variables
- `docker-compose.yml` if using Compose

Docker packages and runs your app. It does not design the app for you.

## 10. How This Helps In JRSS, Mettl, POC, And Interviews

- JRSS labs: containerized apps are easier to run consistently.
- Mettl: Docker questions often test image vs container, Dockerfile, build vs run, port mapping, and Podman awareness.
- POC: Docker shows deployment readiness for the FastAPI backend.
- Interview: you can explain how you package a FastAPI/RAG app for repeatable execution.
