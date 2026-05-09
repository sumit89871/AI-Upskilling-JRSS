from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=1)


class TestCaseRequest(BaseModel):
    requirement: str = Field(min_length=1)


class TestCase(BaseModel):
    title: str
    type: str
    priority: str
    expected_result: str


class TestCaseResponse(BaseModel):
    requirement: str
    test_cases: list[TestCase]
    context_used: list[str]
    mode: str = "mock"

