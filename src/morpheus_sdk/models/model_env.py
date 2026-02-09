from typing import List, Dict, Any, Optional
from pydantic import BaseModel


class ModelChaosConfig(BaseModel):
    process_chaos_enabled: bool = False
    infra_chaos_enabled: bool = False


class ModelCreateEnvInputs(BaseModel):
    name: str
    description: Optional[str] = None
    layout: Optional[str] = None
    real_hours_per_sim_day: Optional[float] = None
    chaos: Optional[ModelChaosConfig] = None


class ModelDeleteEnvInputs(BaseModel):
    world_id: str


class ModelEnvOutput(BaseModel):
    status: Optional[int] = None
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
