class MockLLMClient:
    def generate(self, prompt: str) -> str:
        return f"Mock response for: {prompt}"


if __name__ == "__main__":
    client = MockLLMClient()
    answer = client.generate("Explain RAG simply")
    print(answer)

