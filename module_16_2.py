from fastapi import FastAPI, Path
from typing import Annotated
from pydantic import conint, constr

app = FastAPI()

# Маршрут к главной странице
@app.get("/")
def home():
    return "Главная страница"

# Маршрут к странице администратора
@app.get("/user/admin")
def admin_page():
    return "Вы вошли как администратор"

# Маршрут к странице пользователя с параметром user_id в пути, валидация с Path
@app.get("/user/{user_id}")
def user_page(
    user_id: Annotated[int, Path(title="Enter User ID", description="Must be an integer between 1 and 100", ge=1, le=100)]
):
    return f"Вы вошли как пользователь № {user_id}"


# Маршрут к странице пользователя с параметрами username и age в пути, валидация с Annotated
@app.get("/user/{username}/{age}")
def user_info(
    username: Annotated[str, Path(title="Enter username", description="Must be a string between 5 and 20 characters long", min_length=5, max_length=20)],
    age: Annotated[int, Path(title="Enter age", description="Must be an integer between 18 and 120", ge=18, le=120)]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)