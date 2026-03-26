from fastapi import APIRouter, Form
from app.services import worker_service

router = APIRouter(prefix="/workers", tags=["Workers"])

@router.post("/")
async def create(
    name: str = Form(...),
    email: str = Form(...),
    role: str = Form(...),
    department: str = Form(...),
    status: str = Form(...),
    avatar: str = Form(None),
    daily_capacity_hours: int = Form(...)
):
    data = {
        "name": name,
        "email": email,
        "role": role,
        "department": department,
        "status": status,
        "avatar": avatar,
        "daily_capacity_hours": daily_capacity_hours
    }
    return await worker_service.create_worker(data)


@router.get("/")
async def list_workers():
    return await worker_service.get_workers()