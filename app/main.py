from fastapi import FastAPI
from app.database.connection import engine, Base
from app.models import task, user
from app.routes.task_routes import router as task_router
from fastapi.responses import JSONResponse
from fastapi import Request
from app.routes.auth_routes import router as auth_router

app = FastAPI()

app.include_router(auth_router)
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
    
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal server error",
            "error": str(exc)
        }
    )