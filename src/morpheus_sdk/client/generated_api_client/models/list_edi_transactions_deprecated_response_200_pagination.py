from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListEdiTransactionsDeprecatedResponse200Pagination")


@_attrs_define
class ListEdiTransactionsDeprecatedResponse200Pagination:
    """Pagination metadata. Note: nextCursor and previousCursor are always null in this deprecated endpoint.

    Attributes:
        total_count (Union[Unset, int]): Total number of records matching the filter criteria Example: 156.
        limit (Union[Unset, int]): Number of records per page (same as pageSize parameter) Example: 10.
        has_more (Union[Unset, bool]): Indicates if there are more records available (always true if items returned)
            Example: True.
        next_cursor (Union[Unset, None]): Always null - cursor pagination not supported in this deprecated endpoint
        previous_cursor (Union[Unset, None]): Always null - cursor pagination not supported in this deprecated endpoint
    """

    total_count: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    has_more: Union[Unset, bool] = UNSET
    next_cursor: Union[Unset, None] = UNSET
    previous_cursor: Union[Unset, None] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        limit = self.limit

        has_more = self.has_more

        next_cursor = self.next_cursor

        previous_cursor = self.previous_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if limit is not UNSET:
            field_dict["limit"] = limit
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor
        if previous_cursor is not UNSET:
            field_dict["previousCursor"] = previous_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_count = d.pop("totalCount", UNSET)

        limit = d.pop("limit", UNSET)

        has_more = d.pop("hasMore", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        previous_cursor = d.pop("previousCursor", UNSET)

        list_edi_transactions_deprecated_response_200_pagination = cls(
            total_count=total_count,
            limit=limit,
            has_more=has_more,
            next_cursor=next_cursor,
            previous_cursor=previous_cursor,
        )

        list_edi_transactions_deprecated_response_200_pagination.additional_properties = d
        return list_edi_transactions_deprecated_response_200_pagination

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
