import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_audit_logs_response_200 import GetAuditLogsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: UUID,
    *,
    model: Union[Unset, str] = UNSET,
    document_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["model"] = model

    params["documentId"] = document_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/audit-logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetAuditLogsResponse200]]:
    if response.status_code == 200:
        response_200 = GetAuditLogsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetAuditLogsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    model: Union[Unset, str] = UNSET,
    document_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetAuditLogsResponse200]]:
    """Get audit logs for data changes in a world


    ## Retrieve Data Audit Logs

    Get comprehensive audit logs that track all data changes within a specific world environment.

    ### Features
    - **Complete Change History**: Track all create, update, and delete operations on database records
    - **Before/After Snapshots**: See exactly what changed in each modification
    - **Model-Specific Filtering**: Filter by specific data models (EdiTransaction, WMSTask, etc.)
    - **Document Tracking**: Follow all changes to specific documents using their IDs
    - **Compliance Ready**: Meets regulatory requirements for data change tracking

    ### Common Use Cases
    - Compliance reporting and regulatory audits
    - Data investigation and forensic analysis
    - Security monitoring for unauthorized changes
    - Change impact analysis and rollback planning
    - Debugging data inconsistencies
    - Tracking user actions and system modifications

    ### Audit Log Structure
    Each audit log entry contains:
    - **model**: The type of data model that was changed
    - **documentId**: The unique identifier of the changed document
    - **changedBy**: Who made the change (user ID or system identifier)
    - **before**: Complete state of the document before the change
    - **after**: Complete state of the document after the change
    - **reason**: Optional reason or context for the change
    - **timestamps**: When the audit log entry was created


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        model (Union[Unset, str]):  Example: EdiTransaction.
        document_id (Union[Unset, str]):  Example: edi_txn_123456789.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAuditLogsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        model=model,
        document_id=document_id,
        date_start=date_start,
        date_end=date_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    model: Union[Unset, str] = UNSET,
    document_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetAuditLogsResponse200]]:
    """Get audit logs for data changes in a world


    ## Retrieve Data Audit Logs

    Get comprehensive audit logs that track all data changes within a specific world environment.

    ### Features
    - **Complete Change History**: Track all create, update, and delete operations on database records
    - **Before/After Snapshots**: See exactly what changed in each modification
    - **Model-Specific Filtering**: Filter by specific data models (EdiTransaction, WMSTask, etc.)
    - **Document Tracking**: Follow all changes to specific documents using their IDs
    - **Compliance Ready**: Meets regulatory requirements for data change tracking

    ### Common Use Cases
    - Compliance reporting and regulatory audits
    - Data investigation and forensic analysis
    - Security monitoring for unauthorized changes
    - Change impact analysis and rollback planning
    - Debugging data inconsistencies
    - Tracking user actions and system modifications

    ### Audit Log Structure
    Each audit log entry contains:
    - **model**: The type of data model that was changed
    - **documentId**: The unique identifier of the changed document
    - **changedBy**: Who made the change (user ID or system identifier)
    - **before**: Complete state of the document before the change
    - **after**: Complete state of the document after the change
    - **reason**: Optional reason or context for the change
    - **timestamps**: When the audit log entry was created


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        model (Union[Unset, str]):  Example: EdiTransaction.
        document_id (Union[Unset, str]):  Example: edi_txn_123456789.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAuditLogsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        model=model,
        document_id=document_id,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    model: Union[Unset, str] = UNSET,
    document_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetAuditLogsResponse200]]:
    """Get audit logs for data changes in a world


    ## Retrieve Data Audit Logs

    Get comprehensive audit logs that track all data changes within a specific world environment.

    ### Features
    - **Complete Change History**: Track all create, update, and delete operations on database records
    - **Before/After Snapshots**: See exactly what changed in each modification
    - **Model-Specific Filtering**: Filter by specific data models (EdiTransaction, WMSTask, etc.)
    - **Document Tracking**: Follow all changes to specific documents using their IDs
    - **Compliance Ready**: Meets regulatory requirements for data change tracking

    ### Common Use Cases
    - Compliance reporting and regulatory audits
    - Data investigation and forensic analysis
    - Security monitoring for unauthorized changes
    - Change impact analysis and rollback planning
    - Debugging data inconsistencies
    - Tracking user actions and system modifications

    ### Audit Log Structure
    Each audit log entry contains:
    - **model**: The type of data model that was changed
    - **documentId**: The unique identifier of the changed document
    - **changedBy**: Who made the change (user ID or system identifier)
    - **before**: Complete state of the document before the change
    - **after**: Complete state of the document after the change
    - **reason**: Optional reason or context for the change
    - **timestamps**: When the audit log entry was created


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        model (Union[Unset, str]):  Example: EdiTransaction.
        document_id (Union[Unset, str]):  Example: edi_txn_123456789.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAuditLogsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        model=model,
        document_id=document_id,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    model: Union[Unset, str] = UNSET,
    document_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetAuditLogsResponse200]]:
    """Get audit logs for data changes in a world


    ## Retrieve Data Audit Logs

    Get comprehensive audit logs that track all data changes within a specific world environment.

    ### Features
    - **Complete Change History**: Track all create, update, and delete operations on database records
    - **Before/After Snapshots**: See exactly what changed in each modification
    - **Model-Specific Filtering**: Filter by specific data models (EdiTransaction, WMSTask, etc.)
    - **Document Tracking**: Follow all changes to specific documents using their IDs
    - **Compliance Ready**: Meets regulatory requirements for data change tracking

    ### Common Use Cases
    - Compliance reporting and regulatory audits
    - Data investigation and forensic analysis
    - Security monitoring for unauthorized changes
    - Change impact analysis and rollback planning
    - Debugging data inconsistencies
    - Tracking user actions and system modifications

    ### Audit Log Structure
    Each audit log entry contains:
    - **model**: The type of data model that was changed
    - **documentId**: The unique identifier of the changed document
    - **changedBy**: Who made the change (user ID or system identifier)
    - **before**: Complete state of the document before the change
    - **after**: Complete state of the document after the change
    - **reason**: Optional reason or context for the change
    - **timestamps**: When the audit log entry was created


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        model (Union[Unset, str]):  Example: EdiTransaction.
        document_id (Union[Unset, str]):  Example: edi_txn_123456789.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAuditLogsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            model=model,
            document_id=document_id,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
