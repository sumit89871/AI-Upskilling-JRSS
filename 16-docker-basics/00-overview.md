# Docker Overview

## 1. What Docker Is

Docker is a tool for packaging and running applications in containers.

Simple meaning:

```text
Docker packages your app and its setup so it can run more consistently on different machines.
```

For this course, the most important flow is:

```text
Dockerfile -> image -> container -> running app
```

## 2. The "Works On My Machine" Problem

The "works on my machine" problem means the app works on one computer but fails somewhere else.

Example:

```text
Developer laptop: FastAPI app runs.
Demo laptop: ModuleNotFoundError because FastAPI is not installed.
Server: wrong Python version.
Teammate laptop: app starts but port 8000 is already used.
```

The application code may be correct, but the environment is different.

Docker helps by packaging the application with a repeatable setup:

- base operating system layer
- Python runtime
- dependency installation
- copied source code
- startup command
- exposed app port

Docker does not magically fix bad code. It makes the runtime environment more predictable.

## 3. Image vs Container

Image and container are not the same.

```text
Image = packaged app blueprint
Container = running instance of that image
```

An image is built once and can be used many times. A container is what runs when you start the image.

Example:

```text
fastapi-docker-example image -> container 1
fastapi-docker-example image -> container 2
```

Both containers can come from the same image, just like many objects can be created from one class.

Common mistake:

Saying "I am running a Dockerfile." You do not run a Dockerfile directly. You build an image from it, then run a container from the image.

## 4. Dockerfile

A Dockerfile is a recipe for building a Docker image.

Example:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Read it as:

```text
Start from Python -> create /app folder -> copy dependencies file -> install dependencies -> copy code -> define startup command
```

## 5. Build

Build means create an image from a Dockerfile.

Command:

```powershell
docker build -t fastapi-docker-example .
```

Where to run:

Run from the folder that contains the `Dockerfile`.

For this module:

```powershell
cd 16-docker-basics\implementation\fastapi-docker-example
docker build -t fastapi-docker-example .
```

What each part means:

- `docker` runs the Docker command-line tool
- `build` creates a Docker image
- `-t fastapi-docker-example` tags the image with a readable name
- `.` means use the current folder as the build context

Expected output:

```text
Successfully built ...
Successfully tagged fastapi-docker-example:latest
```

Newer Docker versions may show BuildKit output, but the important result is that the image is tagged.

How to verify:

```powershell
docker images
```

Expected result:

You should see `fastapi-docker-example` in the image list.

Common beginner mistake:

Running `docker build` from the wrong folder. If Docker cannot find the Dockerfile or app files, check your current directory.

## 6. Run

Run means start a container from an image.

Command:

```powershell
docker run -p 8000:8000 fastapi-docker-example
```

Where to run:

You can run this from any folder after the image exists.

What each part means:

- `docker` runs the Docker CLI
- `run` starts a container
- `-p 8000:8000` maps a port from your machine to the container
- first `8000` is the host port on your machine
- second `8000` is the container port inside Docker
- `fastapi-docker-example` is the image name

Expected output:

For this FastAPI example:

```text
Uvicorn running on http://0.0.0.0:8000
```

How to verify:

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

Common beginner mistake:

Using `-p 8000:9000` when the app inside the container actually listens on `8000`. The second port must match the app's container port.

## 7. Port Mapping

Containers have their own network space. If the app listens on port `8000` inside the container, your browser still needs a way to reach it from your machine.

Port mapping connects them:

```text
host port : container port
8000      : 8000
```

Command:

```powershell
docker run -p 8000:8000 fastapi-docker-example
```

Meaning:

```text
When I open port 8000 on my machine, forward traffic to port 8000 inside the container.
```

Common issue:

If port `8000` is already used on your machine, run:

```powershell
docker run -p 8001:8000 fastapi-docker-example
```

Then open:

```text
http://127.0.0.1:8001/health
```

## 8. Environment Variables

Environment variables are configuration values passed to a running process.

Use them for settings such as:

- `APP_ENV=local`
- `USE_MOCK_LLM=true`
- `MODEL_NAME=mock-llm`

Command:

```powershell
docker run -p 8000:8000 -e APP_ENV=local fastapi-docker-example
```

Where to run:

Run after the image exists.

What each part means:

