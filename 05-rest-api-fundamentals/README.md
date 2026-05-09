# 05 REST API Fundamentals

## 1. What This Module Is

This module teaches REST API basics from beginner level.

An API is a way for two software systems to talk to each other. A REST API is a common web API style that uses HTTP methods, URLs, headers, request bodies, response bodies, and status codes.

In this course, REST API knowledge is required before FastAPI, OpenAI/Gemini API calls, Streamlit-to-backend calls, MCP client thinking, Docker health checks, and Kubernetes service checks.

## 2. Why It Matters

Most AI Engineer work is integration work.

You often need to connect:

- frontend UI to FastAPI backend
- FastAPI backend to LLM provider API
- backend to vector database API
- agent workflow to tool API
- Kubernetes health check to running app

If REST API basics are weak, FastAPI code looks like magic.

## 3. What The Learner Should Finish Knowing

After this module, you should be able to explain:

- client vs server
- HTTP
- URL
- endpoint
- resource
- request
- response
- headers
- path parameter
- query parameter
- request body
- response body
- JSON
- status codes
- `GET`, `POST`, `PUT`, `PATCH`, `DELETE`
- authentication basics
- bearer token
- `curl` commands
- API testing thinking

## 4. Study Order

1. `00-overview.md`
2. `01-request-response-methods.md`
3. `02-parameters-headers-auth-curl.md`
4. `exercises.md`
5. `cheatsheet.md`
6. `interview-questions.md`

## 5. File List

- `README.md`: module guide and learning outcomes.
- `00-overview.md`: what APIs are, REST mental model, client/server flow.
- `01-request-response-methods.md`: HTTP methods, JSON bodies, response status, expected output.
- `02-parameters-headers-auth-curl.md`: path/query parameters, headers, bearer token, curl syntax.
- `exercises.md`: hands-on request design and curl practice.
- `cheatsheet.md`: practical API command and concept reference.
- `interview-questions.md`: beginner, practical, scenario, and tricky REST API Q&A.

## 6. Practical Scope

This module does not build a FastAPI server yet. It prepares the vocabulary and mental model needed for FastAPI.

Examples use fake user and AI helper APIs so you can understand the structure before writing backend code.

## 7. What Not To Over-Focus On

Do not memorize every HTTP status code.

First understand the families:

- `2xx`: success
- `4xx`: client/request problem
- `5xx`: server problem

Also do not over-focus on REST theory debates. For this course, the goal is practical API usage.

## 8. How This Helps In AI Engineer JRSS / Mettl / POC / Interview

- **AI Engineer JRSS labs**: you can understand API examples quickly.
- **Mettl screening**: REST method, status code, and JSON questions are common.
- **POC demo**: you can explain how the UI calls the backend.
- **Interview**: you can explain request/response flow clearly instead of saying "API just connects things."

