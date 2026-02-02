from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTMSShipmentsByCarrierResponse200Pagination")


@_attrs_define
class GetTMSShipmentsByCarrierResponse200Pagination:
    """
    Attributes:
        total_count (Union[Unset, int]):  Example: 87.
        limit (Union[Unset, int]):  Example: 50.
        has_more (Union[Unset, bool]):  Example: True.
        next_cursor (Union[None, Unset, str]):  Example: 507f1f77bcf86cd799439025.
        previous_cursor (Union[None, Unset, str]):  Example: 507f1f77bcf86cd799439015.
    """

    total_count: Union[Unset, int] = UNSET
    limit: Union[Unset, int] = UNSET
    has_more: Union[Unset, bool] = UNSET
    next_cursor: Union[None, Unset, str] = UNSET
    previous_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_count = self.total_count

        limit = self.limit

        has_more = self.has_more

        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        previous_cursor: Union[None, Unset, str]
        if isinstance(self.previous_cursor, Unset):
            previous_cursor = UNSET
        else:
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

        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        def _parse_previous_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        previous_cursor = _parse_previous_cursor(d.pop("previousCursor", UNSET))

        get_tms_shipments_by_carrier_response_200_pagination = cls(
            total_count=total_count,
            limit=limit,
            has_more=has_more,
            next_cursor=next_cursor,
            previous_cursor=previous_cursor,
        )

        get_tms_shipments_by_carrier_response_200_pagination.additional_properties = d
        return get_tms_shipments_by_carrier_response_200_pagination

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
