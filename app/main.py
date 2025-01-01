from fastapi import FastAPI
from app.routers import task, user
from app.backend.db import engine
from app.models import Base

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)

Base.metadata.create_all(bind=engine)
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""