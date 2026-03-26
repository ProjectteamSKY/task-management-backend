from fastapi import APIRouter, Form
from typing import Optional
from app.services import project_service
from app.domain.project_domain import ProjectCreate, ProjectUpdate

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/")
async def create_project(
    name: str                     = Form(...),
    description: Optional[str]   = Form(None),
    start_date: Optional[str]    = Form(None),
    end_date: Optional[str]      = Form(None),
    status: str                  = Form("active"),
):
    data = ProjectCreate(
        name=name,
        description=description,
        start_date=start_date,
        end_date=end_date,
        status=status,
    )
    return await project_service.create_project(data)


@router.get("/")
async def list_projects():
    """All projects with task counts and worker counts."""
    return await project_service.get_projects()


@router.get("/status/{status}")
async def list_projects_by_status(status: str):
    return await project_service.get_projects_by_status(status)


@router.get("/{project_id}")
async def get_project(project_id: int):
    return await project_service.get_project(project_id)


@router.get("/{project_id}/tasks")
async def get_project_tasks(project_id: int):
    """All tasks under a project with assignment counts and allocated hours."""
    return await project_service.get_project_tasks(project_id)


@router.get("/{project_id}/workers")
async def get_project_workers(project_id: int):
    """All workers assigned to any task in this project."""
    return await project_service.get_project_workers(project_id)


@router.patch("/{project_id}")
async def update_project(
    project_id: int,
    name: Optional[str]          = Form(None),
    description: Optional[str]   = Form(None),
    start_date: Optional[str]    = Form(None),
    end_date: Optional[str]      = Form(None),
    status: Optional[str]        = Form(None),
):
    data = ProjectUpdate(
        name=name,
        description=description,
        start_date=start_date,
        end_date=end_date,
        status=status,
    )
    return await project_service.update_project(project_id, data)


@router.patch("/{project_id}/status")
async def update_project_status(project_id: int, status: str = Form(...)):
    return await project_service.update_project_status(project_id, status)


@router.delete("/{project_id}")
async def delete_project(project_id: int):
    return await project_service.delete_project(project_id)