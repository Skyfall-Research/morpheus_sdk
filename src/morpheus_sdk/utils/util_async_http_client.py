from __future__ import annotations

from typing import Any, Optional

import httpx

from morpheus_sdk.models.model_http_client import (
    ModelHttpClientInputs,
    ModelHttpAsyncClientOutputs,
)


def async_http_client(base_params: ModelHttpClientInputs) -> ModelHttpAsyncClientOutputs:
    client = httpx.AsyncClient(
        base_url=base_params.base_url,
        headers=base_params.headers,
        timeout=base_params.timeout,
    )

    async def get(
        path: str,
        query: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return await client.get(path, params=query, headers=headers)

    async def post(
        path: str,
        json: Optional[dict[str, Any]] = None,
        data: Optional[Any] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return await client.post(path, json=json, content=data, headers=headers)

    async def put(
        path: str,
        json: Optional[dict[str, Any]] = None,
        data: Optional[Any] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return await client.put(path, json=json, content=data, headers=headers)

    async def delete(
        path: str,
        query: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return await client.delete(path, params=query, headers=headers)

    return ModelHttpAsyncClientOutputs(
        get=get,
        post=post,
        put=put,
        delete=delete,
        aclose=client.aclose,
    )
