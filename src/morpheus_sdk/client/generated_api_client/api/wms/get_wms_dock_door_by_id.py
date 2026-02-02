from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_dock_door_by_id_response_200 import GetWMSDockDoorByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    door_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/dock-doors/{door_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSDockDoorByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSDockDoorByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetWMSDockDoorByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSDockDoorByIdResponse200]]:
    """Get dock door by ID


    ## Get WMS Dock Door Details

    Retrieve comprehensive information about a specific dock door including current status,
    appointments, equipment capabilities, and operational configuration.

    ### Features
    - **Complete Information**: Full dock door configuration and current state
    - **Real-Time Status**: Current appointment and trailer assignments
    - **Equipment Details**: Capabilities, safety equipment, and maintenance schedules
    - **Operating Hours**: Daily schedule for operational planning
    - **Audit Information**: Creation and modification timestamps

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Returns comprehensive dock door information including nested objects
    - Includes current appointment details if door is occupied
    - Shows maintenance and safety inspection schedules
    - Provides operating hours for scheduling validation

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Use Cases
    - **Appointment Planning**: Check door availability and capabilities for scheduling
    - **Maintenance Management**: Review maintenance schedules and safety inspections
    - **Operational Overview**: Get complete door status for warehouse management
    - **Equipment Verification**: Confirm door capabilities for specific trailer requirements
    - **Schedule Coordination**: Verify operating hours for appointment scheduling


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDockDoorByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        door_id=door_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSDockDoorByIdResponse200]]:
    """Get dock door by ID


    ## Get WMS Dock Door Details

    Retrieve comprehensive information about a specific dock door including current status,
    appointments, equipment capabilities, and operational configuration.

    ### Features
    - **Complete Information**: Full dock door configuration and current state
    - **Real-Time Status**: Current appointment and trailer assignments
    - **Equipment Details**: Capabilities, safety equipment, and maintenance schedules
    - **Operating Hours**: Daily schedule for operational planning
    - **Audit Information**: Creation and modification timestamps

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Returns comprehensive dock door information including nested objects
    - Includes current appointment details if door is occupied
    - Shows maintenance and safety inspection schedules
    - Provides operating hours for scheduling validation

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Use Cases
    - **Appointment Planning**: Check door availability and capabilities for scheduling
    - **Maintenance Management**: Review maintenance schedules and safety inspections
    - **Operational Overview**: Get complete door status for warehouse management
    - **Equipment Verification**: Confirm door capabilities for specific trailer requirements
    - **Schedule Coordination**: Verify operating hours for appointment scheduling


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDockDoorByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        door_id=door_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSDockDoorByIdResponse200]]:
    """Get dock door by ID


    ## Get WMS Dock Door Details

    Retrieve comprehensive information about a specific dock door including current status,
    appointments, equipment capabilities, and operational configuration.

    ### Features
    - **Complete Information**: Full dock door configuration and current state
    - **Real-Time Status**: Current appointment and trailer assignments
    - **Equipment Details**: Capabilities, safety equipment, and maintenance schedules
    - **Operating Hours**: Daily schedule for operational planning
    - **Audit Information**: Creation and modification timestamps

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Returns comprehensive dock door information including nested objects
    - Includes current appointment details if door is occupied
    - Shows maintenance and safety inspection schedules
    - Provides operating hours for scheduling validation

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Use Cases
    - **Appointment Planning**: Check door availability and capabilities for scheduling
    - **Maintenance Management**: Review maintenance schedules and safety inspections
    - **Operational Overview**: Get complete door status for warehouse management
    - **Equipment Verification**: Confirm door capabilities for specific trailer requirements
    - **Schedule Coordination**: Verify operating hours for appointment scheduling


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDockDoorByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        door_id=door_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSDockDoorByIdResponse200]]:
    """Get dock door by ID


    ## Get WMS Dock Door Details

    Retrieve comprehensive information about a specific dock door including current status,
    appointments, equipment capabilities, and operational configuration.

    ### Features
    - **Complete Information**: Full dock door configuration and current state
    - **Real-Time Status**: Current appointment and trailer assignments
    - **Equipment Details**: Capabilities, safety equipment, and maintenance schedules
    - **Operating Hours**: Daily schedule for operational planning
    - **Audit Information**: Creation and modification timestamps

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Returns comprehensive dock door information including nested objects
    - Includes current appointment details if door is occupied
    - Shows maintenance and safety inspection schedules
    - Provides operating hours for scheduling validation

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Use Cases
    - **Appointment Planning**: Check door availability and capabilities for scheduling
    - **Maintenance Management**: Review maintenance schedules and safety inspections
    - **Operational Overview**: Get complete door status for warehouse management
    - **Equipment Verification**: Confirm door capabilities for specific trailer requirements
    - **Schedule Coordination**: Verify operating hours for appointment scheduling


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDockDoorByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            door_id=door_id,
            client=client,
        )
    ).parsed
