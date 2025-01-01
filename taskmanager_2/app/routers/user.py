from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from app.schemas import User, UserCreate, UserUpdate
from app.models import User as UserModel
from app.backend.db_depends import get_db
from sqlalchemy.orm import Session
from slugify import slugify
from sqlalchemy import select, insert, update, delete
from typing import Annotated


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[User])
async def all_users(db: Annotated[Session, Depends(get_db)]):
    stmt = select(UserModel)
    users = db.execute(stmt).scalars().all()
    return users

@router.get("/{user_id}", response_model=User)
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = select(UserModel).where(UserModel.id == user_id)
    user = db.execute(stmt).scalar_one_or_none()
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=404, detail="User was not found")


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, db: Annotated[Session, Depends(get_db)]):
    slug = UserModel.create_slug(user_data.firstname + ' ' + user_data.lastname)
    existing_user = db.query(UserModel).filter(UserModel.slug == slug).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    stmt = insert(UserModel).values(**user_data.model_dump(), slug=slug)
    db.execute(stmt)
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update/{user_id}",  status_code=status.HTTP_200_OK)
async def update_user(user_id: int, updated_user: UserUpdate, db: Annotated[Session, Depends(get_db)]):
    stmt = select(UserModel).where(UserModel.id == user_id)
    user = db.execute(stmt).scalar_one_or_none()
    if user is None:
      raise HTTPException(status_code=404, detail="User was not found")
    stmt = update(UserModel).where(UserModel.id == user_id).values(**updated_user.model_dump(exclude_unset=True))
    db.execute(stmt)
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    stmt = select(UserModel).where(UserModel.id == user_id)
    user = db.execute(stmt).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    stmt = delete(UserModel).where(UserModel.id == user_id)
    db.execute(stmt)
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'User deletion is successful!'}