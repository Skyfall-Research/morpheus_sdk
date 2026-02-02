import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_tms_shipment_status_body_status import UpdateTMSShipmentStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTMSShipmentStatusBody")


@_attrs_define
class UpdateTMSShipmentStatusBody:
    """
    Attributes:
        status (UpdateTMSShipmentStatusBodyStatus): New shipment status Example: IN_TRANSIT.
        timestamp (Union[Unset, datetime.datetime]): Timestamp of status change Example: 2024-11-26T14:30:00.000Z.
        location (Union[Unset, str]): Location where status change occurred Example: Memphis, TN.
        note (Union[Unset, str]): Additional notes about status change Example: Shipment departed Memphis hub.
        source (Union[Unset, str]): Source of the status update Example: EDI_214.
    """

    status: UpdateTMSShipmentStatusBodyStatus
    timestamp: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        location = self.location

        note = self.note

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if location is not UNSET:
            field_dict["location"] = location
        if note is not UNSET:
            field_dict["note"] = note
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = UpdateTMSShipmentStatusBodyStatus(d.pop("status"))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        location = d.pop("location", UNSET)

        note = d.pop("note", UNSET)

        source = d.pop("source", UNSET)

        update_tms_shipment_status_body = cls(
            status=status,
            timestamp=timestamp,
            location=location,
            note=note,
            source=source,
        )

        update_tms_shipment_status_body.additional_properties = d
        return update_tms_shipment_status_body

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
