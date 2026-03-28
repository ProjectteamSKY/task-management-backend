from fastapi import APIRouter, Form
from app.services import worker_notes_service
from app.domain.worker_notes_domain import WorkerNoteCreate, WorkerNoteUpdate

router = APIRouter(prefix="/workers/{worker_id}/notes", tags=["Worker Notes"])


@router.post("/")
async def create_note(worker_id: int, notes: str = Form(...)):
    data = WorkerNoteCreate(notes=notes)
    return await worker_notes_service.create_note(worker_id, data)


@router.get("/")
async def list_notes(worker_id: int):
    return await worker_notes_service.get_notes(worker_id)


@router.get("/{note_id}")
async def get_note(worker_id: int, note_id: int):
    return await worker_notes_service.get_note(worker_id, note_id)


@router.put("/{note_id}")
async def update_note(worker_id: int, note_id: int, notes: str = Form(...)):
    data = WorkerNoteUpdate(notes=notes)
    return await worker_notes_service.update_note(worker_id, note_id, data)


@router.delete("/{note_id}")
async def delete_note(worker_id: int, note_id: int):
    return await worker_notes_service.delete_note(worker_id, note_id)

@router.delete("/")
async def delete_all_notes(worker_id: int):
    return await worker_notes_service.delete_all_notes(worker_id)