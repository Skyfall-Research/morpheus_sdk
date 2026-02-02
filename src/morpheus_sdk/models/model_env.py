from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class ModelCreateEnvInputs(BaseModel):
    name: str
    description: Optional[str] = None
    layout: Optional[str] = None
    realHoursPerSimDay: Optional[int] = 24

class ModelEnvActions(BaseModel):
    act: Dict[str, Any]

    