# REST API Interview Questions

## 1. What is an API?

Short answer:

An API is a defined way for software systems to communicate.

Expanded explanation:

The client sends a request using an agreed format. The server processes it and sends a response.

Project example:

Streamlit sends a request to FastAPI to generate test cases.

Common wrong answer:

"API is a website."

Why incomplete:

A website may use APIs, but API itself is the software communication contract.

## 2. What is REST?

Short answer:

REST is a common web API style using HTTP methods, URLs, resources, and status codes.

Expanded explanation:

REST APIs usually expose resource-oriented endpoints such as `/users`, `/documents`, or `/test-cases`.

Project example:

`POST /generate-test-cases` processes a requirement and returns generated cases.

## 3. What is client vs server?

Short answer:

Client sends request. Server sends response.

Expanded explanation:

The client can be a browser, frontend, curl, Postman, or Python script. The server is the app that handles the request.

Project example:

Streamlit is client. FastAPI is server.

## 4. GET vs POST?

Short answer:

`GET` reads data. `POST` sends data to create or process something.

Expanded explanation:

`GET` usually has no request body. `POST` commonly has JSON body.

Project example:

Use `GET /health` to check status. Use `POST /generate-test-cases` to send requirement text.

## 5. Path parameter vs query parameter?

Short answer:

Path parameter identifies a resource. Query parameter filters or modifies the request.

Expanded explanation:

`/users/101` identifies user `101`. `/users?role=qa` filters users by role.

Project example:

`/documents/10` gets document 10. `/documents?topic=rag` filters documents by topic.

## 6. What is a request body?

Short answer:

The data sent by the client to the server.

Expanded explanation:

For JSON APIs, the body often contains structured JSON fields.

Project example:

```json
{"requirement": "User can login"}
```

## 7. What is a response body?

Short answer:

The data returned by the server.

Expanded explanation:

It usually contains result data, error details, or metadata.

Project example:

```json
{"status": "ok"}
```

## 8. What is a header?

Short answer:

A header carries request or response metadata.

Expanded explanation:

Headers can describe body format, authentication, caching, and more.

Project example:

`Content-Type: application/json` tells the server the body is JSON.

## 9. What is bearer token authentication?

Short answer:

The client sends a token in the `Authorization` header.

Expanded explanation:

Format:

```text
Authorization: Bearer <token>
```

Project example:

LLM provider APIs often use bearer-token-like authentication.

## 10. What does status code `200` mean?

Short answer:

The request succeeded.

Expanded explanation:

The server understood and processed the request successfully.

## 11. What does `400` mean?

Short answer:

Bad request.

Expanded explanation:

The client sent invalid data or malformed input.

Project example:

Missing required JSON field.

## 12. What does `401` mean?

Short answer:

Unauthorized.

Expanded explanation:

Authentication is missing or invalid.

Project example:

API key missing or token invalid.

## 13. What does `404` mean?

Short answer:

Not found.

Expanded explanation:

The endpoint or resource does not exist.

Project example:

Calling `/generate-test-case` when the actual endpoint is `/generate-test-cases`.

## 14. What does `500` mean?

Short answer:

Internal server error.

Expanded explanation:

The server failed while processing the request.

Project example:

Backend code raises an unhandled exception.

## 15. Scenario: FastAPI returns `422`. What does it usually mean?

Short answer:

Validation failed.

Expanded explanation:

FastAPI could not match the request body to the expected Pydantic model.

Project example:

Sending `{"text": "login"}` when endpoint expects `{"requirement": "login"}`.

## 16. What is curl?

Short answer:

`curl` is a command-line tool for sending HTTP requests.

Expanded explanation:

It is useful for testing APIs without a browser or UI.

Project example:

```powershell
curl http://127.0.0.1:8000/health
```

Command explanation:

- `curl` sends the HTTP request.
- `http://127.0.0.1:8000/health` is the local health endpoint.
- this is usually a GET request because no method is specified.

Expected output:

```json
{"status":"ok"}
```

Common error:

```text
Failed to connect
```

Meaning:

The backend server is probably not running or the port/path is wrong.

## 17. Why test APIs?

Short answer:

To verify request validation, response shape, status codes, and error handling.

Expanded explanation:

AI apps still need reliable backend behavior even when model output is probabilistic.

Project example:

Test `/generate-test-cases` with valid and invalid request bodies.
