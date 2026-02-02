import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="AssignWMSAppointmentToDoorBody")


@_attrs_define
class AssignWMSAppointmentToDoorBody:
    """
    Example:
        {'appointmentId': 'tms_appointment_674565c1234567890abcdef', 'carrier': 'Swift Transportation', 'trailerNumber':
            'TRL-98765', 'startTime': '2024-11-27T09:00:00Z', 'expectedEndTime': '2024-11-27T13:00:00Z'}

    Attributes:
        appointment_id (str): Unique identifier for the appointment Example: tms_appointment_674565c1234567890abcdef.
        carrier (str): Carrier company name or identifier Example: Swift Transportation.
        trailer_number (str): Trailer identification number Example: TRL-98765.
        start_time (datetime.datetime): Scheduled appointment start time Example: 2024-11-27T09:00:00Z.
        expected_end_time (datetime.datetime): Expected completion time Example: 2024-11-27T13:00:00Z.
    """

    appointment_id: str
    carrier: str
    trailer_number: str
    start_time: datetime.datetime
    expected_end_time: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appointment_id = self.appointment_id

        carrier = self.carrier

        trailer_number = self.trailer_number

        start_time = self.start_time.isoformat()

        expected_end_time = self.expected_end_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "appointmentId": appointment_id,
                "carrier": carrier,
                "trailerNumber": trailer_number,
                "startTime": start_time,
                "expectedEndTime": expected_end_time,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appointment_id = d.pop("appointmentId")

        carrier = d.pop("carrier")

        trailer_number = d.pop("trailerNumber")

        start_time = isoparse(d.pop("startTime"))

        expected_end_time = isoparse(d.pop("expectedEndTime"))

        assign_wms_appointment_to_door_body = cls(
            appointment_id=appointment_id,
            carrier=carrier,
            trailer_number=trailer_number,
            start_time=start_time,
            expected_end_time=expected_end_time,
        )

        assign_wms_appointment_to_door_body.additional_properties = d
        return assign_wms_appointment_to_door_body

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
