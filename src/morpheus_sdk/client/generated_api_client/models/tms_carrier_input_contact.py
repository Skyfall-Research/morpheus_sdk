from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tms_carrier_input_contact_address import TMSCarrierInputContactAddress


T = TypeVar("T", bound="TMSCarrierInputContact")


@_attrs_define
class TMSCarrierInputContact:
    """Carrier contact information

    Attributes:
        primary_contact_name (Union[Unset, str]): Name of the primary contact person Example: John Smith.
        email (Union[Unset, str]): Contact email address Example: dispatch@acmetransport.com.
        phone (Union[Unset, str]): Contact phone number Example: 555-0199.
        address (Union[Unset, TMSCarrierInputContactAddress]): Carrier business address
    """

    primary_contact_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    address: Union[Unset, "TMSCarrierInputContactAddress"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        primary_contact_name = self.primary_contact_name

        email = self.email

        phone = self.phone

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary_contact_name is not UNSET:
            field_dict["primaryContactName"] = primary_contact_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone
        if address is not UNSET:
            field_dict["address"] = address

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tms_carrier_input_contact_address import TMSCarrierInputContactAddress

        d = dict(src_dict)
        primary_contact_name = d.pop("primaryContactName", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, TMSCarrierInputContactAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = TMSCarrierInputContactAddress.from_dict(_address)

        tms_carrier_input_contact = cls(
            primary_contact_name=primary_contact_name,
            email=email,
            phone=phone,
            address=address,
        )

        tms_carrier_input_contact.additional_properties = d
        return tms_carrier_input_contact

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
