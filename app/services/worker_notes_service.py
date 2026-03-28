from app.core.db import query, execute
from app.core.loader import load_queries
from app.domain.worker_notes_domain import WorkerNoteCreate, WorkerNoteUpdate

q = load_queries("worker_notes_queries")["worker_note"]


async def create_note(worker_id: int, data: WorkerNoteCreate):
    return await execute(
        q["create"],
        [worker_id, data.notes],
        fetch_row=True,
    )

async def get_notes(worker_id: int):
    return await query(q["get_all"], [worker_id], fetch_all=True)

async def get_note(worker_id: int, note_id: int):
    return await query(q["get_by_id"], [note_id, worker_id])

async def update_note(worker_id: int, note_id: int, data: WorkerNoteUpdate):
    return await execute(
        q["update"],
        [data.notes, note_id, worker_id],
        fetch_row=True,
    )

async def delete_note(worker_id: int, note_id: int):
    return await execute(
        q["delete"],
        [note_id, worker_id],
        fetch_row=True,
    )

async def delete_all_notes(worker_id: int):
    return await execute(
        q["delete_all"],
        [worker_id],
        fetch_row=True,
    )