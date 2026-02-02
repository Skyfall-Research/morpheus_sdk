from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSDistributionCenterCapacityResponse200DataUtilizationMetrics")


@_attrs_define
class GetWMSDistributionCenterCapacityResponse200DataUtilizationMetrics:
    """Comprehensive utilization metrics

    Attributes:
        total_zones (Union[Unset, float]): Total operational zones Example: 12.
        total_bins (Union[Unset, float]): Total bin locations Example: 5840.
        occupied_bins (Union[Unset, float]): Currently occupied bins Example: 4672.
        utilization_percentage (Union[Unset, float]): Facility utilization percentage Example: 80.
    """

    total_zones: Union[Unset, float] = UNSET
    total_bins: Union[Unset, float] = UNSET
    occupied_bins: Union[Unset, float] = UNSET
    utilization_percentage: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_zones = self.total_zones

        total_bins = self.total_bins

        occupied_bins = self.occupied_bins

        utilization_percentage = self.utilization_percentage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_zones is not UNSET:
            field_dict["totalZones"] = total_zones
        if total_bins is not UNSET:
            field_dict["totalBins"] = total_bins
        if occupied_bins is not UNSET:
            field_dict["occupiedBins"] = occupied_bins
        if utilization_percentage is not UNSET:
            field_dict["utilizationPercentage"] = utilization_percentage

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_zones = d.pop("totalZones", UNSET)

        total_bins = d.pop("totalBins", UNSET)

        occupied_bins = d.pop("occupiedBins", UNSET)

        utilization_percentage = d.pop("utilizationPercentage", UNSET)

        get_wms_distribution_center_capacity_response_200_data_utilization_metrics = cls(
            total_zones=total_zones,
            total_bins=total_bins,
            occupied_bins=occupied_bins,
            utilization_percentage=utilization_percentage,
        )

        get_wms_distribution_center_capacity_response_200_data_utilization_metrics.additional_properties = d
        return get_wms_distribution_center_capacity_response_200_data_utilization_metrics

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
