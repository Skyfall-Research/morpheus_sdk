from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAllERPPaymentsResponse200Pagination")


@_attrs_define
class GetAllERPPaymentsResponse200Pagination:
    """
    Attributes:
        limit (Union[Unset, int]):  Example: 50.
        previous_cursor (Union[Unset, str]):
        total_count (Union[Unset, int]):  Example: 89.
        has_more (Union[Unset, bool]):  Example: True.
        next_cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439025.
    """

    limit: Union[Unset, int] = UNSET
    previous_cursor: Union[Unset, str] = UNSET
    total_count: Union[Unset, int] = UNSET
    has_more: Union[Unset, bool] = UNSET
    next_cursor: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        previous_cursor = self.previous_cursor

        total_count = self.total_count

        has_more = self.has_more

        next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if previous_cursor is not UNSET:
            field_dict["previousCursor"] = previous_cursor
        if total_count is not UNSET:
            field_dict["totalCount"] = total_count
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        limit = d.pop("limit", UNSET)

        previous_cursor = d.pop("previousCursor", UNSET)

        total_count = d.pop("totalCount", UNSET)

        has_more = d.pop("hasMore", UNSET)

        next_cursor = d.pop("nextCursor", UNSET)

        get_all_erp_payments_response_200_pagination = cls(
            limit=limit,
            previous_cursor=previous_cursor,
            total_count=total_count,
            has_more=has_more,
            next_cursor=next_cursor,
        )

        get_all_erp_payments_response_200_pagination.additional_properties = d
        return get_all_erp_payments_response_200_pagination

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
