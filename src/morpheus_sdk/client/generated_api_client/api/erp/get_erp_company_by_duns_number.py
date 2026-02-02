from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_erp_company_by_duns_number_response_200 import GetERPCompanyByDunsNumberResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    duns_number: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/companies/duns/{duns_number}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]]:
    if response.status_code == 200:
        response_200 = GetERPCompanyByDunsNumberResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    duns_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]]:
    """Get ERP company by DUNS number


    Retrieve ERP company by DUNS (Data Universal Numbering System) number for business verification and
    integration.

    **Core Features**:
    - **DUNS Lookup**: Direct company access via standardized DUNS identifier
    - **Business Verification**: Validate company identity using DUNS number
    - **Integration Support**: External system integration using DUNS as key
    - **Credit Bureau Integration**: Support for credit bureau and financial service lookups

    **Use Cases**:
    - **Business Verification**: Verify company legitimacy using DUNS number
    - **Credit Checks**: Integrate with credit bureaus using DUNS identifier
    - **ERP Integration**: Lookup companies during ERP system data exchange
    - **Partner Validation**: Validate business partners using standard DUNS identifier

    **⚠️ Field Naming Note**: Model stores as 'duns' field, route parameter uses 'dunsNumber' for
    clarity.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        duns_number (str):  Example: 123456789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        duns_number=duns_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    duns_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]]:
    """Get ERP company by DUNS number


    Retrieve ERP company by DUNS (Data Universal Numbering System) number for business verification and
    integration.

    **Core Features**:
    - **DUNS Lookup**: Direct company access via standardized DUNS identifier
    - **Business Verification**: Validate company identity using DUNS number
    - **Integration Support**: External system integration using DUNS as key
    - **Credit Bureau Integration**: Support for credit bureau and financial service lookups

    **Use Cases**:
    - **Business Verification**: Verify company legitimacy using DUNS number
    - **Credit Checks**: Integrate with credit bureaus using DUNS identifier
    - **ERP Integration**: Lookup companies during ERP system data exchange
    - **Partner Validation**: Validate business partners using standard DUNS identifier

    **⚠️ Field Naming Note**: Model stores as 'duns' field, route parameter uses 'dunsNumber' for
    clarity.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        duns_number (str):  Example: 123456789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        duns_number=duns_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    duns_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]]:
    """Get ERP company by DUNS number


    Retrieve ERP company by DUNS (Data Universal Numbering System) number for business verification and
    integration.

    **Core Features**:
    - **DUNS Lookup**: Direct company access via standardized DUNS identifier
    - **Business Verification**: Validate company identity using DUNS number
    - **Integration Support**: External system integration using DUNS as key
    - **Credit Bureau Integration**: Support for credit bureau and financial service lookups

    **Use Cases**:
    - **Business Verification**: Verify company legitimacy using DUNS number
    - **Credit Checks**: Integrate with credit bureaus using DUNS identifier
    - **ERP Integration**: Lookup companies during ERP system data exchange
    - **Partner Validation**: Validate business partners using standard DUNS identifier

    **⚠️ Field Naming Note**: Model stores as 'duns' field, route parameter uses 'dunsNumber' for
    clarity.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        duns_number (str):  Example: 123456789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        duns_number=duns_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    duns_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]]:
    """Get ERP company by DUNS number


    Retrieve ERP company by DUNS (Data Universal Numbering System) number for business verification and
    integration.

    **Core Features**:
    - **DUNS Lookup**: Direct company access via standardized DUNS identifier
    - **Business Verification**: Validate company identity using DUNS number
    - **Integration Support**: External system integration using DUNS as key
    - **Credit Bureau Integration**: Support for credit bureau and financial service lookups

    **Use Cases**:
    - **Business Verification**: Verify company legitimacy using DUNS number
    - **Credit Checks**: Integrate with credit bureaus using DUNS identifier
    - **ERP Integration**: Lookup companies during ERP system data exchange
    - **Partner Validation**: Validate business partners using standard DUNS identifier

    **⚠️ Field Naming Note**: Model stores as 'duns' field, route parameter uses 'dunsNumber' for
    clarity.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        duns_number (str):  Example: 123456789.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPCompanyByDunsNumberResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            duns_number=duns_number,
            client=client,
        )
    ).parsed
