from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inventory_transactions_by_reference_response_200 import (
    GetWMSInventoryTransactionsByReferenceResponse200,
)
from ...types import Response


def _get_kwargs(
    world_id: str,
    reference_type: str,
    reference_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inventory-transactions/reference/{reference_type}/{reference_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInventoryTransactionsByReferenceResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    reference_type: str,
    reference_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]]:
    """Get transactions by reference


    ## Get Transactions by Reference

    Retrieve inventory transactions associated with a specific reference document (e.g., Order, PO).

    ### Features
    - **Reference-Based Filtering**: All transactions linked to specific orders, tasks, or counts
    - **Cross-Document Tracking**: Link inventory movements to their originating documents
    - **Complete Transaction Trail**: See all inventory impacts from a single reference
    - **Multi-Reference Support**: Support for PO, ORDER, TASK, CYCLE_COUNT references

    ### Business Logic
    - Filters transactions where referenceType and referenceId match parameters
    - Results ordered by transaction date (newest first)
    - Includes all transaction types linked to the reference document

    ### Use Cases
    - **Order Impact Analysis**: See all inventory transactions for specific orders
    - **Task Completion Tracking**: Review inventory movements from warehouse tasks
    - **Cycle Count Adjustments**: Track adjustments made from cycle count results
    - **Purchase Order Receiving**: Monitor all receipts against purchase orders
    - **Audit Trail**: Complete inventory transaction history for reference documents


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        reference_type (str):
        reference_id (str):  Example: ORD-2024-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        reference_type=reference_type,
        reference_id=reference_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    reference_type: str,
    reference_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]]:
    """Get transactions by reference


    ## Get Transactions by Reference

    Retrieve inventory transactions associated with a specific reference document (e.g., Order, PO).

    ### Features
    - **Reference-Based Filtering**: All transactions linked to specific orders, tasks, or counts
    - **Cross-Document Tracking**: Link inventory movements to their originating documents
    - **Complete Transaction Trail**: See all inventory impacts from a single reference
    - **Multi-Reference Support**: Support for PO, ORDER, TASK, CYCLE_COUNT references

    ### Business Logic
    - Filters transactions where referenceType and referenceId match parameters
    - Results ordered by transaction date (newest first)
    - Includes all transaction types linked to the reference document

    ### Use Cases
    - **Order Impact Analysis**: See all inventory transactions for specific orders
    - **Task Completion Tracking**: Review inventory movements from warehouse tasks
    - **Cycle Count Adjustments**: Track adjustments made from cycle count results
    - **Purchase Order Receiving**: Monitor all receipts against purchase orders
    - **Audit Trail**: Complete inventory transaction history for reference documents


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        reference_type (str):
        reference_id (str):  Example: ORD-2024-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        reference_type=reference_type,
        reference_id=reference_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    reference_type: str,
    reference_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]]:
    """Get transactions by reference


    ## Get Transactions by Reference

    Retrieve inventory transactions associated with a specific reference document (e.g., Order, PO).

    ### Features
    - **Reference-Based Filtering**: All transactions linked to specific orders, tasks, or counts
    - **Cross-Document Tracking**: Link inventory movements to their originating documents
    - **Complete Transaction Trail**: See all inventory impacts from a single reference
    - **Multi-Reference Support**: Support for PO, ORDER, TASK, CYCLE_COUNT references

    ### Business Logic
    - Filters transactions where referenceType and referenceId match parameters
    - Results ordered by transaction date (newest first)
    - Includes all transaction types linked to the reference document

    ### Use Cases
    - **Order Impact Analysis**: See all inventory transactions for specific orders
    - **Task Completion Tracking**: Review inventory movements from warehouse tasks
    - **Cycle Count Adjustments**: Track adjustments made from cycle count results
    - **Purchase Order Receiving**: Monitor all receipts against purchase orders
    - **Audit Trail**: Complete inventory transaction history for reference documents


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        reference_type (str):
        reference_id (str):  Example: ORD-2024-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        reference_type=reference_type,
        reference_id=reference_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    reference_type: str,
    reference_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]]:
    """Get transactions by reference


    ## Get Transactions by Reference

    Retrieve inventory transactions associated with a specific reference document (e.g., Order, PO).

    ### Features
    - **Reference-Based Filtering**: All transactions linked to specific orders, tasks, or counts
    - **Cross-Document Tracking**: Link inventory movements to their originating documents
    - **Complete Transaction Trail**: See all inventory impacts from a single reference
    - **Multi-Reference Support**: Support for PO, ORDER, TASK, CYCLE_COUNT references

    ### Business Logic
    - Filters transactions where referenceType and referenceId match parameters
    - Results ordered by transaction date (newest first)
    - Includes all transaction types linked to the reference document

    ### Use Cases
    - **Order Impact Analysis**: See all inventory transactions for specific orders
    - **Task Completion Tracking**: Review inventory movements from warehouse tasks
    - **Cycle Count Adjustments**: Track adjustments made from cycle count results
    - **Purchase Order Receiving**: Monitor all receipts against purchase orders
    - **Audit Trail**: Complete inventory transaction history for reference documents


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        reference_type (str):
        reference_id (str):  Example: ORD-2024-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryTransactionsByReferenceResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            reference_type=reference_type,
            reference_id=reference_id,
            client=client,
        )
    ).parsed
