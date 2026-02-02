from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_world_schedule_status_response_200_data import GetWorldScheduleStatusResponse200Data
    from ..models.get_world_schedule_status_response_200_meta import GetWorldScheduleStatusResponse200Meta


T = TypeVar("T", bound="GetWorldScheduleStatusResponse200")


@_attrs_define
class GetWorldScheduleStatusResponse200:
    """
    Example:
        {'success': True, 'status': 200, 'data': {'status': 'operational'}, 'meta': {'event': 'message', 'timestamp':
            '2024-01-15T10:30:00.123Z'}}

    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 200.
        data (Union[Unset, GetWorldScheduleStatusResponse200Data]):
        meta (Union[Unset, GetWorldScheduleStatusResponse200Meta]):
    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    data: Union[Unset, "GetWorldScheduleStatusResponse200Data"] = UNSET
    meta: Union[Unset, "GetWorldScheduleStatusResponse200Meta"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        meta: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if status is not UNSET:
            field_dict["status"] = status
        if data is not UNSET:
            field_dict["data"] = data
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_world_schedule_status_response_200_data import GetWorldScheduleStatusResponse200Data
        from ..models.get_world_schedule_status_response_200_meta import GetWorldScheduleStatusResponse200Meta

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, GetWorldScheduleStatusResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = GetWorldScheduleStatusResponse200Data.from_dict(_data)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, GetWorldScheduleStatusResponse200Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = GetWorldScheduleStatusResponse200Meta.from_dict(_meta)

        get_world_schedule_status_response_200 = cls(
            success=success,
            status=status,
            data=data,
            meta=meta,
        )

        get_world_schedule_status_response_200.additional_properties = d
        return get_world_schedule_status_response_200

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
