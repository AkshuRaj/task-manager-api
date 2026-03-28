from sqlalchemy.orm import Session
from app.models.task import Task
from fastapi import HTTPException

def create_task(db: Session, title: str, description: str):
    new_task = Task(
        title=title,
        description=description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

def get_tasks(db, status=None, search=None, page=1, limit=5):
    query = db.query(Task)

    #Filter by status
    if status:
        query = query.filter(Task.status == status)

    #Search in title
    if search:
        query = query.filter(Task.title.ilike(f"%{search}%"))

    #Pagination
    offset = (page - 1) * limit
    tasks = query.offset(offset).limit(limit).all()

    return tasks

def update_task_status(db, task_id: int, new_status: str):
    task = db.query(Task).filter(Task.id == task_id).first()

    #Task not found
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    valid_status = ["pending", "in_progress", "completed"]

    #Invalid status input
    if new_status not in valid_status:
        raise HTTPException(status_code=400, detail="Invalid status value")

    #transition logic
    if task.status == "pending" and new_status == "completed":
        raise HTTPException(status_code=400, detail="Cannot skip status directly to completed")

    if task.status == "completed":
        raise HTTPException(status_code=400, detail="Completed task cannot be modified")

    #Update
    task.status = new_status
    db.commit()
    db.refresh(task)

    return task

def delete_task(db, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    #Task not found
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}