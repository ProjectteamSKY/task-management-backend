from pydantic import BaseModel
from typing import Optional

class AvailabilityCreate(BaseModel):
    status: str                        # available | blocked | recurring | leave
    day_of_week: Optional[int]  = None # available, recurring
    start_time: Optional[str]   = None # available, blocked  "HH:MM"
    end_time: Optional[str]     = None # available, blocked  "HH:MM"
    from_date: Optional[str]    = None # blocked, leave      "YYYY-MM-DD"
    to_date: Optional[str]      = None # leave only
    leave_type: Optional[str]   = None # leave only
    reason: Optional[str]       = None # blocked, recurring, leave
    is_enabled: Optional[bool]  = True # available only

class AvailabilityUpdate(BaseModel):
    day_of_week: Optional[int]  = None
    start_time: Optional[str]   = None
    end_time: Optional[str]     = None
    from_date: Optional[str]    = None
    to_date: Optional[str]      = None
    leave_type: Optional[str]   = None
    reason: Optional[str]       = None
    is_enabled: Optional[bool]  = None

class ApprovalUpdate(BaseModel):
    approval_status: str               # pending | approved | rejected