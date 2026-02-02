from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSOutboundOrderBodyCarrierInfo")


@_attrs_define
class CreateWMSOutboundOrderBodyCarrierInfo:
    """Optional shipping carrier details

    Attributes:
        carrier_id (Union[Unset, str]):  Example: CARRIER-UPS.
        carrier_name (Union[Unset, str]):  Example: UPS.
        service_level (Union[Unset, str]):  Example: GROUND.
        tracking_number (Union[Unset, str]):  Example: 1Z999AA1234567890.
    """

    carrier_id: Union[Unset, str] = UNSET
    carrier_name: Union[Unset, str] = UNSET
    service_level: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        carrier_id = self.carrier_id

        carrier_name = self.carrier_name

        service_level = self.service_level

        tracking_number = self.tracking_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if carrier_id is not UNSET:
            field_dict["carrierId"] = carrier_id
        if carrier_name is not UNSET:
            field_dict["carrierName"] = carrier_name
        if service_level is not UNSET:
            field_dict["serviceLevel"] = service_level
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        carrier_id = d.pop("carrierId", UNSET)

        carrier_name = d.pop("carrierName", UNSET)

        service_level = d.pop("serviceLevel", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        create_wms_outbound_order_body_carrier_info = cls(
            carrier_id=carrier_id,
            carrier_name=carrier_name,
            service_level=service_level,
            tracking_number=tracking_number,
        )

        create_wms_outbound_order_body_carrier_info.additional_properties = d
        return create_wms_outbound_order_body_carrier_info

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
