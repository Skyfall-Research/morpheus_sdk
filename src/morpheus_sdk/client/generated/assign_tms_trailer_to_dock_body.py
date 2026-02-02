from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignTMSTrailerToDockBody")


@_attrs_define
class AssignTMSTrailerToDockBody:
    """
    Attributes:
        dock_door (str): Dock door identifier for assignment Example: DOCK-A-001.
    """

    dock_door: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dock_door = self.dock_door

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dockDoor": dock_door,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        dock_door = d.pop("dockDoor")

        assign_tms_trailer_to_dock_body = cls(
            dock_door=dock_door,
        )

        assign_tms_trailer_to_dock_body.additional_properties = d
        return assign_tms_trailer_to_dock_body

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
