# Parameters, Headers, Authentication, And curl

## 1. What It Is

Parameters and headers add extra information to an API request.

Authentication proves the caller is allowed to access the API.

`curl` is a terminal tool used to send HTTP requests.

## 2. The Most Important Beginner Idea

Not all request data goes in the same place.

API request data may be in:

- path parameter
- query parameter
- header
- request body

Each has a different purpose.

## 3. Why It Matters

If you put data in the wrong place, the API may fail even if your value is correct.

Example:

Bearer token belongs in a header, not in the JSON body.

## 4. Beginner Mental Model

```text
URL path = which resource
Query parameter = filter/options
Header = metadata/auth
Body = main data payload
```

## 5. Path Parameter

Path parameter is part of the URL path.

Example:

```text
GET /users/101
```

Here `101` is a path parameter.

Meaning:

```text
Get the user whose ID is 101.
```

FastAPI style later:

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    ...
```

## 6. Query Parameter

Query parameter comes after `?`.

Example:

```text
GET /users?role=qa&active=true
```

Breakdown:

- `?` starts query parameters.
- `role=qa` means filter role by `qa`.
- `&` separates query parameters.
- `active=true` means only active users.

Meaning:

```text
Get users filtered by role and active status.
```

## 7. Header

Header carries metadata.

Examples:

```text
Content-Type: application/json
Authorization: Bearer abc123
```

`Content-Type` tells the server what format the body uses.

`Authorization` sends authentication information.

## 8. Bearer Token

Bearer token is a common API authentication pattern.

Example:

```text
Authorization: Bearer abc123
```

Breakdown:

- `Authorization` is the header name.
- `Bearer` is the authentication scheme.
- `abc123` represents the token.

Meaning:

```text
The caller is presenting this token as proof of access.
```

Do not put real bearer tokens in screenshots, Git, or course notes.

## 9. `curl` Basics

`curl` sends HTTP requests from terminal.

Simple GET:

```powershell
curl http://127.0.0.1:8000/health
```

Command parts:

- `curl` is the command-line HTTP client.
- `http://127.0.0.1:8000/health` is the URL.

Expected output:

```json
{"status":"ok"}
```

Common error:

```text
Failed to connect
```

Meaning:

The server may not be running, or the URL/port is wrong.

## 10. `curl` With POST JSON

Command:

```powershell
curl -X POST http://127.0.0.1:8000/generate-test-cases -H "Content-Type: application/json" -d "{\"requirement\":\"User can login\"}"
```

Plain English meaning:

```text
Send a POST request with JSON body to the local generate-test-cases endpoint.
```

Command parts:

- `curl` sends the request.
- `-X POST` sets HTTP method to POST.
- URL tells curl where to send the request.
- `-H "Content-Type: application/json"` adds a header.
- `-d` sends request body data.
- escaped quotes `\"` are needed in Windows PowerShell inline JSON.

Expected response:

```json
{
  "requirement": "User can login",
  "test_cases": []
}
```

The exact output depends on the backend implementation.

## 11. `curl` With Bearer Token

Command:

```powershell
curl http://127.0.0.1:8000/private -H "Authorization: Bearer replace_with_token"
```

Command parts:

- `curl` sends an HTTP request.
- `http://127.0.0.1:8000/private` is the protected endpoint.
- `-H` adds a header.
- `Authorization` is the header name.
- `Bearer replace_with_token` is the placeholder token value.

Expected output if token is accepted:

```json
{"message":"private data"}
```

Expected output if token is missing or wrong:

```json
{"detail":"Unauthorized"}
```

The exact response depends on the backend implementation.

Be careful:

Never paste real tokens into shared notes.

## 12. How To Verify It Worked

Check:

- Did the command return JSON?
- Did the status code indicate success?
- Did the server logs show the request?
- Did Swagger UI show the same endpoint behavior?

For more detailed curl output:

```powershell
curl -i http://127.0.0.1:8000/health
```

`-i` includes response headers.

Expected output:

```text
HTTP/1.1 200 OK
content-type: application/json

{"status":"ok"}
```

Meaning:

- `HTTP/1.1 200 OK` means the request succeeded.
- `content-type: application/json` means the response body is JSON.
- `{"status":"ok"}` is the response body.

## 13. Common Mistakes

- Forgetting `-X POST`.
- Forgetting `Content-Type`.
- Invalid JSON quotes.
- Putting token in URL.
- Calling the wrong port.
- Backend server not running.
- Confusing path parameter with query parameter.

## 14. Similar Concepts Beginners Confuse

### Path Parameter vs Query Parameter

Path identifies the resource:

```text
/users/101
```

Query filters or modifies request:

```text
/users?role=qa
```

### Header vs Body

Header is metadata. Body is main payload.

### Authentication vs Authorization

Authentication proves who you are. Authorization decides what you can access.

### curl vs Postman

Both can test APIs. curl runs in terminal. Postman gives a GUI.

## 15. Quick Practice

Write curl commands for:

1. `GET /health`
2. `GET /users/101`
3. `GET /users?role=qa`
4. `POST /summarize` with JSON body
5. `POST /ask` with bearer token header

## 16. Where Used In AI Engineer Work

You use these ideas when:

- testing FastAPI endpoints
- calling LLM APIs
- sending bearer tokens to provider APIs
- debugging Streamlit-to-backend calls
- testing RAG API endpoints
- writing API test cases
- explaining POC integration flow
