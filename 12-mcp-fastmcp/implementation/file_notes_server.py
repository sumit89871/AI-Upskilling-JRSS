from pathlib import Path


def read_note(file_path: str) -> str:
    safe_path = Path(file_path)
    if safe_path.is_absolute():
        return "Absolute paths are blocked in this beginner example."
    if not safe_path.exists():
        return "Note not found."
    return safe_path.read_text(encoding="utf-8")

