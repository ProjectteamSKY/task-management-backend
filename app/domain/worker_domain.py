from pydantic import BaseModel

class WorkerCreate(BaseModel):
    id: str
    name: str
    email: str
    role: str
    department: str
    status: str
    avatar: str
    daily_capacity_hours: int