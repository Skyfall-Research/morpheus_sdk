from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_wms_task_body_task_status import PatchWMSTaskBodyTaskStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_wms_task_body_assignment import PatchWMSTaskBodyAssignment


T = TypeVar("T", bound="PatchWMSTaskBody")


@_attrs_define
class PatchWMSTaskBody:
    """
    Attributes:
        task_status (Union[Unset, PatchWMSTaskBodyTaskStatus]): New status for the task
        assignment (Union[Unset, PatchWMSTaskBodyAssignment]): Assignment information
        priority (Union[Unset, int]): Task priority (higher number = higher priority) Example: 5.
    """

    task_status: Union[Unset, PatchWMSTaskBodyTaskStatus] = UNSET
    assignment: Union[Unset, "PatchWMSTaskBodyAssignment"] = UNSET
    priority: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_status: Union[Unset, str] = UNSET
        if not isinstance(self.task_status, Unset):
            task_status = self.task_status.value

        assignment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assignment, Unset):
            assignment = self.assignment.to_dict()

        priority = self.priority

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_status is not UNSET:
            field_dict["taskStatus"] = task_status
        if assignment is not UNSET:
            field_dict["assignment"] = assignment
        if priority is not UNSET:
            field_dict["priority"] = priority

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_wms_task_body_assignment import PatchWMSTaskBodyAssignment

        d = dict(src_dict)
        _task_status = d.pop("taskStatus", UNSET)
        task_status: Union[Unset, PatchWMSTaskBodyTaskStatus]
        if isinstance(_task_status, Unset):
            task_status = UNSET
        else:
            task_status = PatchWMSTaskBodyTaskStatus(_task_status)

        _assignment = d.pop("assignment", UNSET)
        assignment: Union[Unset, PatchWMSTaskBodyAssignment]
        if isinstance(_assignment, Unset):
            assignment = UNSET
        else:
            assignment = PatchWMSTaskBodyAssignment.from_dict(_assignment)

        priority = d.pop("priority", UNSET)

        patch_wms_task_body = cls(
            task_status=task_status,
            assignment=assignment,
            priority=priority,
        )

        patch_wms_task_body.additional_properties = d
        return patch_wms_task_body

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
