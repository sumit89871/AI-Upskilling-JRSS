from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int


user = User.model_validate({"name": "Asha", "age": 30})

print(user.name)
print(user.age)
print(user.model_dump())

