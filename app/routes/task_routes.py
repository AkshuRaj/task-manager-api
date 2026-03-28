from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import SessionLocal
from app.schemas.task_schema import TaskCreate
from app.controllers.task_controller import create_task

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks")
def create_new_task(task: TaskCreate, db: Session = Depends(get_db)):
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