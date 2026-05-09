import os

from mock_llm_client import MockLLMClient


def get_llm_client():
    use_mock = os.getenv("USE_MOCK_LLM", "true").lower() == "true"
    if use_mock:
        return MockLLMClient()
    return MockLLMClient()


if __name__ == "__main__":
    client = get_llm_client()
    print(client.generate("Generate test cases for login"))

