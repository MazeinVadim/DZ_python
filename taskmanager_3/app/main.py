import os
from fastapi import FastAPI
from app.routers import task, user
from app.models import Base
from app.backend.db import engine, get_db
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO) # Setup basic logging

app = FastAPI()
app.dependency_overrides[get_db] = get_db

app.include_router(task.router)
app.include_router(user.router)


try:
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error creating tables: {e}")
    exit(1)



@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager API"}