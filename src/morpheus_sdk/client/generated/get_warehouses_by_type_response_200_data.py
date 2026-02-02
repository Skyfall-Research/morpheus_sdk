from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_warehouse import WMSWarehouse


T = TypeVar("T", bound="GetWarehousesByTypeResponse200Data")


@_attrs_define
class GetWarehousesByTypeResponse200Data:
    """
    Attributes:
        items (Union[Unset, list['WMSWarehouse']]):
        total_count (Union[Unset, int]):  Example: 5.
        limit (Union[Unset, int]):  Example: 50.
        has_more (Union[Unset, bool]):
        next_cursor (Union[Unset, str]):
    """

    items: Union[Unset, list["WMSWarehouse"]] = UNSET
    total_count: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    has_more: Union[Unset, bool] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        total_count = self.total_count

        limit = self.limit

        has_more = self.has_more

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if limit is not UNSET:
            field_dict["limit"] = limit
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_warehouse import WMSWarehouse

        d = dict(src_dict)
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = WMSWarehouse.from_dict(items_item_data)

            items.append(items_item)

        total_count = d.pop("totalCount", UNSET)

        limit = d.pop("limit", UNSET)

        has_more = d.pop("hasMore", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        get_warehouses_by_type_response_200_data = cls(
            items=items,
            total_count=total_count,
            limit=limit,
            has_more=has_more,
            next_cursor=next_cursor,
        )

        get_warehouses_by_type_response_200_data.additional_properties = d
        return get_warehouses_by_type_response_200_data

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
