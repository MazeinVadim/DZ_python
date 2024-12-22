from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import User, UserCreate, UserUpdate

router = APIRouter(prefix="/user", tags=["user"])

users_db: List[User] = []
user_id_counter = 1


@router.get("/", response_model=List[User])
async def all_users():
    return users_db


@router.get("/{user_id}", response_model=User)
async def user_by_id(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.post("/create", response_model=User, status_code=201)
async def create_user(user_data: UserCreate):
    global user_id_counter
    new_user = User(id=user_id_counter, **user_data.model_dump())
    users_db.append(new_user)
    user_id_counter += 1
    return new_user


@router.put("/update", response_model=User)
async def update_user(updated_user: UserUpdate):
    for i, user in enumerate(users_db):
        if user.id == updated_user.id:
            if updated_user.username:
                users_db[i].username = updated_user.username
            if updated_user.email:
                users_db[i].email = updated_user.email
            if updated_user.full_name:
                users_db[i].full_name = updated_user.full_name
            if updated_user.is_active is not None:
              users_db[i].is_active = updated_user.is_active
            return users_db[i]
    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int):
    global users_db
    users_db = [user for user in users_db if user.id != user_id]
    return {"message": f"User with id {user_id} has been deleted"}