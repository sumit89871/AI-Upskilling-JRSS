from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="FastAPI AI Helper API")


class TextRequest(BaseModel):
    text: str


class RequirementRequest(BaseModel):
    requirement: str


class ContextQuestionRequest(BaseModel):
    question: str
    context: str


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/summarize")
def summarize(request: TextRequest) -> dict:
    summary = request.text[:120]
    return {"summary": summary, "mode": "mock"}


@app.post("/generate-test-case")
def generate_test_case(request: RequirementRequest) -> dict:
    return {
        "requirement": request.requirement,
        "test_cases": [
            {"title": "Valid scenario", "expected_result": "System accepts valid input"},
            {"title": "Invalid scenario", "expected_result": "System rejects invalid input"},
        ],
        "mode": "mock",
    }


@app.post("/ask-context")
def ask_context(request: ContextQuestionRequest) -> dict:
    return {
        "question": request.question,
        "answer": f"Mock answer based on provided context: {request.context[:80]}",
    }

