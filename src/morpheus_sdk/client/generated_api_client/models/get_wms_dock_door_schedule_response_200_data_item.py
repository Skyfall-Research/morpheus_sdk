import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSDockDoorScheduleResponse200DataItem")


@_attrs_define
class GetWMSDockDoorScheduleResponse200DataItem:
    """
    Attributes:
        appointment_id (Union[Unset, str]): Unique appointment identifier Example:
            tms_appointment_674565c1234567890abcdef.
        carrier_name (Union[Unset, str]): Carrier company name Example: Swift Transportation.
        trailer_number (Union[Unset, str]): Trailer identification number Example: TRL-98765.
        scheduled_arrival (Union[Unset, datetime.datetime]): Scheduled appointment arrival time Example:
            2024-11-27T09:00:00Z.
        appointment_type (Union[Unset, str]): Type of appointment Example: SCHEDULED.
        status (Union[Unset, str]): Current appointment status Example: OCCUPIED.
    """

    appointment_id: Union[Unset, str] = UNSET
    carrier_name: Union[Unset, str] = UNSET
    trailer_number: Union[Unset, str] = UNSET
    scheduled_arrival: Union[Unset, datetime.datetime] = UNSET
    appointment_type: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        appointment_id = self.appointment_id

        carrier_name = self.carrier_name

        trailer_number = self.trailer_number

        scheduled_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.scheduled_arrival, Unset):
            scheduled_arrival = self.scheduled_arrival.isoformat()

        appointment_type = self.appointment_type

        status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if appointment_id is not UNSET:
            field_dict["appointmentId"] = appointment_id
        if carrier_name is not UNSET:
            field_dict["carrierName"] = carrier_name
        if trailer_number is not UNSET:
            field_dict["trailerNumber"] = trailer_number
        if scheduled_arrival is not UNSET:
            field_dict["scheduledArrival"] = scheduled_arrival
        if appointment_type is not UNSET:
            field_dict["appointmentType"] = appointment_type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        appointment_id = d.pop("appointmentId", UNSET)

        carrier_name = d.pop("carrierName", UNSET)

        trailer_number = d.pop("trailerNumber", UNSET)

        _scheduled_arrival = d.pop("scheduledArrival", UNSET)
        scheduled_arrival: Union[Unset, datetime.datetime]
        if isinstance(_scheduled_arrival, Unset):
            scheduled_arrival = UNSET
        else:
            scheduled_arrival = isoparse(_scheduled_arrival)

        appointment_type = d.pop("appointmentType", UNSET)

        status = d.pop("status", UNSET)

        get_wms_dock_door_schedule_response_200_data_item = cls(
            appointment_id=appointment_id,
            carrier_name=carrier_name,
            trailer_number=trailer_number,
            scheduled_arrival=scheduled_arrival,
            appointment_type=appointment_type,
            status=status,
        )

        get_wms_dock_door_schedule_response_200_data_item.additional_properties = d
        return get_wms_dock_door_schedule_response_200_data_item

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
