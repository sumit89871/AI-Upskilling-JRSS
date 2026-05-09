# Dockerfile, Run, And Compose

## 1. What This Topic Covers

This file explains how a FastAPI app becomes a Docker container.

The core flow is:

```text
Dockerfile -> image -> container -> running app
```

Beginner translation:

- Dockerfile is the recipe
- image is the packaged result
- container is the running app created from the image
- Docker Compose is a YAML helper for running services with repeatable settings

## 2. Dockerfile vs Image vs Container

Do not merge these concepts.

```text
Dockerfile = instructions for building
Image = packaged app created by build
Container = running process created from image
```

You do not run a Dockerfile directly.

You run:

```text
docker build -> creates image
docker run -> creates/runs container
```

## 3. FastAPI Dockerfile Example

File name:

```text
Dockerfile
```

Folder path:

```text
16-docker-basics/implementation/fastapi-docker-example/Dockerfile
```

What this file is for:

This file tells Docker how to package the FastAPI app into an image.

Full code:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 4. Dockerfile Line-By-Line

### `FROM`

```dockerfile
FROM python:3.11-slim
```

Meaning:

Start from an existing image that already has Python 3.11 installed.

Why it exists:

Your app needs Python before it can run. Instead of installing Python manually inside an empty environment, you start from a trusted Python base image.

Common mistake:

Choosing a base image without the runtime your app needs.

### `WORKDIR`

```dockerfile
WORKDIR /app
```

Meaning:

Set `/app` as the working folder inside the image/container.

Practical effect:

Later commands such as `COPY requirements.txt .` and `RUN pip install ...` run relative to `/app`.

Common mistake:

Forgetting that `/app` is inside the container, not necessarily a folder on your host machine.

### `COPY requirements.txt .`

```dockerfile
COPY requirements.txt .
```

Meaning:

Copy `requirements.txt` from your project folder into the current image folder.

The second dot means:

```text
copy into current container working directory, which is /app
```

Why it is copied before source code:

Dependency installation can be cached more efficiently when `requirements.txt` changes less often than app code.

Common mistake:

Running `docker build` from the wrong folder, so Docker cannot find `requirements.txt`.

### `RUN`

```dockerfile
RUN pip install -r requirements.txt
```

Meaning:

Run this command while building the image.

This installs FastAPI and Uvicorn inside the image.

Important:

`RUN` happens during image build, not when the container starts.

Common mistake:

Thinking `RUN` is the app startup command. The app startup command is usually `CMD`.

### `COPY . .`

```dockerfile
COPY . .
```

Meaning:

Copy the rest of the current build context into `/app` inside the image.

In this example, it copies:

- `main.py`
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`

In real projects, use `.dockerignore` to avoid copying:

- `.venv`
- cache folders
- secrets
- local test artifacts

Common mistake:

Accidentally copying large or sensitive files into the image.

### `CMD`

```dockerfile
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Meaning:

This is the default command that runs when a container starts from the image.

Read it in order:

```text
uvicorn -> main:app -> --host 0.0.0.0 -> --port 8000
```

Breakdown:

- `uvicorn` starts the FastAPI server
- `main:app` means load `app` from `main.py`
- `--host 0.0.0.0` lets traffic reach the app inside the container
- `--port 8000` tells Uvicorn to listen on port `8000`

Common mistake:

Using `--host 127.0.0.1` inside Docker. That can make the app unreachable from your host browser.

## 5. Build The Image

Command:

```powershell
docker build -t fastapi-docker-example .
```

Where to run:

Run from:

```text
16-docker-basics/implementation/fastapi-docker-example/
```

When to run:

Run after creating or changing the Dockerfile, requirements, or app code you want packaged.

What each part means:

- `docker` runs Docker CLI
- `build` creates an image
- `-t fastapi-docker-example` gives the image a readable tag
- `.` uses the current folder as the build context

Expected output:

```text
Successfully tagged fastapi-docker-example:latest
```

How to verify:

```powershell
docker images
```

Expected result:

The image list should include:

```text
fastapi-docker-example
```

Common beginner mistake:

Forgetting the final dot. Without `.`, Docker does not know which build context to use.

## 6. Run The Container

Command:

```powershell
docker run -p 8000:8000 fastapi-docker-example
```

Where to run:

Run from any folder after the image exists.

When to run:

Run when you want to start the FastAPI app in a container.

