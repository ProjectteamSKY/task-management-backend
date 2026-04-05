from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.db import init_db
from app.routers import (
    capability_router,
    project_router,
    schedule_router,
    task_assignment_router,
    task_router,
    worker_availability_router,
    worker_notes_router,
    worker_resources_router,
    worker_router,
    slack_router,
    leave_router,
)

app = FastAPI()

# ── Middleware ────────────────────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Lifecycle ─────────────────────────────────────────────────────────────────

@app.on_event("startup")
async def startup():
    await init_db()

# ── Routers ───────────────────────────────────────────────────────────────────

for router in [
    worker_router.router,
    task_router.router,
    schedule_router.router,
    project_router.router,
    task_assignment_router.router,
    capability_router.router,
    worker_availability_router.router,
    worker_notes_router.router,
    worker_resources_router.router,
    slack_router.router,
    leave_router.global_router,  
    leave_router.router,
]:
    app.include_router(router)