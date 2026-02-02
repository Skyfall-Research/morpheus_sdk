import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ERPShipmentEventsItem")


@_attrs_define
class ERPShipmentEventsItem:
    """
    Attributes:
        ts (Union[Unset, datetime.datetime]):  Example: 2024-01-15T14:30:00Z.
        location (Union[Unset, str]):  Example: Memphis, TN Hub.
        status (Union[Unset, str]):  Example: Package scanned at facility.
        note (Union[Unset, str]):  Example: Package processed through automated sorting.
    """

    ts: Union[Unset, datetime.datetime] = UNSET
    location: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    note: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ts: Union[Unset, str] = UNSET
        if not isinstance(self.ts, Unset):
            ts = self.ts.isoformat()

        location = self.location

        status = self.status

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ts is not UNSET:
            field_dict["ts"] = ts
        if location is not UNSET:
            field_dict["location"] = location
        if status is not UNSET:
            field_dict["status"] = status
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _ts = d.pop("ts", UNSET)
        ts: Union[Unset, datetime.datetime]
        if isinstance(_ts, Unset):
            ts = UNSET
        else:
            ts = isoparse(_ts)

        location = d.pop("location", UNSET)

        status = d.pop("status", UNSET)

        note = d.pop("note", UNSET)

        erp_shipment_events_item = cls(
            ts=ts,
            location=location,
            status=status,
            note=note,
        )

        erp_shipment_events_item.additional_properties = d
        return erp_shipment_events_item

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
