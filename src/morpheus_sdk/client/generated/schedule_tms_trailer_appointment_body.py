import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScheduleTMSTrailerAppointmentBody")


@_attrs_define
class ScheduleTMSTrailerAppointmentBody:
    """
    Attributes:
        scheduled_arrival (datetime.datetime): Scheduled arrival date and time Example: 2024-01-20T08:00:00.000Z.
        dc_id (str): Distribution center identifier Example: DC_ATL_001.
        appointment_id (Union[Unset, str]): Appointment identifier (auto-generated if not provided) Example: APPT-
            ATL-001.
        scheduled_departure (Union[Unset, datetime.datetime]): Scheduled departure time Example:
            2024-01-20T16:00:00.000Z.
        dock_door (Union[Unset, str]): Assigned dock door Example: DOCK-A-001.
        facility_name (Union[Unset, str]): Facility name for driver reference Example: Atlanta Distribution Center.
    """

    scheduled_arrival: datetime.datetime
    dc_id: str
    appointment_id: Union[Unset, str] = UNSET
    scheduled_departure: Union[Unset, datetime.datetime] = UNSET
    dock_door: Union[Unset, str] = UNSET
    facility_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scheduled_arrival = self.scheduled_arrival.isoformat()

        dc_id = self.dc_id

        appointment_id = self.appointment_id

        scheduled_departure: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_departure, Unset):
            scheduled_departure = self.scheduled_departure.isoformat()

        dock_door = self.dock_door

        facility_name = self.facility_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scheduledArrival": scheduled_arrival,
                "dcId": dc_id,
            }
        )
        if appointment_id is not UNSET:
            field_dict["appointmentId"] = appointment_id
        if scheduled_departure is not UNSET:
            field_dict["scheduledDeparture"] = scheduled_departure
        if dock_door is not UNSET:
            field_dict["dockDoor"] = dock_door
        if facility_name is not UNSET:
            field_dict["facilityName"] = facility_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        scheduled_arrival = isoparse(d.pop("scheduledArrival"))

        dc_id = d.pop("dcId")

        appointment_id = d.pop("appointmentId", UNSET)

        _scheduled_departure = d.pop("scheduledDeparture", UNSET)
        scheduled_departure: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_departure, Unset):
            scheduled_departure = UNSET
        else:
            scheduled_departure = isoparse(_scheduled_departure)

        dock_door = d.pop("dockDoor", UNSET)

        facility_name = d.pop("facilityName", UNSET)

        schedule_tms_trailer_appointment_body = cls(
            scheduled_arrival=scheduled_arrival,
            dc_id=dc_id,
            appointment_id=appointment_id,
            scheduled_departure=scheduled_departure,
            dock_door=dock_door,
            facility_name=facility_name,
        )

        schedule_tms_trailer_appointment_body.additional_properties = d
        return schedule_tms_trailer_appointment_body

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
