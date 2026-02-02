from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteODResponse200Data")


@_attrs_define
class DeleteODResponse200Data:
    """
    Attributes:
        message (Union[Unset, str]):
        cancelled_schedules (Union[Unset, int]):
    """

    message: Union[Unset, str] = UNSET
    cancelled_schedules: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        cancelled_schedules = self.cancelled_schedules

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if cancelled_schedules is not UNSET:
            field_dict["cancelledSchedules"] = cancelled_schedules

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        cancelled_schedules = d.pop("cancelledSchedules", UNSET)

        delete_od_response_200_data = cls(
            message=message,
            cancelled_schedules=cancelled_schedules,
        )

        delete_od_response_200_data.additional_properties = d
        return delete_od_response_200_data

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
