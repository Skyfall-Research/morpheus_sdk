from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSCycleCountSummary")


@_attrs_define
class WMSCycleCountSummary:
    """Count summary and accuracy metrics

    Attributes:
        total_bins (Union[Unset, int]): Total bins included in count Example: 25.
        total_products (Union[Unset, int]): Total products counted Example: 47.
        items_matched (Union[Unset, int]): Number of items with exact quantity match Example: 42.
        items_variance (Union[Unset, int]): Number of items with quantity variance Example: 5.
        accuracy_percent (Union[Unset, float]): Overall count accuracy percentage Example: 89.36.
        total_variance_value (Union[Unset, float]): Total monetary value of variances Example: 127.85.
    """

    total_bins: Union[Unset, int] = UNSET
    total_products: Union[Unset, int] = UNSET
    items_matched: Union[Unset, int] = UNSET
    items_variance: Union[Unset, int] = UNSET
    accuracy_percent: Union[Unset, float] = UNSET
    total_variance_value: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_bins = self.total_bins

        total_products = self.total_products

        items_matched = self.items_matched

        items_variance = self.items_variance

        accuracy_percent = self.accuracy_percent

        total_variance_value = self.total_variance_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_bins is not UNSET:
            field_dict["totalBins"] = total_bins
        if total_products is not UNSET:
            field_dict["totalProducts"] = total_products
        if items_matched is not UNSET:
            field_dict["itemsMatched"] = items_matched
        if items_variance is not UNSET:
            field_dict["itemsVariance"] = items_variance
        if accuracy_percent is not UNSET:
            field_dict["accuracyPercent"] = accuracy_percent
        if total_variance_value is not UNSET:
            field_dict["totalVarianceValue"] = total_variance_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_bins = d.pop("totalBins", UNSET)

        total_products = d.pop("totalProducts", UNSET)

        items_matched = d.pop("itemsMatched", UNSET)

        items_variance = d.pop("itemsVariance", UNSET)

        accuracy_percent = d.pop("accuracyPercent", UNSET)

        total_variance_value = d.pop("totalVarianceValue", UNSET)

        wms_cycle_count_summary = cls(
            total_bins=total_bins,
            total_products=total_products,
            items_matched=items_matched,
            items_variance=items_variance,
            accuracy_percent=accuracy_percent,
            total_variance_value=total_variance_value,
        )

        wms_cycle_count_summary.additional_properties = d
        return wms_cycle_count_summary

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
