from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.task_schema import TaskCreate
from app.controllers.task_controller import create_task, delete_task, get_tasks, update_task_status
from typing import Optional
from fastapi import HTTPException
from app.utils.dependency import get_current_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE TASK
@router.post("/tasks")
def create_new_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    new_task = create_task(db, task.title, task.description)
    return {
        "success": True,
        "data": {
            "id": new_task.id,
            "title": new_task.title,
            "description": new_task.description,
            "status": new_task.status
        }
    }

# GET TASKS
@router.get("/tasks")
def get_all_tasks(
    status: Optional[str] = None,
    search: Optional[str] = None,
    page: int = 1,
    limit: int = 5,
    sort: str = "desc",
    db: Session = Depends(get_db),
    user = Depends(get_current_user)   
):
    tasks = get_tasks(db, status, search, page, limit, sort)

    return {
        "success": True,
        "count": len(tasks),
        "data": [
            {
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "status": t.status,
                "created_at": t.created_at
            }
            for t in tasks
        ]
    }

# UPDATE STATUS
@router.patch("/tasks/{task_id}/status")
def update_status(
    task_id: int,
    status: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)  
):
    updated_task = update_task_status(db, task_id, status)

    return {
        "success": True,
        "message": "Task status updated successfully",
        "data": {
            "id": updated_task.id,
            "status": updated_task.status
        }
    }

#  DELETE TASK
@router.delete("/tasks/{task_id}")
def delete_task_api(
    task_id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)   
):
    result = delete_task(db, task_id)

    return {
        "success": True,
        "message": result["message"]
    }