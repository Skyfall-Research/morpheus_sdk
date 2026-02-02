from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSInboundOrderBodyVendor")


@_attrs_define
class CreateWMSInboundOrderBodyVendor:
    """Vendor information and contact details

    Attributes:
        vendor_id (Union[Unset, str]): Unique vendor identifier from ERP Example: VND-SWIFT-001.
        vendor_name (Union[Unset, str]): Vendor company name Example: Swift Manufacturing Co..
        contact_email (Union[Unset, str]): Primary vendor contact email Example: receiving@swift-mfg.com.
        contact_phone (Union[Unset, str]): Primary vendor contact phone Example: +1-555-0123.
    """

    vendor_id: Union[Unset, str] = UNSET
    vendor_name: Union[Unset, str] = UNSET
    contact_email: Union[Unset, str] = UNSET
    contact_phone: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        vendor_id = self.vendor_id

        vendor_name = self.vendor_name

        contact_email = self.contact_email

        contact_phone = self.contact_phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if vendor_id is not UNSET:
            field_dict["vendorId"] = vendor_id
        if vendor_name is not UNSET:
            field_dict["vendorName"] = vendor_name
        if contact_email is not UNSET:
            field_dict["contactEmail"] = contact_email
        if contact_phone is not UNSET:
            field_dict["contactPhone"] = contact_phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        vendor_id = d.pop("vendorId", UNSET)

        vendor_name = d.pop("vendorName", UNSET)

        contact_email = d.pop("contactEmail", UNSET)

        contact_phone = d.pop("contactPhone", UNSET)

        create_wms_inbound_order_body_vendor = cls(
            vendor_id=vendor_id,
            vendor_name=vendor_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
        )

        create_wms_inbound_order_body_vendor.additional_properties = d
        return create_wms_inbound_order_body_vendor

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
