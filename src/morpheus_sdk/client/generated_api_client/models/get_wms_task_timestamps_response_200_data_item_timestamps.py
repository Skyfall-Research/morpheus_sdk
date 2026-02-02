import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSTaskTimestampsResponse200DataItemTimestamps")


@_attrs_define
class GetWMSTaskTimestampsResponse200DataItemTimestamps:
    """
    Attributes:
        created_at (Union[None, Unset, datetime.datetime]):
        released_at (Union[None, Unset, datetime.datetime]):
        assigned_at (Union[None, Unset, datetime.datetime]):
        started_at (Union[None, Unset, datetime.datetime]):
        completed_at (Union[None, Unset, datetime.datetime]):
        estimated_duration (Union[None, Unset, float]):
        actual_duration (Union[None, Unset, float]):
    """

    created_at: Union[None, Unset, datetime.datetime] = UNSET
    released_at: Union[None, Unset, datetime.datetime] = UNSET
    assigned_at: Union[None, Unset, datetime.datetime] = UNSET
    started_at: Union[None, Unset, datetime.datetime] = UNSET
    completed_at: Union[None, Unset, datetime.datetime] = UNSET
    estimated_duration: Union[None, Unset, float] = UNSET
    actual_duration: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[None, Unset, str]
        if isinstance(self.created_at, Unset):
            created_at = UNSET
        elif isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        released_at: Union[None, Unset, str]
        if isinstance(self.released_at, Unset):
            released_at = UNSET
        elif isinstance(self.released_at, datetime.datetime):
            released_at = self.released_at.isoformat()
        else:
            released_at = self.released_at

        assigned_at: Union[None, Unset, str]
        if isinstance(self.assigned_at, Unset):
            assigned_at = UNSET
        elif isinstance(self.assigned_at, datetime.datetime):
            assigned_at = self.assigned_at.isoformat()
        else:
            assigned_at = self.assigned_at

        started_at: Union[None, Unset, str]
        if isinstance(self.started_at, Unset):
            started_at = UNSET
        elif isinstance(self.started_at, datetime.datetime):
            started_at = self.started_at.isoformat()
        else:
            started_at = self.started_at

        completed_at: Union[None, Unset, str]
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        estimated_duration: Union[None, Unset, float]
        if isinstance(self.estimated_duration, Unset):
            estimated_duration = UNSET
        else:
            estimated_duration = self.estimated_duration

        actual_duration: Union[None, Unset, float]
        if isinstance(self.actual_duration, Unset):
            actual_duration = UNSET
        else:
            actual_duration = self.actual_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if released_at is not UNSET:
            field_dict["releasedAt"] = released_at
        if assigned_at is not UNSET:
            field_dict["assignedAt"] = assigned_at
        if started_at is not UNSET:
            field_dict["startedAt"] = started_at
        if completed_at is not UNSET:
            field_dict["completedAt"] = completed_at
        if estimated_duration is not UNSET:
            field_dict["estimatedDuration"] = estimated_duration
        if actual_duration is not UNSET:
            field_dict["actualDuration"] = actual_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_created_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)

                return created_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        created_at = _parse_created_at(d.pop("createdAt", UNSET))

        def _parse_released_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                released_at_type_0 = isoparse(data)

                return released_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        released_at = _parse_released_at(d.pop("releasedAt", UNSET))

        def _parse_assigned_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                assigned_at_type_0 = isoparse(data)

                return assigned_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        assigned_at = _parse_assigned_at(d.pop("assignedAt", UNSET))

        def _parse_started_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                started_at_type_0 = isoparse(data)

                return started_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        started_at = _parse_started_at(d.pop("startedAt", UNSET))

        def _parse_completed_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = isoparse(data)

                return completed_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        completed_at = _parse_completed_at(d.pop("completedAt", UNSET))

        def _parse_estimated_duration(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        estimated_duration = _parse_estimated_duration(d.pop("estimatedDuration", UNSET))

        def _parse_actual_duration(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        actual_duration = _parse_actual_duration(d.pop("actualDuration", UNSET))

        get_wms_task_timestamps_response_200_data_item_timestamps = cls(
            created_at=created_at,
            released_at=released_at,
            assigned_at=assigned_at,
            started_at=started_at,
            completed_at=completed_at,
            estimated_duration=estimated_duration,
            actual_duration=actual_duration,
        )

        get_wms_task_timestamps_response_200_data_item_timestamps.additional_properties = d
        return get_wms_task_timestamps_response_200_data_item_timestamps

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
