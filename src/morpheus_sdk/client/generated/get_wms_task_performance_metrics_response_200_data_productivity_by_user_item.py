from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSTaskPerformanceMetricsResponse200DataProductivityByUserItem")


@_attrs_define
class GetWMSTaskPerformanceMetricsResponse200DataProductivityByUserItem:
    """
    Attributes:
        user_id (Union[Unset, str]):  Example: USER-001.
        tasks_completed (Union[Unset, float]):  Example: 145.
        average_duration (Union[Unset, float]):  Example: 11.2.
        units_per_hour (Union[Unset, float]):  Example: 32.5.
    """

    user_id: Union[Unset, str] = UNSET
    tasks_completed: Union[Unset, float] = UNSET
    average_duration: Union[Unset, float] = UNSET
    units_per_hour: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        tasks_completed = self.tasks_completed

        average_duration = self.average_duration

        units_per_hour = self.units_per_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if tasks_completed is not UNSET:
            field_dict["tasksCompleted"] = tasks_completed
        if average_duration is not UNSET:
            field_dict["averageDuration"] = average_duration
        if units_per_hour is not UNSET:
            field_dict["unitsPerHour"] = units_per_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        tasks_completed = d.pop("tasksCompleted", UNSET)

        average_duration = d.pop("averageDuration", UNSET)

        units_per_hour = d.pop("unitsPerHour", UNSET)

        get_wms_task_performance_metrics_response_200_data_productivity_by_user_item = cls(
            user_id=user_id,
            tasks_completed=tasks_completed,
            average_duration=average_duration,
            units_per_hour=units_per_hour,
        )

        get_wms_task_performance_metrics_response_200_data_productivity_by_user_item.additional_properties = d
        return get_wms_task_performance_metrics_response_200_data_productivity_by_user_item

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
