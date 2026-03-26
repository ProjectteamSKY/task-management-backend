from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.task_assignment_domain import AssignmentCreate, AssignmentUpdate
from datetime import datetime

q = load_queries("assignment_queries")["assignment"]


async def create_assignment(data: AssignmentCreate):
    return await execute(
        q["create"],
        [
            data.task_id,
            data.worker_id,
            data.allocated_hours,
            _parse_date(data.assigned_date),
            data.status,
        ],
        fetch_row=True,
    )

async def get_assignments():
    return await query(q["get_all"], fetch_all=True)

async def get_assignment(assignment_id: int):
    return await query(q["get_by_id"], [assignment_id])

async def get_assignments_by_task(task_id: int):
    return await query(q["get_by_task"], [task_id], fetch_all=True)

async def get_assignments_by_worker(worker_id: int):
    return await query(q["get_by_worker"], [worker_id], fetch_all=True)

async def get_assignments_by_status(status: str):
    return await query(q["get_by_status"], [status], fetch_all=True)

async def update_assignment(assignment_id: int, data: AssignmentUpdate):
    return await execute(
        q["update"],
        [
            data.allocated_hours,
            _parse_date(data.assigned_date),
            data.status,
            assignment_id,
        ],
        fetch_row=True,
    )

async def update_assignment_status(assignment_id: int, status: str):
    return await execute(q["update_status"], [status, assignment_id], fetch_row=True)

async def delete_assignment(assignment_id: int):
    return await execute(q["delete"], [assignment_id], fetch_row=True)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _parse_date(value):
    if not value:
        return None
    if isinstance(value, str):
        return datetime.strptime(value, "%Y-%m-%d").date()
    return value