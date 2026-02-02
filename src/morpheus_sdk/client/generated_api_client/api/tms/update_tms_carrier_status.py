from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_tms_carrier_status_body import UpdateTMSCarrierStatusBody
from ...types import Response


def _get_kwargs(
    world_id: str,
    carrier_id: str,
    *,
    body: UpdateTMSCarrierStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/tms/carriers/{carrier_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTMSCarrierStatusBody,
) -> Response[ErrorResponse]:
    """Update carrier status


    ## Update TMS Carrier Status

    Change the operational status of a carrier to control availability for shipment assignments.

    ### Features
    - **Status Management**: Control carrier availability and operations
    - **Workflow Integration**: Support operational workflows and approvals
    - **Audit Trail**: Track status changes for compliance
    - **Real-Time Impact**: Immediately affects carrier eligibility

    ### Status Values and Meanings
    - **ACTIVE**: Available for new shipment assignments
    - **INACTIVE**: Not accepting new assignments (maintenance, etc.)
    - **SUSPENDED**: Temporarily suspended due to performance/compliance issues
    - **PENDING_APPROVAL**: New carrier awaiting approval process

    ### Business Rules
    - Only ACTIVE carriers appear in shipment tendering
    - Status changes are immediately effective
    - Historical performance data is preserved regardless of status


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        body (UpdateTMSCarrierStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_id=carrier_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTMSCarrierStatusBody,
) -> Optional[ErrorResponse]:
    """Update carrier status


    ## Update TMS Carrier Status

    Change the operational status of a carrier to control availability for shipment assignments.

    ### Features
    - **Status Management**: Control carrier availability and operations
    - **Workflow Integration**: Support operational workflows and approvals
    - **Audit Trail**: Track status changes for compliance
    - **Real-Time Impact**: Immediately affects carrier eligibility

    ### Status Values and Meanings
    - **ACTIVE**: Available for new shipment assignments
    - **INACTIVE**: Not accepting new assignments (maintenance, etc.)
    - **SUSPENDED**: Temporarily suspended due to performance/compliance issues
    - **PENDING_APPROVAL**: New carrier awaiting approval process

    ### Business Rules
    - Only ACTIVE carriers appear in shipment tendering
    - Status changes are immediately effective
    - Historical performance data is preserved regardless of status


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        body (UpdateTMSCarrierStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        world_id=world_id,
        carrier_id=carrier_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTMSCarrierStatusBody,
) -> Response[ErrorResponse]:
    """Update carrier status


    ## Update TMS Carrier Status

    Change the operational status of a carrier to control availability for shipment assignments.

    ### Features
    - **Status Management**: Control carrier availability and operations
    - **Workflow Integration**: Support operational workflows and approvals
    - **Audit Trail**: Track status changes for compliance
    - **Real-Time Impact**: Immediately affects carrier eligibility

    ### Status Values and Meanings
    - **ACTIVE**: Available for new shipment assignments
    - **INACTIVE**: Not accepting new assignments (maintenance, etc.)
    - **SUSPENDED**: Temporarily suspended due to performance/compliance issues
    - **PENDING_APPROVAL**: New carrier awaiting approval process

    ### Business Rules
    - Only ACTIVE carriers appear in shipment tendering
    - Status changes are immediately effective
    - Historical performance data is preserved regardless of status


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        body (UpdateTMSCarrierStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_id=carrier_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTMSCarrierStatusBody,
) -> Optional[ErrorResponse]:
    """Update carrier status


    ## Update TMS Carrier Status

    Change the operational status of a carrier to control availability for shipment assignments.

    ### Features
    - **Status Management**: Control carrier availability and operations
    - **Workflow Integration**: Support operational workflows and approvals
    - **Audit Trail**: Track status changes for compliance
    - **Real-Time Impact**: Immediately affects carrier eligibility

    ### Status Values and Meanings
    - **ACTIVE**: Available for new shipment assignments
    - **INACTIVE**: Not accepting new assignments (maintenance, etc.)
    - **SUSPENDED**: Temporarily suspended due to performance/compliance issues
    - **PENDING_APPROVAL**: New carrier awaiting approval process

    ### Business Rules
    - Only ACTIVE carriers appear in shipment tendering
    - Status changes are immediately effective
    - Historical performance data is preserved regardless of status


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        body (UpdateTMSCarrierStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            carrier_id=carrier_id,
            client=client,
            body=body,
        )
    ).parsed
