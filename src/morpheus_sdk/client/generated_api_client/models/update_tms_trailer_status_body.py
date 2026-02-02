import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_tms_trailer_status_body_status import UpdateTMSTrailerStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTMSTrailerStatusBody")


@_attrs_define
class UpdateTMSTrailerStatusBody:
    """
    Attributes:
        status (UpdateTMSTrailerStatusBodyStatus): New trailer status Example: CHECKED_IN.
        actual_arrival (Union[Unset, datetime.datetime]): Actual arrival timestamp Example: 2024-01-20T08:15:00.000Z.
        actual_departure (Union[Unset, datetime.datetime]): Actual departure timestamp Example:
            2024-01-20T17:30:00.000Z.
        estimated_arrival (Union[Unset, datetime.datetime]): Updated estimated arrival Example:
            2024-01-20T08:30:00.000Z.
        dock_door (Union[Unset, str]): Assigned dock door Example: DOCK-A-001.
    """

    status: UpdateTMSTrailerStatusBodyStatus
    actual_arrival: Union[Unset, datetime.datetime] = UNSET
    actual_departure: Union[Unset, datetime.datetime] = UNSET
    estimated_arrival: Union[Unset, datetime.datetime] = UNSET
    dock_door: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        actual_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.actual_arrival, Unset):
            actual_arrival = self.actual_arrival.isoformat()

        actual_departure: Union[Unset, str] = UNSET
        if not isinstance(self.actual_departure, Unset):
            actual_departure = self.actual_departure.isoformat()

        estimated_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_arrival, Unset):
            estimated_arrival = self.estimated_arrival.isoformat()

        dock_door = self.dock_door

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if actual_arrival is not UNSET:
            field_dict["actualArrival"] = actual_arrival
        if actual_departure is not UNSET:
            field_dict["actualDeparture"] = actual_departure
        if estimated_arrival is not UNSET:
            field_dict["estimatedArrival"] = estimated_arrival
        if dock_door is not UNSET:
            field_dict["dockDoor"] = dock_door

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = UpdateTMSTrailerStatusBodyStatus(d.pop("status"))

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

        _estimated_arrival = d.pop("estimatedArrival", UNSET)
        estimated_arrival: Union[Unset, datetime.datetime]
        if isinstance(_estimated_arrival, Unset):
            estimated_arrival = UNSET
        else:
            estimated_arrival = isoparse(_estimated_arrival)

        dock_door = d.pop("dockDoor", UNSET)

        update_tms_trailer_status_body = cls(
            status=status,
            actual_arrival=actual_arrival,
            actual_departure=actual_departure,
            estimated_arrival=estimated_arrival,
            dock_door=dock_door,
        )

        update_tms_trailer_status_body.additional_properties = d
        return update_tms_trailer_status_body

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
