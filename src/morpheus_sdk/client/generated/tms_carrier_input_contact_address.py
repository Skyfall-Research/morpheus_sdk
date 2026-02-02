from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSCarrierInputContactAddress")


@_attrs_define
class TMSCarrierInputContactAddress:
    """Carrier business address

    Attributes:
        street (Union[Unset, str]):  Example: 100 Logistics Blvd.
        city (Union[Unset, str]):  Example: Atlanta.
        state (Union[Unset, str]):  Example: GA.
        zip_code (Union[Unset, str]):  Example: 30309.
        country (Union[Unset, str]):  Example: US.
    """

    street: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street = self.street

        city = self.city

        state = self.state

        zip_code = self.zip_code

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if street is not UNSET:
            field_dict["street"] = street
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street = d.pop("street", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        country = d.pop("country", UNSET)

        tms_carrier_input_contact_address = cls(
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
        )

        tms_carrier_input_contact_address.additional_properties = d
        return tms_carrier_input_contact_address

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
