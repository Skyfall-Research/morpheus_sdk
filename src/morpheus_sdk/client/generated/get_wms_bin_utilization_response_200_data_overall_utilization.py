from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSBinUtilizationResponse200DataOverallUtilization")


@_attrs_define
class GetWMSBinUtilizationResponse200DataOverallUtilization:
    """
    Attributes:
        weight_percent (Union[Unset, float]):  Example: 72.5.
        volume_percent (Union[Unset, float]):  Example: 68.3.
        count_percent (Union[Unset, float]):  Example: 52.
    """

    weight_percent: Union[Unset, float] = UNSET
    volume_percent: Union[Unset, float] = UNSET
    count_percent: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        weight_percent = self.weight_percent

        volume_percent = self.volume_percent

        count_percent = self.count_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if weight_percent is not UNSET:
            field_dict["weightPercent"] = weight_percent
        if volume_percent is not UNSET:
            field_dict["volumePercent"] = volume_percent
        if count_percent is not UNSET:
            field_dict["countPercent"] = count_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        weight_percent = d.pop("weightPercent", UNSET)

        volume_percent = d.pop("volumePercent", UNSET)

        count_percent = d.pop("countPercent", UNSET)

        get_wms_bin_utilization_response_200_data_overall_utilization = cls(
            weight_percent=weight_percent,
            volume_percent=volume_percent,
            count_percent=count_percent,
        )

        get_wms_bin_utilization_response_200_data_overall_utilization.additional_properties = d
        return get_wms_bin_utilization_response_200_data_overall_utilization

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
