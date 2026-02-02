from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_replenishment_body import CreateWMSReplenishmentBody
from ...models.create_wms_replenishment_response_201 import CreateWMSReplenishmentResponse201
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSReplenishmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/replenishments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CreateWMSReplenishmentResponse201]:
    if response.status_code == 201:
        response_201 = CreateWMSReplenishmentResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CreateWMSReplenishmentResponse201]:
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
    body: CreateWMSReplenishmentBody,
) -> Response[CreateWMSReplenishmentResponse201]:
    """Create replenishment


    ## Create WMS Replenishment

    Creates a new inventory replenishment request for moving stock between bins.

    **Business Process:**
    - Creates replenishment suggestion with from/to bin movement
    - Sets initial status to SUGGESTED
    - Validates bin availability and capacity constraints
    - Supports various replenishment types (MIN_MAX, DEMAND, CYCLE)

    **Use Cases:**
    - Automatic stock replenishment based on min/max levels
    - Demand-driven replenishment for picking zones
    - Cycle-based replenishment scheduling
    - Manual replenishment requests

    **Field Mapping:**
    - Uses `replenishmentId` as primary identifier (consistent with model)
    - Complex nested `fromBin` and `toBin` structures with availability tracking
    - Quantity object with suggested/approved/actual values


    Args:
        world_id (str):
        body (CreateWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWMSReplenishmentResponse201]
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
    body: CreateWMSReplenishmentBody,
) -> Optional[CreateWMSReplenishmentResponse201]:
    """Create replenishment


    ## Create WMS Replenishment

    Creates a new inventory replenishment request for moving stock between bins.

    **Business Process:**
    - Creates replenishment suggestion with from/to bin movement
    - Sets initial status to SUGGESTED
    - Validates bin availability and capacity constraints
    - Supports various replenishment types (MIN_MAX, DEMAND, CYCLE)

    **Use Cases:**
    - Automatic stock replenishment based on min/max levels
    - Demand-driven replenishment for picking zones
    - Cycle-based replenishment scheduling
    - Manual replenishment requests

    **Field Mapping:**
    - Uses `replenishmentId` as primary identifier (consistent with model)
    - Complex nested `fromBin` and `toBin` structures with availability tracking
    - Quantity object with suggested/approved/actual values


    Args:
        world_id (str):
        body (CreateWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWMSReplenishmentResponse201
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
    body: CreateWMSReplenishmentBody,
) -> Response[CreateWMSReplenishmentResponse201]:
    """Create replenishment


    ## Create WMS Replenishment

    Creates a new inventory replenishment request for moving stock between bins.

    **Business Process:**
    - Creates replenishment suggestion with from/to bin movement
    - Sets initial status to SUGGESTED
    - Validates bin availability and capacity constraints
    - Supports various replenishment types (MIN_MAX, DEMAND, CYCLE)

    **Use Cases:**
    - Automatic stock replenishment based on min/max levels
    - Demand-driven replenishment for picking zones
    - Cycle-based replenishment scheduling
    - Manual replenishment requests

    **Field Mapping:**
    - Uses `replenishmentId` as primary identifier (consistent with model)
    - Complex nested `fromBin` and `toBin` structures with availability tracking
    - Quantity object with suggested/approved/actual values


    Args:
        world_id (str):
        body (CreateWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateWMSReplenishmentResponse201]
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
    body: CreateWMSReplenishmentBody,
) -> Optional[CreateWMSReplenishmentResponse201]:
    """Create replenishment


    ## Create WMS Replenishment

    Creates a new inventory replenishment request for moving stock between bins.

    **Business Process:**
    - Creates replenishment suggestion with from/to bin movement
    - Sets initial status to SUGGESTED
    - Validates bin availability and capacity constraints
    - Supports various replenishment types (MIN_MAX, DEMAND, CYCLE)

    **Use Cases:**
    - Automatic stock replenishment based on min/max levels
    - Demand-driven replenishment for picking zones
    - Cycle-based replenishment scheduling
    - Manual replenishment requests

    **Field Mapping:**
    - Uses `replenishmentId` as primary identifier (consistent with model)
    - Complex nested `fromBin` and `toBin` structures with availability tracking
    - Quantity object with suggested/approved/actual values


    Args:
        world_id (str):
        body (CreateWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateWMSReplenishmentResponse201
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
