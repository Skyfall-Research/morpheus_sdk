from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSCycleCountVarianceReportResponse200DataVariancesByWarehouseItem")


@_attrs_define
class GetWMSCycleCountVarianceReportResponse200DataVariancesByWarehouseItem:
    """
    Attributes:
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        total_counts (Union[Unset, int]):  Example: 30.
        accuracy_percent (Union[Unset, float]):  Example: 95.1.
        total_variance_value (Union[Unset, float]):  Example: 892.45.
    """

    warehouse_id: Union[Unset, str] = UNSET
    total_counts: Union[Unset, int] = UNSET
    accuracy_percent: Union[Unset, float] = UNSET
    total_variance_value: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        total_counts = self.total_counts

        accuracy_percent = self.accuracy_percent

        total_variance_value = self.total_variance_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if warehouse_id is not UNSET:
            field_dict["warehouseId"] = warehouse_id
        if total_counts is not UNSET:
            field_dict["totalCounts"] = total_counts
        if accuracy_percent is not UNSET:
            field_dict["accuracyPercent"] = accuracy_percent
        if total_variance_value is not UNSET:
            field_dict["totalVarianceValue"] = total_variance_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId", UNSET)

        total_counts = d.pop("totalCounts", UNSET)

        accuracy_percent = d.pop("accuracyPercent", UNSET)

        total_variance_value = d.pop("totalVarianceValue", UNSET)

        get_wms_cycle_count_variance_report_response_200_data_variances_by_warehouse_item = cls(
            warehouse_id=warehouse_id,
            total_counts=total_counts,
            accuracy_percent=accuracy_percent,
            total_variance_value=total_variance_value,
        )

        get_wms_cycle_count_variance_report_response_200_data_variances_by_warehouse_item.additional_properties = d
        return get_wms_cycle_count_variance_report_response_200_data_variances_by_warehouse_item

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
