import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchWMSOutboundOrderBodyDates")


@_attrs_define
class PatchWMSOutboundOrderBodyDates:
    """
    Attributes:
        required_ship_date (Union[Unset, datetime.datetime]): Updated required ship date
        actual_ship_date (Union[Unset, datetime.datetime]): Actual ship date (auto-set when status is SHIPPED)
    """

    required_ship_date: Union[Unset, datetime.datetime] = UNSET
    actual_ship_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        required_ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.required_ship_date, Unset):
            required_ship_date = self.required_ship_date.isoformat()

        actual_ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.actual_ship_date, Unset):
            actual_ship_date = self.actual_ship_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if required_ship_date is not UNSET:
            field_dict["requiredShipDate"] = required_ship_date
        if actual_ship_date is not UNSET:
            field_dict["actualShipDate"] = actual_ship_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _required_ship_date = d.pop("requiredShipDate", UNSET)
        required_ship_date: Union[Unset, datetime.datetime]
        if isinstance(_required_ship_date, Unset):
            required_ship_date = UNSET
        else:
            required_ship_date = isoparse(_required_ship_date)

        _actual_ship_date = d.pop("actualShipDate", UNSET)
        actual_ship_date: Union[Unset, datetime.datetime]
        if isinstance(_actual_ship_date, Unset):
            actual_ship_date = UNSET
        else:
            actual_ship_date = isoparse(_actual_ship_date)

        patch_wms_outbound_order_body_dates = cls(
            required_ship_date=required_ship_date,
            actual_ship_date=actual_ship_date,
        )

        patch_wms_outbound_order_body_dates.additional_properties = d
        return patch_wms_outbound_order_body_dates

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
