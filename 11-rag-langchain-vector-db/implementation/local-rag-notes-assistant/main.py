from mock_llm import MockLLM
from rag_pipeline import chunk_text, load_text, retrieve
from pathlib import Path


def main() -> None:
    question = "How should login be tested?"
    data_path = Path(__file__).parent / "data" / "notes.txt"
    text = load_text(str(data_path))
    chunks = chunk_text(text)
    retrieved = retrieve(question, chunks)
    context = "\n".join(retrieved)
    answer = MockLLM().answer(question, context)
    print(answer)


if __name__ == "__main__":
    main()
