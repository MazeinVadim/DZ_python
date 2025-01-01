from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas import Task, TaskCreate, TaskUpdate
from app.models import Task as TaskModel
from app.backend.db_depends import get_db
from sqlalchemy.orm import Session
from typing import Annotated

router = APIRouter(prefix="/task", tags=["task"])

@router.get("/", response_model=List[Task])
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.query(TaskModel).all()
    return tasks

@router.get("/{task_id}", response_model=Task)
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/create", response_model=Task, status_code=201)
async def create_task(task_data: TaskCreate, db: Annotated[Session, Depends(get_db)]):
    new_task = TaskModel(**task_data.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.put("/update/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: TaskUpdate, db: Annotated[Session, Depends(get_db)]):
    task = db.query(TaskModel).get(task_id)
    if not task:
         raise HTTPException(status_code=404, detail="Task not found")

    for key, value in updated_task.model_dump(exclude_unset=True).items():
          setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.query(TaskModel).get(task_id)
    if not task:
         raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": f"Task with id {task_id} has been deleted"}