from pydantic import BaseModel


class TestCase(BaseModel):
    title: str
    type: str
    priority: str
    expected_result: str


class TestCaseResponse(BaseModel):
    requirement: str
    test_cases: list[TestCase]
    mode: str = "mock"


response = TestCaseResponse.model_validate({
    "requirement": "User can login",
    "test_cases": [
        {
            "title": "Valid login",
            "type": "positive",
            "priority": "P1",
            "expected_result": "Dashboard opens",
        }
    ],
})

print(response.test_cases[0].title)
print(response.model_dump())

