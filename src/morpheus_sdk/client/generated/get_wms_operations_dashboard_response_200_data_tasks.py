from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_operations_dashboard_response_200_data_tasks_by_type import (
        GetWMSOperationsDashboardResponse200DataTasksByType,
    )


T = TypeVar("T", bound="GetWMSOperationsDashboardResponse200DataTasks")


@_attrs_define
class GetWMSOperationsDashboardResponse200DataTasks:
    """
    Attributes:
        total (Union[Unset, int]):  Example: 3420.
        pending (Union[Unset, int]):  Example: 156.
        in_progress (Union[Unset, int]):  Example: 45.
        completed_today (Union[Unset, int]):  Example: 234.
        by_type (Union[Unset, GetWMSOperationsDashboardResponse200DataTasksByType]):  Example: {'PICK': 1500, 'PUTAWAY':
            800, 'REPLENISHMENT': 420, 'CYCLE_COUNT': 200}.
    """

    total: Union[Unset, int] = UNSET
    pending: Union[Unset, int] = UNSET
    in_progress: Union[Unset, int] = UNSET
    completed_today: Union[Unset, int] = UNSET
    by_type: Union[Unset, "GetWMSOperationsDashboardResponse200DataTasksByType"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        pending = self.pending

        in_progress = self.in_progress

        completed_today = self.completed_today

        by_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.by_type, Unset):
            by_type = self.by_type.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if pending is not UNSET:
            field_dict["pending"] = pending
        if in_progress is not UNSET:
            field_dict["inProgress"] = in_progress
        if completed_today is not UNSET:
            field_dict["completedToday"] = completed_today
        if by_type is not UNSET:
            field_dict["byType"] = by_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_operations_dashboard_response_200_data_tasks_by_type import (
            GetWMSOperationsDashboardResponse200DataTasksByType,
        )

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        pending = d.pop("pending", UNSET)

        in_progress = d.pop("inProgress", UNSET)

        completed_today = d.pop("completedToday", UNSET)

        _by_type = d.pop("byType", UNSET)
        by_type: Union[Unset, GetWMSOperationsDashboardResponse200DataTasksByType]
        if isinstance(_by_type, Unset):
            by_type = UNSET
        else:
            by_type = GetWMSOperationsDashboardResponse200DataTasksByType.from_dict(_by_type)

        get_wms_operations_dashboard_response_200_data_tasks = cls(
            total=total,
            pending=pending,
            in_progress=in_progress,
            completed_today=completed_today,
            by_type=by_type,
        )

        get_wms_operations_dashboard_response_200_data_tasks.additional_properties = d
        return get_wms_operations_dashboard_response_200_data_tasks

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
