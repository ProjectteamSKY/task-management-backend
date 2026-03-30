from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.task_assignment_domain import AssignmentCreate, AssignmentUpdate
from datetime import datetime, time

q = load_queries("assignment_queries")["assignment"]


async def create_assignment(data: AssignmentCreate):
    return await execute(
        q["create"],
        [
            data.task_id,
            data.worker_id,
            data.allocated_hours,
            data.status,
            _parse_date(data.start_date),
            _parse_date(data.end_date),
            _parse_time(data.start_time),
            _parse_time(data.end_time),
            data.duration_units,
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
            data.status,
            _parse_date(data.start_date),
            _parse_date(data.end_date),
            _parse_time(data.start_time),
            _parse_time(data.end_time),
            data.duration_units,
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


def _parse_time(value):
    if not value:
        return None
    if isinstance(value, str):
        # Accept "HH:MM" or "HH:MM:SS"
        parts = value.split(":")
        return time(int(parts[0]), int(parts[1]))
    return value