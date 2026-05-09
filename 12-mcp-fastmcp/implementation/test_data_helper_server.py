def get_test_user(role: str) -> dict:
    return {"username": f"{role}_user", "password": "demo123"}


def get_test_card(card_type: str) -> dict:
    return {"card_type": card_type, "number": "4111111111111111"}

