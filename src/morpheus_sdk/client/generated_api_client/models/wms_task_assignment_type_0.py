import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSTaskAssignmentType0")


@_attrs_define
class WMSTaskAssignmentType0:
    """Task assignment and resource allocation

    Attributes:
        user_id (Union[Unset, str]): Assigned user identifier Example: USER-001.
        user_name (Union[Unset, str]): Assigned user name for display Example: John Smith.
        equipment_id (Union[None, Unset, str]): Assigned equipment identifier Example: FORK-001.
        assigned_at (Union[None, Unset, datetime.datetime]): Timestamp when task was assigned Example:
            2024-11-27T09:15:00Z.
    """

    user_id: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    equipment_id: Union[None, Unset, str] = UNSET
    assigned_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user_name = self.user_name

        equipment_id: Union[None, Unset, str]
        if isinstance(self.equipment_id, Unset):
            equipment_id = UNSET
        else:
            equipment_id = self.equipment_id

        assigned_at: Union[None, Unset, str]
        if isinstance(self.assigned_at, Unset):
            assigned_at = UNSET
        elif isinstance(self.assigned_at, datetime.datetime):
            assigned_at = self.assigned_at.isoformat()
        else:
            assigned_at = self.assigned_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if equipment_id is not UNSET:
            field_dict["equipmentId"] = equipment_id
        if assigned_at is not UNSET:
            field_dict["assignedAt"] = assigned_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        def _parse_equipment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        equipment_id = _parse_equipment_id(d.pop("equipmentId", UNSET))

        def _parse_assigned_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_at_type_0 = isoparse(data)

                return assigned_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        assigned_at = _parse_assigned_at(d.pop("assignedAt", UNSET))

        wms_task_assignment_type_0 = cls(
            user_id=user_id,
            user_name=user_name,
            equipment_id=equipment_id,
            assigned_at=assigned_at,
        )

        wms_task_assignment_type_0.additional_properties = d
        return wms_task_assignment_type_0

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
