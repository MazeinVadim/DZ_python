from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.schemas import Task, TaskCreate, TaskUpdate
from app.models import task as task_model
from app.backend.db import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/", response_model=List[Task])
async def all_tasks(db: Session = Depends(get_db)):
    tasks = db.query(task_model.Task).all()
    return tasks


@router.get("/{task_id}", response_model=Task)
async def task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/create", response_model=Task, status_code=201)
async def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    new_task = task_model.Task(**task_data.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


@router.put("/update", response_model=Task)
async def update_task(updated_task: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(task_model.Task).filter(task_model.Task.id == updated_task.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in updated_task.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": f"Task with id {task_id} has been deleted"}