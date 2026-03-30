from fastapi import APIRouter, Form
from typing import Optional
from app.services import task_assignment_service
from app.domain.task_assignment_domain import AssignmentCreate, AssignmentUpdate

router = APIRouter(prefix="/assignments", tags=["Assignments"])


@router.post("/")
async def create_assignment(
    task_id:         int = Form(...),
    worker_id:       int = Form(...),
    allocated_hours: int = Form(...),
    status:          str = Form("pending"),
    # Date range
    start_date:      str = Form(...),
    end_date:        str = Form(...),
    # Schedule slot
    start_time:      str = Form(...),
    end_time:        str = Form(...),
    duration_units:  int = Form(2),
):
    data = AssignmentCreate(
        task_id=task_id,
        worker_id=worker_id,
        allocated_hours=allocated_hours,
        status=status,
        start_date=start_date,
        end_date=end_date,
        start_time=start_time,
        end_time=end_time,
        duration_units=duration_units,
    )
    return await task_assignment_service.create_assignment(data)


@router.get("/")
async def list_assignments():
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
    assignment_id:   int,
    allocated_hours: Optional[int] = Form(None),
    status:          Optional[str] = Form(None),
    # Date range
    start_date:      Optional[str] = Form(None),
    end_date:        Optional[str] = Form(None),
    # Schedule slot
    start_time:      Optional[str] = Form(None),
    end_time:        Optional[str] = Form(None),
    duration_units:  Optional[int] = Form(None),
):
    data = AssignmentUpdate(
        allocated_hours=allocated_hours,
        status=status,
        start_date=start_date,
        end_date=end_date,
        start_time=start_time,
        end_time=end_time,
        duration_units=duration_units,
    )
    return await task_assignment_service.update_assignment(assignment_id, data)


@router.patch("/{assignment_id}/status")
async def update_assignment_status(assignment_id: int, status: str = Form(...)):
    return await task_assignment_service.update_assignment_status(assignment_id, status)


@router.delete("/{assignment_id}")
async def delete_assignment(assignment_id: int):
    return await task_assignment_service.delete_assignment(assignment_id)