from datetime import date, time, timedelta

from app.core.db import query, execute
from app.core.loader import load_queries

q  = load_queries("worker_availability_queries")["worker_availability"]
sq = load_queries("schedule_queries")["schedule"]

# asyncpg requires native Python objects for typed columns:
#   DATE  → datetime.date
#   TIME  → datetime.time
_LEAVE_START = time(9, 0)   # 09:00
_LEAVE_END   = time(17, 0)  # 17:00


async def get_leaves(worker_id: int):
    """All leave records for one worker regardless of approval status."""
    return await query(q["get_by_status"], [worker_id, "leave"], fetch_all=True)


async def get_all_leaves():
    """All leave records across all workers — uses a dedicated query."""
    return await query(q["get_all_leaves"], [], fetch_all=True)


async def get_leaves_by_approval(worker_id: int, approval_status: str):
    """Leave records for one worker filtered by approval status."""
    return await query(
        q["get_leaves_by_approval"], [worker_id, approval_status], fetch_all=True
    )


# ── Schedule slot helpers ─────────────────────────────────────────────────────

async def _create_leave_slots(worker_id: int, from_date: str, to_date: str):
    """Create one leave schedule slot per day in the leave date range."""
    start   = date.fromisoformat(from_date)
    end     = date.fromisoformat(to_date if to_date else from_date)
    current = start

    while current <= end:
        await execute(
            sq["create"],
            [
                worker_id,      # $1 worker_id  (int)
                None,           # $2 task_id    (None → NULL)
                current,        # $3 date       (datetime.date)
                _LEAVE_START,   # $4 start_time (datetime.time)
                _LEAVE_END,     # $5 end_time   (datetime.time)
                18,             # $6 duration_units — 8 hrs × 2 units/hr
                "leave",        # $7 status
            ],
            fetch_row=True,
        )
        current += timedelta(days=1)


async def _delete_leave_slots(worker_id: int, from_date: str, to_date: str):
    """Delete all leave schedule slots for a worker in the given date range."""
    start   = date.fromisoformat(from_date)
    end     = date.fromisoformat(to_date if to_date else from_date)
    current = start

    while current <= end:
        rows = await query(sq["get_by_worker"], [worker_id], fetch_all=True)
        for row in rows:
            row_date = row.get("date")
            # asyncpg returns DATE columns as datetime.date objects
            if isinstance(row_date, date):
                row_date = row_date.isoformat()
            if row_date == current.isoformat() and row.get("status") == "leave":
                await execute(sq["delete"], [row["id"]], fetch_row=True)
        current += timedelta(days=1)


# ── Helpers to safely coerce asyncpg date return values ──────────────────────

def _to_iso(val) -> str:
    if val is None:
        return ""
    if isinstance(val, date):
        return val.isoformat()
    return str(val)[:10]


# ── Leave approval ────────────────────────────────────────────────────────────

async def approve_leave(worker_id: int, record_id: int):
    """Approve leave and create matching leave slots in the schedule."""
    result = await execute(
        q["update_approval"],
        ["approved", record_id, worker_id],
        fetch_row=True,
    )
    if result:
        from_date = _to_iso(result.get("from_date"))
        to_date   = _to_iso(result.get("to_date") or result.get("from_date"))
        if from_date:
            await _create_leave_slots(worker_id, from_date, to_date)
    return result


async def reject_leave(worker_id: int, record_id: int):
    """Reject leave and remove any matching leave slots from the schedule."""
    result = await execute(
        q["update_approval"],
        ["rejected", record_id, worker_id],
        fetch_row=True,
    )
    if result:
        from_date = _to_iso(result.get("from_date"))
        to_date   = _to_iso(result.get("to_date") or result.get("from_date"))
        if from_date:
            await _delete_leave_slots(worker_id, from_date, to_date)
    return result


async def reset_leave(worker_id: int, record_id: int):
    return await execute(
        q["update_approval"],
        ["pending", record_id, worker_id],
        fetch_row=True,
    )