import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundShipmentEventsItem")


@_attrs_define
class WMSOutboundShipmentEventsItem:
    """
    Attributes:
        timestamp (Union[Unset, datetime.datetime]): Event timestamp Example: 2024-12-01T18:30:00.000Z.
        location (Union[Unset, str]): Event location Example: Atlanta, GA.
        status (Union[Unset, str]): Status at time of event Example: IN_TRANSIT.
        note (Union[Unset, str]): Event description Example: Package departed Atlanta facility.
        source (Union[Unset, str]): Event source system Example: CARRIER_API.
    """

    timestamp: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        location = self.location

        status = self.status

        note = self.note

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if location is not UNSET:
            field_dict["location"] = location
        if status is not UNSET:
            field_dict["status"] = status
        if note is not UNSET:
            field_dict["note"] = note
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        location = d.pop("location", UNSET)

        status = d.pop("status", UNSET)

        note = d.pop("note", UNSET)

        source = d.pop("source", UNSET)

        wms_outbound_shipment_events_item = cls(
            timestamp=timestamp,
            location=location,
            status=status,
            note=note,
            source=source,
        )

        wms_outbound_shipment_events_item.additional_properties = d
        return wms_outbound_shipment_events_item

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
