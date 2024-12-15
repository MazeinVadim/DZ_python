from fastapi import FastAPI, HTTPException
from typing import Annotated
from fastapi import Path

app = FastAPI()

# Имитация базы данных (словарь)
users = {"1": "Имя: Example, возраст: 18"}

# GET запрос по маршруту '/users'
@app.get("/users")
def get_users():
    return users

# POST запрос по маршруту '/user/{username}/{age}'
@app.post("/user/{username}/{age}")
def create_user(
    username: Annotated[str, Path(title="Enter username", description="Must be a string")],
    age: Annotated[int, Path(title="Enter age", description="Must be an integer")]
):
    user_id = str(max([int(k) for k in users.keys()], default=0) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

# PUT запрос по маршруту '/user/{user_id}/{username}/{age}'
@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: Annotated[int, Path(title="Enter User ID", description="Must be an integer")],
    username: Annotated[str, Path(title="Enter username", description="Must be a string")],
    age: Annotated[int, Path(title="Enter age", description="Must be an integer")],
):
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    users[user_id_str] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

# DELETE запрос по маршруту '/user/{user_id}'
@app.delete("/user/{user_id}")
def delete_user(user_id: Annotated[int, Path(title="Enter User ID", description="Must be an integer")]):
    user_id_str = str(user_id)
    if user_id_str not in users:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")
    del users[user_id_str]
    return f"User {user_id} has been deleted"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)