from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSDockDoorBodyEquipment")


@_attrs_define
class CreateWMSDockDoorBodyEquipment:
    """Available equipment and systems

    Attributes:
        forklift_access (Union[Unset, bool]): Forklift access capability Example: True.
        conveyor_system (Union[Unset, bool]): Conveyor system availability
        scales (Union[Unset, bool]): Weighing scales availability Example: True.
        light_system (Union[Unset, bool]): Lighting system capability Example: True.
    """

    forklift_access: Union[Unset, bool] = UNSET
    conveyor_system: Union[Unset, bool] = UNSET
    scales: Union[Unset, bool] = UNSET
    light_system: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        forklift_access = self.forklift_access

        conveyor_system = self.conveyor_system

        scales = self.scales

        light_system = self.light_system

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if forklift_access is not UNSET:
            field_dict["forkliftAccess"] = forklift_access
        if conveyor_system is not UNSET:
            field_dict["conveyorSystem"] = conveyor_system
        if scales is not UNSET:
            field_dict["scales"] = scales
        if light_system is not UNSET:
            field_dict["lightSystem"] = light_system

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        forklift_access = d.pop("forkliftAccess", UNSET)

        conveyor_system = d.pop("conveyorSystem", UNSET)

        scales = d.pop("scales", UNSET)

        light_system = d.pop("lightSystem", UNSET)

        create_wms_dock_door_body_equipment = cls(
            forklift_access=forklift_access,
            conveyor_system=conveyor_system,
            scales=scales,
            light_system=light_system,
        )

        create_wms_dock_door_body_equipment.additional_properties = d
        return create_wms_dock_door_body_equipment

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
