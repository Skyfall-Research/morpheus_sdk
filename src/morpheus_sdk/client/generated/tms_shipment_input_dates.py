import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentInputDates")


@_attrs_define
class TMSShipmentInputDates:
    """Planned shipment dates

    Attributes:
        planned_pickup_date (Union[Unset, datetime.datetime]):  Example: 2024-11-27T08:00:00.000Z.
        planned_delivery_date (Union[Unset, datetime.datetime]):  Example: 2024-11-29T17:00:00.000Z.
    """

    planned_pickup_date: Union[Unset, datetime.datetime] = UNSET
    planned_delivery_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        planned_pickup_date: Union[Unset, str] = UNSET
        if not isinstance(self.planned_pickup_date, Unset):
            planned_pickup_date = self.planned_pickup_date.isoformat()

        planned_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.planned_delivery_date, Unset):
            planned_delivery_date = self.planned_delivery_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if planned_pickup_date is not UNSET:
            field_dict["plannedPickupDate"] = planned_pickup_date
        if planned_delivery_date is not UNSET:
            field_dict["plannedDeliveryDate"] = planned_delivery_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _planned_pickup_date = d.pop("plannedPickupDate", UNSET)
        planned_pickup_date: Union[Unset, datetime.datetime]
        if isinstance(_planned_pickup_date, Unset):
            planned_pickup_date = UNSET
        else:
            planned_pickup_date = isoparse(_planned_pickup_date)

        _planned_delivery_date = d.pop("plannedDeliveryDate", UNSET)
        planned_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_planned_delivery_date, Unset):
            planned_delivery_date = UNSET
        else:
            planned_delivery_date = isoparse(_planned_delivery_date)

        tms_shipment_input_dates = cls(
            planned_pickup_date=planned_pickup_date,
            planned_delivery_date=planned_delivery_date,
        )

        tms_shipment_input_dates.additional_properties = d
        return tms_shipment_input_dates

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
