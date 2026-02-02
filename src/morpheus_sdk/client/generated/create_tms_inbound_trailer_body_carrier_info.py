from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTMSInboundTrailerBodyCarrierInfo")


@_attrs_define
class CreateTMSInboundTrailerBodyCarrierInfo:
    """
    Attributes:
        carrier_id (Union[Unset, str]): Associated carrier identifier Example: CARRIER_FEDEX_001.
        carrier_name (Union[Unset, str]): Carrier company name Example: FedEx Corporation.
        driver_name (Union[Unset, str]): Driver full name Example: John Smith.
        driver_phone (Union[Unset, str]): Driver contact phone Example: +1-555-123-4567.
    """

    carrier_id: Union[Unset, str] = UNSET
    carrier_name: Union[Unset, str] = UNSET
    driver_name: Union[Unset, str] = UNSET
    driver_phone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier_id = self.carrier_id

        carrier_name = self.carrier_name

        driver_name = self.driver_name

        driver_phone = self.driver_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier_id is not UNSET:
            field_dict["carrierId"] = carrier_id
        if carrier_name is not UNSET:
            field_dict["carrierName"] = carrier_name
        if driver_name is not UNSET:
            field_dict["driverName"] = driver_name
        if driver_phone is not UNSET:
            field_dict["driverPhone"] = driver_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carrier_id = d.pop("carrierId", UNSET)

        carrier_name = d.pop("carrierName", UNSET)

        driver_name = d.pop("driverName", UNSET)

        driver_phone = d.pop("driverPhone", UNSET)

        create_tms_inbound_trailer_body_carrier_info = cls(
            carrier_id=carrier_id,
            carrier_name=carrier_name,
            driver_name=driver_name,
            driver_phone=driver_phone,
        )

        create_tms_inbound_trailer_body_carrier_info.additional_properties = d
        return create_tms_inbound_trailer_body_carrier_info

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
