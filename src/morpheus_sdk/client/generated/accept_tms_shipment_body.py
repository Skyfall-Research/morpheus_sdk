import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AcceptTMSShipmentBody")


@_attrs_define
class AcceptTMSShipmentBody:
    """
    Attributes:
        pro_number (Union[Unset, str]): Carrier's Progressive Number Example: PRO123456789.
        tracking_number (Union[Unset, str]): Carrier's tracking reference number Example: TRK987654321.
        estimated_pickup_date (Union[Unset, datetime.datetime]): Estimated pickup date and time Example:
            2024-11-27T08:00:00.000Z.
    """

    pro_number: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    estimated_pickup_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pro_number = self.pro_number

        tracking_number = self.tracking_number

        estimated_pickup_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_pickup_date, Unset):
            estimated_pickup_date = self.estimated_pickup_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pro_number is not UNSET:
            field_dict["proNumber"] = pro_number
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if estimated_pickup_date is not UNSET:
            field_dict["estimatedPickupDate"] = estimated_pickup_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pro_number = d.pop("proNumber", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        _estimated_pickup_date = d.pop("estimatedPickupDate", UNSET)
        estimated_pickup_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_pickup_date, Unset):
            estimated_pickup_date = UNSET
        else:
            estimated_pickup_date = isoparse(_estimated_pickup_date)

        accept_tms_shipment_body = cls(
            pro_number=pro_number,
            tracking_number=tracking_number,
            estimated_pickup_date=estimated_pickup_date,
        )

        accept_tms_shipment_body.additional_properties = d
        return accept_tms_shipment_body

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
