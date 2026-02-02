from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel

class ModelStateInputs(BaseModel):
    time_start: Optional[datetime] = None
    time_end: Optional[datetime] = None
    include: Optional[Dict[str, bool]] = {
        "audit_log": False,
        "logs": True,
    }
    limit: Optional[int] = None
    offset: Optional[int] = None

class ModelStateOutputs(BaseModel):
    status: Optional[int] = None
    world_id: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    success: Optional[bool] = None
    error: Optional[str] = None

