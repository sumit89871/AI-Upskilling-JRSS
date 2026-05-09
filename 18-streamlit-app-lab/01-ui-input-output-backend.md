# UI Input, Output, And Backend Calls

## 1. What It Is

Streamlit collects user input, calls Python logic or a backend API, and displays output.

## 2. Why It Matters

In a POC, the frontend should not contain all business logic. It can call a FastAPI backend.

## 3. How It Works

```text
User enters requirement -> Streamlit button -> call backend/mock function -> display test cases
```

## 4. How I Use It

Mock function:

```python
def generate_test_cases(requirement: str) -> list[str]:
    return [
        f"Valid scenario for {requirement}",
        f"Invalid scenario for {requirement}",
    ]
```

Backend call:

```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/generate-test-case",
    json={"requirement": requirement},
    timeout=10,
)
```

## 5. Syntax Breakdown

- `requests.post` sends an HTTP POST request.
- `json={...}` sends a JSON body.
- `timeout=10` prevents waiting forever.
- `response.json()` converts JSON response into a Python dictionary.

## 6. Small Examples

```python
if st.button("Generate") and requirement:
    test_cases = generate_test_cases(requirement)
    st.json(test_cases)
```

## 7. Expected Output

The app shows test cases after the button click.

## 8. Quick Practice

Add one more input for priority: `P1`, `P2`, or `P3`.

## 9. Common Mistakes

- Backend not running before UI call.
- Wrong endpoint URL.
- Missing `requests` package.
- No error message when backend fails.

## 10. Where Used

Streamlit frontend for final POC and AI demos.

## 11. Beginner Deep Dive

Streamlit is useful for quick AI demos because it turns Python code into a simple web UI.

Beginner mental model:

```text
widget input -> Python variable -> button click -> backend/mock call -> displayed output
```

Streamlit reruns the script when users interact with widgets. This is normal and can surprise beginners.

What the developer creates manually:

- UI widgets such as text areas and buttons
- backend URL
- request payload
- response display logic
- error messages

What Streamlit gives automatically:

- browser page rendering
- widget state handling
- local development server

Common beginner confusion:

- Streamlit is not the backend API.
- `st.button()` does not do work by itself; your code inside the `if` block does the work.
- FastAPI must be running separately if Streamlit calls a backend endpoint.
- Demo UI should not contain hardcoded API keys.

Where this appears in AI Engineer work:

- final POC frontend
- stakeholder demos
- AI test case generator UI
- quick local labs
