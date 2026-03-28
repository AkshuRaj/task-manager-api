from sqlalchemy.orm import Session
from app.models.task import Task

def create_task(db: Session, title: str, description: str):
    new_task = Task(
        title=title,
        description=description
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task