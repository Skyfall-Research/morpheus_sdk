from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDocsMeshResponse200EndpointsItem")


@_attrs_define
class GetDocsMeshResponse200EndpointsItem:
    """
    Attributes:
        path (Union[Unset, str]):  Example: /{worldId}/wms/inbound-orders.
        method (Union[Unset, str]):  Example: post.
        summary (Union[Unset, str]):  Example: Create new inbound order.
        formatted (Union[Unset, str]): The full multi-line formatted documentation string.
    """

    path: Union[Unset, str] = UNSET
    method: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    formatted: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        method = self.method

        summary = self.summary

        formatted = self.formatted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if path is not UNSET:
            field_dict["path"] = path
        if method is not UNSET:
            field_dict["method"] = method
        if summary is not UNSET:
            field_dict["summary"] = summary
        if formatted is not UNSET:
            field_dict["formatted"] = formatted

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        path = d.pop("path", UNSET)

        method = d.pop("method", UNSET)

        summary = d.pop("summary", UNSET)

        formatted = d.pop("formatted", UNSET)

        get_docs_mesh_response_200_endpoints_item = cls(
            path=path,
            method=method,
            summary=summary,
            formatted=formatted,
        )

        get_docs_mesh_response_200_endpoints_item.additional_properties = d
        return get_docs_mesh_response_200_endpoints_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
