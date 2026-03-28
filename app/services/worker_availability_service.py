from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.worker_availability_domain import AvailabilityCreate, AvailabilityUpdate
from datetime import datetime

q = load_queries("worker_availability_queries")["worker_availability"]


async def get_all(worker_id: int):
    return await query(q["get_all"], [worker_id], fetch_all=True)

async def get_by_status(worker_id: int, status: str):
    return await query(q["get_by_status"], [worker_id, status], fetch_all=True)

async def create(worker_id: int, data: AvailabilityCreate):
    return await execute(
        q["create"],
        [
            worker_id,
            data.status,
            data.day_of_week,
            _parse_time(data.start_time),
            _parse_time(data.end_time),
            _parse_date(data.from_date),
            _parse_date(data.to_date),
            data.leave_type,
            data.reason,
            "pending" if data.status == "leave" else None,
            data.is_enabled,
        ],
        fetch_row=True,
    )

async def update(worker_id: int, record_id: int, data: AvailabilityUpdate):
    return await execute(
        q["update"],
        [
            data.day_of_week,
            _parse_time(data.start_time),
            _parse_time(data.end_time),
            _parse_date(data.from_date),
            _parse_date(data.to_date),
            data.leave_type,
            data.reason,
            data.is_enabled,
            record_id,
            worker_id,
        ],
        fetch_row=True,
    )

async def update_approval(worker_id: int, record_id: int, approval_status: str):
    return await execute(
        q["update_approval"],
        [approval_status, record_id, worker_id],
        fetch_row=True,
    )

async def delete(worker_id: int, record_id: int):
    return await execute(q["delete"], [record_id, worker_id], fetch_row=True)


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
        return datetime.strptime(value, "%H:%M").time()
    return value