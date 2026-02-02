from typing import Any, Dict, Literal, Optional
from pydantic import BaseModel

class ModelActionSpaceMeshDocsInputs(BaseModel):
    service: str
    action: Optional[str] = None
    method: Optional[Literal["POST", "GET", "PUT", "DELETE", "PATCH"]] = None
    include_examples: bool = True

class ModelActionSpaceTrajectoryInputs(BaseModel):
    od_id: str

class ModelActionSpaceObservation(BaseModel):
    data: Optional[Dict[str, Any]] = None
    status: Optional[int] = None
    success: Optional[bool] = None
    error: Optional[str] = None
