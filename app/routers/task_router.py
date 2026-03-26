from fastapi import APIRouter, Form
from datetime import datetime
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/")
async def create(
    title: str = Form(...),
    description: str = Form(...),
    status: str = Form(...),
    priority: str = Form(...),
    estimated_hours: int = Form(...),
    assigned_to: str = Form(None),
    project_name: str = Form(...),
    start_date: str = Form(None),
    end_date: str = Form(None),
):
    data = {
        "title": title,
        "description": description,
        "status": status,
        "priority": priority,
        "estimated_hours": estimated_hours,
        "assigned_to": int(assigned_to) if assigned_to else None,
        "project_name": project_name,
       
        "start_date": datetime.strptime(start_date, "%Y-%m-%d").date() if start_date else None,
        "end_date":   datetime.strptime(end_date,   "%Y-%m-%d").date() if end_date   else None,
    }
    return await task_service.create_task(data)


@router.get("/")
async def list_tasks():
    return await task_service.get_tasks()