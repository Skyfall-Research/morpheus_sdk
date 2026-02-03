from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetLogsResponse200Pagination")


@_attrs_define
class GetLogsResponse200Pagination:
    """
    Attributes:
        total_count (int): Total number of logs matching the filter Example: 2847.
        limit (int): Maximum number of logs per page Example: 50.
        has_more (bool): Whether additional pages are available Example: True.
        next_cursor (Union[None, str]): Cursor for the next page Example: 507f1f77bcf86cd799439012.
        previous_cursor (Union[None, str]): Cursor for the previous page Example: 507f1f77bcf86cd799439010.
    """

    total_count: int
    limit: int
    has_more: bool
    next_cursor: Union[None, str]
    previous_cursor: Union[None, str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        limit = self.limit

        has_more = self.has_more

        next_cursor: Union[None, str]
        next_cursor = self.next_cursor

        previous_cursor: Union[None, str]
        previous_cursor = self.previous_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalCount": total_count,
                "limit": limit,
                "hasMore": has_more,
                "nextCursor": next_cursor,
                "previousCursor": previous_cursor,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("totalCount")

        limit = d.pop("limit")

        has_more = d.pop("hasMore")

        def _parse_next_cursor(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", None))
        
        def _parse_previous_cursor(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        previous_cursor = _parse_previous_cursor(d.pop("previousCursor", None))

        get_logs_response_200_pagination = cls(
            total_count=total_count,
            limit=limit,
            has_more=has_more,
            next_cursor=next_cursor,
            previous_cursor=previous_cursor,
        )

        get_logs_response_200_pagination.additional_properties = d
        return get_logs_response_200_pagination

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
