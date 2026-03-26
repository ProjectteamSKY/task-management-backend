from fastapi import APIRouter, Form
from typing import Optional
from app.services import schedule_service
from app.domain.schedule_domain import ScheduleCreate

router = APIRouter(prefix="/schedule", tags=["Schedule"])


@router.post("/")
async def create_slot(
    worker_id:  int          = Form(...),
    task_id:    Optional[int]= Form(None),
    date:       str          = Form(...),
    start_time: str          = Form(...),
    end_time:   str          = Form(...),
    status:     str          = Form(...),
):
    data = ScheduleCreate(
        worker_id=worker_id,
        task_id=task_id,
        date=date,
        start_time=start_time,
        end_time=end_time,
        status=status,
    )
    return await schedule_service.create_schedule(data)


@router.get("/")
async def list_all_slots():
    """All slots with worker name, role, department and task details."""
    return await schedule_service.get_schedule()


@router.get("/date/{date}")
async def list_slots_by_date(date: str):
    """All worker slots for a specific date (YYYY-MM-DD)."""
    return await schedule_service.get_schedule_by_date(date)


@router.get("/worker/{worker_id}")
async def worker_schedule(worker_id: int):
    """All schedule slots for a specific worker."""
    return await schedule_service.get_worker_schedule(worker_id)


@router.get("/worker/{worker_id}/range")
async def worker_schedule_range(
    worker_id:  int,
    start_date: str,
    end_date:   str,
):
    """Worker slots filtered by date range (?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD)."""
    return await schedule_service.get_worker_schedule_range(worker_id, start_date, end_date)


@router.delete("/{slot_id}")
async def delete_slot(slot_id: int):
    return await schedule_service.delete_slot(slot_id)