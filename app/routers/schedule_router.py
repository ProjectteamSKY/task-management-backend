from fastapi import APIRouter, Form
from app.services import schedule_service
from app.domain.schedule_domain import ScheduleCreate

router = APIRouter(prefix="/schedule", tags=["Schedule"])

@router.post("/")
async def create(
    worker_id: int = Form(...),
    task_id: int = Form(None),
    date: str = Form(...),
    start_time: str = Form(...),
    end_time: str = Form(...),
    status: str = Form(...)
):
    data = ScheduleCreate(
        worker_id=worker_id,
        task_id=task_id,
        date=date,
        start_time=start_time,
        end_time=end_time,
        status=status
    )
    return await schedule_service.create_schedule(data)

@router.get("/")
async def list_all():
    return await schedule_service.get_schedule()

@router.get("/{worker_id}")
async def worker_schedule(worker_id: str):
    return await schedule_service.get_worker_schedule(worker_id)