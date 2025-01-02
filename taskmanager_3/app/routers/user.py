from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from app.schemas import User, UserCreate, UserUpdate, Task
from app.models import User as UserModel, Task as TaskModel
from app.backend.db_depends import get_db
from sqlalchemy.orm import Session
from slugify import slugify
from sqlalchemy import select, insert, update, delete
from typing import Annotated
import logging
import sqlite3

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[User])
async def all_users(db: Annotated[Session, Depends(get_db)]):
    logger.info(f"Getting all users")
    try:
        stmt = select(UserModel)
        users = db.execute(stmt).scalars().all()
        return users
    except sqlite3.OperationalError as e:
         logger.exception(f"Database error during fetching all users: {e}")
         raise HTTPException(status_code=500, detail="Database error while fetching all users")

@router.get("/{user_id}", response_model=User)
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    logger.info(f"Getting user by id: {user_id}")
    try:
        stmt = select(UserModel).where(UserModel.id == user_id)
        user = db.execute(stmt).scalar_one_or_none()
        if user is not None:
            return user
        else:
            raise HTTPException(status_code=404, detail="User was not found")
    except sqlite3.OperationalError as e:
          logger.exception(f"Database error during fetching user with id {user_id}: {e}")
          raise HTTPException(status_code=500, detail="Database error while fetching user by id")


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreate, db: Annotated[Session, Depends(get_db)]):
    logger.info(f"Creating new user with data: {user_data}")
    try:
        slug = UserModel.create_slug(user_data.firstname + ' ' + user_data.lastname)
        existing_user = db.query(UserModel).filter(UserModel.slug == slug).first()
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
        stmt = insert(UserModel).values(**user_data.model_dump(), slug=slug)
        db.execute(stmt)
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    except sqlite3.OperationalError as e:
          logger.exception(f"Database error during creation of user: {user_data}, error: {e}")
          raise HTTPException(status_code=500, detail="Database error while creating a user")


@router.put("/update/{user_id}",  status_code=status.HTTP_200_OK)
async def update_user(user_id: int, updated_user: UserUpdate, db: Annotated[Session, Depends(get_db)]):
    logger.info(f"Updating user with id: {user_id} and data: {updated_user}")
    try:
        stmt = select(UserModel).where(UserModel.id == user_id)
        user = db.execute(stmt).scalar_one_or_none()
        if user is None:
          raise HTTPException(status_code=404, detail="User was not found")
        stmt = update(UserModel).where(UserModel.id == user_id).values(**updated_user.model_dump(exclude_unset=True))
        db.execute(stmt)
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
    except sqlite3.OperationalError as e:
         logger.exception(f"Database error while updating user with id {user_id} and data {updated_user}, error: {e}")
         raise HTTPException(status_code=500, detail="Database error while updating the user")


@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    logger.info(f"Deleting user with id: {user_id}")
    try:
        stmt = select(UserModel).where(UserModel.id == user_id)
        user = db.execute(stmt).scalar_one_or_none()
        if user is None:
            raise HTTPException(status_code=404, detail="User was not found")
        # Delete all tasks associated with the user
        stmt = delete(TaskModel).where(TaskModel.user_id == user_id)
        db.execute(stmt)
        # Delete the user
        stmt = delete(UserModel).where(UserModel.id == user_id)
        db.execute(stmt)
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'User deletion is successful!'}
    except sqlite3.OperationalError as e:
        logger.exception(f"Database error while deleting a user with id {user_id}: {e}")
        raise HTTPException(status_code=500, detail="Database error while deleting a user")


@router.get("/{user_id}/tasks", response_model=List[Task])
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    logger.info(f"Getting tasks for user id: {user_id}")
    try:
        stmt = select(TaskModel).where(TaskModel.user_id == user_id)
        tasks = db.execute(stmt).scalars().all()
        return tasks
    except sqlite3.OperationalError as e:
        logger.exception(f"Database error while fetching tasks for user with id: {user_id}")
        raise HTTPException(status_code=500, detail="Database error while fetching tasks for specific user")