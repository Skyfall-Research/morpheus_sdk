from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSTaskPerformanceType0")


@_attrs_define
class WMSTaskPerformanceType0:
    """Performance metrics and productivity data

    Attributes:
        units_per_hour (Union[None, Unset, float]): Units processed per hour Example: 125.5.
        accuracy (Union[None, Unset, float]): Task accuracy percentage Example: 98.5.
    """

    units_per_hour: Union[None, Unset, float] = UNSET
    accuracy: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        units_per_hour: Union[None, Unset, float]
        if isinstance(self.units_per_hour, Unset):
            units_per_hour = UNSET
        else:
            units_per_hour = self.units_per_hour

        accuracy: Union[None, Unset, float]
        if isinstance(self.accuracy, Unset):
            accuracy = UNSET
        else:
            accuracy = self.accuracy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if units_per_hour is not UNSET:
            field_dict["unitsPerHour"] = units_per_hour
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_units_per_hour(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        units_per_hour = _parse_units_per_hour(d.pop("unitsPerHour", UNSET))

        def _parse_accuracy(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        accuracy = _parse_accuracy(d.pop("accuracy", UNSET))

        wms_task_performance_type_0 = cls(
            units_per_hour=units_per_hour,
            accuracy=accuracy,
        )

        wms_task_performance_type_0.additional_properties = d
        return wms_task_performance_type_0

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
