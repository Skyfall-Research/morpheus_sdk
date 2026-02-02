from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSBinUtilizationResponse200DataCapacity")


@_attrs_define
class GetWMSBinUtilizationResponse200DataCapacity:
    """
    Attributes:
        total_weight (Union[Unset, float]):  Example: 2500000.
        available_weight (Union[Unset, float]):  Example: 687500.
        total_volume (Union[Unset, float]):  Example: 125000.
        available_volume (Union[Unset, float]):  Example: 39625.
        total_pallets (Union[Unset, int]):  Example: 1250.
        available_pallets (Union[Unset, int]):  Example: 450.
    """

    total_weight: Union[Unset, float] = UNSET
    available_weight: Union[Unset, float] = UNSET
    total_volume: Union[Unset, float] = UNSET
    available_volume: Union[Unset, float] = UNSET
    total_pallets: Union[Unset, int] = UNSET
    available_pallets: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_weight = self.total_weight

        available_weight = self.available_weight

        total_volume = self.total_volume

        available_volume = self.available_volume

        total_pallets = self.total_pallets

        available_pallets = self.available_pallets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_weight is not UNSET:
            field_dict["totalWeight"] = total_weight
        if available_weight is not UNSET:
            field_dict["availableWeight"] = available_weight
        if total_volume is not UNSET:
            field_dict["totalVolume"] = total_volume
        if available_volume is not UNSET:
            field_dict["availableVolume"] = available_volume
        if total_pallets is not UNSET:
            field_dict["totalPallets"] = total_pallets
        if available_pallets is not UNSET:
            field_dict["availablePallets"] = available_pallets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_weight = d.pop("totalWeight", UNSET)

        available_weight = d.pop("availableWeight", UNSET)

        total_volume = d.pop("totalVolume", UNSET)

        available_volume = d.pop("availableVolume", UNSET)

        total_pallets = d.pop("totalPallets", UNSET)

        available_pallets = d.pop("availablePallets", UNSET)

        get_wms_bin_utilization_response_200_data_capacity = cls(
            total_weight=total_weight,
            available_weight=available_weight,
            total_volume=total_volume,
            available_volume=available_volume,
            total_pallets=total_pallets,
            available_pallets=available_pallets,
        )

        get_wms_bin_utilization_response_200_data_capacity.additional_properties = d
        return get_wms_bin_utilization_response_200_data_capacity

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
