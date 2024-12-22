from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Task, TaskCreate, TaskUpdate

router = APIRouter(prefix="/task", tags=["task"])


tasks_db: List[Task] = []
task_id_counter = 1


@router.get("/", response_model=List[Task])
async def all_tasks():
    return tasks_db


@router.get("/{task_id}", response_model=Task)
async def task_by_id(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.post("/create", response_model=Task, status_code=201)
async def create_task(task_data: TaskCreate):
    global task_id_counter
    new_task = Task(id=task_id_counter, **task_data.model_dump())
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task


@router.put("/update", response_model=Task)
async def update_task(updated_task: TaskUpdate):
    for i, task in enumerate(tasks_db):
        if task.id == updated_task.id:
            if updated_task.title:
              tasks_db[i].title = updated_task.title
            if updated_task.description:
              tasks_db[i].description = updated_task.description
            if updated_task.completed is not None:
              tasks_db[i].completed = updated_task.completed
            return tasks_db[i]
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/delete/{task_id}")
async def delete_task(task_id: int):
    global tasks_db
    tasks_db = [task for task in tasks_db if task.id != task_id]
    return {"message": f"Task with id {task_id} has been deleted"}