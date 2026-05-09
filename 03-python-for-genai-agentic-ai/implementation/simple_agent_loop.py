def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}


def build_prompt(requirement: str, user: dict) -> str:
    return (
        f"Generate positive and negative test cases for: {requirement}. "
        f"Use username {user['username']} for examples."
    )


def run_agent(requirement: str) -> dict:
    state = {
        "requirement": requirement,
        "steps": [],
        "tool_result": None,
        "final_prompt": None,
    }

    state["steps"].append("read_requirement")
    state["tool_result"] = get_test_user("qa")

    state["steps"].append("called_test_user_tool")
    state["final_prompt"] = build_prompt(requirement, state["tool_result"])

    state["steps"].append("built_prompt")
    return state


if __name__ == "__main__":
    result = run_agent("User can reset password")
    print(result["steps"])
    print(result["final_prompt"])