What each part means:

- `docker run` starts a container from an image
- `-p` publishes a port
- first `8000` is the host port on your machine
- second `8000` is the container port
- `fastapi-docker-example` is the image name

Expected output:

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

The terminal stays busy while the container runs. That is normal. Open another terminal if you need to run more commands.

## 7. Run With A Container Name

Command:

```powershell
docker run --name fastapi-demo -p 8000:8000 fastapi-docker-example
```

Where to run:

Run from any folder after the image exists.

What each part means:

- `--name fastapi-demo` gives the container a readable name
- `-p 8000:8000` maps host port to container port
- `fastapi-docker-example` is the image

Expected output:

FastAPI/Uvicorn startup logs.

How to verify:

```powershell
docker ps
```

Expected result:

You should see a running container named `fastapi-demo`.

Common beginner mistake:

Reusing a container name that already exists. Remove the old container or choose another name.

## 8. Stop And Remove A Container

Command:

```powershell
docker ps
```

Where to run:

Run from any folder.

What each part means:

- `docker` runs the Docker CLI
- `ps` lists running containers

Expected output:

A table with container ID, image, status, and ports.

How to verify:

Find your running FastAPI container in the list.

Common mistake:

Looking for stopped containers with `docker ps`. Use `docker ps -a` to include stopped containers.

Command:

```powershell
docker stop <container_id>
```

Where to run:

Run from any folder after you know the container ID or name.

What each part means:

- `docker stop` stops a running container
- `<container_id>` is the ID shown by `docker ps`

Expected output:

Docker prints the stopped container ID or name.

How to verify:

```powershell
docker ps
```

The container should no longer appear in the running list.

Common mistake:

Typing the image name instead of the container ID/name.

## 9. Container Logs

Command:

```powershell
docker logs <container_id>
```

Where to run:

Run from any folder.

What each part means:

- `docker logs` prints container output
- `<container_id>` identifies the container

Expected output:

For FastAPI:

```text
Uvicorn running on http://0.0.0.0:8000
```

How to verify:

Use logs to confirm the app started or to see startup errors.

Common mistake:

Debugging only with the browser. Always check container logs when a Dockerized app fails.

## 10. Docker Compose Example

File name:

```text
docker-compose.yml
```

Folder path:

```text
16-docker-basics/implementation/fastapi-docker-example/docker-compose.yml
```

What this file is for:

This file describes how to run the FastAPI app as a Compose service.

Full code:

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - APP_ENV=local
```

## 11. Compose YAML Line-By-Line

`services`:

```yaml
services:
```

Groups the containers Compose should manage.

`app`:

```yaml
  app:
```

Defines one service named `app`.

`build: .`:

```yaml
    build: .
```

Tells Compose to build an image from the Dockerfile in the current folder.

`ports`:

```yaml
    ports:
      - "8000:8000"
```

Maps host port `8000` to container port `8000`.

`environment`:

```yaml
    environment:
      - APP_ENV=local
```

Sets an environment variable inside the container.

Common YAML mistake:

Indentation matters. Use spaces, not tabs.

## 12. Compose Up

Command:

```powershell
docker compose up
```

Where to run:

Run from the folder containing `docker-compose.yml`.

When to run:

Run when you want Compose to build and start the service.

What each part means:

- `docker compose` runs Docker Compose
- `up` creates and starts services

Expected output:

You should see build logs and app startup logs.

How to verify:

Open:

```text
http://127.0.0.1:8000/health
```

Common beginner mistake:

Running Compose from the wrong folder. Compose looks for `docker-compose.yml` in the current folder by default.

## 13. Compose Down

Command:

```powershell
docker compose down
```

Where to run:

Run from the folder containing `docker-compose.yml`.

When to run:

Run when you want to stop and remove Compose-created containers and networks.

What each part means:

- `docker compose` runs Compose
- `down` stops and removes Compose resources

Expected output:

```text
Container ... Removed
Network ... Removed
```

How to verify:

```powershell
docker ps
```

The Compose container should no longer be running.

Common beginner mistake:

Closing the terminal but leaving containers running in detached scenarios. Use `docker ps` to check.

## 14. Where This Appears In AI Engineer Work

Dockerfile and Compose appear in:

- FastAPI backend packaging
- local RAG app packaging
- app plus vector database local setup
- final POC demo readiness
- Kubernetes image preparation
- interview deployment discussions
