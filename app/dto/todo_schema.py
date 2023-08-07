from pydantic import BaseModel
from typing import Optional
from enum import Enum

class StatusEnum(str, Enum):
    finished= "finished"
    deleted= "deleted"
    active= "active"

class ToDo(BaseModel):
    id: Optional[int]
    title: str
    description: str
    finished_at: Optional[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted_at: Optional[str] = None
    status: StatusEnum = StatusEnum.active