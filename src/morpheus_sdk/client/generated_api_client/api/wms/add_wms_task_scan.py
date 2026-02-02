from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_wms_task_scan_body import AddWMSTaskScanBody
from ...models.add_wms_task_scan_response_200 import AddWMSTaskScanResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    task_id: str,
    *,
    body: AddWMSTaskScanBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/tasks/{task_id}/scans",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddWMSTaskScanResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddWMSTaskScanResponse200.from_dict(response.json())

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
) -> Response[Union[AddWMSTaskScanResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddWMSTaskScanBody,
) -> Response[Union[AddWMSTaskScanResponse200, ErrorResponse]]:
    """Add task scan


    ## Add Task Scan

    Record barcode/RFID scan data for task validation and verification.

    **Scan Types:**
    - **BIN**: Location verification
    - **PRODUCT**: Product identification
    - **LPN**: License plate number tracking
    - **DESTINATION**: Destination verification

    **Scan Results:**
    - **MATCH**: Scan matches expected value
    - **MISMATCH**: Scan does not match expected value
    - **OVERRIDE**: Manual override by supervisor

    **Use Cases:**
    - Pick accuracy validation
    - Location verification
    - Product identification
    - Quality control and audit trails

    **Field Mapping:**
    - Pushes scan data to `scans` array with automatic timestamp
    - Uses `taskId` for task identification


    Args:
        world_id (str):
        task_id (str):
        body (AddWMSTaskScanBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddWMSTaskScanResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_id=task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddWMSTaskScanBody,
) -> Optional[Union[AddWMSTaskScanResponse200, ErrorResponse]]:
    """Add task scan


    ## Add Task Scan

    Record barcode/RFID scan data for task validation and verification.

    **Scan Types:**
    - **BIN**: Location verification
    - **PRODUCT**: Product identification
    - **LPN**: License plate number tracking
    - **DESTINATION**: Destination verification

    **Scan Results:**
    - **MATCH**: Scan matches expected value
    - **MISMATCH**: Scan does not match expected value
    - **OVERRIDE**: Manual override by supervisor

    **Use Cases:**
    - Pick accuracy validation
    - Location verification
    - Product identification
    - Quality control and audit trails

    **Field Mapping:**
    - Pushes scan data to `scans` array with automatic timestamp
    - Uses `taskId` for task identification


    Args:
        world_id (str):
        task_id (str):
        body (AddWMSTaskScanBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddWMSTaskScanResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddWMSTaskScanBody,
) -> Response[Union[AddWMSTaskScanResponse200, ErrorResponse]]:
    """Add task scan


    ## Add Task Scan

    Record barcode/RFID scan data for task validation and verification.

    **Scan Types:**
    - **BIN**: Location verification
    - **PRODUCT**: Product identification
    - **LPN**: License plate number tracking
    - **DESTINATION**: Destination verification

    **Scan Results:**
    - **MATCH**: Scan matches expected value
    - **MISMATCH**: Scan does not match expected value
    - **OVERRIDE**: Manual override by supervisor

    **Use Cases:**
    - Pick accuracy validation
    - Location verification
    - Product identification
    - Quality control and audit trails

    **Field Mapping:**
    - Pushes scan data to `scans` array with automatic timestamp
    - Uses `taskId` for task identification


    Args:
        world_id (str):
        task_id (str):
        body (AddWMSTaskScanBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddWMSTaskScanResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddWMSTaskScanBody,
) -> Optional[Union[AddWMSTaskScanResponse200, ErrorResponse]]:
    """Add task scan


    ## Add Task Scan

    Record barcode/RFID scan data for task validation and verification.

    **Scan Types:**
    - **BIN**: Location verification
    - **PRODUCT**: Product identification
    - **LPN**: License plate number tracking
    - **DESTINATION**: Destination verification

    **Scan Results:**
    - **MATCH**: Scan matches expected value
    - **MISMATCH**: Scan does not match expected value
    - **OVERRIDE**: Manual override by supervisor

    **Use Cases:**
    - Pick accuracy validation
    - Location verification
    - Product identification
    - Quality control and audit trails

    **Field Mapping:**
    - Pushes scan data to `scans` array with automatic timestamp
    - Uses `taskId` for task identification


    Args:
        world_id (str):
        task_id (str):
        body (AddWMSTaskScanBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddWMSTaskScanResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
