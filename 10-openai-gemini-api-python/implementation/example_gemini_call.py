import os


def call_gemini_example(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY not found. Use mock mode."
    return "Install Gemini SDK and replace this placeholder with real provider call."


if __name__ == "__main__":
    print(call_gemini_example("Explain RAG"))

