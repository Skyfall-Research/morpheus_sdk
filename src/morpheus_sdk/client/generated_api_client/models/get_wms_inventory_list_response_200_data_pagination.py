from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInventoryListResponse200DataPagination")


@_attrs_define
class GetWMSInventoryListResponse200DataPagination:
    """
    Attributes:
        total (Union[Unset, int]):  Example: 1250.
        limit (Union[Unset, int]):  Example: 50.
        offset (Union[Unset, int]):
        has_more (Union[Unset, bool]):  Example: True.
    """

    total: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    offset: Union[Unset, int] = UNSET
    has_more: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        limit = self.limit

        offset = self.offset

        has_more = self.has_more

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        has_more = d.pop("hasMore", UNSET)

        get_wms_inventory_list_response_200_data_pagination = cls(
            total=total,
            limit=limit,
            offset=offset,
            has_more=has_more,
        )

        get_wms_inventory_list_response_200_data_pagination.additional_properties = d
        return get_wms_inventory_list_response_200_data_pagination

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
