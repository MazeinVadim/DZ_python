from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from app.schemas import Task, TaskCreate, TaskUpdate
from app.models import Task as TaskModel, User as UserModel
from app.backend.db_depends import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete
from typing import Annotated
from slugify import slugify
import logging
import sqlite3

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/", response_model=List[Task])
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
   logger.info(f"Executing all_tasks")
   try:
        stmt = select(TaskModel)
        tasks = db.execute(stmt).scalars().all()
        return tasks
   except sqlite3.OperationalError as e:
        logger.exception(f"Database error during fetching tasks: {e}")
        raise HTTPException(status_code=500, detail="Database error while fetching tasks")


@router.get("/{task_id}", response_model=Task)
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
   logger.info(f"Executing task_by_id, task_id: {task_id}")
   try:
        stmt = select(TaskModel).where(TaskModel.id == task_id)
        task = db.execute(stmt).scalar_one_or_none()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task
   except sqlite3.OperationalError as e:
        logger.exception(f"Database error during fetching task with id: {task_id}, error {e}")
        raise HTTPException(status_code=500, detail="Database error while fetching task by id")


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate, db: Annotated[Session, Depends(get_db)]):
    logger.info(f"Entering create_task with {task_data}")
    try:
        user_id = task_data.user_id
        logger.info(f"User_id is: {user_id}")
        stmt = select(UserModel).where(UserModel.id == user_id)
        user = db.execute(stmt).scalar_one_or_none()
        if not user:
            logger.error(f"User with id {user_id} was not found")
            raise HTTPException(status_code=404, detail="User was not found")
        slug = slugify(task_data.title)
        logger.info(f"Slug for the task is: {slug}")
        stmt = insert(TaskModel).values(**task_data.model_dump(exclude={"user_id"}), user_id=user_id, slug=slug)
        logger.info(f"Insert statement is: {stmt}")
        db.execute(stmt)
        logger.info(f"Successfully executed insert")
        db.commit()
        logger.info(f"Transaction was successfully committed")
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    except sqlite3.OperationalError as e:
        logger.exception(f"Database error during task creation: {e}")
        raise HTTPException(status_code=500, detail="Database error during task creation.")



@router.put("/update/{task_id}",  status_code=status.HTTP_200_OK)
async def update_task(task_id: int, updated_task: TaskUpdate, db: Annotated[Session, Depends(get_db)]):
   logger.info(f"Updating task with id: {task_id} with values: {updated_task}")
   try:
        stmt = select(TaskModel).where(TaskModel.id == task_id)
        task = db.execute(stmt).scalar_one_or_none()
        if not task:
          raise HTTPException(status_code=404, detail="Task not found")

        stmt = update(TaskModel).where(TaskModel.id == task_id).values(**updated_task.model_dump(exclude_unset=True))
        db.execute(stmt)
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}
   except sqlite3.OperationalError as e:
        logger.exception(f"Database error during task update: {e}")
        raise HTTPException(status_code=500, detail="Database error during task update.")


@router.delete("/delete/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    logger.info(f"Deleting task with id: {task_id}")
    try:
        stmt = select(TaskModel).where(TaskModel.id == task_id)
        task = db.execute(stmt).scalar_one_or_none()
        if not task:
           raise HTTPException(status_code=404, detail="Task not found")

        stmt = delete(TaskModel).where(TaskModel.id == task_id)
        db.execute(stmt)
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task deletion is successful!'}
    except sqlite3.OperationalError as e:
        logger.exception(f"Database error during deleting task with id: {task_id}, error {e}")
        raise HTTPException(status_code=500, detail="Database error while deleting a task.")