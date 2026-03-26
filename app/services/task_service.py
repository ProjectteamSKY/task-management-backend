from app.core.db import query, execute
from app.core.loader import load_queries

q = load_queries("task_queries")["task"]

async def create_task(data: dict):
    return await execute(q["create"], list(data.values()), fetch_row=True)

async def get_tasks():
    return await query(q["get_all"], fetch_all=True)

async def get_task(id):
    return await query(q["get_by_id"], [id])