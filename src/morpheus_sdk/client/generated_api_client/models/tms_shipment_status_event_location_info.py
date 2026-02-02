from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentStatusEventLocationInfo")


@_attrs_define
class TMSShipmentStatusEventLocationInfo:
    """Location details for LOCATION_UPDATE events

    Attributes:
        latitude (Union[Unset, float]): Latitude coordinate of the current position Example: 35.1495.
        longitude (Union[Unset, float]): Longitude coordinate of the current position Example: -90.049.
        city (Union[Unset, str]): City name at the current location Example: Memphis.
        state (Union[Unset, str]): State or province code Example: TN.
        zip_code (Union[Unset, str]): Postal or ZIP code at the current location Example: 38103.
        facility (Union[Unset, str]): Name of the facility if at a known location Example: Memphis Hub.
    """

    latitude: Union[Unset, float] = UNSET
    longitude: Union[Unset, float] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    facility: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        city = self.city

        state = self.state

        zip_code = self.zip_code

        facility = self.facility

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latitude is not UNSET:
            field_dict["latitude"] = latitude
        if longitude is not UNSET:
            field_dict["longitude"] = longitude
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if zip_code is not UNSET:
            field_dict["zipCode"] = zip_code
        if facility is not UNSET:
            field_dict["facility"] = facility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude", UNSET)

        longitude = d.pop("longitude", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        zip_code = d.pop("zipCode", UNSET)

        facility = d.pop("facility", UNSET)

        tms_shipment_status_event_location_info = cls(
            latitude=latitude,
            longitude=longitude,
            city=city,
            state=state,
            zip_code=zip_code,
            facility=facility,
        )

        tms_shipment_status_event_location_info.additional_properties = d
        return tms_shipment_status_event_location_info

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
