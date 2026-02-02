from typing import Any, Optional, Literal
from pydantic import BaseModel

class ModelActInputs(BaseModel):
    path: str
    method: Literal["POST", "GET", "PUT", "DELETE", "PATCH"]
    body: Optional[dict[str, Any]] = None
    query_params: Optional[dict[str, Any]] = None
    path_params: Optional[dict[str, Any]] = None
    
class ModelActObservation(BaseModel):
    action_response: Optional[dict[str, Any]] = None
    status: Optional[int] = None
    data: Optional[dict[str, Any]] = None
    success: Optional[bool] = None
    error: Optional[str] = None