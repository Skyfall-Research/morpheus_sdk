from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSTaskPerformanceMetricsResponse200DataTaskTypeMetricsItem")


@_attrs_define
class GetWMSTaskPerformanceMetricsResponse200DataTaskTypeMetricsItem:
    """
    Attributes:
        task_type (Union[Unset, str]):  Example: PICK.
        count (Union[Unset, float]):  Example: 1250.
        average_duration (Union[Unset, float]):  Example: 8.7.
    """

    task_type: Union[Unset, str] = UNSET
    count: Union[Unset, float] = UNSET
    average_duration: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_type = self.task_type

        count = self.count

        average_duration = self.average_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if count is not UNSET:
            field_dict["count"] = count
        if average_duration is not UNSET:
            field_dict["averageDuration"] = average_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        task_type = d.pop("taskType", UNSET)

        count = d.pop("count", UNSET)

        average_duration = d.pop("averageDuration", UNSET)

        get_wms_task_performance_metrics_response_200_data_task_type_metrics_item = cls(
            task_type=task_type,
            count=count,
            average_duration=average_duration,
        )

        get_wms_task_performance_metrics_response_200_data_task_type_metrics_item.additional_properties = d
        return get_wms_task_performance_metrics_response_200_data_task_type_metrics_item

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
