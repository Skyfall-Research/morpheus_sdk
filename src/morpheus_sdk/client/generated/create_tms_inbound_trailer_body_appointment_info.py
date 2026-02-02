import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateTMSInboundTrailerBodyAppointmentInfo")


@_attrs_define
class CreateTMSInboundTrailerBodyAppointmentInfo:
    """
    Attributes:
        scheduled_arrival (datetime.datetime): Scheduled arrival date and time Example: 2024-01-20T08:00:00.000Z.
        scheduled_departure (Union[Unset, datetime.datetime]): Scheduled departure time Example:
            2024-01-20T16:00:00.000Z.
        dock_door (Union[Unset, str]): Assigned dock door Example: DOCK-A-001.
    """

    scheduled_arrival: datetime.datetime
    scheduled_departure: Union[Unset, datetime.datetime] = UNSET
    dock_door: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_arrival = self.scheduled_arrival.isoformat()

        scheduled_departure: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_departure, Unset):
            scheduled_departure = self.scheduled_departure.isoformat()

        dock_door = self.dock_door

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledArrival": scheduled_arrival,
            }
        )
        if scheduled_departure is not UNSET:
            field_dict["scheduledDeparture"] = scheduled_departure
        if dock_door is not UNSET:
            field_dict["dockDoor"] = dock_door

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheduled_arrival = isoparse(d.pop("scheduledArrival"))

        _scheduled_departure = d.pop("scheduledDeparture", UNSET)
        scheduled_departure: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_departure, Unset):
            scheduled_departure = UNSET
        else:
            scheduled_departure = isoparse(_scheduled_departure)

        dock_door = d.pop("dockDoor", UNSET)

        create_tms_inbound_trailer_body_appointment_info = cls(
            scheduled_arrival=scheduled_arrival,
            scheduled_departure=scheduled_departure,
            dock_door=dock_door,
        )

        create_tms_inbound_trailer_body_appointment_info.additional_properties = d
        return create_tms_inbound_trailer_body_appointment_info

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
