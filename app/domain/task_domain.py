from pydantic import BaseModel

class TaskCreate(BaseModel):
    id: str
    title: str
    description: str
    duration_units: int
    status: str