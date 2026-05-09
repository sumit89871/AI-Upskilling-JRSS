def build_prompt(requirement: str) -> str:
    return f"Generate test cases for: {requirement}"


def is_success_status(code: int) -> bool:
    return code >= 200 and code < 300


if __name__ == "__main__":
    print(build_prompt("User can reset password"))
    print(is_success_status(200))
    print(is_success_status(404))

