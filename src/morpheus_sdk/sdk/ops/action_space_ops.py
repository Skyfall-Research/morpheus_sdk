import logging
from typing import Optional, Union

from ...models.model_action_space import (
    ModelActionSpaceInputs, 
    ModelActionSpaceMeshDocsInputs, 
    ModelActionSpaceTrajectoryInputs, 
    ModelActionSpaceObservation
)
from ...client.api.action_space import ActionSpace, AsyncActionSpace
from ...client.generated_api_client.models.get_docs_mesh_method import GetDocsMeshMethod

logger = logging.getLogger("morpheus_sdk")

def execute_action_space_sync(wrapper: Optional[ActionSpace], inputs: ModelActionSpaceInputs) -> ModelActionSpaceObservation:
    if not wrapper:
        return ModelActionSpaceObservation(status=400, error="World not initialized")
    
    try:
        if isinstance(inputs, ModelActionSpaceMeshDocsInputs):
             method_enum = None
             if inputs.method:
                 try:
                     method_enum = GetDocsMeshMethod(inputs.method.lower())
                 except ValueError:
                     return ModelActionSpaceObservation(status=400, error=f"Invalid method: {inputs.method}")

             res = wrapper.mesh_docs(
                 service=inputs.service,
                 action=inputs.action,
                 method=method_enum,
                 include_examples=inputs.include_examples
             )
        elif isinstance(inputs, ModelActionSpaceTrajectoryInputs):
             res = wrapper.get_trajectory(od_id=inputs.od_id)
        else:
             return ModelActionSpaceObservation(status=400, error="Invalid action space inputs")
        
        return ModelActionSpaceObservation(
            success=True,
            status=200, 
            data=res.to_dict() if hasattr(res, "to_dict") else res
        )
    except Exception as e:
        logger.error(f"Action Space failed: {e}")
        return ModelActionSpaceObservation(success=False, status=500, error=str(e))

async def execute_action_space_async(wrapper: Optional[AsyncActionSpace], inputs: ModelActionSpaceInputs) -> ModelActionSpaceObservation:
    if not wrapper:
        return ModelActionSpaceObservation(status=400, error="World not initialized")
    
    try:
        if isinstance(inputs, ModelActionSpaceMeshDocsInputs):
             method_enum = None
             if inputs.method:
                 try:
                     method_enum = GetDocsMeshMethod(inputs.method.lower())
                 except ValueError:
                     return ModelActionSpaceObservation(status=400, error=f"Invalid method: {inputs.method}")

             res = await wrapper.mesh_docs(
                 service=inputs.service,
                 action=inputs.action,
                 method=method_enum,
                 include_examples=inputs.include_examples
             )
        elif isinstance(inputs, ModelActionSpaceTrajectoryInputs):
             res = await wrapper.get_trajectory(od_id=inputs.od_id)
        else:
             return ModelActionSpaceObservation(status=400, error="Invalid action space inputs")
        
        return ModelActionSpaceObservation(
            success=True,
            status=200, 
            data=res.to_dict() if hasattr(res, "to_dict") else res
        )
    except Exception as e:
        logger.error(f"Action Space failed: {e}")
        return ModelActionSpaceObservation(success=False, status=500, error=str(e))
