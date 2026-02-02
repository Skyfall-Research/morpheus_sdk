from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_erp_shipment_document_body import AddERPShipmentDocumentBody
from ...models.add_erp_shipment_document_response_200 import AddERPShipmentDocumentResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: AddERPShipmentDocumentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/erp/shipments/{shipment_id}/documents",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddERPShipmentDocumentResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddERPShipmentDocumentResponse200.from_dict(response.json())

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
) -> Response[Union[AddERPShipmentDocumentResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddERPShipmentDocumentBody,
) -> Response[Union[AddERPShipmentDocumentResponse200, ErrorResponse]]:
    """Add ERP shipment document


    Add document URL to ERP shipment for comprehensive documentation and compliance tracking.

    **Core Features**:
    - **Document Management**: Attach documents to shipments for reference
    - **URL Storage**: Store document URLs for bills of lading, labels, and certificates
    - **Compliance Support**: Maintain required shipping documentation
    - **Integration Ready**: Support for document management system integration

    **Use Cases**:
    - **Shipping Labels**: Attach shipping label URLs for carrier pickup
    - **Bills of Lading**: Store BOL documents for freight shipments
    - **Customs Documentation**: Attach customs forms for international shipments
    - **Compliance**: Maintain required shipping and regulatory documentation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (AddERPShipmentDocumentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddERPShipmentDocumentResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddERPShipmentDocumentBody,
) -> Optional[Union[AddERPShipmentDocumentResponse200, ErrorResponse]]:
    """Add ERP shipment document


    Add document URL to ERP shipment for comprehensive documentation and compliance tracking.

    **Core Features**:
    - **Document Management**: Attach documents to shipments for reference
    - **URL Storage**: Store document URLs for bills of lading, labels, and certificates
    - **Compliance Support**: Maintain required shipping documentation
    - **Integration Ready**: Support for document management system integration

    **Use Cases**:
    - **Shipping Labels**: Attach shipping label URLs for carrier pickup
    - **Bills of Lading**: Store BOL documents for freight shipments
    - **Customs Documentation**: Attach customs forms for international shipments
    - **Compliance**: Maintain required shipping and regulatory documentation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (AddERPShipmentDocumentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddERPShipmentDocumentResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        shipment_id=shipment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddERPShipmentDocumentBody,
) -> Response[Union[AddERPShipmentDocumentResponse200, ErrorResponse]]:
    """Add ERP shipment document


    Add document URL to ERP shipment for comprehensive documentation and compliance tracking.

    **Core Features**:
    - **Document Management**: Attach documents to shipments for reference
    - **URL Storage**: Store document URLs for bills of lading, labels, and certificates
    - **Compliance Support**: Maintain required shipping documentation
    - **Integration Ready**: Support for document management system integration

    **Use Cases**:
    - **Shipping Labels**: Attach shipping label URLs for carrier pickup
    - **Bills of Lading**: Store BOL documents for freight shipments
    - **Customs Documentation**: Attach customs forms for international shipments
    - **Compliance**: Maintain required shipping and regulatory documentation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (AddERPShipmentDocumentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddERPShipmentDocumentResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddERPShipmentDocumentBody,
) -> Optional[Union[AddERPShipmentDocumentResponse200, ErrorResponse]]:
    """Add ERP shipment document


    Add document URL to ERP shipment for comprehensive documentation and compliance tracking.

    **Core Features**:
    - **Document Management**: Attach documents to shipments for reference
    - **URL Storage**: Store document URLs for bills of lading, labels, and certificates
    - **Compliance Support**: Maintain required shipping documentation
    - **Integration Ready**: Support for document management system integration

    **Use Cases**:
    - **Shipping Labels**: Attach shipping label URLs for carrier pickup
    - **Bills of Lading**: Store BOL documents for freight shipments
    - **Customs Documentation**: Attach customs forms for international shipments
    - **Compliance**: Maintain required shipping and regulatory documentation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (AddERPShipmentDocumentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddERPShipmentDocumentResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
