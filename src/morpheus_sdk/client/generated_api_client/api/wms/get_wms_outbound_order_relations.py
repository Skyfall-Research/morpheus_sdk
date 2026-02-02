from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_outbound_order_relations_response_200 import GetWMSOutboundOrderRelationsResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    order_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/outbound-orders/{order_id}/relations",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSOutboundOrderRelationsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]]:
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
) -> Response[Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]]:
    """Get outbound order cross-service relations


    ## Get WMS Outbound Order Relations

    Retrieve cross-service related data for an outbound order, including linked ERP orders, EDI
    documents, and finance transactions.

    ### Features
    - **ERP Integration**: Link to source ERP sales order
    - **EDI Documents**: Related EDI transactions (850 PO, 810 Invoice, etc.)
    - **Finance Tracking**: Associated payment_in finance transactions
    - **Cross-Reference**: Connect warehouse fulfillment to enterprise systems

    ### Related Data Types
    - **erpOrder**: Original ERP sales order with status and amount
    - **ediDocuments**: EDI documents (purchase orders, invoices) linked to the order
    - **financeTransaction**: Payment transactions associated with the order

    ### Business Logic
    - Uses order number to find related ERP order
    - Searches EDI documents by businessDocumentNumber or customer ID
    - Finds finance transactions with matching sourceId
    - Returns empty arrays/undefined for missing relations

    ### Use Cases
    - **Order Traceability**: Track order from sales to fulfillment to payment
    - **EDI Reconciliation**: View related EDI documents for compliance
    - **Finance Integration**: Link fulfillment to accounts receivable
    - **Audit Trail**: Complete visibility across enterprise systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: wms_outbound-order_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
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
) -> Optional[Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]]:
    """Get outbound order cross-service relations


    ## Get WMS Outbound Order Relations

    Retrieve cross-service related data for an outbound order, including linked ERP orders, EDI
    documents, and finance transactions.

    ### Features
    - **ERP Integration**: Link to source ERP sales order
    - **EDI Documents**: Related EDI transactions (850 PO, 810 Invoice, etc.)
    - **Finance Tracking**: Associated payment_in finance transactions
    - **Cross-Reference**: Connect warehouse fulfillment to enterprise systems

    ### Related Data Types
    - **erpOrder**: Original ERP sales order with status and amount
    - **ediDocuments**: EDI documents (purchase orders, invoices) linked to the order
    - **financeTransaction**: Payment transactions associated with the order

    ### Business Logic
    - Uses order number to find related ERP order
    - Searches EDI documents by businessDocumentNumber or customer ID
    - Finds finance transactions with matching sourceId
    - Returns empty arrays/undefined for missing relations

    ### Use Cases
    - **Order Traceability**: Track order from sales to fulfillment to payment
    - **EDI Reconciliation**: View related EDI documents for compliance
    - **Finance Integration**: Link fulfillment to accounts receivable
    - **Audit Trail**: Complete visibility across enterprise systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: wms_outbound-order_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]]:
    """Get outbound order cross-service relations


    ## Get WMS Outbound Order Relations

    Retrieve cross-service related data for an outbound order, including linked ERP orders, EDI
    documents, and finance transactions.

    ### Features
    - **ERP Integration**: Link to source ERP sales order
    - **EDI Documents**: Related EDI transactions (850 PO, 810 Invoice, etc.)
    - **Finance Tracking**: Associated payment_in finance transactions
    - **Cross-Reference**: Connect warehouse fulfillment to enterprise systems

    ### Related Data Types
    - **erpOrder**: Original ERP sales order with status and amount
    - **ediDocuments**: EDI documents (purchase orders, invoices) linked to the order
    - **financeTransaction**: Payment transactions associated with the order

    ### Business Logic
    - Uses order number to find related ERP order
    - Searches EDI documents by businessDocumentNumber or customer ID
    - Finds finance transactions with matching sourceId
    - Returns empty arrays/undefined for missing relations

    ### Use Cases
    - **Order Traceability**: Track order from sales to fulfillment to payment
    - **EDI Reconciliation**: View related EDI documents for compliance
    - **Finance Integration**: Link fulfillment to accounts receivable
    - **Audit Trail**: Complete visibility across enterprise systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: wms_outbound-order_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]]:
    """Get outbound order cross-service relations


    ## Get WMS Outbound Order Relations

    Retrieve cross-service related data for an outbound order, including linked ERP orders, EDI
    documents, and finance transactions.

    ### Features
    - **ERP Integration**: Link to source ERP sales order
    - **EDI Documents**: Related EDI transactions (850 PO, 810 Invoice, etc.)
    - **Finance Tracking**: Associated payment_in finance transactions
    - **Cross-Reference**: Connect warehouse fulfillment to enterprise systems

    ### Related Data Types
    - **erpOrder**: Original ERP sales order with status and amount
    - **ediDocuments**: EDI documents (purchase orders, invoices) linked to the order
    - **financeTransaction**: Payment transactions associated with the order

    ### Business Logic
    - Uses order number to find related ERP order
    - Searches EDI documents by businessDocumentNumber or customer ID
    - Finds finance transactions with matching sourceId
    - Returns empty arrays/undefined for missing relations

    ### Use Cases
    - **Order Traceability**: Track order from sales to fulfillment to payment
    - **EDI Reconciliation**: View related EDI documents for compliance
    - **Finance Integration**: Link fulfillment to accounts receivable
    - **Audit Trail**: Complete visibility across enterprise systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: wms_outbound-order_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSOutboundOrderRelationsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            order_id=order_id,
            client=client,
        )
    ).parsed
