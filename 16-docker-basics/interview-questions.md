# Docker Interview Questions

## 1. What is Docker?

Short answer:

Docker packages and runs applications in containers.

Expanded answer:

Docker helps reduce environment mismatch by packaging code, dependencies, runtime setup, and startup commands into an image. A container runs from that image.

Project example:

In the AI QA Assistant POC, Docker can package the FastAPI backend so it runs consistently on another machine.

Common wrong answer:

Docker is just a virtual machine. Containers are lighter than traditional VMs and share the host OS kernel.

## 2. What problem does Docker solve?

Short answer:

It reduces "works on my machine" problems.

Expanded answer:

Apps often fail on another machine because Python version, packages, environment variables, or startup commands differ. Docker captures those assumptions in an image.

Project example:

A FastAPI app that needs `fastapi` and `uvicorn` can be packaged so another user does not manually install them one by one.

Common wrong answer:

Docker fixes all bugs. Docker improves environment consistency; it does not fix bad application logic.

## 3. Image vs container?

Short answer:

Image is the packaged blueprint. Container is the running instance.

Expanded answer:

You build an image from a Dockerfile. You run a container from an image. One image can create many containers.

Project example:

`docker build -t fastapi-docker-example .` creates the image. `docker run -p 8000:8000 fastapi-docker-example` starts a container.

Common wrong answer:

Image and container are the same thing.

## 4. What is a Dockerfile?

Short answer:

A Dockerfile is a recipe for building a Docker image.

Expanded answer:

It defines the base image, working directory, copied files, dependency installation, and startup command.

Project example:

The FastAPI Dockerfile starts from `python:3.11-slim`, installs `requirements.txt`, copies the app, and runs Uvicorn.

Common wrong answer:

A Dockerfile is the running app. It is only the build recipe.

## 5. What is `docker build`?

Short answer:

`docker build` creates an image.

Expanded answer:

Docker reads the Dockerfile and build context, executes build steps, and produces a tagged image.

Project example:

```powershell
docker build -t fastapi-docker-example .
```

Common wrong answer:

`docker build` starts the app. It creates the image; `docker run` starts the container.

## 6. What is `docker run`?

Short answer:

`docker run` starts a container from an image.

Expanded answer:

It creates a container, starts the image's default command, and can pass runtime options such as ports and environment variables.

Project example:

```powershell
docker run -p 8000:8000 fastapi-docker-example
```

Common wrong answer:

`docker run` rebuilds the image every time.

## 7. What is port mapping?

Short answer:

Port mapping connects a port on your machine to a port inside the container.

Expanded answer:

Containers have their own network environment. `-p 8000:8000` forwards traffic from host port `8000` to container port `8000`.

Project example:

The browser opens `http://127.0.0.1:8000/health`, and Docker forwards the request to FastAPI inside the container.

Common wrong answer:

The two ports always have to be the same. They can differ, such as `8001:8000`.

## 8. Why does FastAPI in Docker use `--host 0.0.0.0`?

Short answer:

So the app listens for traffic from outside the container.

Expanded answer:

If Uvicorn listens only on `127.0.0.1` inside the container, port mapping may not expose it properly to the host machine. `0.0.0.0` listens on all interfaces inside the container.

Project example:

```dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Common wrong answer:

`0.0.0.0` is the browser URL. You still open `http://127.0.0.1:8000` from your machine.

## 9. What are environment variables in Docker?

Short answer:

They are runtime configuration values passed into a container.

Expanded answer:

Environment variables let you configure behavior without changing source code or rebuilding images.

Project example:

```powershell
docker run -e APP_ENV=local fastapi-docker-example
```

Common wrong answer:

Environment variables should be hardcoded in the Dockerfile, including secrets.

## 10. What is a Docker volume?

Short answer:

A volume shares or persists files outside the container lifecycle.

Expanded answer:

Containers can be removed. Volumes help keep data or mount host folders into containers.

Project example:

A RAG app may mount a local documents folder into a container for development.

Common wrong answer:

All files created inside a container automatically persist forever.

## 11. Dockerfile vs docker-compose.yml?

Short answer:

Dockerfile builds an image. Compose defines how to run one or more services.

Expanded answer:

Compose can build from a Dockerfile and set ports, environment variables, volumes, and multi-service relationships.

Project example:

The FastAPI example uses a Dockerfile to package the app and `docker-compose.yml` to run the `app` service on port `8000`.

Common wrong answer:

Compose replaces Dockerfile. Compose often uses the Dockerfile.

## 12. Scenario: Container starts but browser cannot access app. What do you check?

Short answer:

Check port mapping, app host binding, container status, and logs.

Expanded answer:

The app may be listening on the wrong host or port, host port may be busy, the container may have exited, or the app may have crashed.

Project example:

Check:

```powershell
docker ps
docker logs <container_id>
```

Common wrong answer:

Assume Docker is broken without checking logs.

## Question: What is Podman and how is it related to Docker?

Short answer:

Podman is a container tool that can build and run containers with command patterns similar to Docker.

Expanded answer:

Docker and Podman both use core container concepts: image, container, build, run, port mapping, environment variables, and logs. Docker is very common for local development. Podman is also used in some Linux and enterprise environments, often because of rootless container support and daemonless operation. For beginner AI Engineer readiness, the key is to understand the shared container model.

Project example:

If the FastAPI POC has a Dockerfile, a Podman-based environment may build it with `podman build -t qa-assistant .` and run it with `podman run -p 8000:8000 qa-assistant`.

Common wrong answer:

"Podman is Kubernetes."

Why wrong:

Podman runs containers. Kubernetes orchestrates containers across pods, deployments, and services.

When to say this in interview:

Use this if the interviewer asks about deployment tools from the reskilling PPT or asks how Docker knowledge transfers to Podman.
