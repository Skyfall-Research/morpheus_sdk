from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours import (
        GetWMSDistributionCenterCapacityResponse200DataOperationalHours,
    )
    from ..models.get_wms_distribution_center_capacity_response_200_data_utilization_metrics import (
        GetWMSDistributionCenterCapacityResponse200DataUtilizationMetrics,
    )


T = TypeVar("T", bound="GetWMSDistributionCenterCapacityResponse200Data")


@_attrs_define
class GetWMSDistributionCenterCapacityResponse200Data:
    """
    Attributes:
        dc_id (Union[Unset, str]): Distribution center identifier Example: wms_distribution-
            center_674565c1234567890abcdef.
        dc_name (Union[Unset, str]): Distribution center name Example: Atlanta Fulfillment Center East.
        total_sq_footage (Union[Unset, float]): Total facility square footage Example: 250000.
        utilization_metrics (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataUtilizationMetrics]):
            Comprehensive utilization metrics
        operational_hours (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHours]): Facility
            operating hours schedule
    """

    dc_id: Union[Unset, str] = UNSET
    dc_name: Union[Unset, str] = UNSET
    total_sq_footage: Union[Unset, float] = UNSET
    utilization_metrics: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataUtilizationMetrics"] = UNSET
    operational_hours: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataOperationalHours"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dc_id = self.dc_id

        dc_name = self.dc_name

        total_sq_footage = self.total_sq_footage

        utilization_metrics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.utilization_metrics, Unset):
            utilization_metrics = self.utilization_metrics.to_dict()

        operational_hours: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.operational_hours, Unset):
            operational_hours = self.operational_hours.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dc_id is not UNSET:
            field_dict["dcId"] = dc_id
        if dc_name is not UNSET:
            field_dict["dcName"] = dc_name
        if total_sq_footage is not UNSET:
            field_dict["totalSqFootage"] = total_sq_footage
        if utilization_metrics is not UNSET:
            field_dict["utilizationMetrics"] = utilization_metrics
        if operational_hours is not UNSET:
            field_dict["operationalHours"] = operational_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours import (
            GetWMSDistributionCenterCapacityResponse200DataOperationalHours,
        )
        from ..models.get_wms_distribution_center_capacity_response_200_data_utilization_metrics import (
            GetWMSDistributionCenterCapacityResponse200DataUtilizationMetrics,
        )

        d = dict(src_dict)
        dc_id = d.pop("dcId", UNSET)

        dc_name = d.pop("dcName", UNSET)

        total_sq_footage = d.pop("totalSqFootage", UNSET)

        _utilization_metrics = d.pop("utilizationMetrics", UNSET)
        utilization_metrics: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataUtilizationMetrics]
        if isinstance(_utilization_metrics, Unset):
            utilization_metrics = UNSET
        else:
            utilization_metrics = GetWMSDistributionCenterCapacityResponse200DataUtilizationMetrics.from_dict(
                _utilization_metrics
            )

        _operational_hours = d.pop("operationalHours", UNSET)
        operational_hours: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHours]
        if isinstance(_operational_hours, Unset):
            operational_hours = UNSET
        else:
            operational_hours = GetWMSDistributionCenterCapacityResponse200DataOperationalHours.from_dict(
                _operational_hours
            )

        get_wms_distribution_center_capacity_response_200_data = cls(
            dc_id=dc_id,
            dc_name=dc_name,
            total_sq_footage=total_sq_footage,
            utilization_metrics=utilization_metrics,
            operational_hours=operational_hours,
        )

        get_wms_distribution_center_capacity_response_200_data.additional_properties = d
        return get_wms_distribution_center_capacity_response_200_data

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
