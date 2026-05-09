from fastapi import FastAPI

from backend.models import AskRequest, TestCaseRequest, TestCaseResponse
from graph.workflow import run_workflow
from rag.rag_service import retrieve_context


app = FastAPI(title="AI QA Knowledge Assistant")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/ask")
def ask(request: AskRequest) -> dict:
    context = retrieve_context(request.question)
    return {
        "question": request.question,
        "answer": f"Mock answer based on context: {' '.join(context)}",
        "context_used": context,
    }


@app.post("/generate-test-cases", response_model=TestCaseResponse)
def generate_test_cases(request: TestCaseRequest) -> dict:
    result = run_workflow(request.requirement)
    return {
        "requirement": request.requirement,
        "test_cases": result["test_cases"],
        "context_used": result["context"],
        "mode": "mock",
    }

