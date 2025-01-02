from pydantic import BaseModel
from typing import Optional


class Task(BaseModel):
    id: int
    title: str
    content: str
    priority: int
    completed: bool
    user_id: int
    slug: str


class TaskCreate(BaseModel):
    title: str
    content: str
    priority: int = 0
    user_id: int


class TaskUpdate(BaseModel):
    id: int
    title: Optional[str] = None
    content: Optional[str] = None
    priority: Optional[int] = None
    completed: Optional[bool] = None
    user_id: Optional[int] = None
    slug: Optional[str] = None


class User(BaseModel):
    id: int
    username: str
    firstname: str
    lastname: str
    age: int
    slug: str
    is_active: bool


class UserCreate(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


class UserUpdate(BaseModel):
    id: int
    username: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = None
    is_active: Optional[bool] = None