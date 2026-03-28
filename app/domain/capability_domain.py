from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CapabilityItem(BaseModel):
    capability: str
    proficiency: int = Field(..., ge=1, le=5)


class CapabilityCreate(BaseModel):
    capability: str
    proficiency: int = Field(..., ge=1, le=5)


class CapabilityBulkCreate(BaseModel):
    capabilities: list[CapabilityItem]


class CapabilityUpdate(BaseModel):
    capability: Optional[str] = None
    proficiency: Optional[int] = Field(None, ge=1, le=5)


class CapabilityOut(BaseModel):
    id: int
    worker_id: int
    capability: str
    proficiency: int
    created_at: datetime