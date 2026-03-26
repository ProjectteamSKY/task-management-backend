from fastapi import APIRouter, Form
from typing import Optional
from app.services import worker_service
from app.domain.worker_domain import WorkerCreate

router = APIRouter(prefix="/workers", tags=["Workers"])


@router.post("/")
async def create_worker(
    name: str                     = Form(...),
    email: str                    = Form(...),
    role: str                     = Form(...),
    department: str               = Form(...),
    status: str                   = Form(...),
    avatar: Optional[str]         = Form(None),
    daily_capacity_hours: int     = Form(...),
):
    data = WorkerCreate(
        name=name,
        email=email,
        role=role,
        department=department,
        status=status,
        avatar=avatar,
        daily_capacity_hours=daily_capacity_hours,
    )
    return await worker_service.create_worker(data)


@router.get("/")
async def list_workers():
    return await worker_service.get_workers()


@router.get("/with-tasks")
async def list_workers_with_tasks():
    """Returns each worker with their assignment counts and total allocated hours."""
    return await worker_service.get_workers_with_tasks()


@router.get("/department/{department}")
async def list_workers_by_department(department: str):
    return await worker_service.get_workers_by_department(department)


@router.get("/{worker_id}")
async def get_worker(worker_id: int):
    return await worker_service.get_worker(worker_id)


@router.get("/{worker_id}/assignments")
async def get_worker_assignments(worker_id: int):
    """All task assignments for a worker, with task & project details."""
    from app.services import task_service
    return await task_service.get_assignments_by_worker(worker_id)


@router.patch("/{worker_id}/status")
async def update_worker_status(worker_id: int, status: str = Form(...)):
    return await worker_service.update_worker_status(worker_id, status)