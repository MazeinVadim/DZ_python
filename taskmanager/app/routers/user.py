from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas import User, UserCreate, UserUpdate
from app.models import user as user_model
from app.backend.db import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[User])
async def all_users(db: Session = Depends(get_db)):
    users = db.query(user_model.User).all()
    return users

@router.get("/{user_id}", response_model=User)
async def user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/create", response_model=User, status_code=201)
async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    new_user = user_model.User(**user_data.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.put("/update", response_model=User)
async def update_user(updated_user: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == updated_user.id).first()
    if not user:
         raise HTTPException(status_code=404, detail="User not found")

    for key, value in updated_user.model_dump(exclude_unset=True).items():
          setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
         raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return {"message": f"User with id {user_id} has been deleted"}