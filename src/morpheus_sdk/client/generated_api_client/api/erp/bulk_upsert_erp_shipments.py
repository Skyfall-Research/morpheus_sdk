from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_upsert_erp_shipments_body import BulkUpsertERPShipmentsBody
from ...models.bulk_upsert_erp_shipments_response_200 import BulkUpsertERPShipmentsResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: BulkUpsertERPShipmentsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/erp/shipments/bulk",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = BulkUpsertERPShipmentsResponse200.from_dict(response.json())

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
) -> Response[Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]]:
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
    body: BulkUpsertERPShipmentsBody,
) -> Response[Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]]:
    """Bulk upsert ERP shipments


    Perform bulk upsert operations on multiple ERP shipments for efficient data management.

    **Core Features**:
    - **Bulk Operations**: Process multiple shipments in a single transaction
    - **Upsert Logic**: Insert new shipments or update existing ones
    - **Performance Optimized**: Efficient bulk processing for large datasets
    - **Atomic Operations**: Ensures data consistency across bulk operations

    **Use Cases**:
    - **Data Migration**: Import large shipment datasets from external systems
    - **EDI Processing**: Bulk processing of EDI 856 shipment notices
    - **System Integration**: Synchronize shipments from multiple sources
    - **Performance**: High-volume shipment processing operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (BulkUpsertERPShipmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]]
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
    body: BulkUpsertERPShipmentsBody,
) -> Optional[Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]]:
    """Bulk upsert ERP shipments


    Perform bulk upsert operations on multiple ERP shipments for efficient data management.

    **Core Features**:
    - **Bulk Operations**: Process multiple shipments in a single transaction
    - **Upsert Logic**: Insert new shipments or update existing ones
    - **Performance Optimized**: Efficient bulk processing for large datasets
    - **Atomic Operations**: Ensures data consistency across bulk operations

    **Use Cases**:
    - **Data Migration**: Import large shipment datasets from external systems
    - **EDI Processing**: Bulk processing of EDI 856 shipment notices
    - **System Integration**: Synchronize shipments from multiple sources
    - **Performance**: High-volume shipment processing operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (BulkUpsertERPShipmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]
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
    body: BulkUpsertERPShipmentsBody,
) -> Response[Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]]:
    """Bulk upsert ERP shipments


    Perform bulk upsert operations on multiple ERP shipments for efficient data management.

    **Core Features**:
    - **Bulk Operations**: Process multiple shipments in a single transaction
    - **Upsert Logic**: Insert new shipments or update existing ones
    - **Performance Optimized**: Efficient bulk processing for large datasets
    - **Atomic Operations**: Ensures data consistency across bulk operations

    **Use Cases**:
    - **Data Migration**: Import large shipment datasets from external systems
    - **EDI Processing**: Bulk processing of EDI 856 shipment notices
    - **System Integration**: Synchronize shipments from multiple sources
    - **Performance**: High-volume shipment processing operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (BulkUpsertERPShipmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]]
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
    body: BulkUpsertERPShipmentsBody,
) -> Optional[Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]]:
    """Bulk upsert ERP shipments


    Perform bulk upsert operations on multiple ERP shipments for efficient data management.

    **Core Features**:
    - **Bulk Operations**: Process multiple shipments in a single transaction
    - **Upsert Logic**: Insert new shipments or update existing ones
    - **Performance Optimized**: Efficient bulk processing for large datasets
    - **Atomic Operations**: Ensures data consistency across bulk operations

    **Use Cases**:
    - **Data Migration**: Import large shipment datasets from external systems
    - **EDI Processing**: Bulk processing of EDI 856 shipment notices
    - **System Integration**: Synchronize shipments from multiple sources
    - **Performance**: High-volume shipment processing operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (BulkUpsertERPShipmentsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkUpsertERPShipmentsResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
