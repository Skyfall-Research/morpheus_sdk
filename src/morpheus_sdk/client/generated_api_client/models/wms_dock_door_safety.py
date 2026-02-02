import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDockDoorSafety")


@_attrs_define
class WMSDockDoorSafety:
    """Safety equipment and inspection schedules for compliance management

    Attributes:
        emergency_stop (Union[Unset, bool]): Emergency stop system availability Example: True.
        safety_lights (Union[Unset, bool]): Safety lighting system operational status Example: True.
        last_safety_inspection (Union[None, Unset, datetime.datetime]): Timestamp of last completed safety inspection
            Example: 2024-11-20T10:00:00Z.
        next_safety_inspection (Union[None, Unset, datetime.datetime]): Scheduled next safety inspection timestamp
            Example: 2024-12-20T10:00:00Z.
    """

    emergency_stop: Union[Unset, bool] = UNSET
    safety_lights: Union[Unset, bool] = UNSET
    last_safety_inspection: Union[None, Unset, datetime.datetime] = UNSET
    next_safety_inspection: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emergency_stop = self.emergency_stop

        safety_lights = self.safety_lights

        last_safety_inspection: Union[None, Unset, str]
        if isinstance(self.last_safety_inspection, Unset):
            last_safety_inspection = UNSET
        elif isinstance(self.last_safety_inspection, datetime.datetime):
            last_safety_inspection = self.last_safety_inspection.isoformat()
        else:
            last_safety_inspection = self.last_safety_inspection

        next_safety_inspection: Union[None, Unset, str]
        if isinstance(self.next_safety_inspection, Unset):
            next_safety_inspection = UNSET
        elif isinstance(self.next_safety_inspection, datetime.datetime):
            next_safety_inspection = self.next_safety_inspection.isoformat()
        else:
            next_safety_inspection = self.next_safety_inspection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if emergency_stop is not UNSET:
            field_dict["emergencyStop"] = emergency_stop
        if safety_lights is not UNSET:
            field_dict["safetyLights"] = safety_lights
        if last_safety_inspection is not UNSET:
            field_dict["lastSafetyInspection"] = last_safety_inspection
        if next_safety_inspection is not UNSET:
            field_dict["nextSafetyInspection"] = next_safety_inspection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        emergency_stop = d.pop("emergencyStop", UNSET)

        safety_lights = d.pop("safetyLights", UNSET)

        def _parse_last_safety_inspection(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_safety_inspection_type_0 = isoparse(data)

                return last_safety_inspection_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_safety_inspection = _parse_last_safety_inspection(d.pop("lastSafetyInspection", UNSET))

        def _parse_next_safety_inspection(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_safety_inspection_type_0 = isoparse(data)

                return next_safety_inspection_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_safety_inspection = _parse_next_safety_inspection(d.pop("nextSafetyInspection", UNSET))

        wms_dock_door_safety = cls(
            emergency_stop=emergency_stop,
            safety_lights=safety_lights,
            last_safety_inspection=last_safety_inspection,
            next_safety_inspection=next_safety_inspection,
        )

        wms_dock_door_safety.additional_properties = d
        return wms_dock_door_safety

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
