from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSWarehouseAddress")


@_attrs_define
class WMSWarehouseAddress:
    """Physical warehouse address information

    Attributes:
        city (str): City name Example: Atlanta.
        state (str): State or province Example: GA.
        postal_code (str): Postal or ZIP code Example: 30309.
        country (str): Country name Example: USA.
        street (Union[Unset, str]): Street address Example: 1234 Industrial Blvd.
        latitude (Union[None, Unset, float]): Geographic latitude coordinate Example: 33.749.
        longitude (Union[None, Unset, float]): Geographic longitude coordinate Example: -84.388.
    """

    city: str
    state: str
    postal_code: str
    country: str
    street: Union[Unset, str] = UNSET
    latitude: Union[None, Unset, float] = UNSET
    longitude: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        state = self.state

        postal_code = self.postal_code

        country = self.country

        street = self.street

        latitude: Union[None, Unset, float]
        if isinstance(self.latitude, Unset):
            latitude = UNSET
        else:
            latitude = self.latitude

        longitude: Union[None, Unset, float]
        if isinstance(self.longitude, Unset):
            longitude = UNSET
        else:
            longitude = self.longitude

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "state": state,
                "postalCode": postal_code,
                "country": country,
            }
        )
        if street is not UNSET:
            field_dict["street"] = street
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city")

        state = d.pop("state")

        postal_code = d.pop("postalCode")

        country = d.pop("country")

        street = d.pop("street", UNSET)

        def _parse_latitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        latitude = _parse_latitude(d.pop("latitude", UNSET))

        def _parse_longitude(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        longitude = _parse_longitude(d.pop("longitude", UNSET))

        wms_warehouse_address = cls(
            city=city,
            state=state,
            postal_code=postal_code,
            country=country,
            street=street,
            latitude=latitude,
            longitude=longitude,
        )

        wms_warehouse_address.additional_properties = d
        return wms_warehouse_address

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
