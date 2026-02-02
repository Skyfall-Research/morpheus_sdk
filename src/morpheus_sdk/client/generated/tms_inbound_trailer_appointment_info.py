import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSInboundTrailerAppointmentInfo")


@_attrs_define
class TMSInboundTrailerAppointmentInfo:
    """Appointment scheduling and timing details

    Attributes:
        appointment_id (Union[Unset, str]): Unique appointment identifier Example: APPT-ATL-001.
        scheduled_arrival (Union[Unset, datetime.datetime]): Scheduled arrival date and time Example:
            2024-01-20T08:00:00.000Z.
        scheduled_departure (Union[Unset, datetime.datetime]): Scheduled departure time Example:
            2024-01-20T16:00:00.000Z.
        estimated_arrival (Union[Unset, datetime.datetime]): Current estimated arrival time Example:
            2024-01-20T08:15:00.000Z.
        actual_arrival (Union[Unset, datetime.datetime]): Actual arrival timestamp Example: 2024-01-20T08:12:00.000Z.
        actual_departure (Union[Unset, datetime.datetime]): Actual departure timestamp Example:
            2024-01-20T17:30:00.000Z.
        dock_door (Union[Unset, str]): Assigned dock door Example: DOCK-A-001.
    """

    appointment_id: Union[Unset, str] = UNSET
    scheduled_arrival: Union[Unset, datetime.datetime] = UNSET
    scheduled_departure: Union[Unset, datetime.datetime] = UNSET
    estimated_arrival: Union[Unset, datetime.datetime] = UNSET
    actual_arrival: Union[Unset, datetime.datetime] = UNSET
    actual_departure: Union[Unset, datetime.datetime] = UNSET
    dock_door: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appointment_id = self.appointment_id

        scheduled_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_arrival, Unset):
            scheduled_arrival = self.scheduled_arrival.isoformat()

        scheduled_departure: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_departure, Unset):
            scheduled_departure = self.scheduled_departure.isoformat()

        estimated_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_arrival, Unset):
            estimated_arrival = self.estimated_arrival.isoformat()

        actual_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.actual_arrival, Unset):
            actual_arrival = self.actual_arrival.isoformat()

        actual_departure: Union[Unset, str] = UNSET
        if not isinstance(self.actual_departure, Unset):
            actual_departure = self.actual_departure.isoformat()

        dock_door = self.dock_door

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_id is not UNSET:
            field_dict["appointmentId"] = appointment_id
        if scheduled_arrival is not UNSET:
            field_dict["scheduledArrival"] = scheduled_arrival
        if scheduled_departure is not UNSET:
            field_dict["scheduledDeparture"] = scheduled_departure
        if estimated_arrival is not UNSET:
            field_dict["estimatedArrival"] = estimated_arrival
        if actual_arrival is not UNSET:
            field_dict["actualArrival"] = actual_arrival
        if actual_departure is not UNSET:
            field_dict["actualDeparture"] = actual_departure
        if dock_door is not UNSET:
            field_dict["dockDoor"] = dock_door

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appointment_id = d.pop("appointmentId", UNSET)

        _scheduled_arrival = d.pop("scheduledArrival", UNSET)
        scheduled_arrival: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_arrival, Unset):
            scheduled_arrival = UNSET
        else:
            scheduled_arrival = isoparse(_scheduled_arrival)

        _scheduled_departure = d.pop("scheduledDeparture", UNSET)
        scheduled_departure: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_departure, Unset):
            scheduled_departure = UNSET
        else:
            scheduled_departure = isoparse(_scheduled_departure)

        _estimated_arrival = d.pop("estimatedArrival", UNSET)
        estimated_arrival: Union[Unset, datetime.datetime]
        if isinstance(_estimated_arrival, Unset):
            estimated_arrival = UNSET
        else:
            estimated_arrival = isoparse(_estimated_arrival)

        _actual_arrival = d.pop("actualArrival", UNSET)
        actual_arrival: Union[Unset, datetime.datetime]
        if isinstance(_actual_arrival, Unset):
            actual_arrival = UNSET
        else:
            actual_arrival = isoparse(_actual_arrival)

        _actual_departure = d.pop("actualDeparture", UNSET)
        actual_departure: Union[Unset, datetime.datetime]
        if isinstance(_actual_departure, Unset):
            actual_departure = UNSET
        else:
            actual_departure = isoparse(_actual_departure)

        dock_door = d.pop("dockDoor", UNSET)

        tms_inbound_trailer_appointment_info = cls(
            appointment_id=appointment_id,
            scheduled_arrival=scheduled_arrival,
            scheduled_departure=scheduled_departure,
            estimated_arrival=estimated_arrival,
            actual_arrival=actual_arrival,
            actual_departure=actual_departure,
            dock_door=dock_door,
        )

        tms_inbound_trailer_appointment_info.additional_properties = d
        return tms_inbound_trailer_appointment_info

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
