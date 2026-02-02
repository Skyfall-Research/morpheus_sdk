from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.world_log import WorldLog


T = TypeVar("T", bound="GetLogsResponse200Data")


@_attrs_define
class GetLogsResponse200Data:
    """
    Attributes:
        items (list['WorldLog']): Array of log entries matching the filter criteria
        total_count (int): Total number of logs matching the filter (not limited by pagination) Example: 2847.
        limit (int): Number of logs returned in this response Example: 50.
        has_more (bool): Whether more logs are available beyond this page Example: True.
        next_cursor (Union[None, Unset, str]): Cursor for retrieving the next page of results Example:
            507f1f77bcf86cd799439012.
    """

    items: list["WorldLog"]
    total_count: int
    limit: int
    has_more: bool
    next_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        total_count = self.total_count

        limit = self.limit

        has_more = self.has_more

        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "totalCount": total_count,
                "limit": limit,
                "hasMore": has_more,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.world_log import WorldLog

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = WorldLog.from_dict(items_item_data)

            items.append(items_item)

        total_count = d.pop("totalCount")

        limit = d.pop("limit")

        has_more = d.pop("hasMore")

        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        get_logs_response_200_data = cls(
            items=items,
            total_count=total_count,
            limit=limit,
            has_more=has_more,
            next_cursor=next_cursor,
        )

        get_logs_response_200_data.additional_properties = d
        return get_logs_response_200_data

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
