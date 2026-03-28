from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.worker_domain import ShiftScheduleCreate, EquipmentCreate, TrainingDevelopmentCreate

q = load_queries("worker_resources_queries")["worker_resources"]


# ── Shift ──────────────────────────────────────────────────────────────────────

async def upsert_shift(worker_id: int, data: ShiftScheduleCreate):
    return await execute(
        q["upsert_shift"],
        [worker_id, data.shift_type, data.working_days,
         data.start_time, data.end_time, data.break_duration],
        fetch_row=True,
    )

async def get_shift(worker_id: int):
    return await query(q["get_shift"], [worker_id])

async def delete_shift(worker_id: int):
    return await execute(q["delete_shift"], [worker_id], fetch_row=True)


# ── Equipment ──────────────────────────────────────────────────────────────────

async def add_equipment(worker_id: int, data: EquipmentCreate):
    return await execute(
        q["add_equipment"],
        [worker_id, data.name, data.equipment_ref, data.category,
         data.condition, data.assigned_date, data.return_date],
        fetch_row=True,
    )

async def get_equipment(worker_id: int):
    return await query(q["get_equipment"], [worker_id], fetch_all=True)

async def update_equipment(worker_id: int, equipment_id: int, data: EquipmentCreate):
    return await execute(
        q["update_equipment"],
        [data.name, data.equipment_ref, data.category, data.condition,
         data.assigned_date, data.return_date, equipment_id, worker_id],
        fetch_row=True,
    )

async def delete_equipment(worker_id: int, equipment_id: int):
    return await execute(q["delete_equipment"], [equipment_id, worker_id], fetch_row=True)


# ── Training & Goals ───────────────────────────────────────────────────────────

async def add_training_development(worker_id: int, data: TrainingDevelopmentCreate):
    return await execute(
        q["add_training_development"],
        [worker_id, data.type, data.title, data.progress, data.due_date,
         data.provider, data.category, data.status,
         data.start_date, data.end_date, data.notes],
        fetch_row=True,
    )

async def get_training_development(worker_id: int):
    return await query(q["get_training_development"], [worker_id], fetch_all=True)

async def update_training_development(worker_id: int, record_id: int, data: TrainingDevelopmentCreate):
    return await execute(
        q["update_training_development"],
        [data.title, data.progress, data.due_date,
         data.provider, data.category, data.status,
         data.start_date, data.end_date, data.notes,
         record_id, worker_id],
        fetch_row=True,
    )

async def delete_training_development(worker_id: int, record_id: int):
    return await execute(q["delete_training_development"], [record_id, worker_id], fetch_row=True)