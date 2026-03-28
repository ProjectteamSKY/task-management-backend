from pydantic import BaseModel


class WorkerNoteCreate(BaseModel):
    notes: str


class WorkerNoteUpdate(BaseModel):
    notes: str