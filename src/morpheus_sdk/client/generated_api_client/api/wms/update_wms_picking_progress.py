from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_wms_picking_progress_body import UpdateWMSPickingProgressBody
from ...models.update_wms_picking_progress_response_200 import UpdateWMSPickingProgressResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    order_id: str,
    *,
    body: UpdateWMSPickingProgressBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/outbound-orders/{order_id}/picking-progress",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateWMSPickingProgressResponse200]:
    if response.status_code == 200:
        response_200 = UpdateWMSPickingProgressResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateWMSPickingProgressResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSPickingProgressBody,
) -> Response[UpdateWMSPickingProgressResponse200]:
    r"""Update picked quantities for order lines


    **Picking Progress Tracking**

    Update picked quantities with automatic line status management.

    **Status Logic:**
    - `pickedQuantity > 0` → Line status becomes \"PICKED\"
    - `pickedQuantity = 0` → Line status remains \"PICKING\"

    **Use Cases:**
    - Real-time picking progress updates
    - Partial picking scenarios
    - Pick completion confirmation


    Args:
        world_id (str):
        order_id (str):
        body (UpdateWMSPickingProgressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWMSPickingProgressResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSPickingProgressBody,
) -> Optional[UpdateWMSPickingProgressResponse200]:
    r"""Update picked quantities for order lines


    **Picking Progress Tracking**

    Update picked quantities with automatic line status management.

    **Status Logic:**
    - `pickedQuantity > 0` → Line status becomes \"PICKED\"
    - `pickedQuantity = 0` → Line status remains \"PICKING\"

    **Use Cases:**
    - Real-time picking progress updates
    - Partial picking scenarios
    - Pick completion confirmation


    Args:
        world_id (str):
        order_id (str):
        body (UpdateWMSPickingProgressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWMSPickingProgressResponse200
    """

    return sync_detailed(
        world_id=world_id,
        order_id=order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSPickingProgressBody,
) -> Response[UpdateWMSPickingProgressResponse200]:
    r"""Update picked quantities for order lines


    **Picking Progress Tracking**

    Update picked quantities with automatic line status management.

    **Status Logic:**
    - `pickedQuantity > 0` → Line status becomes \"PICKED\"
    - `pickedQuantity = 0` → Line status remains \"PICKING\"

    **Use Cases:**
    - Real-time picking progress updates
    - Partial picking scenarios
    - Pick completion confirmation


    Args:
        world_id (str):
        order_id (str):
        body (UpdateWMSPickingProgressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateWMSPickingProgressResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSPickingProgressBody,
) -> Optional[UpdateWMSPickingProgressResponse200]:
    r"""Update picked quantities for order lines


    **Picking Progress Tracking**

    Update picked quantities with automatic line status management.

    **Status Logic:**
    - `pickedQuantity > 0` → Line status becomes \"PICKED\"
    - `pickedQuantity = 0` → Line status remains \"PICKING\"

    **Use Cases:**
    - Real-time picking progress updates
    - Partial picking scenarios
    - Pick completion confirmation


    Args:
        world_id (str):
        order_id (str):
        body (UpdateWMSPickingProgressBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateWMSPickingProgressResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
