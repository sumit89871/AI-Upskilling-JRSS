# REST API Cheatsheet

## API

Meaning:

A defined way for software systems to communicate.

Use when:

One app needs data or action from another app.

Example:

```text
Streamlit UI calls FastAPI backend.
```

Be careful:

API is not the same as UI.

## Endpoint

Meaning:

A method plus path exposed by a server.

Example:

```text
POST /generate-test-cases
```

Use when:

You describe what operation the client calls.

## `GET`

Meaning:

Read data.

Example:

```text
GET /health
```

Be careful:

Do not send sensitive data in URL query strings.

## `POST`

Meaning:

Create or process data.

Example:

```text
POST /summarize
```

Use when:

You need to send JSON body such as text, requirement, or question.

## Request Body

Meaning:

Main data sent from client to server.

Example:

```json
{"question": "What is RAG?"}
```

Be careful:

Strict JSON requires double quotes.

## Response Body

Meaning:

Data returned from server to client.

Example:

```json
{"answer": "RAG retrieves context before generation."}
```

## Header

Meaning:

Metadata sent with request or response.

Example:

```text
Content-Type: application/json
Authorization: Bearer token_here
```

## Path Parameter

Meaning:

Value inside the URL path identifying a resource.

Example:

```text
/users/101
```

## Query Parameter

Meaning:

Filter or option after `?`.

Example:

```text
/users?role=qa
```

## curl GET

Command:

```powershell
curl http://127.0.0.1:8000/health
```

Meaning:

Send GET request to local health endpoint.

Where to run:

Run it in PowerShell while the FastAPI server is already running.

Expected output:

```json
{"status":"ok"}
```

Common error:

```text
Failed to connect
```

Meaning:

The backend is not running, the port is wrong, or the endpoint URL is wrong.

## curl POST JSON

Command:

```powershell
curl -X POST http://127.0.0.1:8000/ask -H "Content-Type: application/json" -d "{\"question\":\"What is RAG?\"}"
```

Meaning:

Send JSON body to `/ask`.

Command breakdown:

- `curl` sends an HTTP request.
- `-X POST` sets the method to POST.
- `http://127.0.0.1:8000/ask` is the endpoint URL.
- `-H "Content-Type: application/json"` tells the server the body is JSON.
- `-d` sends the request body.

Expected output:

```json
{"answer":"..."}
```

The exact answer depends on your backend.

How to verify:

Check that the response is JSON and the backend terminal logs show the request.

Be careful:

PowerShell needs escaped quotes for inline JSON.

## Status Code Families

- `2xx`: success
- `4xx`: client/request problem
- `5xx`: server problem
