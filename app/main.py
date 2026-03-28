from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models import task
from app.routes.task_routes import router as task_router

app = FastAPI()

app.include_router(task_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Task Manager API is running"}


@app.get("/test-db")
def test_db():
    try:
        connection = engine.connect()
        connection.close()
        return {"message": "Database connected successfully"}
    except Exception as e:
        return {"error": str(e)}