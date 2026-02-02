from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSTaskBodyTiming")


@_attrs_define
class CreateWMSTaskBodyTiming:
    """Task timing estimates

    Attributes:
        estimated_duration (Union[Unset, float]): Estimated duration in minutes Example: 15.
    """

    estimated_duration: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        estimated_duration = self.estimated_duration

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if estimated_duration is not UNSET:
            field_dict["estimatedDuration"] = estimated_duration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        estimated_duration = d.pop("estimatedDuration", UNSET)

        create_wms_task_body_timing = cls(
            estimated_duration=estimated_duration,
        )

        create_wms_task_body_timing.additional_properties = d
        return create_wms_task_body_timing

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
