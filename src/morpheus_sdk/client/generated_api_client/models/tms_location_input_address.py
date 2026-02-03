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
        city (str): City name Example: Atlanta.
        state (str): State or province code Example: GA.
        street1 (Union[Unset, str]): Street address including number and street name Example: 1000 Industrial Blvd.
        postal_code (Union[Unset, str]): Postal or ZIP code Example: 30309.
        country (Union[Unset, str]): Country code (ISO 3166-1 alpha-2) Example: US.
    """

    city: str
    state: str
    street1: Union[Unset, str] = UNSET
    postal_code: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        state = self.state

        street1 = self.street1

        postal_code = self.postal_code

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "state": state,
            }
        )
        if street1 is not UNSET:
            field_dict["street1"] = street1
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city")

        state = d.pop("state")

        street1 = d.pop("street1", UNSET)

        postal_code = d.pop("postalCode", UNSET)

        country = d.pop("country", UNSET)

        tms_location_input_address = cls(
            city=city,
            state=state,
            street1=street1,
            postal_code=postal_code,
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
