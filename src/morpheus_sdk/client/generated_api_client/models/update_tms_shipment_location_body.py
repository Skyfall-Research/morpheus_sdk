import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_tms_shipment_location_body_source import UpdateTMSShipmentLocationBodySource
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTMSShipmentLocationBody")


@_attrs_define
class UpdateTMSShipmentLocationBody:
    """
    Attributes:
        latitude (float): GPS latitude coordinate Example: 35.1495.
        longitude (float): GPS longitude coordinate Example: -90.049.
        city (Union[Unset, str]): Current city location Example: Memphis.
        state (Union[Unset, str]): Current state/province Example: TN.
        timestamp (Union[Unset, datetime.datetime]): Timestamp of location update Example: 2024-11-26T14:30:00.000Z.
        source (Union[Unset, UpdateTMSShipmentLocationBodySource]): Source of the location update Example: GPS.
    """

    latitude: float
    longitude: float
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    source: Union[Unset, UpdateTMSShipmentLocationBodySource] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        latitude = self.latitude

        longitude = self.longitude

        city = self.city

        state = self.state

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "latitude": latitude,
                "longitude": longitude,
            }
        )
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        latitude = d.pop("latitude")

        longitude = d.pop("longitude")

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        _source = d.pop("source", UNSET)
        source: Union[Unset, UpdateTMSShipmentLocationBodySource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = UpdateTMSShipmentLocationBodySource(_source)

        update_tms_shipment_location_body = cls(
            latitude=latitude,
            longitude=longitude,
            city=city,
            state=state,
            timestamp=timestamp,
            source=source,
        )

        update_tms_shipment_location_body.additional_properties = d
        return update_tms_shipment_location_body

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
