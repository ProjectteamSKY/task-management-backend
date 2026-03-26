from app.core.db import query, execute
from app.core.loader import load_queries

q = load_queries("worker_queries")["worker"]

async def create_worker(data: dict):
    return await execute(q["create"], list(data.values()), fetch_row=True)

async def get_workers():
    return await query(q["get_all"], fetch_all=True)

async def get_worker(id):
    return await query(q["get_by_id"], [id])