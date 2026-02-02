from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_outbound_order_body import CreateWMSOutboundOrderBody
from ...models.create_wms_outbound_order_response_201 import CreateWMSOutboundOrderResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSOutboundOrderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/outbound-orders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSOutboundOrderResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSOutboundOrderResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWMSOutboundOrderResponse201, ErrorResponse]]:
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
    body: CreateWMSOutboundOrderBody,
) -> Response[Union[CreateWMSOutboundOrderResponse201, ErrorResponse]]:
    """Create new outbound order


    **Create New Outbound Order**

    Creates a new outbound order for warehouse fulfillment with comprehensive line item management.

    **Key Features:**
    - Multi-line order support with detailed product specifications
    - Customer and shipping address management
    - Priority-based order classification
    - Integrated timing workflow tracking
    - Warehouse-scoped order processing

    **Validation Requirements:**
    - warehouseId, orderNumber, and lines array are required
    - orderNumber must be unique within world scope
    - lines array must contain at least one item

    **Business Workflow:**
    1. Order created in PENDING status
    2. Released to warehouse (RELEASED status)
    3. Inventory allocated (ALLOCATED status)
    4. Picking process (PICKING → PICKED)
    5. Packing and shipping (PACKED → SHIPPED)


    Args:
        world_id (str):
        body (CreateWMSOutboundOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSOutboundOrderResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSOutboundOrderBody,
) -> Optional[Union[CreateWMSOutboundOrderResponse201, ErrorResponse]]:
    """Create new outbound order


    **Create New Outbound Order**

    Creates a new outbound order for warehouse fulfillment with comprehensive line item management.

    **Key Features:**
    - Multi-line order support with detailed product specifications
    - Customer and shipping address management
    - Priority-based order classification
    - Integrated timing workflow tracking
    - Warehouse-scoped order processing

    **Validation Requirements:**
    - warehouseId, orderNumber, and lines array are required
    - orderNumber must be unique within world scope
    - lines array must contain at least one item

    **Business Workflow:**
    1. Order created in PENDING status
    2. Released to warehouse (RELEASED status)
    3. Inventory allocated (ALLOCATED status)
    4. Picking process (PICKING → PICKED)
    5. Packing and shipping (PACKED → SHIPPED)


    Args:
        world_id (str):
        body (CreateWMSOutboundOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSOutboundOrderResponse201, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSOutboundOrderBody,
) -> Response[Union[CreateWMSOutboundOrderResponse201, ErrorResponse]]:
    """Create new outbound order


    **Create New Outbound Order**

    Creates a new outbound order for warehouse fulfillment with comprehensive line item management.

    **Key Features:**
    - Multi-line order support with detailed product specifications
    - Customer and shipping address management
    - Priority-based order classification
    - Integrated timing workflow tracking
    - Warehouse-scoped order processing

    **Validation Requirements:**
    - warehouseId, orderNumber, and lines array are required
    - orderNumber must be unique within world scope
    - lines array must contain at least one item

    **Business Workflow:**
    1. Order created in PENDING status
    2. Released to warehouse (RELEASED status)
    3. Inventory allocated (ALLOCATED status)
    4. Picking process (PICKING → PICKED)
    5. Packing and shipping (PACKED → SHIPPED)


    Args:
        world_id (str):
        body (CreateWMSOutboundOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSOutboundOrderResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSOutboundOrderBody,
) -> Optional[Union[CreateWMSOutboundOrderResponse201, ErrorResponse]]:
    """Create new outbound order


    **Create New Outbound Order**

    Creates a new outbound order for warehouse fulfillment with comprehensive line item management.

    **Key Features:**
    - Multi-line order support with detailed product specifications
    - Customer and shipping address management
    - Priority-based order classification
    - Integrated timing workflow tracking
    - Warehouse-scoped order processing

    **Validation Requirements:**
    - warehouseId, orderNumber, and lines array are required
    - orderNumber must be unique within world scope
    - lines array must contain at least one item

    **Business Workflow:**
    1. Order created in PENDING status
    2. Released to warehouse (RELEASED status)
    3. Inventory allocated (ALLOCATED status)
    4. Picking process (PICKING → PICKED)
    5. Packing and shipping (PACKED → SHIPPED)


    Args:
        world_id (str):
        body (CreateWMSOutboundOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSOutboundOrderResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
