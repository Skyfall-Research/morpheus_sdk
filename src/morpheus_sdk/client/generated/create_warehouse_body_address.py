from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWarehouseBodyAddress")


@_attrs_define
class CreateWarehouseBodyAddress:
    """Physical warehouse address

    Attributes:
        street (str):  Example: 1234 Industrial Blvd.
        city (str):  Example: Atlanta.
        state (str):  Example: GA.
        postal_code (str):  Example: 30309.
        country (str):  Example: USA.
        latitude (Union[Unset, float]):  Example: 33.749.
        longitude (Union[Unset, float]):  Example: -84.388.
    """

    street: str
    city: str
    state: str
    postal_code: str
    country: str
    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        street = self.street

        city = self.city

        state = self.state

        postal_code = self.postal_code

        country = self.country

        latitude = self.latitude

        longitude = self.longitude

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
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        street = d.pop("street")

        city = d.pop("city")

        state = d.pop("state")

        postal_code = d.pop("postalCode")

        country = d.pop("country")

        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        create_warehouse_body_address = cls(
            street=street,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            latitude=latitude,
            longitude=longitude,
        )

        create_warehouse_body_address.additional_properties = d
        return create_warehouse_body_address

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
