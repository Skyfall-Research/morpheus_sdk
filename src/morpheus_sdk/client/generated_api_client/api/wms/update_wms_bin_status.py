from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_bin_status_body import UpdateWMSBinStatusBody
from ...models.update_wms_bin_status_response_200 import UpdateWMSBinStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    bin_id: str,
    *,
    body: UpdateWMSBinStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/bins/{bin_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSBinStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSBinStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSBinStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSBinStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSBinStatusResponse200]]:
    """Update bin status


    ## Update WMS Bin Status

    Update the operational status of a warehouse bin with optional reason documentation for audit and
    operational tracking.

    ### Features
    - **Status Management**: Control bin operational availability and usage
    - **Reason Documentation**: Optional reason field for audit trail and communication
    - **Workflow Integration**: Trigger downstream processes based on status changes
    - **Audit Trail**: Track all status changes with timestamps and reasons
    - **Operational Control**: Support maintenance, blocking, and reservation workflows

    ### Status Transitions
    - **AVAILABLE** ↔ **OCCUPIED**: Inventory placement and removal
    - **AVAILABLE** ↔ **RESERVED**: Reserve for specific operations
    - **Any Status** → **DAMAGED**: Mark as damaged for maintenance
    - **Any Status** → **BLOCKED**: Temporarily block for operations
    - **DAMAGED** → **AVAILABLE**: Repair completion and restoration
    - **BLOCKED** → **AVAILABLE**: Remove operational block

    ### Business Rules
    - Status field is required for all updates
    - Reason field is optional but recommended for non-standard changes
    - Status changes are logged for audit compliance
    - Some status changes may trigger workflow notifications
    - Bins with DAMAGED or BLOCKED status are excluded from availability

    ### Use Cases
    - **Maintenance Management**: Mark bins as damaged for repair workflows
    - **Operational Control**: Block bins for cleaning or reorganization
    - **Reservation Management**: Reserve bins for specific operations or inventory
    - **Status Monitoring**: Track bin status for operational dashboards


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN_ATL_A01_001.
        body (UpdateWMSBinStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSBinStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_id=bin_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSBinStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSBinStatusResponse200]]:
    """Update bin status


    ## Update WMS Bin Status

    Update the operational status of a warehouse bin with optional reason documentation for audit and
    operational tracking.

    ### Features
    - **Status Management**: Control bin operational availability and usage
    - **Reason Documentation**: Optional reason field for audit trail and communication
    - **Workflow Integration**: Trigger downstream processes based on status changes
    - **Audit Trail**: Track all status changes with timestamps and reasons
    - **Operational Control**: Support maintenance, blocking, and reservation workflows

    ### Status Transitions
    - **AVAILABLE** ↔ **OCCUPIED**: Inventory placement and removal
    - **AVAILABLE** ↔ **RESERVED**: Reserve for specific operations
    - **Any Status** → **DAMAGED**: Mark as damaged for maintenance
    - **Any Status** → **BLOCKED**: Temporarily block for operations
    - **DAMAGED** → **AVAILABLE**: Repair completion and restoration
    - **BLOCKED** → **AVAILABLE**: Remove operational block

    ### Business Rules
    - Status field is required for all updates
    - Reason field is optional but recommended for non-standard changes
    - Status changes are logged for audit compliance
    - Some status changes may trigger workflow notifications
    - Bins with DAMAGED or BLOCKED status are excluded from availability

    ### Use Cases
    - **Maintenance Management**: Mark bins as damaged for repair workflows
    - **Operational Control**: Block bins for cleaning or reorganization
    - **Reservation Management**: Reserve bins for specific operations or inventory
    - **Status Monitoring**: Track bin status for operational dashboards


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN_ATL_A01_001.
        body (UpdateWMSBinStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSBinStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        bin_id=bin_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSBinStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSBinStatusResponse200]]:
    """Update bin status


    ## Update WMS Bin Status

    Update the operational status of a warehouse bin with optional reason documentation for audit and
    operational tracking.

    ### Features
    - **Status Management**: Control bin operational availability and usage
    - **Reason Documentation**: Optional reason field for audit trail and communication
    - **Workflow Integration**: Trigger downstream processes based on status changes
    - **Audit Trail**: Track all status changes with timestamps and reasons
    - **Operational Control**: Support maintenance, blocking, and reservation workflows

    ### Status Transitions
    - **AVAILABLE** ↔ **OCCUPIED**: Inventory placement and removal
    - **AVAILABLE** ↔ **RESERVED**: Reserve for specific operations
    - **Any Status** → **DAMAGED**: Mark as damaged for maintenance
    - **Any Status** → **BLOCKED**: Temporarily block for operations
    - **DAMAGED** → **AVAILABLE**: Repair completion and restoration
    - **BLOCKED** → **AVAILABLE**: Remove operational block

    ### Business Rules
    - Status field is required for all updates
    - Reason field is optional but recommended for non-standard changes
    - Status changes are logged for audit compliance
    - Some status changes may trigger workflow notifications
    - Bins with DAMAGED or BLOCKED status are excluded from availability

    ### Use Cases
    - **Maintenance Management**: Mark bins as damaged for repair workflows
    - **Operational Control**: Block bins for cleaning or reorganization
    - **Reservation Management**: Reserve bins for specific operations or inventory
    - **Status Monitoring**: Track bin status for operational dashboards


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN_ATL_A01_001.
        body (UpdateWMSBinStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSBinStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_id=bin_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSBinStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSBinStatusResponse200]]:
    """Update bin status


    ## Update WMS Bin Status

    Update the operational status of a warehouse bin with optional reason documentation for audit and
    operational tracking.

    ### Features
    - **Status Management**: Control bin operational availability and usage
    - **Reason Documentation**: Optional reason field for audit trail and communication
    - **Workflow Integration**: Trigger downstream processes based on status changes
    - **Audit Trail**: Track all status changes with timestamps and reasons
    - **Operational Control**: Support maintenance, blocking, and reservation workflows

    ### Status Transitions
    - **AVAILABLE** ↔ **OCCUPIED**: Inventory placement and removal
    - **AVAILABLE** ↔ **RESERVED**: Reserve for specific operations
    - **Any Status** → **DAMAGED**: Mark as damaged for maintenance
    - **Any Status** → **BLOCKED**: Temporarily block for operations
    - **DAMAGED** → **AVAILABLE**: Repair completion and restoration
    - **BLOCKED** → **AVAILABLE**: Remove operational block

    ### Business Rules
    - Status field is required for all updates
    - Reason field is optional but recommended for non-standard changes
    - Status changes are logged for audit compliance
    - Some status changes may trigger workflow notifications
    - Bins with DAMAGED or BLOCKED status are excluded from availability

    ### Use Cases
    - **Maintenance Management**: Mark bins as damaged for repair workflows
    - **Operational Control**: Block bins for cleaning or reorganization
    - **Reservation Management**: Reserve bins for specific operations or inventory
    - **Status Monitoring**: Track bin status for operational dashboards


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN_ATL_A01_001.
        body (UpdateWMSBinStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSBinStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            bin_id=bin_id,
            client=client,
            body=body,
        )
    ).parsed
