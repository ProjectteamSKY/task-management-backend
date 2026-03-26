from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.project_domain import ProjectCreate, ProjectUpdate
from datetime import datetime

q = load_queries("project_queries")["project"]


async def create_project(data: ProjectCreate):
    return await execute(
        q["create"],
        [
            data.name,
            data.description,
            _parse_date(data.start_date),
            _parse_date(data.end_date),
            data.status,
        ],
        fetch_row=True,
    )

async def get_projects():
    return await query(q["get_all"], fetch_all=True)

async def get_project(project_id: int):
    return await query(q["get_by_id"], [project_id])

async def get_projects_by_status(status: str):
    return await query(q["get_by_status"], [status], fetch_all=True)

async def update_project(project_id: int, data: ProjectUpdate):
    return await execute(
        q["update"],
        [
            data.name,
            data.description,
            _parse_date(data.start_date),
            _parse_date(data.end_date),
            data.status,
            project_id,
        ],
        fetch_row=True,
    )

async def update_project_status(project_id: int, status: str):
    return await execute(q["update_status"], [status, project_id], fetch_row=True)

async def delete_project(project_id: int):
    return await execute(q["delete"], [project_id], fetch_row=True)

async def get_project_tasks(project_id: int):
    return await query(q["get_tasks"], [project_id], fetch_all=True)

async def get_project_workers(project_id: int):
    return await query(q["get_workers"], [project_id], fetch_all=True)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _parse_date(value):
    if not value:
        return None
    if isinstance(value, str):
        return datetime.strptime(value, "%Y-%m-%d").date()
    return value