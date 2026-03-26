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
            data.status
        ],
        fetch_row=True
    )

async def get_schedule():
    return await query(q["get_all"], fetch_all=True)

async def get_worker_schedule(worker_id):
    return await query(q["get_by_worker"], [int(worker_id)], fetch_all=True)  # cast to int, removed [schedule]