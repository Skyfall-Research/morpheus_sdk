import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_invoice_statistics_response_200 import GetInvoiceStatisticsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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
        "url": f"/{world_id}/edi/statistics/invoice",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetInvoiceStatisticsResponse200]:
    if response.status_code == 200:
        response_200 = GetInvoiceStatisticsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetInvoiceStatisticsResponse200]:
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
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetInvoiceStatisticsResponse200]:
    """Get invoice processing statistics

    Args:
        world_id (str):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInvoiceStatisticsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
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
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetInvoiceStatisticsResponse200]:
    """Get invoice processing statistics

    Args:
        world_id (str):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInvoiceStatisticsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetInvoiceStatisticsResponse200]:
    """Get invoice processing statistics

    Args:
        world_id (str):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetInvoiceStatisticsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetInvoiceStatisticsResponse200]:
    """Get invoice processing statistics

    Args:
        world_id (str):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetInvoiceStatisticsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
