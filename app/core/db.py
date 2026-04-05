import asyncpg

DATABASE_URL = "postgresql://keerthana:Jh9GnMLtPLDj7rTeIZehgA@taskmanagement-24324.j77.aws-ap-south-1.cockroachlabs.cloud:26257/defaultdb?sslmode=require"
_pool = None
SCHEMA = "task_managment"


async def _set_schema(conn):
    await conn.execute(f"SET search_path TO {SCHEMA}")


async def init_db():
    global _pool
    _pool = await asyncpg.create_pool(
        dsn=DATABASE_URL,
        min_size=1,
        max_size=10
    )
    # Debug check
    async with _pool.acquire() as conn:
        schema = await conn.fetchval("SELECT current_schema()")
        db = await conn.fetchval("SELECT current_database()")
        tables = await conn.fetch(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"
        )
        print(f"✅ Database: {db} | Schema: {schema}")
        print(f"📋 Tables: {[r['table_name'] for r in tables]}")


def get_pool():
    if _pool is None:
        raise Exception("DB not initialized. Call init_db() first.")
    return _pool


def _row_to_dict(row):
    return dict(row) if row else None


async def query(sql: str, params: list = None, fetch_all: bool = False):
    params = params or []
    async with get_pool().acquire() as conn:
        if fetch_all:
            rows = await conn.fetch(sql, *params)
            return [_row_to_dict(r) for r in rows]
        row = await conn.fetchrow(sql, *params)
        return _row_to_dict(row) if row else None


async def execute(sql: str, params: list = None, fetch_row: bool = False):
    params = params or []
    async with get_pool().acquire() as conn:
        if fetch_row:
            row = await conn.fetchrow(sql, *params)
            return _row_to_dict(row) if row else None
        await conn.execute(sql, *params)