# Docker Cheatsheet

## Mental Model

Syntax:

```text
Dockerfile -> image -> container -> running app
```

Meaning:

Dockerfile is the recipe, image is the packaged result, container is the running instance.

When to use:

Use this to debug whether you are building, running, or inspecting.

Example:

```text
docker build creates image
docker run starts container
```

Be careful:

Do not say "run a Dockerfile." You build from a Dockerfile.

## Check Docker Version

Command:

```powershell
docker --version
```

Meaning:

Checks whether Docker CLI is installed.

When to use:

Use before Docker exercises or troubleshooting.

Example:

```text
Docker version ...
```

Be careful:

This checks the CLI. Docker Desktop/engine must also be running for build/run commands.

## Build Image

Command:

```powershell
docker build -t app-name .
```

Meaning:

Builds an image from the Dockerfile in the current folder.

When to use:

Use after creating or changing a Dockerfile/app.

Example:

```powershell
docker build -t fastapi-docker-example .
```

Be careful:

Run from the folder containing `Dockerfile`. The final dot is the build context.

## List Images

Command:

```powershell
docker images
```

Meaning:

Lists images available locally.

When to use:

Use after `docker build` to verify the image exists.

Example:

```text
fastapi-docker-example   latest   ...
```

Be careful:

Images are not running containers.

## Run Container With Port

Command:

```powershell
docker run -p 8000:8000 app-name
```

Meaning:

Starts a container and maps host port to container port.

When to use:

Use to run a web app container locally.

Example:

```powershell
docker run -p 8000:8000 fastapi-docker-example
```

Be careful:

First port is your machine. Second port is inside the container.

## Run With Environment Variable

Command:

```powershell
docker run -e APP_ENV=local app-name
```

Meaning:

Sets `APP_ENV` inside the container.

When to use:

Use for runtime configuration.

Example:

```powershell
docker run -p 8000:8000 -e APP_ENV=local fastapi-docker-example
```

Be careful:

Do not bake real secrets into images.

## Run With Volume

Command:

```powershell
docker run -v ${PWD}:/app app-name
```

Meaning:

Mounts the current host folder into `/app` inside the container.

When to use:

Use for shared files or local development.

Example:

```powershell
docker run -p 8000:8000 -v ${PWD}:/app fastapi-docker-example
```

Be careful:

A mount can hide files copied into the image at the same path.

## List Running Containers

Command:

```powershell
docker ps
```

Meaning:

Shows running containers.

When to use:

Use to find container ID, port mapping, and status.

Example:

```text
CONTAINER ID   IMAGE                    STATUS   PORTS
abc123         fastapi-docker-example   Up ...   0.0.0.0:8000->8000/tcp
```

Be careful:

Stopped containers require `docker ps -a`.

## Show Logs

Command:

```powershell
docker logs <container_id>
```

Meaning:

Prints logs from a container.

When to use:

Use when the app fails, exits, or browser cannot connect.

Example:

```powershell
docker logs abc123
```

Be careful:

Use container ID/name, not image name.

## Stop Container

Command:

```powershell
docker stop <container_id>
```

Meaning:

Stops a running container.

When to use:

Use when you need to stop an app or free a port.

Example:

```powershell
docker stop abc123
```

Be careful:

Stopping a container does not delete the image.

## Docker Compose Up

Command:

```powershell
docker compose up
```

Meaning:

Starts services defined in `docker-compose.yml`.

When to use:

Use when run settings are stored in Compose YAML.

Example:

```powershell
cd 16-docker-basics\implementation\fastapi-docker-example
docker compose up
```

Be careful:

Run from the folder containing `docker-compose.yml`.

## Docker Compose Down

Command:

```powershell
docker compose down
```

Meaning:

Stops and removes Compose-created containers and networks.

When to use:

Use after testing Compose services.

Example:

```powershell
docker compose down
```

Be careful:

This removes Compose containers, not your source code.

## Core Terms

- Docker: tool for packaging and running apps in containers.
- Dockerfile: image recipe.
- Image: packaged app blueprint.
- Container: running image instance.
- Build: create image.
- Run: start container.
- Port mapping: connect host port to container port.
- Environment variable: runtime configuration value.
- Volume: mounted shared/persistent file location.
- Compose: YAML-based multi-service runner.

## Podman Awareness

Command:

```powershell
podman build -t app-name .
```

Meaning:

Builds a container image using Podman. The command shape is similar to `docker build`.

When to use:

Use when an enterprise or Linux environment uses Podman instead of Docker.

Example:

```powershell
podman build -t fastapi-app .
```

Be careful:

Do not claim Podman and Docker are exactly the same internally. For beginner exam/interview purposes, connect them through shared concepts: image, container, build, run, port mapping, logs.

Command:

```powershell
podman run -p 8000:8000 app-name
```

Meaning:

Starts a container from an image and maps a host port to a container port.

When to use:

Use when running a containerized FastAPI or demo app in a Podman-based environment.

Example:

```powershell
podman run -p 8000:8000 fastapi-app
```

Be careful:

The first port is on your machine. The second port is inside the container, just like Docker port mapping.
