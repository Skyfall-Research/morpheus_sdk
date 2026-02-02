from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_tms_carrier_performance_body import UpdateTMSCarrierPerformanceBody
from ...types import Response


def _get_kwargs(
    world_id: str,
    carrier_id: str,
    *,
    body: UpdateTMSCarrierPerformanceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/tms/carriers/{carrier_id}/performance",
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
    body: UpdateTMSCarrierPerformanceBody,
) -> Response[ErrorResponse]:
    """Update carrier performance metrics


    ## Update TMS Carrier Performance

    Update carrier performance metrics based on completed shipments and operational data.

    ### Features
    - **Performance Tracking**: Update key performance indicators
    - **Historical Preservation**: Maintains performance history and trends
    - **Automatic Timestamping**: Records when metrics were last updated
    - **Selective Updates**: Update individual metrics without affecting others
    - **Impact Analysis**: Performance changes affect carrier scoring and selection

    ### Performance Metrics
    - **On-Time Delivery Rate**: Percentage (0.0-1.0) of shipments delivered on time
    - **Damage Claim Rate**: Percentage (0.0-1.0) of shipments with damage claims
    - **Average Transit Time**: Average hours from pickup to delivery
    - **Total Shipments Completed**: Cumulative shipment count for volume tracking

    ### Update Strategy
    - Metrics can be updated individually or in combination
    - Last update timestamp is automatically recorded
    - Historical trends are preserved for analysis
    - Performance changes immediately affect carrier rankings


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        body (UpdateTMSCarrierPerformanceBody):

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
    body: UpdateTMSCarrierPerformanceBody,
) -> Optional[ErrorResponse]:
    """Update carrier performance metrics


    ## Update TMS Carrier Performance

    Update carrier performance metrics based on completed shipments and operational data.

    ### Features
    - **Performance Tracking**: Update key performance indicators
    - **Historical Preservation**: Maintains performance history and trends
    - **Automatic Timestamping**: Records when metrics were last updated
    - **Selective Updates**: Update individual metrics without affecting others
    - **Impact Analysis**: Performance changes affect carrier scoring and selection

    ### Performance Metrics
    - **On-Time Delivery Rate**: Percentage (0.0-1.0) of shipments delivered on time
    - **Damage Claim Rate**: Percentage (0.0-1.0) of shipments with damage claims
    - **Average Transit Time**: Average hours from pickup to delivery
    - **Total Shipments Completed**: Cumulative shipment count for volume tracking

    ### Update Strategy
    - Metrics can be updated individually or in combination
    - Last update timestamp is automatically recorded
    - Historical trends are preserved for analysis
    - Performance changes immediately affect carrier rankings


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        body (UpdateTMSCarrierPerformanceBody):

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
    body: UpdateTMSCarrierPerformanceBody,
) -> Response[ErrorResponse]:
    """Update carrier performance metrics


    ## Update TMS Carrier Performance

    Update carrier performance metrics based on completed shipments and operational data.

    ### Features
    - **Performance Tracking**: Update key performance indicators
    - **Historical Preservation**: Maintains performance history and trends
    - **Automatic Timestamping**: Records when metrics were last updated
    - **Selective Updates**: Update individual metrics without affecting others
    - **Impact Analysis**: Performance changes affect carrier scoring and selection

    ### Performance Metrics
    - **On-Time Delivery Rate**: Percentage (0.0-1.0) of shipments delivered on time
    - **Damage Claim Rate**: Percentage (0.0-1.0) of shipments with damage claims
    - **Average Transit Time**: Average hours from pickup to delivery
    - **Total Shipments Completed**: Cumulative shipment count for volume tracking

    ### Update Strategy
    - Metrics can be updated individually or in combination
    - Last update timestamp is automatically recorded
    - Historical trends are preserved for analysis
    - Performance changes immediately affect carrier rankings


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        body (UpdateTMSCarrierPerformanceBody):

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
    body: UpdateTMSCarrierPerformanceBody,
) -> Optional[ErrorResponse]:
    """Update carrier performance metrics


    ## Update TMS Carrier Performance

    Update carrier performance metrics based on completed shipments and operational data.

    ### Features
    - **Performance Tracking**: Update key performance indicators
    - **Historical Preservation**: Maintains performance history and trends
    - **Automatic Timestamping**: Records when metrics were last updated
    - **Selective Updates**: Update individual metrics without affecting others
    - **Impact Analysis**: Performance changes affect carrier scoring and selection

    ### Performance Metrics
    - **On-Time Delivery Rate**: Percentage (0.0-1.0) of shipments delivered on time
    - **Damage Claim Rate**: Percentage (0.0-1.0) of shipments with damage claims
    - **Average Transit Time**: Average hours from pickup to delivery
    - **Total Shipments Completed**: Cumulative shipment count for volume tracking

    ### Update Strategy
    - Metrics can be updated individually or in combination
    - Last update timestamp is automatically recorded
    - Historical trends are preserved for analysis
    - Performance changes immediately affect carrier rankings


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.
        body (UpdateTMSCarrierPerformanceBody):

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
