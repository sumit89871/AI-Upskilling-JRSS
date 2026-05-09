# Streamlit App Lab Overview

## 1. What it is

Streamlit is a Python framework for building simple web UIs quickly.

For AI Engineer demos, Streamlit is useful because you can create an interface without writing HTML, CSS, and JavaScript from scratch.

Typical demo:

```text
text input -> button -> call backend/mock LLM -> display result
```

## 2. The most important beginner idea

Streamlit is for demo UI, not the core backend.

A practical AI POC often separates responsibilities:

```text
Streamlit frontend -> FastAPI backend -> RAG/LLM/tools/workflow
```

Streamlit collects user input and displays results. FastAPI usually owns backend logic.

## 3. Why it matters

During a POC demo, users need to see the system working.

Streamlit helps show:

- requirement input
- generated test cases
- retrieved context
- API response output
- error messages
- mock vs real LLM behavior

It is especially useful for stand-and-deliver demos.

## 4. Beginner mental model

```text
Python script reruns -> widgets keep values -> button triggers action -> output appears on page
```

Important beginner point:

Streamlit reruns the script when a user interacts with widgets. This is normal.

## 5. Basic Streamlit example

File name: `app.py`

Example code:

```python
import streamlit as st

st.title("AI Test Case Generator")

requirement = st.text_area("Requirement")

if st.button("Generate"):
    st.write(f"Mock test cases for: {requirement}")
```

Syntax breakdown:

- `import streamlit as st` imports Streamlit and gives it the short name `st`.
- `st.title(...)` displays a page title.
- `st.text_area(...)` creates a multi-line text input.
- The returned value is stored in `requirement`.
- `st.button(...)` creates a button.
- `if st.button(...):` runs the block when the button is clicked.
- `st.write(...)` displays output on the page.

## 6. Run command

```powershell
streamlit run app.py
```

Command explanation:

- `streamlit` runs the Streamlit command-line tool.
- `run` tells Streamlit to start an app.
- `app.py` is the Python file containing the UI.

Expected output:

```text
Local URL: http://localhost:8501
```

How to verify:

Open the local URL in a browser. You should see the page title and input box.

## 7. Connecting to FastAPI

Frontend-backend flow:

```text
User types requirement in Streamlit
Streamlit sends HTTP request to FastAPI
FastAPI runs validation/workflow
FastAPI returns JSON
Streamlit displays JSON result
```

Beginner point:

Streamlit does not automatically know about FastAPI. You manually write Python code that calls the backend URL.

## 8. Similar concepts beginners confuse

### Streamlit vs FastAPI

Streamlit is mainly for UI.

FastAPI is mainly for backend APIs.

### Button click vs function call

The button does not generate output by itself. Your code inside the `if st.button(...)` block runs after click.

### Local app vs deployed app

Local app runs on your machine.

Deployed app runs on a server or platform for others to access.

## 9. Common mistakes

- Putting all business logic in Streamlit instead of backend modules.
- Forgetting that the script reruns after interactions.
- Calling a backend URL that is not running.
- Hardcoding API keys in UI code.
- Showing raw tracebacks to demo users.
- Not using mock mode before real LLM integration.

## 10. Where used in AI Engineer work

- POC demos
- AI test case generator UI
- RAG assistant UI
- stakeholder demos
- fast feedback during labs
- stand-and-deliver presentations
