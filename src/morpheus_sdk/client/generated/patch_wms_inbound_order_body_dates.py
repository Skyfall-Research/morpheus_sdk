import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchWMSInboundOrderBodyDates")


@_attrs_define
class PatchWMSInboundOrderBodyDates:
    """
    Attributes:
        expected_arrival (Union[Unset, datetime.datetime]): Updated expected arrival date
    """

    expected_arrival: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expected_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.expected_arrival, Unset):
            expected_arrival = self.expected_arrival.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expected_arrival is not UNSET:
            field_dict["expectedArrival"] = expected_arrival

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expected_arrival = d.pop("expectedArrival", UNSET)
        expected_arrival: Union[Unset, datetime.datetime]
        if isinstance(_expected_arrival, Unset):
            expected_arrival = UNSET
        else:
            expected_arrival = isoparse(_expected_arrival)

        patch_wms_inbound_order_body_dates = cls(
            expected_arrival=expected_arrival,
        )

        patch_wms_inbound_order_body_dates.additional_properties = d
        return patch_wms_inbound_order_body_dates

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
