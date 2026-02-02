from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resume_world_schedules_response_200_data import ResumeWorldSchedulesResponse200Data
    from ..models.resume_world_schedules_response_200_meta import ResumeWorldSchedulesResponse200Meta


T = TypeVar("T", bound="ResumeWorldSchedulesResponse200")


@_attrs_define
class ResumeWorldSchedulesResponse200:
    """
    Example:
        {'success': True, 'status': 200, 'data': {'message': 'Resumed 5 schedules for world', 'count': 5}, 'meta':
            {'event': 'message', 'timestamp': '2024-01-15T10:30:00.123Z'}}

    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 200.
        data (Union[Unset, ResumeWorldSchedulesResponse200Data]):
        meta (Union[Unset, ResumeWorldSchedulesResponse200Meta]):
    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    data: Union[Unset, "ResumeWorldSchedulesResponse200Data"] = UNSET
    meta: Union[Unset, "ResumeWorldSchedulesResponse200Meta"] = UNSET
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
        from ..models.resume_world_schedules_response_200_data import ResumeWorldSchedulesResponse200Data
        from ..models.resume_world_schedules_response_200_meta import ResumeWorldSchedulesResponse200Meta

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ResumeWorldSchedulesResponse200Data]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ResumeWorldSchedulesResponse200Data.from_dict(_data)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ResumeWorldSchedulesResponse200Meta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ResumeWorldSchedulesResponse200Meta.from_dict(_meta)

        resume_world_schedules_response_200 = cls(
            success=success,
            status=status,
            data=data,
            meta=meta,
        )

        resume_world_schedules_response_200.additional_properties = d
        return resume_world_schedules_response_200

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
