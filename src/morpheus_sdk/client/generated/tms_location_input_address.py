from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSLocationInputAddress")


@_attrs_define
class TMSLocationInputAddress:
    """Physical address of the location

    Attributes:
        street (str): Street address including number and street name Example: 1000 Industrial Blvd.
        city (str): City name Example: Atlanta.
        state (str): State or province code Example: GA.
        zip_code (str): Postal or ZIP code Example: 30309.
        country (Union[Unset, str]): Country code (ISO 3166-1 alpha-2) Example: US.
    """

    street: str
    city: str
    state: str
    zip_code: str
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
        field_dict.update(
            {
                "street": street,
                "city": city,
                "state": state,
                "zipCode": zip_code,
            }
        )
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street = d.pop("street")

        city = d.pop("city")

        state = d.pop("state")

        zip_code = d.pop("zipCode")

        country = d.pop("country", UNSET)

        tms_location_input_address = cls(
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            country=country,
        )

        tms_location_input_address.additional_properties = d
        return tms_location_input_address

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
