# REST API and FastAPI MCQs

## MCQ 1: API meaning

Question:

What is an API?

Options:

A. A way for software systems to communicate  
B. A database table only  
C. A Python loop  
D. A Docker image

Correct answer:

A. A way for software systems to communicate

Explanation:

An API defines how one software component can request data or actions from another component.

Common trap:

Thinking API only means a public internet service. APIs can also be internal.

## MCQ 2: REST endpoint

Question:

In this URL, what is the endpoint path?

```text
https://api.example.com/users/10
```

Options:

A. `https`  
B. `api.example.com`  
C. `/users/10`  
D. `10`

Correct answer:

C. `/users/10`

Explanation:

The endpoint path is the part after the domain that identifies the resource or action.

Common trap:

Confusing domain with endpoint path.

## MCQ 3: GET method

Question:

Which HTTP method is normally used to read data?

Options:

A. GET  
B. POST  
C. DELETE  
D. PATCH

Correct answer:

A. GET

Explanation:

GET is normally used to retrieve data without changing server state.

Common trap:

Using POST for every API call because it can send a body. Method choice should match intent.

## MCQ 4: POST method

Question:

Which method is normally used to create a new resource or submit data?

Options:

A. GET  
B. POST  
C. HEAD  
D. OPTIONS

Correct answer:

B. POST

Explanation:

POST is commonly used to submit data to the server, such as creating a user or generating test cases.

Common trap:

Thinking POST always means database creation. In GenAI apps, POST can also submit a prompt for processing.

## MCQ 5: Status code 404

Question:

What does HTTP `404` usually mean?

Options:

A. Success  
B. Unauthorized  
C. Not found  
D. Server error

Correct answer:

C. Not found

Explanation:

`404` means the requested resource or route was not found.

Common trap:

Confusing `404` with `500`. `500` means server-side error.

## MCQ 6: Status code 422 in FastAPI

Question:

FastAPI returns `422` for a POST request. What is a likely reason?

Options:

A. Request body failed validation  
B. Docker is not installed  
C. Git branch is missing  
D. Browser cache issue only

Correct answer:

A. Request body failed validation

Explanation:

FastAPI uses Pydantic for request validation. If required fields are missing or types are wrong, FastAPI may return `422`.

Common trap:

Thinking the endpoint function must have crashed. Often the function did not run because validation failed first.

## MCQ 7: Path parameter

Question:

In `/users/{user_id}`, what is `user_id`?

Options:

A. Header  
B. Path parameter  
C. Request body  
D. Status code

Correct answer:

B. Path parameter

Explanation:

`user_id` is part of the URL path and changes per request, such as `/users/10`.

Common trap:

Confusing path parameters with query parameters.

## MCQ 8: Query parameter

Question:

In `/search?q=rag`, what is `q=rag`?

Options:

A. Query parameter  
B. Path parameter  
C. Request body  
D. HTTP method

Correct answer:

A. Query parameter

Explanation:

Query parameters come after `?` in the URL and usually filter or modify the request.

Common trap:

Thinking query parameters are JSON body fields.

## MCQ 9: FastAPI app object

Question:

What does this line create?

```python
app = FastAPI()
```

Options:

A. A FastAPI application object  
B. A database table  
C. A Docker container  
D. A Git repository

Correct answer:

A. A FastAPI application object

Explanation:

`FastAPI()` creates the main application object. Uvicorn runs this object.

Common trap:

Thinking `app` is a reserved keyword. It is just a variable name, but `app` is commonly used.

## MCQ 10: Route decorator

Question:

What does this decorator do?

```python
@app.get("/health")
```

Options:

A. Registers a GET endpoint at `/health`  
B. Creates a Python class  
C. Installs FastAPI  
D. Starts Docker

Correct answer:

A. Registers a GET endpoint at `/health`

Explanation:

The decorator tells FastAPI to call the function below it when a GET request arrives at `/health`.

Common trap:

Thinking the decorator runs the server. Uvicorn runs the server; the decorator registers the route.

## MCQ 11: Request body model

Question:

Why use a Pydantic model in FastAPI request body?

Options:

A. To validate incoming JSON shape  
B. To create a Git commit  
C. To build a Docker image  
D. To replace HTTP

Correct answer:

A. To validate incoming JSON shape

Explanation:

Pydantic checks required fields and types before your endpoint logic runs.

Common trap:

Thinking Pydantic is only documentation. It performs runtime validation.

## MCQ 12: Swagger UI

Question:

What is FastAPI Swagger UI used for?

Options:

A. Interactive API documentation and testing  
B. Python package installation  
C. Git conflict resolution  
D. Kubernetes scaling

Correct answer:

A. Interactive API documentation and testing

Explanation:

FastAPI automatically provides docs where you can inspect and test endpoints.

Common trap:

Thinking Swagger UI is the backend itself. It is documentation and testing UI around the API.
