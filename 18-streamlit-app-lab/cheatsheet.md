# Streamlit Cheatsheet

## streamlit run

Command: `streamlit run app.py`

Meaning: Start the Streamlit app from `app.py`.

Use when: Running a local demo UI.

Example: Open `http://localhost:8501`.

Be careful: Run from the folder containing `app.py`.

## st.text_input

Meaning: Creates a text box.

Use when: User needs to enter a requirement or question.

Example: `requirement = st.text_input("Requirement")`

Be careful: Empty input should be handled.

## st.button

Meaning: Creates a clickable button.

Use when: Triggering generation or API call.

Example: `if st.button("Generate"):`

Be careful: Button click reruns the script.

## st.write

Meaning: Display text, dictionaries, tables, or output.

Use when: Showing generated test cases.

Be careful: Do not expose secrets in UI output.
