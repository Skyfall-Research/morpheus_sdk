from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSReplenishmentMetricsResponse200DataReplenishmentsByTypeItem")


@_attrs_define
class GetWMSReplenishmentMetricsResponse200DataReplenishmentsByTypeItem:
    """
    Attributes:
        type_ (Union[Unset, str]):  Example: MIN_MAX.
        count (Union[Unset, float]):  Example: 650.
        completion_rate (Union[Unset, float]):  Example: 94.5.
    """

    type_: Union[Unset, str] = UNSET
    count: Union[Unset, float] = UNSET
    completion_rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        count = self.count

        completion_rate = self.completion_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if count is not UNSET:
            field_dict["count"] = count
        if completion_rate is not UNSET:
            field_dict["completionRate"] = completion_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        count = d.pop("count", UNSET)

        completion_rate = d.pop("completionRate", UNSET)

        get_wms_replenishment_metrics_response_200_data_replenishments_by_type_item = cls(
            type_=type_,
            count=count,
            completion_rate=completion_rate,
        )

        get_wms_replenishment_metrics_response_200_data_replenishments_by_type_item.additional_properties = d
        return get_wms_replenishment_metrics_response_200_data_replenishments_by_type_item

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
