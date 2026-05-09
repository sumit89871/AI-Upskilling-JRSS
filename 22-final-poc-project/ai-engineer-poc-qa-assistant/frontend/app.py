import os

import requests
import streamlit as st


BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

st.title("AI QA Knowledge Assistant")

tab_ask, tab_tests = st.tabs(["Ask Knowledge Base", "Generate Test Cases"])

with tab_ask:
    question = st.text_area("Question")
    if st.button("Ask"):
        response = requests.post(f"{BACKEND_URL}/ask", json={"question": question}, timeout=10)
        st.json(response.json())

with tab_tests:
    requirement = st.text_area("Requirement")
    if st.button("Generate"):
        response = requests.post(
            f"{BACKEND_URL}/generate-test-cases",
            json={"requirement": requirement},
            timeout=10,
        )
        st.json(response.json())

