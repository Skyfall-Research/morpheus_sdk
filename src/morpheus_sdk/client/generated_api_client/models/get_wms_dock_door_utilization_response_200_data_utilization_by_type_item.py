from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_wms_dock_door_utilization_response_200_data_utilization_by_type_item_door_type import (
    GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItemDoorType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItem")


@_attrs_define
class GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItem:
    """
    Attributes:
        door_type (Union[Unset, GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItemDoorType]):  Example:
            INBOUND.
        total_doors (Union[Unset, float]): Total doors of this type Example: 8.
        occupied_doors (Union[Unset, float]): Occupied doors of this type Example: 3.
        utilization_percentage (Union[Unset, float]): Type-specific utilization percentage Example: 37.5.
    """

    door_type: Union[Unset, GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItemDoorType] = UNSET
    total_doors: Union[Unset, float] = UNSET
    occupied_doors: Union[Unset, float] = UNSET
    utilization_percentage: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        door_type: Union[Unset, str] = UNSET
        if not isinstance(self.door_type, Unset):
            door_type = self.door_type.value

        total_doors = self.total_doors

        occupied_doors = self.occupied_doors

        utilization_percentage = self.utilization_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if door_type is not UNSET:
            field_dict["doorType"] = door_type
        if total_doors is not UNSET:
            field_dict["totalDoors"] = total_doors
        if occupied_doors is not UNSET:
            field_dict["occupiedDoors"] = occupied_doors
        if utilization_percentage is not UNSET:
            field_dict["utilizationPercentage"] = utilization_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _door_type = d.pop("doorType", UNSET)
        door_type: Union[Unset, GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItemDoorType]
        if isinstance(_door_type, Unset):
            door_type = UNSET
        else:
            door_type = GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItemDoorType(_door_type)

        total_doors = d.pop("totalDoors", UNSET)

        occupied_doors = d.pop("occupiedDoors", UNSET)

        utilization_percentage = d.pop("utilizationPercentage", UNSET)

        get_wms_dock_door_utilization_response_200_data_utilization_by_type_item = cls(
            door_type=door_type,
            total_doors=total_doors,
            occupied_doors=occupied_doors,
            utilization_percentage=utilization_percentage,
        )

        get_wms_dock_door_utilization_response_200_data_utilization_by_type_item.additional_properties = d
        return get_wms_dock_door_utilization_response_200_data_utilization_by_type_item

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
