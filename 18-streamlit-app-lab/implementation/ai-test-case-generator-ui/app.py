import streamlit as st


def generate_mock_test_cases(requirement: str) -> list[dict]:
    return [
        {
            "title": "Valid scenario",
            "type": "positive",
            "expected_result": f"System handles valid input for: {requirement}",
        },
        {
            "title": "Invalid scenario",
            "type": "negative",
            "expected_result": "System shows a clear validation error",
        },
    ]


st.title("AI Test Case Generator")
st.write("Mock-first demo. No API key required.")

requirement = st.text_area("Enter requirement")

if st.button("Generate Test Cases"):
    if not requirement.strip():
        st.error("Enter a requirement first.")
    else:
        st.json(generate_mock_test_cases(requirement))

