from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_distribution_center_status_body import UpdateWMSDistributionCenterStatusBody
from ...models.update_wms_distribution_center_status_response_200 import UpdateWMSDistributionCenterStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    dc_id: str,
    *,
    body: UpdateWMSDistributionCenterStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/distribution-centers/{dc_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSDistributionCenterStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    dc_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDistributionCenterStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]]:
    """Update distribution center operational status


    ## Update WMS Distribution Center Status

    Update the operational status of a distribution center with optional reason tracking for facility
    management and operational coordination.

    ### Features
    - **Status Management**: Update operational status for facility management
    - **Reason Tracking**: Optional reason documentation for status changes
    - **Timestamp Tracking**: Automatic timestamp recording for status change audit trail
    - **Validation**: Comprehensive validation of status values and facility existence
    - **Audit Trail**: Complete audit trail through status change tracking

    ### Operational Status Values
    - **ACTIVE**: Fully operational, accepting all operations and workflows
    - **INACTIVE**: Temporarily inactive, facility available but not processing operations
    - **MAINTENANCE**: Under maintenance, all operations suspended for facility maintenance

    ### Request Body
    - **status**: Required - New operational status for the facility
    - **reason**: Optional - Reason for status change (recommended for audit trail)

    ### Business Rules
    - dcId must reference an existing distribution center
    - status must be a valid operational status value
    - Optional reason field is stored for audit trail and compliance
    - Automatic timestamp recording for status change tracking
    - Status change immediately affects facility operational availability

    ### Use Cases
    - **Maintenance Mode**: Set facility to maintenance status during scheduled maintenance
    - **Activation**: Activate facilities for operational use
    - **Emergency Shutdown**: Quickly disable facility operations during emergencies
    - **Planned Downtime**: Schedule facility downtime with reason documentation
    - **Status Compliance**: Maintain facility status compliance and audit trails


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.
        body (UpdateWMSDistributionCenterStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dc_id=dc_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    dc_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDistributionCenterStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]]:
    """Update distribution center operational status


    ## Update WMS Distribution Center Status

    Update the operational status of a distribution center with optional reason tracking for facility
    management and operational coordination.

    ### Features
    - **Status Management**: Update operational status for facility management
    - **Reason Tracking**: Optional reason documentation for status changes
    - **Timestamp Tracking**: Automatic timestamp recording for status change audit trail
    - **Validation**: Comprehensive validation of status values and facility existence
    - **Audit Trail**: Complete audit trail through status change tracking

    ### Operational Status Values
    - **ACTIVE**: Fully operational, accepting all operations and workflows
    - **INACTIVE**: Temporarily inactive, facility available but not processing operations
    - **MAINTENANCE**: Under maintenance, all operations suspended for facility maintenance

    ### Request Body
    - **status**: Required - New operational status for the facility
    - **reason**: Optional - Reason for status change (recommended for audit trail)

    ### Business Rules
    - dcId must reference an existing distribution center
    - status must be a valid operational status value
    - Optional reason field is stored for audit trail and compliance
    - Automatic timestamp recording for status change tracking
    - Status change immediately affects facility operational availability

    ### Use Cases
    - **Maintenance Mode**: Set facility to maintenance status during scheduled maintenance
    - **Activation**: Activate facilities for operational use
    - **Emergency Shutdown**: Quickly disable facility operations during emergencies
    - **Planned Downtime**: Schedule facility downtime with reason documentation
    - **Status Compliance**: Maintain facility status compliance and audit trails


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.
        body (UpdateWMSDistributionCenterStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        dc_id=dc_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    dc_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDistributionCenterStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]]:
    """Update distribution center operational status


    ## Update WMS Distribution Center Status

    Update the operational status of a distribution center with optional reason tracking for facility
    management and operational coordination.

    ### Features
    - **Status Management**: Update operational status for facility management
    - **Reason Tracking**: Optional reason documentation for status changes
    - **Timestamp Tracking**: Automatic timestamp recording for status change audit trail
    - **Validation**: Comprehensive validation of status values and facility existence
    - **Audit Trail**: Complete audit trail through status change tracking

    ### Operational Status Values
    - **ACTIVE**: Fully operational, accepting all operations and workflows
    - **INACTIVE**: Temporarily inactive, facility available but not processing operations
    - **MAINTENANCE**: Under maintenance, all operations suspended for facility maintenance

    ### Request Body
    - **status**: Required - New operational status for the facility
    - **reason**: Optional - Reason for status change (recommended for audit trail)

    ### Business Rules
    - dcId must reference an existing distribution center
    - status must be a valid operational status value
    - Optional reason field is stored for audit trail and compliance
    - Automatic timestamp recording for status change tracking
    - Status change immediately affects facility operational availability

    ### Use Cases
    - **Maintenance Mode**: Set facility to maintenance status during scheduled maintenance
    - **Activation**: Activate facilities for operational use
    - **Emergency Shutdown**: Quickly disable facility operations during emergencies
    - **Planned Downtime**: Schedule facility downtime with reason documentation
    - **Status Compliance**: Maintain facility status compliance and audit trails


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.
        body (UpdateWMSDistributionCenterStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dc_id=dc_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    dc_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDistributionCenterStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]]:
    """Update distribution center operational status


    ## Update WMS Distribution Center Status

    Update the operational status of a distribution center with optional reason tracking for facility
    management and operational coordination.

    ### Features
    - **Status Management**: Update operational status for facility management
    - **Reason Tracking**: Optional reason documentation for status changes
    - **Timestamp Tracking**: Automatic timestamp recording for status change audit trail
    - **Validation**: Comprehensive validation of status values and facility existence
    - **Audit Trail**: Complete audit trail through status change tracking

    ### Operational Status Values
    - **ACTIVE**: Fully operational, accepting all operations and workflows
    - **INACTIVE**: Temporarily inactive, facility available but not processing operations
    - **MAINTENANCE**: Under maintenance, all operations suspended for facility maintenance

    ### Request Body
    - **status**: Required - New operational status for the facility
    - **reason**: Optional - Reason for status change (recommended for audit trail)

    ### Business Rules
    - dcId must reference an existing distribution center
    - status must be a valid operational status value
    - Optional reason field is stored for audit trail and compliance
    - Automatic timestamp recording for status change tracking
    - Status change immediately affects facility operational availability

    ### Use Cases
    - **Maintenance Mode**: Set facility to maintenance status during scheduled maintenance
    - **Activation**: Activate facilities for operational use
    - **Emergency Shutdown**: Quickly disable facility operations during emergencies
    - **Planned Downtime**: Schedule facility downtime with reason documentation
    - **Status Compliance**: Maintain facility status compliance and audit trails


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.
        body (UpdateWMSDistributionCenterStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSDistributionCenterStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            dc_id=dc_id,
            client=client,
            body=body,
        )
    ).parsed
