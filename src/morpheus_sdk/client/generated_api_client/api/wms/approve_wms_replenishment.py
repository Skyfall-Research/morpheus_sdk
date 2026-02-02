from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.approve_wms_replenishment_body import ApproveWMSReplenishmentBody
from ...models.approve_wms_replenishment_response_200 import ApproveWMSReplenishmentResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    replenishment_id: str,
    *,
    body: ApproveWMSReplenishmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/replenishments/{replenishment_id}/approve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ApproveWMSReplenishmentResponse200]:
    if response.status_code == 200:
        response_200 = ApproveWMSReplenishmentResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ApproveWMSReplenishmentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    replenishment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApproveWMSReplenishmentBody,
) -> Response[ApproveWMSReplenishmentResponse200]:
    """Approve replenishment


    ## Approve Replenishment Request

    Approve a suggested replenishment with optional quantity adjustments.

    **Business Process:**
    - Changes status from SUGGESTED to APPROVED
    - Sets approval metadata (approvedBy, approvedDate)
    - Allows quantity adjustments from original suggestion
    - Triggers downstream workflow processes

    **Use Cases:**
    - Management approval workflows
    - Quantity adjustment and optimization
    - Approval audit trail maintenance
    - Integration with approval systems


    Args:
        world_id (str):
        replenishment_id (str):
        body (ApproveWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApproveWMSReplenishmentResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        replenishment_id=replenishment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    replenishment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApproveWMSReplenishmentBody,
) -> Optional[ApproveWMSReplenishmentResponse200]:
    """Approve replenishment


    ## Approve Replenishment Request

    Approve a suggested replenishment with optional quantity adjustments.

    **Business Process:**
    - Changes status from SUGGESTED to APPROVED
    - Sets approval metadata (approvedBy, approvedDate)
    - Allows quantity adjustments from original suggestion
    - Triggers downstream workflow processes

    **Use Cases:**
    - Management approval workflows
    - Quantity adjustment and optimization
    - Approval audit trail maintenance
    - Integration with approval systems


    Args:
        world_id (str):
        replenishment_id (str):
        body (ApproveWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApproveWMSReplenishmentResponse200
    """

    return sync_detailed(
        world_id=world_id,
        replenishment_id=replenishment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    replenishment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApproveWMSReplenishmentBody,
) -> Response[ApproveWMSReplenishmentResponse200]:
    """Approve replenishment


    ## Approve Replenishment Request

    Approve a suggested replenishment with optional quantity adjustments.

    **Business Process:**
    - Changes status from SUGGESTED to APPROVED
    - Sets approval metadata (approvedBy, approvedDate)
    - Allows quantity adjustments from original suggestion
    - Triggers downstream workflow processes

    **Use Cases:**
    - Management approval workflows
    - Quantity adjustment and optimization
    - Approval audit trail maintenance
    - Integration with approval systems


    Args:
        world_id (str):
        replenishment_id (str):
        body (ApproveWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ApproveWMSReplenishmentResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        replenishment_id=replenishment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    replenishment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ApproveWMSReplenishmentBody,
) -> Optional[ApproveWMSReplenishmentResponse200]:
    """Approve replenishment


    ## Approve Replenishment Request

    Approve a suggested replenishment with optional quantity adjustments.

    **Business Process:**
    - Changes status from SUGGESTED to APPROVED
    - Sets approval metadata (approvedBy, approvedDate)
    - Allows quantity adjustments from original suggestion
    - Triggers downstream workflow processes

    **Use Cases:**
    - Management approval workflows
    - Quantity adjustment and optimization
    - Approval audit trail maintenance
    - Integration with approval systems


    Args:
        world_id (str):
        replenishment_id (str):
        body (ApproveWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ApproveWMSReplenishmentResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            replenishment_id=replenishment_id,
            client=client,
            body=body,
        )
    ).parsed
