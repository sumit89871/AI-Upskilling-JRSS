# Requests, Responses, JSON, And HTTP Methods

## 1. What It Is

A request is what the client sends to the server.

A response is what the server sends back.

An HTTP method tells the server what kind of action the client wants.

## 2. The Most Important Beginner Idea

The same URL path can behave differently depending on the method.

Example:

```text
GET /users
POST /users
```

These are not the same:

- `GET /users` usually means read users.
- `POST /users` usually means create a user.

## 3. Why It Matters

FastAPI route decorators directly use HTTP methods:

```python
@app.get("/health")
@app.post("/generate-test-cases")
```

If you do not understand methods, route decorators look random.

## 4. How Request And Response Work

Request contains:

- method
- URL/path
- headers
- optional body

Response contains:

- status code
- headers
- optional body

Mental model:

```text
Client sends method + endpoint + data
Server runs code
Server returns status + data
```

## 5. HTTP Methods

### `GET`

Use `GET` to read data.

Example:

```text
GET /health
GET /users/101
```

Usually no request body is needed.

### `POST`

Use `POST` to create or process data.

Example:

```text
POST /generate-test-cases
```

This usually has a request body:

```json
{
  "requirement": "User can reset password"
}
```

### `PUT`

Use `PUT` to replace a whole resource.

Example:

```text
PUT /users/101
```

Meaning:

Replace user `101` with the body data.

### `PATCH`

Use `PATCH` to partially update a resource.

Example:

```text
PATCH /users/101
```

Meaning:

Update only selected fields.

### `DELETE`

Use `DELETE` to remove a resource.

Example:

```text
DELETE /users/101
```

Meaning:

Delete user `101`.

## 6. JSON Request Body

JSON is structured text data.

Example request body:

```json
{
  "requirement": "User can login",
  "priority": "P1"
}
```

Syntax breakdown:

- `{}` creates a JSON object.
- `"requirement"` is a key.
- `:` separates key and value.
- `"User can login"` is a string value.
- comma separates fields.

Important:

Strict JSON uses double quotes, not single quotes.

Valid:

```json
{"name": "Asha"}
```

Invalid JSON:

```text
{'name': 'Asha'}
```

## 7. JSON Response Body

Example response:

```json
{
  "test_cases": [
    {
      "title": "Valid login",
      "expected_result": "Dashboard opens"
    }
  ]
}
```

Syntax breakdown:

- `test_cases` is a key.
- `[]` creates a list/array.
- inside the list, each `{}` is one object.
- this structure is common for generated test cases.

## 8. Status Codes

Status code tells whether the request succeeded.

Common status codes:

- `200 OK`: request succeeded.
- `201 Created`: new resource created.
- `400 Bad Request`: request data is wrong.
- `401 Unauthorized`: missing or invalid authentication.
- `403 Forbidden`: authenticated but not allowed.
- `404 Not Found`: resource or endpoint not found.
- `422 Unprocessable Entity`: validation failed, common in FastAPI.
- `500 Internal Server Error`: server crashed or failed.

## 9. Small Example: AI Test Case API

Request:

```http
POST /generate-test-cases
Content-Type: application/json

{
  "requirement": "User can reset password"
}
```

Meaning:

- `POST` means process/create something.
- `/generate-test-cases` is the endpoint.
- `Content-Type: application/json` says body is JSON.
- body contains the requirement.

Response:

```json
{
  "requirement": "User can reset password",
  "test_cases": [
    {
      "title": "Valid reset request",
      "type": "positive",
      "expected_result": "Reset link is sent"
    },
    {
      "title": "Unknown email",
      "type": "negative",
      "expected_result": "Safe error message is shown"
    }
  ]
}
```

## 10. Expected Output Meaning

If response status is `200`, the request worked.

If response status is `422` in FastAPI, your JSON shape may not match the Pydantic model.

Example problem:

Expected:

```json
{"requirement": "User can login"}
```

Sent:

```json
{"text": "User can login"}
```

FastAPI may reject it because `requirement` is missing.

## 11. How To Verify It Worked

For a FastAPI app:

1. Start server with `uvicorn`.
2. Open Swagger UI at `/docs`.
3. Try endpoint.
4. Check status code.
5. Check JSON response body.

## 12. Common Mistakes

- Using `GET` for an operation that needs a JSON body.
- Forgetting `Content-Type: application/json`.
- Sending invalid JSON.
- Ignoring response status code.
- Assuming every API error means server is broken. Sometimes the request is wrong.

## 13. Similar Concepts Beginners Confuse

### Request Body vs Response Body

Request body is sent by client. Response body is returned by server.

### `POST` vs `PUT`

`POST` commonly creates/processes. `PUT` replaces a known resource.

### `PATCH` vs `PUT`

`PATCH` partially updates. `PUT` replaces.

### `400` vs `500`

`400` means client/request problem. `500` means server problem.

## 14. Quick Practice

Write request and response examples for:

1. `GET /health`
2. `GET /users/101`
3. `POST /summarize`
4. `POST /generate-test-cases`
5. `DELETE /documents/10`

## 15. Where Used In AI Engineer Work

HTTP method and JSON knowledge appears in:

- FastAPI route decorators
- OpenAI/Gemini request payloads
- Python `requests.post(...)`
- RAG answer APIs
- Streamlit backend calls
- API test generation prompts
- Mettl REST MCQs

