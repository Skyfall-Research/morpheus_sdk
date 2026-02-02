from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_bin_utilization_response_200_data_overall_utilization import (
        GetWMSBinUtilizationResponse200DataOverallUtilization,
    )


T = TypeVar("T", bound="GetWMSBinUtilizationResponse200DataOverall")


@_attrs_define
class GetWMSBinUtilizationResponse200DataOverall:
    """
    Attributes:
        total_bins (Union[Unset, int]):  Example: 1250.
        available_bins (Union[Unset, int]):  Example: 450.
        occupied_bins (Union[Unset, int]):  Example: 650.
        utilization (Union[Unset, GetWMSBinUtilizationResponse200DataOverallUtilization]):
    """

    total_bins: Union[Unset, int] = UNSET
    available_bins: Union[Unset, int] = UNSET
    occupied_bins: Union[Unset, int] = UNSET
    utilization: Union[Unset, "GetWMSBinUtilizationResponse200DataOverallUtilization"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_bins = self.total_bins

        available_bins = self.available_bins

        occupied_bins = self.occupied_bins

        utilization: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.utilization, Unset):
            utilization = self.utilization.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_bins is not UNSET:
            field_dict["totalBins"] = total_bins
        if available_bins is not UNSET:
            field_dict["availableBins"] = available_bins
        if occupied_bins is not UNSET:
            field_dict["occupiedBins"] = occupied_bins
        if utilization is not UNSET:
            field_dict["utilization"] = utilization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_bin_utilization_response_200_data_overall_utilization import (
            GetWMSBinUtilizationResponse200DataOverallUtilization,
        )

        d = dict(src_dict)
        total_bins = d.pop("totalBins", UNSET)

        available_bins = d.pop("availableBins", UNSET)

        occupied_bins = d.pop("occupiedBins", UNSET)

        _utilization = d.pop("utilization", UNSET)
        utilization: Union[Unset, GetWMSBinUtilizationResponse200DataOverallUtilization]
        if isinstance(_utilization, Unset):
            utilization = UNSET
        else:
            utilization = GetWMSBinUtilizationResponse200DataOverallUtilization.from_dict(_utilization)

        get_wms_bin_utilization_response_200_data_overall = cls(
            total_bins=total_bins,
            available_bins=available_bins,
            occupied_bins=occupied_bins,
            utilization=utilization,
        )

        get_wms_bin_utilization_response_200_data_overall.additional_properties = d
        return get_wms_bin_utilization_response_200_data_overall

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
