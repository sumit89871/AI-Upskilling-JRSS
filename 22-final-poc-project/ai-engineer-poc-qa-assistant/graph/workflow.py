from mcp_tools.test_data_tools import get_api_test_data, get_test_user
from rag.rag_service import retrieve_context


def understand_query(state: dict) -> dict:
    state["steps"].append("understand_query")
    state["intent"] = "generate_test_cases"
    return state


def retrieve(state: dict) -> dict:
    state["steps"].append("retrieve_context")
    state["context"] = retrieve_context(state["requirement"])
    return state


def generate(state: dict) -> dict:
    state["steps"].append("generate")
    user = get_test_user("qa")
    api_data = get_api_test_data()
    state["test_cases"] = [
        {
            "title": "Valid requirement scenario",
            "type": "positive",
            "priority": "P1",
            "expected_result": f"System accepts valid input for {user['username']} with status {api_data['valid_status']}",
        },
        {
            "title": "Invalid requirement scenario",
            "type": "negative",
            "priority": "P2",
            "expected_result": f"System rejects invalid input with status {api_data['validation_error_status']}",
        },
    ]
    return state


def review(state: dict) -> dict:
    state["steps"].append("review")
    state["review_status"] = "mock_review_passed"
    return state


def run_workflow(requirement: str) -> dict:
    state = {"requirement": requirement, "steps": []}
    for node in [understand_query, retrieve, generate, review]:
        state = node(state)
    return state

