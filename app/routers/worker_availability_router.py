from fastapi import APIRouter, Form
from typing import Optional
from app.services import worker_availability_service as svc
from app.domain.worker_availability_domain import AvailabilityCreate, AvailabilityUpdate

router = APIRouter(prefix="/workers/{worker_id}/availability", tags=["Worker Availability"])


@router.get("/")
async def get_availability(worker_id: int):
    """All availability records for a worker."""
    return await svc.get_all(worker_id)


@router.get("/{status}")
async def get_by_status(worker_id: int, status: str):
    """Filter by status: available | blocked | recurring | leave"""
    return await svc.get_by_status(worker_id, status)


@router.post("/")
async def create_availability(
    worker_id: int,
    status: str                     = Form(...),
    day_of_week: Optional[int]      = Form(None),
    start_time: Optional[str]       = Form(None),
    end_time: Optional[str]         = Form(None),
    from_date: Optional[str]        = Form(None),
    to_date: Optional[str]          = Form(None),
    leave_type: Optional[str]       = Form(None),
    reason: Optional[str]           = Form(None),
    is_enabled: Optional[bool]      = Form(True),
):
    data = AvailabilityCreate(
        status=status, day_of_week=day_of_week,
        start_time=start_time, end_time=end_time,
        from_date=from_date, to_date=to_date,
        leave_type=leave_type, reason=reason,
        is_enabled=is_enabled,
    )
    return await svc.create(worker_id, data)


@router.patch("/{record_id}")
async def update_availability(
    worker_id: int,
    record_id: int,
    day_of_week: Optional[int]      = Form(None),
    start_time: Optional[str]       = Form(None),
    end_time: Optional[str]         = Form(None),
    from_date: Optional[str]        = Form(None),
    to_date: Optional[str]          = Form(None),
    leave_type: Optional[str]       = Form(None),
    reason: Optional[str]           = Form(None),
    is_enabled: Optional[bool]      = Form(None),
):
    data = AvailabilityUpdate(
        day_of_week=day_of_week, start_time=start_time,
        end_time=end_time, from_date=from_date,
        to_date=to_date, leave_type=leave_type,
        reason=reason, is_enabled=is_enabled,
    )
    return await svc.update(worker_id, record_id, data)


@router.patch("/{record_id}/approval")
async def update_approval(
    worker_id: int,
    record_id: int,
    approval_status: str = Form(...),  # pending | approved | rejected
):
    return await svc.update_approval(worker_id, record_id, approval_status)


@router.delete("/{record_id}")
async def delete_availability(worker_id: int, record_id: int):
    return await svc.delete(worker_id, record_id)