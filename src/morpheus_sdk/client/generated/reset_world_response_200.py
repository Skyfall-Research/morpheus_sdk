from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.reset_world_response_200_data import ResetWorldResponse200Data


T = TypeVar("T", bound="ResetWorldResponse200")


@_attrs_define
class ResetWorldResponse200:
    """
    Attributes:
        success (bool):  Example: True.
        status (int):  Example: 200.
        data (ResetWorldResponse200Data):
    """

    success: bool
    status: int
    data: "ResetWorldResponse200Data"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reset_world_response_200_data import ResetWorldResponse200Data

        d = dict(src_dict)
        success = d.pop("success")

        status = d.pop("status")

        data = ResetWorldResponse200Data.from_dict(d.pop("data"))

        reset_world_response_200 = cls(
            success=success,
            status=status,
            data=data,
        )

        reset_world_response_200.additional_properties = d
        return reset_world_response_200

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
