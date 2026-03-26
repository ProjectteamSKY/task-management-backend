from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.worker_domain import WorkerCreate

q = load_queries("worker_queries")["worker"]


async def create_worker(data: WorkerCreate):
    return await execute(
        q["create"],
        [
            data.name,
            data.email,
            data.role,
            data.department,
            data.status,
            data.avatar,
            data.daily_capacity_hours,
        ],
        fetch_row=True,
    )

async def get_workers():
    return await query(q["get_all"], fetch_all=True)

async def get_worker(worker_id: int):
    return await query(q["get_by_id"], [worker_id])

async def get_workers_by_department(department: str):
    return await query(q["get_by_department"], [department], fetch_all=True)

async def get_workers_with_tasks():
    return await query(q["get_with_tasks"], fetch_all=True)

async def update_worker_status(worker_id: int, status: str):
    return await execute(q["update_status"], [status, worker_id], fetch_row=True)