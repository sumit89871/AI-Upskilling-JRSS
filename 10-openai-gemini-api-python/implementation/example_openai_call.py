import os


def call_openai_example(prompt: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "OPENAI_API_KEY not found. Use mock mode."
    return "Install OpenAI SDK and replace this placeholder with real provider call."


if __name__ == "__main__":
    print(call_openai_example("Explain FastAPI"))

