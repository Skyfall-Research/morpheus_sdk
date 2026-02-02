from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignWMSTaskBody")


@_attrs_define
class AssignWMSTaskBody:
    """
    Attributes:
        user_id (str): Unique identifier of the user being assigned Example: user_picker_001.
        user_name (str): Display name of the user Example: John Smith.
    """

    user_id: str
    user_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user_name = self.user_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "userName": user_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        user_name = d.pop("userName")

        assign_wms_task_body = cls(
            user_id=user_id,
            user_name=user_name,
        )

        assign_wms_task_body.additional_properties = d
        return assign_wms_task_body

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
