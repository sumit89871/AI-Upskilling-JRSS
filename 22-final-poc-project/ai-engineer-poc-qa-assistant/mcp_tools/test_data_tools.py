def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}


def get_api_test_data() -> dict:
    return {
        "valid_status": 200,
        "validation_error_status": 400,
        "auth_error_status": 401,
    }

