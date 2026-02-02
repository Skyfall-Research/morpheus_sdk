from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_wms_cycle_count_status_body_status import UpdateWMSCycleCountStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWMSCycleCountStatusBody")


@_attrs_define
class UpdateWMSCycleCountStatusBody:
    """
    Attributes:
        status (UpdateWMSCycleCountStatusBodyStatus): New count status Example: COMPLETED.
        completed_by (Union[Unset, str]): User identifier who completed the count (required for COMPLETED status)
            Example: USER_001.
    """

    status: UpdateWMSCycleCountStatusBodyStatus
    completed_by: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        completed_by = self.completed_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = UpdateWMSCycleCountStatusBodyStatus(d.pop("status"))

        completed_by = d.pop("completedBy", UNSET)

        update_wms_cycle_count_status_body = cls(
            status=status,
            completed_by=completed_by,
        )

        update_wms_cycle_count_status_body.additional_properties = d
        return update_wms_cycle_count_status_body

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
