from pathlib import Path


def load_text(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def chunk_text(text: str, chunk_size: int = 160) -> list[str]:
    return [text[index:index + chunk_size] for index in range(0, len(text), chunk_size)]


def retrieve(question: str, chunks: list[str]) -> list[str]:
    words = [word.lower() for word in question.split()]
    matches = []
    for chunk in chunks:
        chunk_lower = chunk.lower()
        if any(word in chunk_lower for word in words):
            matches.append(chunk)
    return matches[:3]

