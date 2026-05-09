def extract_answer(response: dict) -> str:
    try:
        return response["data"]["answer"]
    except KeyError:
        return "No answer found in response"


if __name__ == "__main__":
    sample_response = {
        "status": "success",
        "data": {"answer": "Validate input before calling the model."},
    }

    print(extract_answer(sample_response))

