import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CheckInTMSTrailerBody")


@_attrs_define
class CheckInTMSTrailerBody:
    """
    Attributes:
        actual_arrival (datetime.datetime): Actual arrival timestamp Example: 2024-01-20T08:15:00.000Z.
        driver_name (Union[Unset, str]): Driver full name Example: John Smith.
        driver_phone (Union[Unset, str]): Driver contact phone number Example: +1-555-123-4567.
        seal_number (Union[Unset, str]): Trailer seal number Example: SEAL-789456.
        dock_door (Union[Unset, str]): Assigned dock door Example: DOCK-A-001.
    """

    actual_arrival: datetime.datetime
    driver_name: Union[Unset, str] = UNSET
    driver_phone: Union[Unset, str] = UNSET
    seal_number: Union[Unset, str] = UNSET
    dock_door: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        actual_arrival = self.actual_arrival.isoformat()

        driver_name = self.driver_name

        driver_phone = self.driver_phone

        seal_number = self.seal_number

        dock_door = self.dock_door

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actualArrival": actual_arrival,
            }
        )
        if driver_name is not UNSET:
            field_dict["driverName"] = driver_name
        if driver_phone is not UNSET:
            field_dict["driverPhone"] = driver_phone
        if seal_number is not UNSET:
            field_dict["sealNumber"] = seal_number
        if dock_door is not UNSET:
            field_dict["dockDoor"] = dock_door

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        actual_arrival = isoparse(d.pop("actualArrival"))

        driver_name = d.pop("driverName", UNSET)

        driver_phone = d.pop("driverPhone", UNSET)

        seal_number = d.pop("sealNumber", UNSET)

        dock_door = d.pop("dockDoor", UNSET)

        check_in_tms_trailer_body = cls(
            actual_arrival=actual_arrival,
            driver_name=driver_name,
            driver_phone=driver_phone,
            seal_number=seal_number,
            dock_door=dock_door,
        )

        check_in_tms_trailer_body.additional_properties = d
        return check_in_tms_trailer_body

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
