from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.db import init_db
from app.routers import worker_router, task_router, schedule_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await init_db()

app.include_router(worker_router.router)
app.include_router(task_router.router)
app.include_router(schedule_router.router)