from fastapi import FastAPI

# Создание объекта FastAPI
app = FastAPI()

# Создание маршрута к главной странице "/"
@app.get("/")
def home():
    return "Главная страница"

# Создание маршрута к странице администратора "/user/admin"
@app.get("/user/admin")
def admin_page():
    return "Вы вошли как администратор"

# Маршрут к странице пользователя с параметром user_id
@app.get("/user/{user_id}")
def user_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

# Маршрут к странице пользователя с параметрами username и age в адресной строке
@app.get("/user")
def user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
