import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentExternalEventsItem")


@_attrs_define
class TMSShipmentExternalEventsItem:
    """
    Attributes:
        event_type (Union[Unset, str]): Type of external event Example: EDI_214.
        event_description (Union[Unset, str]): Detailed description of the event Example: Shipment arrived at cross-dock
            facility.
        event_time (Union[Unset, datetime.datetime]): Timestamp when the event occurred Example:
            2024-11-27T10:30:00.000Z.
        source (Union[Unset, str]): Source system that generated the event Example: CARRIER_EDI.
    """

    event_type: Union[Unset, str] = UNSET
    event_description: Union[Unset, str] = UNSET
    event_time: Union[Unset, datetime.datetime] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        event_description = self.event_description

        event_time: Union[Unset, str] = UNSET
        if not isinstance(self.event_time, Unset):
            event_time = self.event_time.isoformat()

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event_type is not UNSET:
            field_dict["eventType"] = event_type
        if event_description is not UNSET:
            field_dict["eventDescription"] = event_description
        if event_time is not UNSET:
            field_dict["eventTime"] = event_time
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = d.pop("eventType", UNSET)

        event_description = d.pop("eventDescription", UNSET)

        _event_time = d.pop("eventTime", UNSET)
        event_time: Union[Unset, datetime.datetime]
        if isinstance(_event_time, Unset):
            event_time = UNSET
        else:
            event_time = isoparse(_event_time)

        source = d.pop("source", UNSET)

        tms_shipment_external_events_item = cls(
            event_type=event_type,
            event_description=event_description,
            event_time=event_time,
            source=source,
        )

        tms_shipment_external_events_item.additional_properties = d
        return tms_shipment_external_events_item

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
