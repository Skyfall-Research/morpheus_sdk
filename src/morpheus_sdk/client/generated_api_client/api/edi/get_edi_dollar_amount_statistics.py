import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_edi_dollar_amount_statistics_aggregation_type import GetEdiDollarAmountStatisticsAggregationType
from ...models.get_edi_dollar_amount_statistics_response_200 import GetEdiDollarAmountStatisticsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    aggregation_type: GetEdiDollarAmountStatisticsAggregationType,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_aggregation_type = aggregation_type.value
    params["aggregationType"] = json_aggregation_type

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/edi/statistics/amount",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]]:
    if response.status_code == 200:
        response_200 = GetEdiDollarAmountStatisticsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregation_type: GetEdiDollarAmountStatisticsAggregationType,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]]:
    """Get EDI dollar amount exposure statistics


    ## Get EDI Dollar Amount Exposure Statistics

    Retrieve aggregated dollar value statistics for EDI transactions, grouped by trading partner or
    document type.

    ### Features
    - **Partner Analysis**: View dollar exposure by trading partner
    - **Document Type Analysis**: View dollar exposure by EDI document type
    - **Date Filtering**: Filter statistics within a date range
    - **Top Results**: Returns up to 100 aggregated results

    ### Use Cases
    - Financial exposure monitoring per partner
    - Revenue analysis by document type
    - Risk assessment for trading relationships
    - Budget planning and forecasting


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        aggregation_type (GetEdiDollarAmountStatisticsAggregationType):  Example: by-partners.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-12-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        aggregation_type=aggregation_type,
        date_start=date_start,
        date_end=date_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregation_type: GetEdiDollarAmountStatisticsAggregationType,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]]:
    """Get EDI dollar amount exposure statistics


    ## Get EDI Dollar Amount Exposure Statistics

    Retrieve aggregated dollar value statistics for EDI transactions, grouped by trading partner or
    document type.

    ### Features
    - **Partner Analysis**: View dollar exposure by trading partner
    - **Document Type Analysis**: View dollar exposure by EDI document type
    - **Date Filtering**: Filter statistics within a date range
    - **Top Results**: Returns up to 100 aggregated results

    ### Use Cases
    - Financial exposure monitoring per partner
    - Revenue analysis by document type
    - Risk assessment for trading relationships
    - Budget planning and forecasting


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        aggregation_type (GetEdiDollarAmountStatisticsAggregationType):  Example: by-partners.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-12-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        aggregation_type=aggregation_type,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregation_type: GetEdiDollarAmountStatisticsAggregationType,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]]:
    """Get EDI dollar amount exposure statistics


    ## Get EDI Dollar Amount Exposure Statistics

    Retrieve aggregated dollar value statistics for EDI transactions, grouped by trading partner or
    document type.

    ### Features
    - **Partner Analysis**: View dollar exposure by trading partner
    - **Document Type Analysis**: View dollar exposure by EDI document type
    - **Date Filtering**: Filter statistics within a date range
    - **Top Results**: Returns up to 100 aggregated results

    ### Use Cases
    - Financial exposure monitoring per partner
    - Revenue analysis by document type
    - Risk assessment for trading relationships
    - Budget planning and forecasting


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        aggregation_type (GetEdiDollarAmountStatisticsAggregationType):  Example: by-partners.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-12-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        aggregation_type=aggregation_type,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    aggregation_type: GetEdiDollarAmountStatisticsAggregationType,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]]:
    """Get EDI dollar amount exposure statistics


    ## Get EDI Dollar Amount Exposure Statistics

    Retrieve aggregated dollar value statistics for EDI transactions, grouped by trading partner or
    document type.

    ### Features
    - **Partner Analysis**: View dollar exposure by trading partner
    - **Document Type Analysis**: View dollar exposure by EDI document type
    - **Date Filtering**: Filter statistics within a date range
    - **Top Results**: Returns up to 100 aggregated results

    ### Use Cases
    - Financial exposure monitoring per partner
    - Revenue analysis by document type
    - Risk assessment for trading relationships
    - Budget planning and forecasting


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        aggregation_type (GetEdiDollarAmountStatisticsAggregationType):  Example: by-partners.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-12-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetEdiDollarAmountStatisticsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            aggregation_type=aggregation_type,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
