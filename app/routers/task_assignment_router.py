from fastapi import APIRouter, Form
from typing import Optional
from app.services import task_assignment_service
from app.domain.task_assignment_domain import AssignmentCreate, AssignmentUpdate

router = APIRouter(prefix="/assignments", tags=["Assignments"])


@router.post("/")
async def create_assignment(
    task_id: int                  = Form(...),
    worker_id: int                = Form(...),
    allocated_hours: int          = Form(...),
    assigned_date: str            = Form(...),
    status: str                   = Form("pending"),
):
    data = AssignmentCreate(
        task_id=task_id,
        worker_id=worker_id,
        allocated_hours=allocated_hours,
        assigned_date=assigned_date,
        status=status,
    )
    return await task_assignment_service.create_assignment(data)


@router.get("/")
async def list_assignments():
    """All assignments with full worker, task and project details."""
    return await task_assignment_service.get_assignments()


@router.get("/status/{status}")
async def list_assignments_by_status(status: str):
    return await task_assignment_service.get_assignments_by_status(status)


@router.get("/task/{task_id}")
async def list_assignments_by_task(task_id: int):
    return await task_assignment_service.get_assignments_by_task(task_id)


@router.get("/worker/{worker_id}")
async def list_assignments_by_worker(worker_id: int):
    return await task_assignment_service.get_assignments_by_worker(worker_id)


@router.get("/{assignment_id}")
async def get_assignment(assignment_id: int):
    return await task_assignment_service.get_assignment(assignment_id)


@router.patch("/{assignment_id}")
async def update_assignment(
    assignment_id: int,
    allocated_hours: Optional[int] = Form(None),
    assigned_date: Optional[str]   = Form(None),
    status: Optional[str]          = Form(None),
):
    data = AssignmentUpdate(
        allocated_hours=allocated_hours,
        assigned_date=assigned_date,
        status=status,
    )
    return await task_assignment_service.update_assignment(assignment_id, data)


@router.patch("/{assignment_id}/status")
async def update_assignment_status(assignment_id: int, status: str = Form(...)):
    return await task_assignment_service.update_assignment_status(assignment_id, status)


@router.delete("/{assignment_id}")
async def delete_assignment(assignment_id: int):
    return await task_assignment_service.delete_assignment(assignment_id)