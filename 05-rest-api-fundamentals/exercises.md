# REST API Exercises

## Exercise 1: Explain Client And Server

### Task

Write a simple explanation using this flow:

```text
Client sends request -> Server sends response
```

Use a food-ordering analogy.

### Expected Result

Your explanation should include:

- who asks
- who responds
- what information is sent
- what result comes back

### Common Mistake

Saying "server is the internet." The server is a specific application or machine responding to requests.

### Self-Check Question

In a Streamlit + FastAPI POC, which one is usually the client and which one is the server?

## Exercise 2: Break Down A URL

### Task

Break this URL into parts:

```text
http://127.0.0.1:8000/users/101?active=true
```

### Expected Answer

- protocol: `http`
- host: `127.0.0.1`
- port: `8000`
- path: `/users/101`
- query parameter: `active=true`

### Common Mistake

Calling the full URL an endpoint. In practical discussion, endpoint usually means method plus path.

## Exercise 3: Design A Request Body

### Task

Create JSON for this API:

```text
POST /generate-test-cases
```

Required fields:

- `requirement`
- `priority`

### Expected JSON

```json
{
  "requirement": "User can reset password",
  "priority": "P1"
}
```

### Common Mistake

Using single quotes, which is not strict JSON.

## Exercise 4: Choose The Correct Method

### Task

Choose method for each:

- read health status
- create user
- replace user details
- update only user email
- delete document

### Expected Answer

- read health status: `GET`
- create user: `POST`
- replace user details: `PUT`
- update only user email: `PATCH`
- delete document: `DELETE`

### Self-Check Question

Why is `POST` better than `GET` for sending a large requirement body?

## Exercise 5: Write curl Commands

### Task

Write curl command for:

```text
POST http://127.0.0.1:8000/generate-test-cases
```

Body:

```json
{"requirement": "User can login"}
```

### Expected Command

```powershell
curl -X POST http://127.0.0.1:8000/generate-test-cases -H "Content-Type: application/json" -d "{\"requirement\":\"User can login\"}"
```

### Command Explanation

- `curl` sends an HTTP request from the terminal.
- `-X POST` tells curl to use the POST method.
- `http://127.0.0.1:8000/generate-test-cases` is the local API endpoint.
- `-H "Content-Type: application/json"` adds a header saying the body is JSON.
- `-d "{\"requirement\":\"User can login\"}"` sends the JSON request body.

### Expected Output

If the backend is running and the endpoint exists, you should receive JSON similar to:

```json
{
  "requirement": "User can login",
  "test_cases": []
}
```

The exact `test_cases` value depends on the backend implementation.

### How To Verify

- Confirm the response is JSON.
- Confirm the server terminal shows a `POST /generate-test-cases` request.
- Try the same endpoint in Swagger UI if using FastAPI.

### Common Mistake

Forgetting escaped quotes in Windows PowerShell inline JSON.

### Self-Check Question

What does `-H` do?

## Exercise 6: Interpret Status Codes

### Task

Explain these:

- `200`
- `201`
- `400`
- `401`
- `404`
- `422`
- `500`

### Expected Result

You should identify success vs client problem vs server problem.

### Common Mistake

Assuming every `4xx` is a server bug. Usually `4xx` means request/client problem.
