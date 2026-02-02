from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_dock_door_status_body import UpdateWMSDockDoorStatusBody
from ...models.update_wms_dock_door_status_response_200 import UpdateWMSDockDoorStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    door_id: str,
    *,
    body: UpdateWMSDockDoorStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/dock-doors/{door_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSDockDoorStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]]:
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
    body: UpdateWMSDockDoorStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]]:
    """Update dock door status


    ## Update WMS Dock Door Status

    Update the operational status of a dock door with optional reason tracking for comprehensive status
    management and audit trail maintenance.

    ### Features
    - **Status Lifecycle Management**: AVAILABLE → OCCUPIED → MAINTENANCE → CLOSED transitions
    - **Reason Tracking**: Optional status change reasoning for audit trails
    - **Timestamp Recording**: Automatic status change timestamps
    - **Validation Logic**: Ensures valid status transitions based on business rules
    - **Audit Trail**: Complete history of status modifications with timestamps and reasons

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Status must be one of the valid enumerated values
    - Status changes are tracked with automatic timestamps
    - Optional reason field captures business justification for status changes
    - Previous status transitions are maintained in audit trail
    - Concurrent appointment management ensures data consistency

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **status**: Required - New operational status (AVAILABLE, OCCUPIED, MAINTENANCE, CLOSED)
    - **reason**: Optional - Explanation for status change

    ### Business Rules
    - OCCUPIED status typically reserved for doors with active appointments
    - MAINTENANCE status requires coordination with appointment scheduling
    - CLOSED status removes door from all operational scheduling
    - AVAILABLE status enables immediate appointment scheduling

    ### Use Cases
    - **Operational Management**: Change door status based on operational requirements
    - **Maintenance Coordination**: Mark doors as under maintenance to prevent scheduling
    - **Emergency Closure**: Temporarily close doors due to safety or equipment issues
    - **Capacity Management**: Manage overall dock capacity by controlling door availability
    - **Audit Compliance**: Track status changes with timestamps and reasoning


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (UpdateWMSDockDoorStatusBody):  Example: {'status': 'MAINTENANCE', 'reason':
            'Scheduled weekly maintenance and safety inspection'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        door_id=door_id,
        body=body,
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
    body: UpdateWMSDockDoorStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]]:
    """Update dock door status


    ## Update WMS Dock Door Status

    Update the operational status of a dock door with optional reason tracking for comprehensive status
    management and audit trail maintenance.

    ### Features
    - **Status Lifecycle Management**: AVAILABLE → OCCUPIED → MAINTENANCE → CLOSED transitions
    - **Reason Tracking**: Optional status change reasoning for audit trails
    - **Timestamp Recording**: Automatic status change timestamps
    - **Validation Logic**: Ensures valid status transitions based on business rules
    - **Audit Trail**: Complete history of status modifications with timestamps and reasons

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Status must be one of the valid enumerated values
    - Status changes are tracked with automatic timestamps
    - Optional reason field captures business justification for status changes
    - Previous status transitions are maintained in audit trail
    - Concurrent appointment management ensures data consistency

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **status**: Required - New operational status (AVAILABLE, OCCUPIED, MAINTENANCE, CLOSED)
    - **reason**: Optional - Explanation for status change

    ### Business Rules
    - OCCUPIED status typically reserved for doors with active appointments
    - MAINTENANCE status requires coordination with appointment scheduling
    - CLOSED status removes door from all operational scheduling
    - AVAILABLE status enables immediate appointment scheduling

    ### Use Cases
    - **Operational Management**: Change door status based on operational requirements
    - **Maintenance Coordination**: Mark doors as under maintenance to prevent scheduling
    - **Emergency Closure**: Temporarily close doors due to safety or equipment issues
    - **Capacity Management**: Manage overall dock capacity by controlling door availability
    - **Audit Compliance**: Track status changes with timestamps and reasoning


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (UpdateWMSDockDoorStatusBody):  Example: {'status': 'MAINTENANCE', 'reason':
            'Scheduled weekly maintenance and safety inspection'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        door_id=door_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDockDoorStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]]:
    """Update dock door status


    ## Update WMS Dock Door Status

    Update the operational status of a dock door with optional reason tracking for comprehensive status
    management and audit trail maintenance.

    ### Features
    - **Status Lifecycle Management**: AVAILABLE → OCCUPIED → MAINTENANCE → CLOSED transitions
    - **Reason Tracking**: Optional status change reasoning for audit trails
    - **Timestamp Recording**: Automatic status change timestamps
    - **Validation Logic**: Ensures valid status transitions based on business rules
    - **Audit Trail**: Complete history of status modifications with timestamps and reasons

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Status must be one of the valid enumerated values
    - Status changes are tracked with automatic timestamps
    - Optional reason field captures business justification for status changes
    - Previous status transitions are maintained in audit trail
    - Concurrent appointment management ensures data consistency

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **status**: Required - New operational status (AVAILABLE, OCCUPIED, MAINTENANCE, CLOSED)
    - **reason**: Optional - Explanation for status change

    ### Business Rules
    - OCCUPIED status typically reserved for doors with active appointments
    - MAINTENANCE status requires coordination with appointment scheduling
    - CLOSED status removes door from all operational scheduling
    - AVAILABLE status enables immediate appointment scheduling

    ### Use Cases
    - **Operational Management**: Change door status based on operational requirements
    - **Maintenance Coordination**: Mark doors as under maintenance to prevent scheduling
    - **Emergency Closure**: Temporarily close doors due to safety or equipment issues
    - **Capacity Management**: Manage overall dock capacity by controlling door availability
    - **Audit Compliance**: Track status changes with timestamps and reasoning


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (UpdateWMSDockDoorStatusBody):  Example: {'status': 'MAINTENANCE', 'reason':
            'Scheduled weekly maintenance and safety inspection'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        door_id=door_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDockDoorStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]]:
    """Update dock door status


    ## Update WMS Dock Door Status

    Update the operational status of a dock door with optional reason tracking for comprehensive status
    management and audit trail maintenance.

    ### Features
    - **Status Lifecycle Management**: AVAILABLE → OCCUPIED → MAINTENANCE → CLOSED transitions
    - **Reason Tracking**: Optional status change reasoning for audit trails
    - **Timestamp Recording**: Automatic status change timestamps
    - **Validation Logic**: Ensures valid status transitions based on business rules
    - **Audit Trail**: Complete history of status modifications with timestamps and reasons

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Status must be one of the valid enumerated values
    - Status changes are tracked with automatic timestamps
    - Optional reason field captures business justification for status changes
    - Previous status transitions are maintained in audit trail
    - Concurrent appointment management ensures data consistency

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **status**: Required - New operational status (AVAILABLE, OCCUPIED, MAINTENANCE, CLOSED)
    - **reason**: Optional - Explanation for status change

    ### Business Rules
    - OCCUPIED status typically reserved for doors with active appointments
    - MAINTENANCE status requires coordination with appointment scheduling
    - CLOSED status removes door from all operational scheduling
    - AVAILABLE status enables immediate appointment scheduling

    ### Use Cases
    - **Operational Management**: Change door status based on operational requirements
    - **Maintenance Coordination**: Mark doors as under maintenance to prevent scheduling
    - **Emergency Closure**: Temporarily close doors due to safety or equipment issues
    - **Capacity Management**: Manage overall dock capacity by controlling door availability
    - **Audit Compliance**: Track status changes with timestamps and reasoning


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (UpdateWMSDockDoorStatusBody):  Example: {'status': 'MAINTENANCE', 'reason':
            'Scheduled weekly maintenance and safety inspection'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSDockDoorStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            door_id=door_id,
            client=client,
            body=body,
        )
    ).parsed
