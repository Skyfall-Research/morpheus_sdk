from typing import Any, Dict, Optional, Union

from ...client.generated_api_client.client import Client
from ...client.generated_api_client.api.world import act
from ...client.generated_api_client.models.act_body import ActBody
from ...client.generated_api_client.models.act_body_params import ActBodyParams
from ...client.generated_api_client.models.act_body_query import ActBodyQuery
from ...client.generated_api_client.models.act_body_body import ActBodyBody
from ...client.generated_api_client.models.act_response_200 import ActResponse200

class Act:
    def __init__(self, client: Client):
        self.client = client

    def call(
        self, 
        path: str, 
        method: str = "GET", 
        params: Optional[Dict[str, Any]] = None, 
        query: Optional[Dict[str, Any]] = None, 
        body: Optional[Dict[str, Any]] = None
    ) -> Union[ActResponse200, Any]:
        """
        Execute a dynamic internal API call.
        """
        # Construct ActBody parts
        act_params = None
        if params is not None:
            act_params = ActBodyParams.from_dict(params)

        act_query = None
        if query is not None:
            act_query = ActBodyQuery.from_dict(query)

        act_body_content = None
        if body is not None:
            act_body_content = ActBodyBody.from_dict(body)

        act_ref = ActBody(
            path=path,
            method=method,
            params=act_params,  # type: ignore # Models might expect Unset if None, but factory/default handles it usually or we need Unset
            query=act_query,    # type: ignore
            body=act_body_content # type: ignore
        )
        
        # Note: The generated models usually default to UNSET if not provided in __init__, but if provided as None it might error if strict.
        # Let's check ActBody signature again via inspection or just rely on ignoring types if we are confident.
        # Actually better to only pass if not None to constructor to rely on UNSET defaults.
        
        # Re-construct with kwargs to be safe about UNSET
        act_body_kwargs = {
            "path": path,
            "method": method
        }
        if act_params:
            act_body_kwargs["params"] = act_params
        if act_query:
            act_body_kwargs["query"] = act_query
        if act_body_content:
            act_body_kwargs["body"] = act_body_content
            
        act_ref = ActBody(**act_body_kwargs)

        response = act.sync_detailed(
            client=self.client,
            body=act_ref
        )

        if response.status_code == 200:
            if isinstance(response.parsed, ActResponse200):
                return response.parsed
            return response.parsed # It might be Any
        else:
             raise Exception(f"Failed to execute act: {response.status_code} {response.content}")


class AsyncAct:
    def __init__(self, client: Client):
        self.client = client

    async def call(
        self, 
        path: str, 
        method: str = "GET", 
        params: Optional[Dict[str, Any]] = None, 
        query: Optional[Dict[str, Any]] = None, 
        body: Optional[Dict[str, Any]] = None
    ) -> Union[ActResponse200, Any]:
        """
        Execute a dynamic internal API call.
        """
        # Construct ActBody parts
        act_params = None
        if params is not None:
            act_params = ActBodyParams.from_dict(params)

        act_query = None
        if query is not None:
            act_query = ActBodyQuery.from_dict(query)

        act_body_content = None
        if body is not None:
            act_body_content = ActBodyBody.from_dict(body)

        # Re-construct with kwargs to be safe about UNSET
        act_body_kwargs = {
            "path": path,
            "method": method
        }
        if act_params:
            act_body_kwargs["params"] = act_params
        if act_query:
            act_body_kwargs["query"] = act_query
        if act_body_content:
            act_body_kwargs["body"] = act_body_content
            
        act_ref = ActBody(**act_body_kwargs)

        response = await act.asyncio_detailed(
            client=self.client,
            body=act_ref
        )

        if response.status_code == 200:
            if isinstance(response.parsed, ActResponse200):
                return response.parsed
            return response.parsed # It might be Any
        else:
             raise Exception(f"Failed to execute act: {response.status_code} {response.content}")
