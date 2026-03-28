from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.task_domain import TaskCreate
from datetime import datetime

q = load_queries("task_queries")["task"]


async def create_task(data: TaskCreate):
    return await execute(
        q["create"],
        [
            data.title,
            data.description,
            data.status,
            data.priority,
            data.task_type,
            data.estimated_hours,
            data.project_id,
            _parse_date(data.start_date),
            _parse_date(data.end_date),
        ],
        fetch_row=True,
    )

async def get_tasks():
    return await query(q["get_all"], fetch_all=True)

async def get_task(task_id: int):
    return await query(q["get_by_id"], [task_id])

async def get_tasks_by_project(project_id: int):
    return await query(q["get_by_project"], [project_id], fetch_all=True)

async def get_tasks_by_status(status: str):
    return await query(q["get_by_status"], [status], fetch_all=True)

async def update_task_status(task_id: int, status: str):
    return await execute(q["update_status"], [status, task_id], fetch_row=True)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _parse_date(value):
    if not value:
        return None
    if isinstance(value, str):
        return datetime.strptime(value, "%Y-%m-%d").date()
    return value