from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_erp_companies_company_type import GetAllERPCompaniesCompanyType
from ...models.get_all_erp_companies_response_200 import GetAllERPCompaniesResponse200
from ...models.get_all_erp_companies_status import GetAllERPCompaniesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: Union[Unset, GetAllERPCompaniesStatus] = UNSET,
    company_type: Union[Unset, GetAllERPCompaniesCompanyType] = UNSET,
    currency: Union[Unset, str] = UNSET,
    is_mpc_company: Union[Unset, bool] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_company_type: Union[Unset, str] = UNSET
    if not isinstance(company_type, Unset):
        json_company_type = company_type.value

    params["companyType"] = json_company_type

    params["currency"] = currency

    params["isMpcCompany"] = is_mpc_company

    params["search"] = search

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/companies",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllERPCompaniesResponse200]:
    if response.status_code == 200:
        response_200 = GetAllERPCompaniesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllERPCompaniesResponse200]:
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
    status: Union[Unset, GetAllERPCompaniesStatus] = UNSET,
    company_type: Union[Unset, GetAllERPCompaniesCompanyType] = UNSET,
    currency: Union[Unset, str] = UNSET,
    is_mpc_company: Union[Unset, bool] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPCompaniesResponse200]:
    """Get all ERP companies


    Retrieve all ERP companies with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, type, currency, and MPC designation
    - **Text Search**: Search by company name or DUNS number
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Business Data**: Returns full company profiles with addresses and contacts

    **Use Cases**:
    - **Partner Management**: View complete business partner network
    - **ERP Synchronization**: Bulk operations and system integration
    - **Financial Analysis**: Filter companies by currency and credit status
    - **Business Intelligence**: Comprehensive company data for reporting


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPCompaniesStatus]):  Example: ACTIVE.
        company_type (Union[Unset, GetAllERPCompaniesCompanyType]):  Example: CUSTOMER.
        currency (Union[Unset, str]):  Example: USD.
        is_mpc_company (Union[Unset, bool]):
        search (Union[Unset, str]):  Example: Acme.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPCompaniesResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        company_type=company_type,
        currency=currency,
        is_mpc_company=is_mpc_company,
        search=search,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPCompaniesStatus] = UNSET,
    company_type: Union[Unset, GetAllERPCompaniesCompanyType] = UNSET,
    currency: Union[Unset, str] = UNSET,
    is_mpc_company: Union[Unset, bool] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPCompaniesResponse200]:
    """Get all ERP companies


    Retrieve all ERP companies with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, type, currency, and MPC designation
    - **Text Search**: Search by company name or DUNS number
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Business Data**: Returns full company profiles with addresses and contacts

    **Use Cases**:
    - **Partner Management**: View complete business partner network
    - **ERP Synchronization**: Bulk operations and system integration
    - **Financial Analysis**: Filter companies by currency and credit status
    - **Business Intelligence**: Comprehensive company data for reporting


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPCompaniesStatus]):  Example: ACTIVE.
        company_type (Union[Unset, GetAllERPCompaniesCompanyType]):  Example: CUSTOMER.
        currency (Union[Unset, str]):  Example: USD.
        is_mpc_company (Union[Unset, bool]):
        search (Union[Unset, str]):  Example: Acme.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPCompaniesResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        company_type=company_type,
        currency=currency,
        is_mpc_company=is_mpc_company,
        search=search,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPCompaniesStatus] = UNSET,
    company_type: Union[Unset, GetAllERPCompaniesCompanyType] = UNSET,
    currency: Union[Unset, str] = UNSET,
    is_mpc_company: Union[Unset, bool] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPCompaniesResponse200]:
    """Get all ERP companies


    Retrieve all ERP companies with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, type, currency, and MPC designation
    - **Text Search**: Search by company name or DUNS number
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Business Data**: Returns full company profiles with addresses and contacts

    **Use Cases**:
    - **Partner Management**: View complete business partner network
    - **ERP Synchronization**: Bulk operations and system integration
    - **Financial Analysis**: Filter companies by currency and credit status
    - **Business Intelligence**: Comprehensive company data for reporting


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPCompaniesStatus]):  Example: ACTIVE.
        company_type (Union[Unset, GetAllERPCompaniesCompanyType]):  Example: CUSTOMER.
        currency (Union[Unset, str]):  Example: USD.
        is_mpc_company (Union[Unset, bool]):
        search (Union[Unset, str]):  Example: Acme.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPCompaniesResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        company_type=company_type,
        currency=currency,
        is_mpc_company=is_mpc_company,
        search=search,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPCompaniesStatus] = UNSET,
    company_type: Union[Unset, GetAllERPCompaniesCompanyType] = UNSET,
    currency: Union[Unset, str] = UNSET,
    is_mpc_company: Union[Unset, bool] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPCompaniesResponse200]:
    """Get all ERP companies


    Retrieve all ERP companies with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, type, currency, and MPC designation
    - **Text Search**: Search by company name or DUNS number
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Business Data**: Returns full company profiles with addresses and contacts

    **Use Cases**:
    - **Partner Management**: View complete business partner network
    - **ERP Synchronization**: Bulk operations and system integration
    - **Financial Analysis**: Filter companies by currency and credit status
    - **Business Intelligence**: Comprehensive company data for reporting


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPCompaniesStatus]):  Example: ACTIVE.
        company_type (Union[Unset, GetAllERPCompaniesCompanyType]):  Example: CUSTOMER.
        currency (Union[Unset, str]):  Example: USD.
        is_mpc_company (Union[Unset, bool]):
        search (Union[Unset, str]):  Example: Acme.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPCompaniesResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            company_type=company_type,
            currency=currency,
            is_mpc_company=is_mpc_company,
            search=search,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
