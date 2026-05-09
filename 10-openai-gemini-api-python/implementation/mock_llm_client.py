class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return f"Mock LLM response for: {prompt}"

