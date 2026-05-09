# Streamlit Exercises

## Exercise 1: Explain Streamlit role

Task:

Explain Streamlit vs FastAPI in the POC.

Expected answer:

Streamlit provides quick demo UI. FastAPI provides backend API endpoints and business logic.

Self-check:

Should API validation live only in Streamlit?

Common mistake:

Putting all backend logic into the UI.

## Exercise 2: Run the UI

Task:

Run:

```powershell
streamlit run app.py
```

Expected output:

Streamlit shows a local URL such as `http://localhost:8501`.

Hint:

Run from the folder containing `app.py`.

Common mistake:

Running from the wrong folder.

## Exercise 3: Backend not running

Task:

Explain what happens if the UI calls FastAPI but backend is stopped.

Expected answer:

The request fails. The UI should show a clear error such as "Backend is not running."

Common mistake:

Assuming Streamlit automatically starts FastAPI.
