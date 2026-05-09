# FastAPI Docker Example

## 1. Project Goal

This folder contains a minimal FastAPI app that can run locally or inside Docker.

The purpose is to connect the Docker mental model to a real app:

```text
Dockerfile -> image -> container -> running FastAPI app
```

## 2. Files In This Folder

Folder:

```text
16-docker-basics/implementation/fastapi-docker-example/
```

Files:

- `main.py`: minimal FastAPI app with `GET /health`.
- `requirements.txt`: Python package list.
- `Dockerfile`: image build recipe.
- `docker-compose.yml`: Compose service definition.
- `README.md`: setup and explanation.

## 3. `main.py`

What this file is for:

Defines the FastAPI app.

Code:

```python
from fastapi import FastAPI


app = FastAPI()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
```

Line-by-line:

- `from fastapi import FastAPI` imports the FastAPI class.
- `app = FastAPI()` creates the app object.
- `@app.get("/health")` registers a GET endpoint.
- `def health() -> dict:` defines the route function.
- `return {"status": "ok"}` returns a Python dictionary.
- FastAPI converts the dictionary to JSON.

## 4. `requirements.txt`

Current contents:

```text
fastapi
uvicorn
```

Meaning:

- `fastapi` is the API framework.
- `uvicorn` is the server that runs the FastAPI app.

Docker uses this file during image build:

```dockerfile
RUN pip install -r requirements.txt
```

## 5. `Dockerfile`

Current contents:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Meaning:

- `FROM python:3.11-slim` starts from a Python base image.
- `WORKDIR /app` sets the container working folder.
- `COPY requirements.txt .` copies the dependency list.
- `RUN pip install -r requirements.txt` installs dependencies into the image.
- `COPY . .` copies app files into the image.
- `CMD [...]` starts Uvicorn when the container runs.

Important:

`--host 0.0.0.0` is needed so traffic forwarded from Docker port mapping can reach the app.

## 6. `docker-compose.yml`

Current contents:

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - APP_ENV=local
```

Meaning:

- `services` groups Compose services.
- `app` is the service name.
- `build: .` builds from the Dockerfile in this folder.
- `"8000:8000"` maps host port to container port.
- `APP_ENV=local` sets an environment variable.

## 7. Run Locally Without Docker

Command:

```powershell
pip install -r requirements.txt
```

Where to run:

Run from:

```text
16-docker-basics/implementation/fastapi-docker-example/
```

What each part means:

- `pip` installs Python packages
- `install` tells pip to install
- `-r` means read from a requirements file
- `requirements.txt` contains package names

Expected output:

```text
Successfully installed fastapi uvicorn ...
```

How to verify:

```powershell
pip show fastapi
```

Common mistake:

Installing packages into the wrong Python environment.

Command:

```powershell
uvicorn main:app --reload
```

Where to run:

Run from the same folder as `main.py`.

What each part means:

- `uvicorn` starts the server
- `main` means `main.py`
- `app` means the FastAPI object inside `main.py`
- `--reload` restarts when code changes

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
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

Common mistake:

Running Uvicorn from a folder that does not contain `main.py`.

## 8. Build Docker Image

Command:

```powershell
docker build -t fastapi-docker-example .
```

Where to run:

Run from:

```text
16-docker-basics/implementation/fastapi-docker-example/
```

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

Expected result:

You should see `fastapi-docker-example`.

Common mistake:

Forgetting Docker Desktop must be running.

## 9. Run Container

Command:

```powershell
docker run -p 8000:8000 fastapi-docker-example
```

Where to run:

Run from any folder after the image is built.

What each part means:

- `docker run` starts a container
- `-p 8000:8000` maps host port `8000` to container port `8000`
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

Common mistake:

If port `8000` is busy, use:

```powershell
docker run -p 8001:8000 fastapi-docker-example
```

Then open:

```text
http://127.0.0.1:8001/health
```

## 10. Run With Docker Compose

Command:

```powershell
docker compose up
```

Where to run:

Run from the folder containing `docker-compose.yml`.

What each part means:

- `docker compose` runs Compose
- `up` builds and starts services

Expected output:

Build logs followed by FastAPI/Uvicorn startup logs.

How to verify:

Open:

```text
http://127.0.0.1:8000/health
```

Common mistake:

Running the command from a folder without `docker-compose.yml`.

Command:

```powershell
docker compose down
```

Where to run:

Run from the folder containing `docker-compose.yml`.

What each part means:

- `down` stops and removes Compose-created containers and networks

Expected output:

```text
Container ... Removed
Network ... Removed
```

How to verify:

```powershell
docker ps
```

The Compose container should not be running.

Common mistake:

Stopping the visible logs with `Ctrl+C` but not checking whether containers remain running.

## 11. Common Errors

### `Cannot connect to the Docker daemon`

Meaning:

Docker Desktop is not running.

Fix:

Start Docker Desktop.

### `port is already allocated`

Meaning:

Port `8000` is already used on your machine.

Fix:

Use a different host port:

```powershell
docker run -p 8001:8000 fastapi-docker-example
```

### Browser Cannot Reach App

Check:

- container is running with `docker ps`
- port mapping is correct
- Dockerfile uses `--host 0.0.0.0`
- app logs do not show startup errors

### Image Not Found

Meaning:

The image was not built or the name is wrong.

Fix:

```powershell
docker build -t fastapi-docker-example .
```
