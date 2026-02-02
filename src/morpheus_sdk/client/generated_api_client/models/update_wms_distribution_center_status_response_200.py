from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_distribution_center import WMSDistributionCenter


T = TypeVar("T", bound="UpdateWMSDistributionCenterStatusResponse200")


@_attrs_define
class UpdateWMSDistributionCenterStatusResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        data (Union[Unset, WMSDistributionCenter]): Complete WMS distribution center record for comprehensive facility
            management and operational coordination
    """

    success: Union[Unset, bool] = UNSET
    data: Union[Unset, "WMSDistributionCenter"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_distribution_center import WMSDistributionCenter

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WMSDistributionCenter]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WMSDistributionCenter.from_dict(_data)

        update_wms_distribution_center_status_response_200 = cls(
            success=success,
            data=data,
        )

        update_wms_distribution_center_status_response_200.additional_properties = d
        return update_wms_distribution_center_status_response_200

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
