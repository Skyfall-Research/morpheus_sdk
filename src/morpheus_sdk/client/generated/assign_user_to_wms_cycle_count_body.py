from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AssignUserToWMSCycleCountBody")


@_attrs_define
class AssignUserToWMSCycleCountBody:
    """
    Attributes:
        user_id (str): Unique user identifier for assignment Example: USER_001.
        user_name (str): User display name for assignment tracking and communication Example: John Smith.
        assigned_bins (list[str]): Array of bin identifiers assigned to this user for counting Example:
            ['BIN_ATL_A01_001', 'BIN_ATL_A01_002', 'BIN_ATL_A01_003'].
    """

    user_id: str
    user_name: str
    assigned_bins: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user_name = self.user_name

        assigned_bins = self.assigned_bins

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "userName": user_name,
                "assignedBins": assigned_bins,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        user_name = d.pop("userName")

        assigned_bins = cast(list[str], d.pop("assignedBins"))

        assign_user_to_wms_cycle_count_body = cls(
            user_id=user_id,
            user_name=user_name,
            assigned_bins=assigned_bins,
        )

        assign_user_to_wms_cycle_count_body.additional_properties = d
        return assign_user_to_wms_cycle_count_body

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
