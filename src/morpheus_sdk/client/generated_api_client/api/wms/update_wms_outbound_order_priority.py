from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_outbound_order_priority_body import UpdateWMSOutboundOrderPriorityBody
from ...models.update_wms_outbound_order_priority_response_200 import UpdateWMSOutboundOrderPriorityResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    order_id: str,
    *,
    body: UpdateWMSOutboundOrderPriorityBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/outbound-orders/{order_id}/priority",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSOutboundOrderPriorityResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]]:
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
    body: UpdateWMSOutboundOrderPriorityBody,
) -> Response[Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]]:
    """Update outbound order priority


    ## Update WMS Outbound Order Priority

    Update the priority level of an outbound order to expedite or deprioritize fulfillment.

    ### Features
    - **Priority Management**: Change order priority for fulfillment sequencing
    - **Workflow Impact**: Higher priority orders are processed first
    - **Audit Trail**: Priority changes are tracked for reporting

    ### Priority Levels
    - **RUSH**: Highest priority, immediate processing required
    - **URGENT**: High priority, expedited processing
    - **NORMAL**: Standard priority, regular processing
    - **STANDARD**: Lowest priority, process when capacity allows

    ### Use Cases
    - **Customer Escalation**: Elevate priority for VIP customers
    - **Deadline Management**: Rush orders with tight ship dates
    - **Resource Balancing**: Deprioritize orders to manage capacity


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: wms_outbound-order_674565c1234567890abcdef.
        body (UpdateWMSOutboundOrderPriorityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]]
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
    body: UpdateWMSOutboundOrderPriorityBody,
) -> Optional[Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]]:
    """Update outbound order priority


    ## Update WMS Outbound Order Priority

    Update the priority level of an outbound order to expedite or deprioritize fulfillment.

    ### Features
    - **Priority Management**: Change order priority for fulfillment sequencing
    - **Workflow Impact**: Higher priority orders are processed first
    - **Audit Trail**: Priority changes are tracked for reporting

    ### Priority Levels
    - **RUSH**: Highest priority, immediate processing required
    - **URGENT**: High priority, expedited processing
    - **NORMAL**: Standard priority, regular processing
    - **STANDARD**: Lowest priority, process when capacity allows

    ### Use Cases
    - **Customer Escalation**: Elevate priority for VIP customers
    - **Deadline Management**: Rush orders with tight ship dates
    - **Resource Balancing**: Deprioritize orders to manage capacity


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: wms_outbound-order_674565c1234567890abcdef.
        body (UpdateWMSOutboundOrderPriorityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]
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
    body: UpdateWMSOutboundOrderPriorityBody,
) -> Response[Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]]:
    """Update outbound order priority


    ## Update WMS Outbound Order Priority

    Update the priority level of an outbound order to expedite or deprioritize fulfillment.

    ### Features
    - **Priority Management**: Change order priority for fulfillment sequencing
    - **Workflow Impact**: Higher priority orders are processed first
    - **Audit Trail**: Priority changes are tracked for reporting

    ### Priority Levels
    - **RUSH**: Highest priority, immediate processing required
    - **URGENT**: High priority, expedited processing
    - **NORMAL**: Standard priority, regular processing
    - **STANDARD**: Lowest priority, process when capacity allows

    ### Use Cases
    - **Customer Escalation**: Elevate priority for VIP customers
    - **Deadline Management**: Rush orders with tight ship dates
    - **Resource Balancing**: Deprioritize orders to manage capacity


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: wms_outbound-order_674565c1234567890abcdef.
        body (UpdateWMSOutboundOrderPriorityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]]
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
    body: UpdateWMSOutboundOrderPriorityBody,
) -> Optional[Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]]:
    """Update outbound order priority


    ## Update WMS Outbound Order Priority

    Update the priority level of an outbound order to expedite or deprioritize fulfillment.

    ### Features
    - **Priority Management**: Change order priority for fulfillment sequencing
    - **Workflow Impact**: Higher priority orders are processed first
    - **Audit Trail**: Priority changes are tracked for reporting

    ### Priority Levels
    - **RUSH**: Highest priority, immediate processing required
    - **URGENT**: High priority, expedited processing
    - **NORMAL**: Standard priority, regular processing
    - **STANDARD**: Lowest priority, process when capacity allows

    ### Use Cases
    - **Customer Escalation**: Elevate priority for VIP customers
    - **Deadline Management**: Rush orders with tight ship dates
    - **Resource Balancing**: Deprioritize orders to manage capacity


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: wms_outbound-order_674565c1234567890abcdef.
        body (UpdateWMSOutboundOrderPriorityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSOutboundOrderPriorityResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
