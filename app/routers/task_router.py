from fastapi import APIRouter, Form
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
async def create(
    title: str = Form(...),
    description: str = Form(None),
    status: str = Form(...),
    priority: str = Form(...),
    estimated_hours: int = Form(...),
    assigned_to: str = Form(None)
):
    data = {
    "title": title,
    "description": description,
    "status": status,
    "priority": priority,
    "estimated_hours": estimated_hours,
    "assigned_to": int(assigned_to) if assigned_to else None  # <-- fix this line
}
    return await task_service.create_task(data)


@router.get("/")
async def list_tasks():
    return await task_service.get_tasks()