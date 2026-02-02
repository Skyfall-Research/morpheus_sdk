import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddERPShipmentEventBody")


@_attrs_define
class AddERPShipmentEventBody:
    """
    Attributes:
        ts (datetime.datetime): Event timestamp (required) Example: 2024-01-15T14:30:00Z.
        location (str): Event location (required) Example: Memphis, TN Hub.
        status (str): Event status description (required) Example: Package scanned at facility.
        note (Union[Unset, str]): Optional event note Example: Package processed through automated sorting facility.
    """

    ts: datetime.datetime
    location: str
    status: str
    note: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ts = self.ts.isoformat()

        location = self.location

        status = self.status

        note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ts": ts,
                "location": location,
                "status": status,
            }
        )
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ts = isoparse(d.pop("ts"))

        location = d.pop("location")

        status = d.pop("status")

        note = d.pop("note", UNSET)

        add_erp_shipment_event_body = cls(
            ts=ts,
            location=location,
            status=status,
            note=note,
        )

        add_erp_shipment_event_body.additional_properties = d
        return add_erp_shipment_event_body

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
