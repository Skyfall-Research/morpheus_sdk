from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Address")


@_attrs_define
class Address:
    """Physical address for billing, shipping, or remittance

    Attributes:
        street (str): Street address Example: 123 Main St.
        city (str): City name Example: Atlanta.
        state (str): State or province code Example: GA.
        postal_code (str): Postal/ZIP code Example: 30303.
        country (str): Country code (ISO 3166-1 alpha-2) Example: US.
        street2 (Union[Unset, str]): Additional address line Example: Suite 100.
    """

    street: str
    city: str
    state: str
    postal_code: str
    country: str
    street2: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street = self.street

        city = self.city

        state = self.state

        postal_code = self.postal_code

        country = self.country

        street2 = self.street2

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "street": street,
                "city": city,
                "state": state,
                "postalCode": postal_code,
                "country": country,
            }
        )
        if street2 is not UNSET:
            field_dict["street2"] = street2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street = d.pop("street")

        city = d.pop("city")

        state = d.pop("state")

        postal_code = d.pop("postalCode")

        country = d.pop("country")

        street2 = d.pop("street2", UNSET)

        address = cls(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            street2=street2,
        )

        address.additional_properties = d
        return address

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
