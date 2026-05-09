# AI Test Case Generator UI

## Project goal

This mini project demonstrates a beginner Streamlit UI for generating AI-style test cases.

It should be understood as a demo frontend, not a production frontend.

## What Streamlit does here

Streamlit lets Python code create a quick browser UI.

Typical flow:

```text
User types requirement -> clicks button -> app shows generated/mock test cases
```

## How to run

Command:

```powershell
streamlit run app.py
```

Where to run:

Run this from:

```text
18-streamlit-app-lab/implementation/ai-test-case-generator-ui/
```

What each part means:

- `streamlit` runs the Streamlit CLI.
- `run` tells Streamlit to start an app.
- `app.py` is the Python file containing the UI.

Expected output:

Streamlit prints a local URL such as:

```text
Local URL: http://localhost:8501
```

Open that URL in a browser.

## Common errors

If Streamlit is not installed:

```text
streamlit is not recognized
```

Fix:

```powershell
pip install streamlit
```

If backend connection fails:

The UI may show an error or no generated result. Check whether the FastAPI backend is running and whether the backend URL is correct.

## What to explain in demo

Say:

```text
Streamlit is used only for quick demo UI. The real AI/backend logic should stay in FastAPI services so it can be tested, secured, and deployed independently.
```
