from datetime import datetime
from typing import Optional, Union, List

from ...client.generated_api_client.client import Client
from ...client.generated_api_client.api.logs import get_audit_logs, get_logs
from ...client.generated_api_client.models.get_audit_logs_model import GetAuditLogsModel
from ...client.generated_api_client.models.get_audit_logs_response_200 import GetAuditLogsResponse200
from ...client.generated_api_client.models.get_logs_service_type import GetLogsServiceType
from ...client.generated_api_client.models.get_logs_level import GetLogsLevel
from ...client.generated_api_client.models.get_logs_response_200 import GetLogsResponse200
from ...client.generated_api_client.types import UNSET

class Observation:
    def __init__(self, client: Client, world_id: str):
        self.client = client
        self.world_id = world_id

    def audit(
        self, 
        model: Optional[Union[GetAuditLogsModel, str]] = None,
        document_id: Optional[str] = None,
        date_start: Optional[datetime] = None,
        date_end: Optional[datetime] = None
    ) -> GetAuditLogsResponse200:
        """
        Get audit logs for data changes in a world.
        """
        # Handle inputs
        kwargs = {}
        if model is not None:
            if isinstance(model, str):
                kwargs["model"] = GetAuditLogsModel(model)
            else:
                kwargs["model"] = model
        
        if document_id is not None:
            kwargs["document_id"] = document_id
            
        if date_start is not None:
            kwargs["date_start"] = date_start
            
        if date_end is not None:
            kwargs["date_end"] = date_end

        response = get_audit_logs.sync_detailed(
            client=self.client, 
            world_id=self.world_id, 
            **kwargs
        )

        if response.status_code == 200:
            if isinstance(response.parsed, GetAuditLogsResponse200):
                return response.parsed
            raise Exception(f"Unexpected response type for audit logs: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to get audit logs: {response.status_code} {response.content}")

    def operational(
        self,
        service_type: Optional[Union[GetLogsServiceType, str]] = None,
        level: Optional[Union[GetLogsLevel, str]] = None,
        search_text: Optional[str] = None,
        date_start: Optional[datetime] = None,
        date_end: Optional[datetime] = None,
        limit: int = 100,
        cursor: Optional[str] = None
    ) -> GetLogsResponse200:
        """
        Get operational logs for a world.
        """
        # Handle inputs
        kwargs = {}
        if service_type is not None:
            if isinstance(service_type, str):
                kwargs["service_type"] = GetLogsServiceType(service_type)
            else:
                kwargs["service_type"] = service_type
        
        if level is not None:
            if isinstance(level, str):
                kwargs["level"] = GetLogsLevel(level)
            else:
                kwargs["level"] = level

        if search_text is not None:
            kwargs["search_text"] = search_text
            
        if date_start is not None:
            kwargs["date_start"] = date_start
            
        if date_end is not None:
            kwargs["date_end"] = date_end
            
        if limit is not None:
            kwargs["limit"] = limit
            
        if cursor is not None:
            kwargs["cursor"] = cursor

        response = get_logs.sync_detailed(
            client=self.client,
            world_id=self.world_id,
            **kwargs
        )

        if response.status_code == 200:
            if isinstance(response.parsed, GetLogsResponse200):
                return response.parsed
            raise Exception(f"Unexpected response type for operational logs: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to get operational logs: {response.status_code} {response.content}")


class AsyncObservation:
    def __init__(self, client: Client, world_id: str):
        self.client = client
        self.world_id = UUID(world_id)

    async def audit(
        self, 
        model: Optional[Union[GetAuditLogsModel, str]] = None,
        document_id: Optional[str] = None,
        date_start: Optional[datetime] = None,
        date_end: Optional[datetime] = None
    ) -> GetAuditLogsResponse200:
        """
        Get audit logs for data changes in a world.
        """
        # Handle inputs
        kwargs = {}
        if model is not None:
            if isinstance(model, str):
                kwargs["model"] = GetAuditLogsModel(model)
            else:
                kwargs["model"] = model
        
        if document_id is not None:
            kwargs["document_id"] = document_id
            
        if date_start is not None:
            kwargs["date_start"] = date_start
            
        if date_end is not None:
            kwargs["date_end"] = date_end

        response = await get_audit_logs.asyncio_detailed(
            client=self.client, 
            world_id=self.world_id, 
            **kwargs
        )

        if response.status_code == 200:
            if isinstance(response.parsed, GetAuditLogsResponse200):
                return response.parsed
            raise Exception(f"Unexpected response type for audit logs: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to get audit logs: {response.status_code} {response.content}")

    async def operational(
        self,
        service_type: Optional[Union[GetLogsServiceType, str]] = None,
        level: Optional[Union[GetLogsLevel, str]] = None,
        search_text: Optional[str] = None,
        date_start: Optional[datetime] = None,
        date_end: Optional[datetime] = None,
        limit: int = 100,
        cursor: Optional[str] = None
    ) -> GetLogsResponse200:
        """
        Get operational logs for a world.
        """
        # Handle inputs
        kwargs = {}
        if service_type is not None:
            if isinstance(service_type, str):
                kwargs["service_type"] = GetLogsServiceType(service_type)
            else:
                kwargs["service_type"] = service_type
        
        if level is not None:
            if isinstance(level, str):
                kwargs["level"] = GetLogsLevel(level)
            else:
                kwargs["level"] = level

        if search_text is not None:
            kwargs["search_text"] = search_text
            
        if date_start is not None:
            kwargs["date_start"] = date_start
            
        if date_end is not None:
            kwargs["date_end"] = date_end
            
        if limit is not None:
            kwargs["limit"] = limit
            
        if cursor is not None:
            kwargs["cursor"] = cursor

        response = await get_logs.asyncio_detailed(
            client=self.client,
            world_id=self.world_id,
            **kwargs
        )

        if response.status_code == 200:
            if isinstance(response.parsed, GetLogsResponse200):
                return response.parsed
            raise Exception(f"Unexpected response type for operational logs: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to get operational logs: {response.status_code} {response.content}")
