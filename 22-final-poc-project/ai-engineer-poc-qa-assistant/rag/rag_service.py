from pathlib import Path


def load_notes(path: str | None = None) -> str:
    notes_path = Path(path) if path else Path(__file__).parents[1] / "data" / "requirements_notes.txt"
    return notes_path.read_text(encoding="utf-8")


def chunk_text(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return lines


def retrieve_context(query: str, max_chunks: int = 3) -> list[str]:
    text = load_notes()
    chunks = chunk_text(text)
    words = [word.lower() for word in query.split()]
    matches = []
    for chunk in chunks:
        if any(word in chunk.lower() for word in words):
            matches.append(chunk)
    return matches[:max_chunks] or chunks[:max_chunks]
