class MockLLM:
    def answer(self, question: str, context: str) -> str:
        return f"Mock answer for '{question}' using context: {context[:120]}"

