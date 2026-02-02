import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_wms_task_status_body_status import UpdateWMSTaskStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWMSTaskStatusBody")


@_attrs_define
class UpdateWMSTaskStatusBody:
    """
    Attributes:
        status (UpdateWMSTaskStatusBodyStatus): New task status Example: IN_PROGRESS.
        timestamp (Union[Unset, datetime.datetime]): Optional custom timestamp (defaults to current time) Example:
            2024-11-27T14:30:00Z.
        user_id (Union[Unset, str]): User ID for assignment or completion tracking Example: USER-001.
    """

    status: UpdateWMSTaskStatusBodyStatus
    timestamp: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        user_id = self.user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if user_id is not UNSET:
            field_dict["userId"] = user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = UpdateWMSTaskStatusBodyStatus(d.pop("status"))

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        user_id = d.pop("userId", UNSET)

        update_wms_task_status_body = cls(
            status=status,
            timestamp=timestamp,
            user_id=user_id,
        )

        update_wms_task_status_body.additional_properties = d
        return update_wms_task_status_body

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
