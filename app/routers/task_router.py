from fastapi import APIRouter, Form
from typing import Optional
from app.services import task_service
from app.domain.task_domain import TaskCreate

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# ── Tasks ─────────────────────────────────────────────────────────────────────

@router.post("/")
async def create_task(
    title: str           = Form(...),
    description: str     = Form(...),
    status: str          = Form(...),
    priority: str        = Form(...),
    task_type: str       = Form("GENERAL"),
    estimated_hours: int = Form(...),
    project_id: Optional[int] = Form(None),
    start_date: Optional[str] = Form(None),
    end_date:   Optional[str] = Form(None),
):
    data = TaskCreate(
        title=title,
        description=description,
        status=status,
        priority=priority,
        task_type=task_type,
        estimated_hours=estimated_hours,
        project_id=project_id,
        start_date=start_date,
        end_date=end_date,
    )
    return await task_service.create_task(data)


@router.get("/")
async def list_tasks():
    return await task_service.get_tasks()


@router.get("/status/{status}")
async def list_tasks_by_status(status: str):
    return await task_service.get_tasks_by_status(status)


@router.get("/project/{project_id}")
async def list_tasks_by_project(project_id: int):
    return await task_service.get_tasks_by_project(project_id)


@router.get("/{task_id}")
async def get_task(task_id: int):
    return await task_service.get_task(task_id)


@router.patch("/{task_id}/status")
async def update_task_status(task_id: int, status: str = Form(...)):
    return await task_service.update_task_status(task_id, status)