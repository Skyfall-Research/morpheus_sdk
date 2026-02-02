import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDockDoorCurrentAppointmentType0")


@_attrs_define
class WMSDockDoorCurrentAppointmentType0:
    """Current active appointment assigned to dock door

    Attributes:
        appointment_id (Union[Unset, str]): Unique appointment identifier from scheduling system Example:
            tms_appointment_674565c1234567890abcdef.
        carrier (Union[Unset, str]): Carrier company name responsible for the appointment Example: Swift Transportation.
        trailer_number (Union[Unset, str]): Trailer identification number for operational tracking Example: TRL-98765.
        start_time (Union[Unset, datetime.datetime]): Scheduled appointment start time Example: 2024-11-27T09:00:00Z.
        expected_end_time (Union[Unset, datetime.datetime]): Expected completion time for resource planning Example:
            2024-11-27T13:00:00Z.
    """

    appointment_id: Union[Unset, str] = UNSET
    carrier: Union[Unset, str] = UNSET
    trailer_number: Union[Unset, str] = UNSET
    start_time: Union[Unset, datetime.datetime] = UNSET
    expected_end_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appointment_id = self.appointment_id

        carrier = self.carrier

        trailer_number = self.trailer_number

        start_time: Union[Unset, str] = UNSET
        if not isinstance(self.start_time, Unset):
            start_time = self.start_time.isoformat()

        expected_end_time: Union[Unset, str] = UNSET
        if not isinstance(self.expected_end_time, Unset):
            expected_end_time = self.expected_end_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_id is not UNSET:
            field_dict["appointmentId"] = appointment_id
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if trailer_number is not UNSET:
            field_dict["trailerNumber"] = trailer_number
        if start_time is not UNSET:
            field_dict["startTime"] = start_time
        if expected_end_time is not UNSET:
            field_dict["expectedEndTime"] = expected_end_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appointment_id = d.pop("appointmentId", UNSET)

        carrier = d.pop("carrier", UNSET)

        trailer_number = d.pop("trailerNumber", UNSET)

        _start_time = d.pop("startTime", UNSET)
        start_time: Union[Unset, datetime.datetime]
        if isinstance(_start_time, Unset):
            start_time = UNSET
        else:
            start_time = isoparse(_start_time)

        _expected_end_time = d.pop("expectedEndTime", UNSET)
        expected_end_time: Union[Unset, datetime.datetime]
        if isinstance(_expected_end_time, Unset):
            expected_end_time = UNSET
        else:
            expected_end_time = isoparse(_expected_end_time)

        wms_dock_door_current_appointment_type_0 = cls(
            appointment_id=appointment_id,
            carrier=carrier,
            trailer_number=trailer_number,
            start_time=start_time,
            expected_end_time=expected_end_time,
        )

        wms_dock_door_current_appointment_type_0.additional_properties = d
        return wms_dock_door_current_appointment_type_0

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
