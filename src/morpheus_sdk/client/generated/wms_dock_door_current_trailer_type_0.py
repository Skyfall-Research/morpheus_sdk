import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDockDoorCurrentTrailerType0")


@_attrs_define
class WMSDockDoorCurrentTrailerType0:
    """Current trailer positioned at dock door for operations

    Attributes:
        trailer_id (Union[Unset, str]): Unique trailer identifier from TMS system Example: tms_inbound-
            trailer_674565c1234567890abcdef.
        trailer_number (Union[Unset, str]): Physical trailer identification number Example: TRL-98765.
        seal_numbers (Union[Unset, list[str]]): Security seal numbers for cargo verification Example: ['SEAL-12345',
            'SEAL-67890'].
        arrival_time (Union[Unset, datetime.datetime]): Actual trailer arrival time at dock Example:
            2024-11-27T08:45:00Z.
    """

    trailer_id: Union[Unset, str] = UNSET
    trailer_number: Union[Unset, str] = UNSET
    seal_numbers: Union[Unset, list[str]] = UNSET
    arrival_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trailer_id = self.trailer_id

        trailer_number = self.trailer_number

        seal_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.seal_numbers, Unset):
            seal_numbers = self.seal_numbers

        arrival_time: Union[Unset, str] = UNSET
        if not isinstance(self.arrival_time, Unset):
            arrival_time = self.arrival_time.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trailer_id is not UNSET:
            field_dict["trailerId"] = trailer_id
        if trailer_number is not UNSET:
            field_dict["trailerNumber"] = trailer_number
        if seal_numbers is not UNSET:
            field_dict["sealNumbers"] = seal_numbers
        if arrival_time is not UNSET:
            field_dict["arrivalTime"] = arrival_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trailer_id = d.pop("trailerId", UNSET)

        trailer_number = d.pop("trailerNumber", UNSET)

        seal_numbers = cast(list[str], d.pop("sealNumbers", UNSET))

        _arrival_time = d.pop("arrivalTime", UNSET)
        arrival_time: Union[Unset, datetime.datetime]
        if isinstance(_arrival_time, Unset):
            arrival_time = UNSET
        else:
            arrival_time = isoparse(_arrival_time)

        wms_dock_door_current_trailer_type_0 = cls(
            trailer_id=trailer_id,
            trailer_number=trailer_number,
            seal_numbers=seal_numbers,
            arrival_time=arrival_time,
        )

        wms_dock_door_current_trailer_type_0.additional_properties = d
        return wms_dock_door_current_trailer_type_0

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
