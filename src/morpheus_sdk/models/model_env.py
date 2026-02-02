from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class ModelCreateEnvInputs(BaseModel):
    name: str
    description: Optional[str] = None
    layout: Optional[str] = None
    realHoursPerSimDay: Optional[int] = 24

class ModelDeleteEnvInputs(BaseModel):
    world_id: str


class ModelEnvOutput(BaseModel):
    status: Optional[int] = None
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
