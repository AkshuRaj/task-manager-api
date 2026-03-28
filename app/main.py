from fastapi import FastAPI
from app.database.connection import engine

app = FastAPI()

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