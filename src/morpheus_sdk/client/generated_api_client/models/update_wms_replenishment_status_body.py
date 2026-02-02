from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_wms_replenishment_status_body_status import UpdateWMSReplenishmentStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWMSReplenishmentStatusBody")


@_attrs_define
class UpdateWMSReplenishmentStatusBody:
    """
    Attributes:
        status (UpdateWMSReplenishmentStatusBodyStatus): New status for the replenishment Example: APPROVED.
        task_id (Union[Unset, str]): Task ID when status is TASK_CREATED Example: TASK-12345.
    """

    status: UpdateWMSReplenishmentStatusBodyStatus
    task_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        task_id = self.task_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if task_id is not UNSET:
            field_dict["taskId"] = task_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = UpdateWMSReplenishmentStatusBodyStatus(d.pop("status"))

        task_id = d.pop("taskId", UNSET)

        update_wms_replenishment_status_body = cls(
            status=status,
            task_id=task_id,
        )

        update_wms_replenishment_status_body.additional_properties = d
        return update_wms_replenishment_status_body

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
