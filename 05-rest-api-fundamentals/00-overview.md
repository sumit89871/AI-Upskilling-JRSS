# REST API Overview

## 1. What It Is

An API is a contract that lets one software system use another software system.

Simple meaning:

```text
API = a defined way for software to ask for something and get a response
```

A REST API is a web API style that commonly uses:

- HTTP
- URLs
- methods such as `GET` and `POST`
- JSON request/response bodies
- status codes

## 2. The Most Important Beginner Idea

An API is not the UI.

The UI is what a human sees. The API is what software calls.

Example:

```text
Human -> clicks "Generate Test Cases" in Streamlit UI
Streamlit app -> sends POST request to FastAPI API
FastAPI -> returns JSON response
```

The user clicks a button, but the software talks through an API.

## 3. Why It Matters

AI Engineer work often means connecting systems.

Example final POC flow:

```text
Streamlit UI -> FastAPI endpoint -> RAG helper -> mock LLM -> JSON response
```

Without REST API basics, you may not understand:

- what endpoint the frontend is calling
- why `POST` is used for test generation
- why request body must be JSON
- why `400` means validation problem
- why bearer tokens go in headers

## 4. How It Works

Basic flow:

```text
Client sends request -> Server processes request -> Server sends response
```

### Client

The client is the caller.

Examples:

- browser
- Streamlit frontend
- Postman
- `curl`
- Python `requests`
- another backend service

### Server

The server receives the request and sends a response.

Examples:

- FastAPI app
- OpenAI API
- Gemini API
- vector database service
- internal company API

## 5. Beginner Mental Model

```text
Client
  sends request:
    method + URL + headers + optional body

Server
  runs logic

Client
  receives response:
    status code + headers + optional body
```

Example:

```text
Client asks: POST /generate-test-cases with requirement JSON
Server answers: 200 OK with generated test cases JSON
```

## 6. What Is HTTP?

HTTP is the communication protocol used by web APIs.

When you see:

```text
http://127.0.0.1:8000/health
```

Breakdown:

- `http` is the protocol.
- `127.0.0.1` means your own machine.
- `8000` is the port.
- `/health` is the endpoint path.

## 7. What Is A URL?

A URL is the full address for a web resource.

Example:

```text
http://127.0.0.1:8000/users/101?active=true
```

Breakdown:

- `http://` is the protocol.
- `127.0.0.1` is the host.
- `8000` is the port.
- `/users/101` is the path.
- `?active=true` is the query string.

## 8. What Is An Endpoint?

An endpoint is a specific API path where a server exposes functionality.

Examples:

```text
GET /health
POST /summarize
POST /generate-test-cases
GET /users/101
```

The endpoint is not only the path. In practical API discussion, method plus path matters.

`GET /users` and `POST /users` are different operations.

## 9. What Is A Resource?

A resource is the thing the API works with.

Examples:

- user
- order
- document
- test case
- requirement note

REST APIs often use nouns in paths:

```text
/users
/documents
/test-cases
```

## 10. Small Example

Request:

```http
GET /health HTTP/1.1
Host: 127.0.0.1:8000
```

Meaning:

```text
Client asks server: are you running?
```

Response:

```json
{
  "status": "ok"
}
```

Meaning:

```text
Server says: yes, I am running.
```

## 11. How To Verify It Worked

For a local FastAPI app, you can verify using browser or curl.

Browser:

```text
http://127.0.0.1:8000/health
```

curl:

```powershell
curl http://127.0.0.1:8000/health
```

Command parts:

- `curl` sends an HTTP request from terminal.
- URL tells curl which endpoint to call.

Expected output:

```json
{"status":"ok"}
```

## 12. Common Mistakes

- Thinking API means UI screen.
- Thinking URL and endpoint are always the same. URL is full address; endpoint is usually method plus path.
- Sending JSON with invalid syntax.
- Using `GET` when the server expects `POST`.
- Ignoring status codes.
- Putting secrets in query parameters.

## 13. Similar Concepts Beginners Confuse

### API vs UI

UI is for humans. API is for software.

### URL vs Endpoint

URL is the full address. Endpoint is the server operation path plus method.

### Request vs Response

Request goes from client to server. Response comes back from server to client.

### Client vs Server

Client asks. Server answers.

## 14. Where Used In AI Engineer Work

REST API basics appear in:

- FastAPI endpoints
- OpenAI/Gemini SDK calls
- Python `requests`
- Streamlit frontend calling backend
- RAG service APIs
- MCP clients and server transport concepts
- Docker health checks
- Kubernetes service checks
- Mettl REST questions
- POC architecture explanation

