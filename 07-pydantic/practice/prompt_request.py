from pydantic import BaseModel, Field, ValidationError


class PromptRequest(BaseModel):
    prompt: str = Field(min_length=1)
    model: str = "mock-llm"
    temperature: float = 0.2
    max_tokens: int = 300


valid_request = PromptRequest.model_validate({
    "prompt": "Generate test cases for login"
})

print(valid_request.model_dump())

try:
    PromptRequest.model_validate({"prompt": ""})
except ValidationError as error:
    print("Validation failed")
    print(error)

