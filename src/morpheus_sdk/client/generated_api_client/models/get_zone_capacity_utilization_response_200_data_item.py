from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetZoneCapacityUtilizationResponse200DataItem")


@_attrs_define
class GetZoneCapacityUtilizationResponse200DataItem:
    """
    Attributes:
        zone_id (Union[Unset, str]):  Example: ZNE_507f1f77bcf86cd799439012.
        zone_code (Union[Unset, str]):  Example: picking-zone-a.
        zone_name (Union[Unset, str]):  Example: Picking Zone A.
        zone_type (Union[Unset, str]):  Example: PICKING.
        total_capacity (Union[Unset, float]): ⚠️ Hardcoded to 0
        used_capacity (Union[Unset, float]): ⚠️ Hardcoded to 0
        utilization_percentage (Union[Unset, float]): ⚠️ Hardcoded to 0
        bin_count (Union[Unset, float]): ⚠️ Hardcoded to 0
        available_bin_count (Union[Unset, float]): ⚠️ Hardcoded to 0
    """

    zone_id: Union[Unset, str] = UNSET
    zone_code: Union[Unset, str] = UNSET
    zone_name: Union[Unset, str] = UNSET
    zone_type: Union[Unset, str] = UNSET
    total_capacity: Union[Unset, float] = UNSET
    used_capacity: Union[Unset, float] = UNSET
    utilization_percentage: Union[Unset, float] = UNSET
    bin_count: Union[Unset, float] = UNSET
    available_bin_count: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        zone_id = self.zone_id

        zone_code = self.zone_code

        zone_name = self.zone_name

        zone_type = self.zone_type

        total_capacity = self.total_capacity

        used_capacity = self.used_capacity

        utilization_percentage = self.utilization_percentage

        bin_count = self.bin_count

        available_bin_count = self.available_bin_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if zone_code is not UNSET:
            field_dict["zoneCode"] = zone_code
        if zone_name is not UNSET:
            field_dict["zoneName"] = zone_name
        if zone_type is not UNSET:
            field_dict["zoneType"] = zone_type
        if total_capacity is not UNSET:
            field_dict["totalCapacity"] = total_capacity
        if used_capacity is not UNSET:
            field_dict["usedCapacity"] = used_capacity
        if utilization_percentage is not UNSET:
            field_dict["utilizationPercentage"] = utilization_percentage
        if bin_count is not UNSET:
            field_dict["binCount"] = bin_count
        if available_bin_count is not UNSET:
            field_dict["availableBinCount"] = available_bin_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        zone_id = d.pop("zoneId", UNSET)

        zone_code = d.pop("zoneCode", UNSET)

        zone_name = d.pop("zoneName", UNSET)

        zone_type = d.pop("zoneType", UNSET)

        total_capacity = d.pop("totalCapacity", UNSET)

        used_capacity = d.pop("usedCapacity", UNSET)

        utilization_percentage = d.pop("utilizationPercentage", UNSET)

        bin_count = d.pop("binCount", UNSET)

        available_bin_count = d.pop("availableBinCount", UNSET)

        get_zone_capacity_utilization_response_200_data_item = cls(
            zone_id=zone_id,
            zone_code=zone_code,
            zone_name=zone_name,
            zone_type=zone_type,
            total_capacity=total_capacity,
            used_capacity=used_capacity,
            utilization_percentage=utilization_percentage,
            bin_count=bin_count,
            available_bin_count=available_bin_count,
        )

        get_zone_capacity_utilization_response_200_data_item.additional_properties = d
        return get_zone_capacity_utilization_response_200_data_item

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
