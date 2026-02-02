from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.allocate_wms_order_line_body import AllocateWMSOrderLineBody
from ...models.allocate_wms_order_line_response_200 import AllocateWMSOrderLineResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    order_id: str,
    line_id: str,
    *,
    body: AllocateWMSOrderLineBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/outbound-orders/{order_id}/lines/{line_id}/allocate",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AllocateWMSOrderLineResponse200]:
    if response.status_code == 200:
        response_200 = AllocateWMSOrderLineResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AllocateWMSOrderLineResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    order_id: str,
    line_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AllocateWMSOrderLineBody,
) -> Response[AllocateWMSOrderLineResponse200]:
    """Allocate inventory to specific order line


    **Line-Level Inventory Allocation**

    Allocate inventory to a specific order line with detailed bin-level tracking.

    **Allocation Features:**
    - Precise quantity allocation per line
    - Optional bin-level allocation details
    - Lot number tracking support
    - Automatic line status update to ALLOCATED

    **Repository Logic:**
    - Updates matching line by `lineNumber` field
    - Sets `allocatedQuantity` and `lineStatus`
    - Stores detailed `allocations` array if provided


    Args:
        world_id (str):
        order_id (str):
        line_id (str):
        body (AllocateWMSOrderLineBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocateWMSOrderLineResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
        line_id=line_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    order_id: str,
    line_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AllocateWMSOrderLineBody,
) -> Optional[AllocateWMSOrderLineResponse200]:
    """Allocate inventory to specific order line


    **Line-Level Inventory Allocation**

    Allocate inventory to a specific order line with detailed bin-level tracking.

    **Allocation Features:**
    - Precise quantity allocation per line
    - Optional bin-level allocation details
    - Lot number tracking support
    - Automatic line status update to ALLOCATED

    **Repository Logic:**
    - Updates matching line by `lineNumber` field
    - Sets `allocatedQuantity` and `lineStatus`
    - Stores detailed `allocations` array if provided


    Args:
        world_id (str):
        order_id (str):
        line_id (str):
        body (AllocateWMSOrderLineBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocateWMSOrderLineResponse200
    """

    return sync_detailed(
        world_id=world_id,
        order_id=order_id,
        line_id=line_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    order_id: str,
    line_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AllocateWMSOrderLineBody,
) -> Response[AllocateWMSOrderLineResponse200]:
    """Allocate inventory to specific order line


    **Line-Level Inventory Allocation**

    Allocate inventory to a specific order line with detailed bin-level tracking.

    **Allocation Features:**
    - Precise quantity allocation per line
    - Optional bin-level allocation details
    - Lot number tracking support
    - Automatic line status update to ALLOCATED

    **Repository Logic:**
    - Updates matching line by `lineNumber` field
    - Sets `allocatedQuantity` and `lineStatus`
    - Stores detailed `allocations` array if provided


    Args:
        world_id (str):
        order_id (str):
        line_id (str):
        body (AllocateWMSOrderLineBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AllocateWMSOrderLineResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
        line_id=line_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    order_id: str,
    line_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AllocateWMSOrderLineBody,
) -> Optional[AllocateWMSOrderLineResponse200]:
    """Allocate inventory to specific order line


    **Line-Level Inventory Allocation**

    Allocate inventory to a specific order line with detailed bin-level tracking.

    **Allocation Features:**
    - Precise quantity allocation per line
    - Optional bin-level allocation details
    - Lot number tracking support
    - Automatic line status update to ALLOCATED

    **Repository Logic:**
    - Updates matching line by `lineNumber` field
    - Sets `allocatedQuantity` and `lineStatus`
    - Stores detailed `allocations` array if provided


    Args:
        world_id (str):
        order_id (str):
        line_id (str):
        body (AllocateWMSOrderLineBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AllocateWMSOrderLineResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            order_id=order_id,
            line_id=line_id,
            client=client,
            body=body,
        )
    ).parsed
