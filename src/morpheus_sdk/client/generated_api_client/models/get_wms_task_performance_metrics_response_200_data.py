from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_task_performance_metrics_response_200_data_productivity_by_user_item import (
        GetWMSTaskPerformanceMetricsResponse200DataProductivityByUserItem,
    )
    from ..models.get_wms_task_performance_metrics_response_200_data_task_type_metrics_item import (
        GetWMSTaskPerformanceMetricsResponse200DataTaskTypeMetricsItem,
    )


T = TypeVar("T", bound="GetWMSTaskPerformanceMetricsResponse200Data")


@_attrs_define
class GetWMSTaskPerformanceMetricsResponse200Data:
    """
    Attributes:
        total_tasks (Union[Unset, float]):  Example: 2450.
        completed_tasks (Union[Unset, float]):  Example: 2380.
        average_duration (Union[Unset, float]): Average duration in minutes Example: 12.5.
        on_time_completion (Union[Unset, float]): Count of on-time completions Example: 2156.
        productivity_by_user (Union[Unset, list['GetWMSTaskPerformanceMetricsResponse200DataProductivityByUserItem']]):
        task_type_metrics (Union[Unset, list['GetWMSTaskPerformanceMetricsResponse200DataTaskTypeMetricsItem']]):
    """

    total_tasks: Union[Unset, float] = UNSET
    completed_tasks: Union[Unset, float] = UNSET
    average_duration: Union[Unset, float] = UNSET
    on_time_completion: Union[Unset, float] = UNSET
    productivity_by_user: Union[Unset, list["GetWMSTaskPerformanceMetricsResponse200DataProductivityByUserItem"]] = (
        UNSET
    )
    task_type_metrics: Union[Unset, list["GetWMSTaskPerformanceMetricsResponse200DataTaskTypeMetricsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_tasks = self.total_tasks

        completed_tasks = self.completed_tasks

        average_duration = self.average_duration

        on_time_completion = self.on_time_completion

        productivity_by_user: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.productivity_by_user, Unset):
            productivity_by_user = []
            for productivity_by_user_item_data in self.productivity_by_user:
                productivity_by_user_item = productivity_by_user_item_data.to_dict()
                productivity_by_user.append(productivity_by_user_item)

        task_type_metrics: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.task_type_metrics, Unset):
            task_type_metrics = []
            for task_type_metrics_item_data in self.task_type_metrics:
                task_type_metrics_item = task_type_metrics_item_data.to_dict()
                task_type_metrics.append(task_type_metrics_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_tasks is not UNSET:
            field_dict["totalTasks"] = total_tasks
        if completed_tasks is not UNSET:
            field_dict["completedTasks"] = completed_tasks
        if average_duration is not UNSET:
            field_dict["averageDuration"] = average_duration
        if on_time_completion is not UNSET:
            field_dict["onTimeCompletion"] = on_time_completion
        if productivity_by_user is not UNSET:
            field_dict["productivityByUser"] = productivity_by_user
        if task_type_metrics is not UNSET:
            field_dict["taskTypeMetrics"] = task_type_metrics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_task_performance_metrics_response_200_data_productivity_by_user_item import (
            GetWMSTaskPerformanceMetricsResponse200DataProductivityByUserItem,
        )
        from ..models.get_wms_task_performance_metrics_response_200_data_task_type_metrics_item import (
            GetWMSTaskPerformanceMetricsResponse200DataTaskTypeMetricsItem,
        )

        d = dict(src_dict)
        total_tasks = d.pop("totalTasks", UNSET)

        completed_tasks = d.pop("completedTasks", UNSET)

        average_duration = d.pop("averageDuration", UNSET)

        on_time_completion = d.pop("onTimeCompletion", UNSET)

        productivity_by_user = []
        _productivity_by_user = d.pop("productivityByUser", UNSET)
        for productivity_by_user_item_data in _productivity_by_user or []:
            productivity_by_user_item = GetWMSTaskPerformanceMetricsResponse200DataProductivityByUserItem.from_dict(
                productivity_by_user_item_data
            )

            productivity_by_user.append(productivity_by_user_item)

        task_type_metrics = []
        _task_type_metrics = d.pop("taskTypeMetrics", UNSET)
        for task_type_metrics_item_data in _task_type_metrics or []:
            task_type_metrics_item = GetWMSTaskPerformanceMetricsResponse200DataTaskTypeMetricsItem.from_dict(
                task_type_metrics_item_data
            )

            task_type_metrics.append(task_type_metrics_item)

        get_wms_task_performance_metrics_response_200_data = cls(
            total_tasks=total_tasks,
            completed_tasks=completed_tasks,
            average_duration=average_duration,
            on_time_completion=on_time_completion,
            productivity_by_user=productivity_by_user,
            task_type_metrics=task_type_metrics,
        )

        get_wms_task_performance_metrics_response_200_data.additional_properties = d
        return get_wms_task_performance_metrics_response_200_data

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
