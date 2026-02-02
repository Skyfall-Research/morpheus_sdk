import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWMSTrackingEventBody")


@_attrs_define
class AddWMSTrackingEventBody:
    """
    Attributes:
        event_type (str): Type of tracking event Example: DEPARTED_FACILITY.
        event_date (datetime.datetime): Timestamp of the event Example: 2024-12-01T18:30:00.000Z.
        location (str): Location where event occurred Example: Atlanta, GA.
        description (str): Human-readable event description Example: Package departed Atlanta facility.
        carrier_event_code (Union[Unset, str]): Optional carrier-specific event code Example: DP.
    """

    event_type: str
    event_date: datetime.datetime
    location: str
    description: str
    carrier_event_code: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event_type = self.event_type

        event_date = self.event_date.isoformat()

        location = self.location

        description = self.description

        carrier_event_code = self.carrier_event_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "eventType": event_type,
                "eventDate": event_date,
                "location": location,
                "description": description,
            }
        )
        if carrier_event_code is not UNSET:
            field_dict["carrierEventCode"] = carrier_event_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event_type = d.pop("eventType")

        event_date = isoparse(d.pop("eventDate"))

        location = d.pop("location")

        description = d.pop("description")

        carrier_event_code = d.pop("carrierEventCode", UNSET)

        add_wms_tracking_event_body = cls(
            event_type=event_type,
            event_date=event_date,
            location=location,
            description=description,
            carrier_event_code=carrier_event_code,
        )

        add_wms_tracking_event_body.additional_properties = d
        return add_wms_tracking_event_body

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
