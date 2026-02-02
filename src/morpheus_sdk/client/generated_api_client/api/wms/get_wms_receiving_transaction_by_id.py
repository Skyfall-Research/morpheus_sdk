from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_receiving_transaction_by_id_response_200 import GetWMSReceivingTransactionByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    transaction_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/receiving-transactions/{transaction_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSReceivingTransactionByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]]:
    """Get receiving transaction by ID


    ## Get WMS Receiving Transaction by ID

    Retrieve a specific receiving transaction with complete details including quality control, damage
    assessment, and putaway information.

    ### Features
    - **Complete Transaction Details**: Full transaction record with all nested data
    - **Quality Control Information**: Inspection results and quality status
    - **Damage Documentation**: Comprehensive damage assessment details
    - **Putaway Tracking**: Location assignment and putaway progress
    - **Item-Level Details**: Detailed product and quantity information
    - **Audit Information**: Creation, update, and status change tracking

    ### Response Data Includes
    - **Transaction Metadata**: IDs, references, and timestamps
    - **Product Information**: SKU, product name, quantities, and UOM
    - **Quality Control**: Inspection status, inspector, and notes
    - **Damage Assessment**: Damage flags, descriptions, and quantities
    - **Putaway Details**: Location assignments and instructions
    - **Status Information**: Current status and workflow progression
    - **Custom Fields**: Additional configurable data points

    **CRITICAL NOTE**: The URL parameter uses 'transactionId' but the model field is 'receivingId'. This
    reflects actual implementation behavior.

    ### Use Cases
    - **Transaction Details View**: Complete receiving transaction information
    - **Quality Control Review**: Access quality inspection results
    - **Damage Assessment**: Review damage documentation and claims
    - **Putaway Coordination**: Check location assignments and instructions
    - **Audit and Compliance**: Transaction traceability and documentation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        transaction_id=transaction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]]:
    """Get receiving transaction by ID


    ## Get WMS Receiving Transaction by ID

    Retrieve a specific receiving transaction with complete details including quality control, damage
    assessment, and putaway information.

    ### Features
    - **Complete Transaction Details**: Full transaction record with all nested data
    - **Quality Control Information**: Inspection results and quality status
    - **Damage Documentation**: Comprehensive damage assessment details
    - **Putaway Tracking**: Location assignment and putaway progress
    - **Item-Level Details**: Detailed product and quantity information
    - **Audit Information**: Creation, update, and status change tracking

    ### Response Data Includes
    - **Transaction Metadata**: IDs, references, and timestamps
    - **Product Information**: SKU, product name, quantities, and UOM
    - **Quality Control**: Inspection status, inspector, and notes
    - **Damage Assessment**: Damage flags, descriptions, and quantities
    - **Putaway Details**: Location assignments and instructions
    - **Status Information**: Current status and workflow progression
    - **Custom Fields**: Additional configurable data points

    **CRITICAL NOTE**: The URL parameter uses 'transactionId' but the model field is 'receivingId'. This
    reflects actual implementation behavior.

    ### Use Cases
    - **Transaction Details View**: Complete receiving transaction information
    - **Quality Control Review**: Access quality inspection results
    - **Damage Assessment**: Review damage documentation and claims
    - **Putaway Coordination**: Check location assignments and instructions
    - **Audit and Compliance**: Transaction traceability and documentation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        transaction_id=transaction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]]:
    """Get receiving transaction by ID


    ## Get WMS Receiving Transaction by ID

    Retrieve a specific receiving transaction with complete details including quality control, damage
    assessment, and putaway information.

    ### Features
    - **Complete Transaction Details**: Full transaction record with all nested data
    - **Quality Control Information**: Inspection results and quality status
    - **Damage Documentation**: Comprehensive damage assessment details
    - **Putaway Tracking**: Location assignment and putaway progress
    - **Item-Level Details**: Detailed product and quantity information
    - **Audit Information**: Creation, update, and status change tracking

    ### Response Data Includes
    - **Transaction Metadata**: IDs, references, and timestamps
    - **Product Information**: SKU, product name, quantities, and UOM
    - **Quality Control**: Inspection status, inspector, and notes
    - **Damage Assessment**: Damage flags, descriptions, and quantities
    - **Putaway Details**: Location assignments and instructions
    - **Status Information**: Current status and workflow progression
    - **Custom Fields**: Additional configurable data points

    **CRITICAL NOTE**: The URL parameter uses 'transactionId' but the model field is 'receivingId'. This
    reflects actual implementation behavior.

    ### Use Cases
    - **Transaction Details View**: Complete receiving transaction information
    - **Quality Control Review**: Access quality inspection results
    - **Damage Assessment**: Review damage documentation and claims
    - **Putaway Coordination**: Check location assignments and instructions
    - **Audit and Compliance**: Transaction traceability and documentation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        transaction_id=transaction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]]:
    """Get receiving transaction by ID


    ## Get WMS Receiving Transaction by ID

    Retrieve a specific receiving transaction with complete details including quality control, damage
    assessment, and putaway information.

    ### Features
    - **Complete Transaction Details**: Full transaction record with all nested data
    - **Quality Control Information**: Inspection results and quality status
    - **Damage Documentation**: Comprehensive damage assessment details
    - **Putaway Tracking**: Location assignment and putaway progress
    - **Item-Level Details**: Detailed product and quantity information
    - **Audit Information**: Creation, update, and status change tracking

    ### Response Data Includes
    - **Transaction Metadata**: IDs, references, and timestamps
    - **Product Information**: SKU, product name, quantities, and UOM
    - **Quality Control**: Inspection status, inspector, and notes
    - **Damage Assessment**: Damage flags, descriptions, and quantities
    - **Putaway Details**: Location assignments and instructions
    - **Status Information**: Current status and workflow progression
    - **Custom Fields**: Additional configurable data points

    **CRITICAL NOTE**: The URL parameter uses 'transactionId' but the model field is 'receivingId'. This
    reflects actual implementation behavior.

    ### Use Cases
    - **Transaction Details View**: Complete receiving transaction information
    - **Quality Control Review**: Access quality inspection results
    - **Damage Assessment**: Review damage documentation and claims
    - **Putaway Coordination**: Check location assignments and instructions
    - **Audit and Compliance**: Transaction traceability and documentation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSReceivingTransactionByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            transaction_id=transaction_id,
            client=client,
        )
    ).parsed
