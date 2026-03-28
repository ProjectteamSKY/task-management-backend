from pydantic import BaseModel
from typing import Optional
from typing import List

class WorkerCreate(BaseModel):

    name: str
    email: str
    role: str
    department: str
    status: str
    avatar: Optional[str] = None
    daily_capacity_hours: int

class EmergencyContactCreate(BaseModel):
    full_name:    str
    relationship: Optional[str] = None
    phone:        str
    email:        Optional[str] = None
    address:      Optional[str] = None

class EmergencyContactUpdate(BaseModel):
    full_name:    Optional[str] = None
    relationship: Optional[str] = None
    phone:        Optional[str] = None
    email:        Optional[str] = None
    address:      Optional[str] = None

class ShiftScheduleCreate(BaseModel):
    shift_type:     str
    working_days:   List[str]
    start_time:     str
    end_time:       str
    break_duration: int = 30

class EquipmentCreate(BaseModel):
    name:          str
    equipment_ref: str
    category:      str
    condition:     str = "Good"
    assigned_date: str
    return_date:   Optional[str] = None

class TrainingDevelopmentCreate(BaseModel):
    type:       str          
    title:      str
    progress:   int = 0
    due_date:   Optional[str] = None
    provider:   Optional[str] = None
    category:   Optional[str] = None
    status:     Optional[str] = None
    start_date: Optional[str] = None
    end_date:   Optional[str] = None
    notes:      Optional[str] = None