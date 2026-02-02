from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDistributionCenterContactInfo")


@_attrs_define
class WMSDistributionCenterContactInfo:
    """Contact information for the facility

    Attributes:
        phone (Union[Unset, str]): Primary phone number Example: +1-404-555-0123.
        email (Union[Unset, str]): Primary email address Example: ops@atlanta-east.company.com.
        manager (Union[Unset, str]): Facility manager name Example: John Smith.
    """

    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    manager: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        phone = self.phone

        email = self.email

        manager = self.manager

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if manager is not UNSET:
            field_dict["manager"] = manager

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        manager = d.pop("manager", UNSET)

        wms_distribution_center_contact_info = cls(
            phone=phone,
            email=email,
            manager=manager,
        )

        wms_distribution_center_contact_info.additional_properties = d
        return wms_distribution_center_contact_info

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
