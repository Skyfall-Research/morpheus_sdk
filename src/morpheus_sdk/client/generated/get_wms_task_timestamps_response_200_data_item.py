from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_task_timestamps_response_200_data_item_timestamps import (
        GetWMSTaskTimestampsResponse200DataItemTimestamps,
    )


T = TypeVar("T", bound="GetWMSTaskTimestampsResponse200DataItem")


@_attrs_define
class GetWMSTaskTimestampsResponse200DataItem:
    """
    Attributes:
        task_id (Union[Unset, str]):  Example: wms_task_674565c1234567890abcdef.
        task_type (Union[Unset, str]):  Example: PICK.
        user_id (Union[None, Unset, str]):  Example: USER-001.
        timestamps (Union[Unset, GetWMSTaskTimestampsResponse200DataItemTimestamps]):
    """

    task_id: Union[Unset, str] = UNSET
    task_type: Union[Unset, str] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    timestamps: Union[Unset, "GetWMSTaskTimestampsResponse200DataItemTimestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        task_id = self.task_id

        task_type = self.task_type

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if task_type is not UNSET:
            field_dict["taskType"] = task_type
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_task_timestamps_response_200_data_item_timestamps import (
            GetWMSTaskTimestampsResponse200DataItemTimestamps,
        )

        d = dict(src_dict)
        task_id = d.pop("taskId", UNSET)

        task_type = d.pop("taskType", UNSET)

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, GetWMSTaskTimestampsResponse200DataItemTimestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = GetWMSTaskTimestampsResponse200DataItemTimestamps.from_dict(_timestamps)

        get_wms_task_timestamps_response_200_data_item = cls(
            task_id=task_id,
            task_type=task_type,
            user_id=user_id,
            timestamps=timestamps,
        )

        get_wms_task_timestamps_response_200_data_item.additional_properties = d
        return get_wms_task_timestamps_response_200_data_item

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
