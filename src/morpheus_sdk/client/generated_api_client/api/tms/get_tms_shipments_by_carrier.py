import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_shipments_by_carrier_response_200 import GetTMSShipmentsByCarrierResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    carrier_id: str,
    *,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_from_: Union[Unset, str] = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: Union[Unset, str] = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/shipments/carrier/{carrier_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]]:
    if response.status_code == 200:
        response_200 = GetTMSShipmentsByCarrierResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]]:
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
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]]:
    """Get shipments by carrier


    ## Get Shipments by Carrier

    Retrieve all shipments assigned to a specific carrier with optional status filtering.

    ### Features
    - **Carrier-Specific View**: All shipments for a particular carrier
    - **Performance Analytics**: Carrier performance metrics and KPIs
    - **Status Breakdown**: Distribution of shipments by status
    - **Historical Data**: Past shipment performance for the carrier

    ### Use Cases
    - Carrier performance monitoring
    - Capacity planning and allocation
    - Service level agreement (SLA) tracking
    - Carrier scorecard generation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59.999Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_id=carrier_id,
        from_=from_,
        to=to,
        limit=limit,
        cursor=cursor,
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
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]]:
    """Get shipments by carrier


    ## Get Shipments by Carrier

    Retrieve all shipments assigned to a specific carrier with optional status filtering.

    ### Features
    - **Carrier-Specific View**: All shipments for a particular carrier
    - **Performance Analytics**: Carrier performance metrics and KPIs
    - **Status Breakdown**: Distribution of shipments by status
    - **Historical Data**: Past shipment performance for the carrier

    ### Use Cases
    - Carrier performance monitoring
    - Capacity planning and allocation
    - Service level agreement (SLA) tracking
    - Carrier scorecard generation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59.999Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        carrier_id=carrier_id,
        client=client,
        from_=from_,
        to=to,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]]:
    """Get shipments by carrier


    ## Get Shipments by Carrier

    Retrieve all shipments assigned to a specific carrier with optional status filtering.

    ### Features
    - **Carrier-Specific View**: All shipments for a particular carrier
    - **Performance Analytics**: Carrier performance metrics and KPIs
    - **Status Breakdown**: Distribution of shipments by status
    - **Historical Data**: Past shipment performance for the carrier

    ### Use Cases
    - Carrier performance monitoring
    - Capacity planning and allocation
    - Service level agreement (SLA) tracking
    - Carrier scorecard generation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59.999Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_id=carrier_id,
        from_=from_,
        to=to,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]]:
    """Get shipments by carrier


    ## Get Shipments by Carrier

    Retrieve all shipments assigned to a specific carrier with optional status filtering.

    ### Features
    - **Carrier-Specific View**: All shipments for a particular carrier
    - **Performance Analytics**: Carrier performance metrics and KPIs
    - **Status Breakdown**: Distribution of shipments by status
    - **Historical Data**: Past shipment performance for the carrier

    ### Use Cases
    - Carrier performance monitoring
    - Capacity planning and allocation
    - Service level agreement (SLA) tracking
    - Carrier scorecard generation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59.999Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSShipmentsByCarrierResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            carrier_id=carrier_id,
            client=client,
            from_=from_,
            to=to,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
