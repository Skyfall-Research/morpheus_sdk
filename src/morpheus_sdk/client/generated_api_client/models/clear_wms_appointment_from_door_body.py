from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClearWMSAppointmentFromDoorBody")


@_attrs_define
class ClearWMSAppointmentFromDoorBody:
    """
    Example:
        {'completionNotes': 'Unloading completed successfully. Minor delay due to trailer seal issues.'}

    Attributes:
        completion_notes (Union[Unset, str]): Optional notes about appointment completion Example: Unloading completed
            successfully. Minor delay due to trailer seal issues..
    """

    completion_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completion_notes = self.completion_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if completion_notes is not UNSET:
            field_dict["completionNotes"] = completion_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completion_notes = d.pop("completionNotes", UNSET)

        clear_wms_appointment_from_door_body = cls(
            completion_notes=completion_notes,
        )

        clear_wms_appointment_from_door_body.additional_properties = d
        return clear_wms_appointment_from_door_body

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
