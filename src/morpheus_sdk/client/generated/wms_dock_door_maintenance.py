import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDockDoorMaintenance")


@_attrs_define
class WMSDockDoorMaintenance:
    """Maintenance schedules and documentation for operational continuity

    Attributes:
        last_maintenance (Union[None, Unset, datetime.datetime]): Timestamp of last completed maintenance Example:
            2024-11-15T14:30:00Z.
        next_maintenance (Union[None, Unset, datetime.datetime]): Scheduled next maintenance timestamp Example:
            2024-12-15T14:30:00Z.
        maintenance_notes (Union[None, Unset, str]): Notes from last maintenance activity Example: Hydraulic system
            serviced, leveling dock calibrated.
    """

    last_maintenance: Union[None, Unset, datetime.datetime] = UNSET
    next_maintenance: Union[None, Unset, datetime.datetime] = UNSET
    maintenance_notes: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        last_maintenance: Union[None, Unset, str]
        if isinstance(self.last_maintenance, Unset):
            last_maintenance = UNSET
        elif isinstance(self.last_maintenance, datetime.datetime):
            last_maintenance = self.last_maintenance.isoformat()
        else:
            last_maintenance = self.last_maintenance

        next_maintenance: Union[None, Unset, str]
        if isinstance(self.next_maintenance, Unset):
            next_maintenance = UNSET
        elif isinstance(self.next_maintenance, datetime.datetime):
            next_maintenance = self.next_maintenance.isoformat()
        else:
            next_maintenance = self.next_maintenance

        maintenance_notes: Union[None, Unset, str]
        if isinstance(self.maintenance_notes, Unset):
            maintenance_notes = UNSET
        else:
            maintenance_notes = self.maintenance_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_maintenance is not UNSET:
            field_dict["lastMaintenance"] = last_maintenance
        if next_maintenance is not UNSET:
            field_dict["nextMaintenance"] = next_maintenance
        if maintenance_notes is not UNSET:
            field_dict["maintenanceNotes"] = maintenance_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_last_maintenance(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_maintenance_type_0 = isoparse(data)

                return last_maintenance_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        last_maintenance = _parse_last_maintenance(d.pop("lastMaintenance", UNSET))

        def _parse_next_maintenance(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_maintenance_type_0 = isoparse(data)

                return next_maintenance_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        next_maintenance = _parse_next_maintenance(d.pop("nextMaintenance", UNSET))

        def _parse_maintenance_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        maintenance_notes = _parse_maintenance_notes(d.pop("maintenanceNotes", UNSET))

        wms_dock_door_maintenance = cls(
            last_maintenance=last_maintenance,
            next_maintenance=next_maintenance,
            maintenance_notes=maintenance_notes,
        )

        wms_dock_door_maintenance.additional_properties = d
        return wms_dock_door_maintenance

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
