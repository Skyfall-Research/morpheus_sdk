import logging
from typing import Optional
from ...models.model_task import ModelTaskInputs, ModelTaskOutputs
from ...client.api.tasks import Tasks, AsyncTasks

logger = logging.getLogger("morpheus_sdk")

def execute_task_sync(wrapper: Optional[Tasks], inputs: ModelTaskInputs) -> ModelTaskOutputs:
    if not wrapper:
        return ModelTaskOutputs(status=400, error="World not initialized")
        
    try:
        if inputs.filters:
             if inputs.filters.task_id:
                 res = wrapper.get(inputs.filters.task_id)
                 data = res.to_dict() if hasattr(res, "to_dict") else res
             else:
                 cursor = inputs.filters.cursor
                 limit = inputs.filters.limit if inputs.filters.limit else 100
                 res = wrapper.list(limit=limit, cursor=cursor, status=inputs.filters.status)
                 data = res.to_dict() if hasattr(res, "to_dict") else res
        else:
            res = wrapper.list()
            data = res.to_dict() if hasattr(res, "to_dict") else res

        return ModelTaskOutputs(success=True, status=200, data=data)

    except Exception as e:
        logger.error(f"Task failed: {e}")
        return ModelTaskOutputs(success=False, status=500, error=str(e))

async def execute_task_async(wrapper: Optional[AsyncTasks], inputs: ModelTaskInputs) -> ModelTaskOutputs:
     if not wrapper:
        return ModelTaskOutputs(status=400, error="World not initialized")
     try:
        if inputs.filters:
             if inputs.filters.task_id:
                 res = await wrapper.get(inputs.filters.task_id)
                 data = res.to_dict() if hasattr(res, "to_dict") else res
             else:
                 cursor = inputs.filters.cursor
                 limit = inputs.filters.limit if inputs.filters.limit else 100
                 res = await wrapper.list(limit=limit, cursor=cursor, status=inputs.filters.status)
                 data = res.to_dict() if hasattr(res, "to_dict") else res
        else:
            res = await wrapper.list()
            data = res.to_dict() if hasattr(res, "to_dict") else res

        return ModelTaskOutputs(success=True, status=200, data=data)

     except Exception as e:
        logger.error(f"Task failed: {e}")
        return ModelTaskOutputs(success=False, status=500, error=str(e))
