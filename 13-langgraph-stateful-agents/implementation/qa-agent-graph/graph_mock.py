def analyze_requirement(state: dict) -> dict:
    state["analysis"] = f"Analyzed: {state['requirement']}"
    return state


def generate_scenarios(state: dict) -> dict:
    state["scenarios"] = ["valid case", "invalid case", "boundary case"]
    return state


def generate_api_tests(state: dict) -> dict:
    state["api_tests"] = ["check 200 response", "check 400 validation"]
    return state


def review(state: dict) -> dict:
    state["review"] = "Mock review passed"
    state["final"] = {
        "analysis": state["analysis"],
        "scenarios": state["scenarios"],
        "api_tests": state["api_tests"],
    }
    return state


def run_graph(requirement: str) -> dict:
    state = {"requirement": requirement}
    for node in [analyze_requirement, generate_scenarios, generate_api_tests, review]:
        state = node(state)
    return state


if __name__ == "__main__":
    result = run_graph("User can login")
    print(result["final"])

