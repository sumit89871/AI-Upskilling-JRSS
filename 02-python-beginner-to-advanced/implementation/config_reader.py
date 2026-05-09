import os


def read_config() -> dict:
    return {
        "app_env": os.getenv("APP_ENV", "local"),
        "use_mock_llm": os.getenv("USE_MOCK_LLM", "true").lower() == "true",
    }


if __name__ == "__main__":
    print(read_config())

