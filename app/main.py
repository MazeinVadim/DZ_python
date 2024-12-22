from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)