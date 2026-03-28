from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.schedule_domain import ScheduleCreate

q = load_queries("schedule_queries")["schedule"]


async def create_schedule(data: ScheduleCreate):
    return await execute(
        q["create"],
        [
            data.worker_id,
            data.task_id,
            data.date,
            data.start_time,
            data.end_time,
            data.duration_units,
            data.status,
        ],
        fetch_row=True,
    )

async def get_schedule():
    return await query(q["get_all"], fetch_all=True)

async def get_worker_schedule(worker_id: int):
    return await query(q["get_by_worker"], [worker_id], fetch_all=True)

async def get_schedule_by_date(date: str):
    return await query(q["get_by_date"], [date], fetch_all=True)

async def get_worker_schedule_range(worker_id: int, start_date: str, end_date: str):
    return await query(
        q["get_by_worker_and_date_range"],
        [worker_id, start_date, end_date],
        fetch_all=True,
    )

async def delete_slot(slot_id: int):
    return await execute(q["delete"], [slot_id], fetch_row=True)