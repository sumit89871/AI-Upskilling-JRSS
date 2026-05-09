# REST API Cheatsheet

## Endpoint

Syntax: `/users/{user_id}`

Meaning: API path the client calls.

Use when: Designing routes.

Example: `/health`, `/ask-context`.

Be careful: Domain is not the same as endpoint path.

## GET

Meaning: Read data.

Use when: No server state should change.

Example: `GET /health`

Be careful: Do not send sensitive data in query strings.

## POST

Meaning: Submit data for processing or creation.

Use when: Sending JSON body.

Example: `POST /generate-test-cases`

Be careful: Validate request body.

## Status Codes

Syntax: `200`, `400`, `401`, `404`, `422`, `500`

Meaning: Server result category.

Use when: Debugging API responses.

Example: `422` in FastAPI often means validation failed.

Be careful: `404` is not found; `500` is server error.
