# Docker Exercises

Use this mental model for every exercise:

```text
Dockerfile -> image -> container -> running app
```

## Exercise 1: Explain Image vs Container

### Task

Write a short explanation of image vs container using the FastAPI Docker example.

### Expected Answer

```text
An image is the packaged FastAPI app blueprint created by docker build.
A container is the running FastAPI app created by docker run from that image.
```

### Expected Commands

No command is required for this exercise.

### Expected Output

You should be able to explain:

```text
Dockerfile -> docker build -> image -> docker run -> container
```

### Hints

- Image exists even when the app is not running.
- Container exists when an image is started.

### Self-Check

Can you create two containers from the same image?

Expected answer:

Yes, one image can be used to create multiple containers.

### Solution Outline

1. Define image.
2. Define container.
3. Explain build creates image.
4. Explain run creates container.

### Common Mistake

Saying "Dockerfile is the container." The Dockerfile is only the recipe.

## Exercise 2: Explain Every Line Of The Dockerfile

### Task

Open:

```text
16-docker-basics/implementation/fastapi-docker-example/Dockerfile
```

Explain every instruction.

### Expected Code

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Expected Commands

No Docker command is required, but you can view the file from the module folder:

```powershell
Get-Content implementation\fastapi-docker-example\Dockerfile
```

Where to run:

Run from:

```text
16-docker-basics/
```

What each part means:

- `Get-Content` prints a file in PowerShell
- `implementation\fastapi-docker-example\Dockerfile` is the file path

Expected output:

The Dockerfile contents should print in the terminal.

How to verify:

Check that you can explain `FROM`, `WORKDIR`, `COPY`, `RUN`, and `CMD`.

Common mistake:

Thinking `RUN` starts the app. `RUN` happens while building the image. `CMD` is the default container startup command.

### Hints

- `FROM` chooses the base image.
- `COPY` moves files into the image.
- `RUN` executes during build.
- `CMD` runs when the container starts.

### Self-Check

Why does the Dockerfile use `--host 0.0.0.0`?

Expected answer:

So the app can receive traffic forwarded into the container.

### Solution Outline

1. Explain base image.
2. Explain working directory.
3. Explain dependency copy.
4. Explain dependency install.
5. Explain source copy.
6. Explain startup command.

## Exercise 3: Build The FastAPI Image

### Task

Build the image named:

```text
fastapi-docker-example
```

### Expected Commands

Command:

```powershell
cd 16-docker-basics\implementation\fastapi-docker-example
```

Where to run:

Run from the course root.

What each part means:

- `cd` changes folder
- the path moves into the folder containing the Dockerfile

Expected output:

PowerShell changes into the folder. Usually there is no success message.

How to verify:

Run:

```powershell
Get-ChildItem
```

You should see `Dockerfile`.

Common mistake:

Building from the wrong folder.

Command:

```powershell
docker build -t fastapi-docker-example .
```

Where to run:

Run from the folder containing `Dockerfile`.

What each part means:

- `docker` runs Docker CLI
- `build` creates an image
- `-t fastapi-docker-example` names the image
- `.` uses the current folder as build context

Expected output:

```text
Successfully tagged fastapi-docker-example:latest
```

How to verify:

```powershell
docker images
```

You should see `fastapi-docker-example`.

### Hints

- Docker Desktop must be running.
- The final dot is required.

### Self-Check

What did you create: image or container?

Expected answer:

An image.

### Solution Outline

1. Move into the implementation folder.
2. Run `docker build`.
3. Verify with `docker images`.

### Common Mistake

Expecting the app to be running after `docker build`. Build creates an image; it does not start the app.

## Exercise 4: Run The FastAPI Container

### Task

Run a container from the image and open `/health`.

### Expected Command

```powershell
docker run -p 8000:8000 fastapi-docker-example
```

Where to run:

Run from any folder after the image exists.

What each part means:

- `docker run` starts a container
- `-p 8000:8000` maps your machine's port `8000` to the container's port `8000`
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

### Hints

- Keep the terminal running.
- Open the browser separately.
- If port 8000 is busy, use `8001:8000`.

### Self-Check

In `8000:8000`, which port is on your machine?

Expected answer:

The first `8000`.

### Solution Outline

1. Make sure image exists.
2. Run the container with port mapping.
3. Open `/health`.
4. Stop the container with `Ctrl+C` or `docker stop`.

### Common Mistake

Opening `http://127.0.0.1:8000/health` before the container has finished starting.

## Exercise 5: Run With An Environment Variable

### Task

Run the container with an environment variable named `APP_ENV`.

### Expected Command

```powershell
docker run -p 8000:8000 -e APP_ENV=local fastapi-docker-example
```

Where to run:

Run from any folder after the image exists.

What each part means:

- `-e` sets an environment variable
- `APP_ENV=local` is available inside the container
- the rest starts the FastAPI container

Expected output:

The app starts normally.

How to verify:

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

### Hints

- Environment variables configure a running container.
- Do not put real API keys directly into a Dockerfile.

### Self-Check

Why are environment variables useful for AI apps?

Expected answer:

They can hold settings such as environment name, mock mode, model name, or external service URLs without changing source code.

### Solution Outline

1. Run `docker run` with `-e`.
2. Verify the container still starts.
3. Explain how real apps can read environment variables.

### Common Mistake

Hardcoding secrets into the image instead of passing them at runtime.

## Exercise 6: Use Docker Compose

### Task

Start the FastAPI service using `docker-compose.yml`.

### Expected Command

```powershell
docker compose up
```

Where to run:

Run from:

```text
16-docker-basics/implementation/fastapi-docker-example/
```

What each part means:

- `docker compose` runs Compose
- `up` starts services from `docker-compose.yml`

Expected output:

Build logs and FastAPI startup logs.

How to verify:

Open:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{"status":"ok"}
```

### Hints

- Compose reads `docker-compose.yml`.
- The service name is `app`.
- The file maps `"8000:8000"`.

### Self-Check

What is the difference between Dockerfile and `docker-compose.yml`?

Expected answer:

Dockerfile builds the image. Compose describes how to run one or more services.

### Solution Outline

1. Move into the implementation folder.
2. Run `docker compose up`.
3. Verify `/health`.
4. Stop with `Ctrl+C`.
5. Run `docker compose down`.

### Common Mistake

Running `docker compose up` from a folder that does not contain `docker-compose.yml`.
