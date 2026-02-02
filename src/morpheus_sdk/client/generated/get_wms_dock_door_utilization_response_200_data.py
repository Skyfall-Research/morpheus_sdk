from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_dock_door_utilization_response_200_data_utilization_by_type_item import (
        GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItem,
    )


T = TypeVar("T", bound="GetWMSDockDoorUtilizationResponse200Data")


@_attrs_define
class GetWMSDockDoorUtilizationResponse200Data:
    """
    Attributes:
        total_doors (Union[Unset, float]): Total number of dock doors in warehouse Example: 12.
        available_doors (Union[Unset, float]): Number of doors currently available Example: 7.
        occupied_doors (Union[Unset, float]): Number of doors currently occupied Example: 4.
        maintenance_doors (Union[Unset, float]): Number of doors under maintenance Example: 1.
        utilization_percentage (Union[Unset, float]): Overall utilization percentage Example: 33.33.
        utilization_by_type (Union[Unset, list['GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItem']]):
            Utilization breakdown by door type
    """

    total_doors: Union[Unset, float] = UNSET
    available_doors: Union[Unset, float] = UNSET
    occupied_doors: Union[Unset, float] = UNSET
    maintenance_doors: Union[Unset, float] = UNSET
    utilization_percentage: Union[Unset, float] = UNSET
    utilization_by_type: Union[Unset, list["GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_doors = self.total_doors

        available_doors = self.available_doors

        occupied_doors = self.occupied_doors

        maintenance_doors = self.maintenance_doors

        utilization_percentage = self.utilization_percentage

        utilization_by_type: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.utilization_by_type, Unset):
            utilization_by_type = []
            for utilization_by_type_item_data in self.utilization_by_type:
                utilization_by_type_item = utilization_by_type_item_data.to_dict()
                utilization_by_type.append(utilization_by_type_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_doors is not UNSET:
            field_dict["totalDoors"] = total_doors
        if available_doors is not UNSET:
            field_dict["availableDoors"] = available_doors
        if occupied_doors is not UNSET:
            field_dict["occupiedDoors"] = occupied_doors
        if maintenance_doors is not UNSET:
            field_dict["maintenanceDoors"] = maintenance_doors
        if utilization_percentage is not UNSET:
            field_dict["utilizationPercentage"] = utilization_percentage
        if utilization_by_type is not UNSET:
            field_dict["utilizationByType"] = utilization_by_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_dock_door_utilization_response_200_data_utilization_by_type_item import (
            GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItem,
        )

        d = dict(src_dict)
        total_doors = d.pop("totalDoors", UNSET)

        available_doors = d.pop("availableDoors", UNSET)

        occupied_doors = d.pop("occupiedDoors", UNSET)

        maintenance_doors = d.pop("maintenanceDoors", UNSET)

        utilization_percentage = d.pop("utilizationPercentage", UNSET)

        utilization_by_type = []
        _utilization_by_type = d.pop("utilizationByType", UNSET)
        for utilization_by_type_item_data in _utilization_by_type or []:
            utilization_by_type_item = GetWMSDockDoorUtilizationResponse200DataUtilizationByTypeItem.from_dict(
                utilization_by_type_item_data
            )

            utilization_by_type.append(utilization_by_type_item)

        get_wms_dock_door_utilization_response_200_data = cls(
            total_doors=total_doors,
            available_doors=available_doors,
            occupied_doors=occupied_doors,
            maintenance_doors=maintenance_doors,
            utilization_percentage=utilization_percentage,
            utilization_by_type=utilization_by_type,
        )

        get_wms_dock_door_utilization_response_200_data.additional_properties = d
        return get_wms_dock_door_utilization_response_200_data

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
