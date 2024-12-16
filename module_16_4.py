from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi import Path
from typing import Annotated

app = FastAPI()

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Имитация базы данных
users: List[User] = []

# GET запрос по маршруту '/users'
@app.get("/users")
def get_users() -> List[User]:
    return users

# POST запрос по маршруту '/user/{username}/{age}'
@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(title="Enter username", description="Must be a string")],
    age: Annotated[int, Path(title="Enter age", description="Must be an integer")]
) -> User:
    user_id = 1 if not users else users[-1].id + 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user

# PUT запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[int, Path(title="Enter User ID", description="Must be an integer")],
    username: Annotated[str, Path(title="Enter username", description="Must be a string")],
    age: Annotated[int, Path(title="Enter age", description="Must be an integer")]
) -> User:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# DELETE запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(title="Enter User ID", description="Must be an integer")]) -> User:
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)