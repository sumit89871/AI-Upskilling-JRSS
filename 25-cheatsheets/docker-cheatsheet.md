# Docker Cheatsheet

## Dockerfile

Meaning: Recipe for building an image.

Use when: Packaging an app.

Example: `FROM python:3.11-slim`

Be careful: Dockerfile is not the running app.

## Image

Meaning: Packaged template.

Use when: Creating containers.

Example: `docker build -t qa-api .`

Be careful: Rebuild image after Dockerfile/code changes.

## Container

Meaning: Running instance of an image.

Use when: Running packaged app.

Example: `docker run -p 8000:8000 qa-api`

Be careful: Container stops when main process stops.

## Port Mapping

Syntax: `8000:8000`

Meaning: host port to container port.

Use when: Accessing app from browser.

Be careful: Left side is host; right side is container.