- `-e` sets an environment variable inside the container
- `APP_ENV=local` is the variable name and value
- the app can read this value if the code is written to use it

Expected output:

The container starts normally. The variable may not print unless the app logs it.

How to verify:

For a real app, add an endpoint or log line that reads the environment variable. For this beginner example, understand the command shape.

Common beginner mistake:

Hardcoding secrets into a Dockerfile. Do not bake API keys into images.

## 9. Volumes

A volume maps files or folders between your machine and the container.

Use volumes when:

- you want data to persist after a container stops
- you want the container to read files from your machine
- you are doing local development with mounted source code

Example command:

```powershell
docker run -p 8000:8000 -v ${PWD}:/app fastapi-docker-example
```

Where to run:

Run from the folder you want to mount into the container.

What each part means:

- `-v` creates a volume mount
- `${PWD}` means current PowerShell folder
- `/app` is the folder inside the container
- `${PWD}:/app` maps current host folder to `/app` in the container

Expected output:

The container starts and sees the mounted files.

How to verify:

Use an app behavior or shell inspection in advanced practice. For now, know the direction:

```text
host folder -> container folder
```

Common beginner mistake:

Mounting over `/app` can hide files that were copied into the image. Volumes are powerful, but they can confuse beginners during debugging.

## 10. Docker Compose

Docker Compose runs one or more services from a YAML file named `docker-compose.yml`.

Simple meaning:

```text
Compose lets you describe container run settings in a file instead of typing a long docker run command.
```

Example:

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - APP_ENV=local
```

Command:

```powershell
docker compose up
```

Where to run:

Run from the folder containing `docker-compose.yml`.

What each part means:

- `docker compose` runs Docker Compose
- `up` creates and starts the services from the YAML file

Expected output:

You should see build logs and FastAPI/Uvicorn startup logs.

How to verify:

Open:

```text
http://127.0.0.1:8000/health
```

Common beginner mistake:

Thinking Compose replaces Dockerfile. Compose can build using the Dockerfile, but they solve different problems:

```text
Dockerfile = how to build image
docker-compose.yml = how to run service(s)
```

## 11. Container Logs

Container logs are the output printed by the app inside the container.

Command:

```powershell
docker logs <container_id>
```

Where to run:

Run from any folder after the container has started.

What each part means:

- `docker logs` shows logs for a container
- `<container_id>` is the ID from `docker ps`

Expected output:

For FastAPI, logs may include:

```text
Uvicorn running on http://0.0.0.0:8000
```

How to verify:

Run:

```powershell
docker ps
docker logs <container_id>
```

Common beginner mistake:

Looking only at the browser error and not checking container logs. Logs often show import errors, missing packages, or startup failures.

## 12. Containerizing FastAPI

FastAPI inside Docker needs one important detail:

```text
Use --host 0.0.0.0, not only 127.0.0.1.
```

Why:

- `127.0.0.1` inside a container means inside the container only
- `0.0.0.0` means listen on all network interfaces inside the container
- port mapping can then forward traffic from your machine to the container

Good Dockerfile command:

```dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Common mistake:

The container is running, but the browser cannot reach the app because Uvicorn is listening only on `127.0.0.1` inside the container.

## 13. Common Docker Errors

### Docker Desktop Not Running

Error:

```text
Cannot connect to the Docker daemon
```

Meaning:

Docker CLI is installed, but the Docker engine is not running.

Fix:

Start Docker Desktop and try again.

### Port Already Allocated

Error:

```text
port is already allocated
```

Meaning:

Another process or container is using the host port.

Fix:

Use another host port:

```powershell
docker run -p 8001:8000 fastapi-docker-example
```

### Image Not Found

Error:

```text
Unable to find image 'fastapi-docker-example:latest' locally
```

Meaning:

The image has not been built locally, or the name is wrong.

Fix:

Run:

```powershell
docker build -t fastapi-docker-example .
```

### App Starts Then Container Exits

Meaning:

The startup command failed or finished. Containers keep running only while their main process keeps running.

How to debug:

```powershell
docker ps -a
docker logs <container_id>
```

## 14. Where Docker Appears In AI Engineer Work

Docker appears in:

- FastAPI backend packaging
- Streamlit demo packaging
- local RAG app setup
- vector database local stacks
- model server experiments
- final POC deployment readiness
- Kubernetes deployment preparation
- interview questions about repeatable environments
