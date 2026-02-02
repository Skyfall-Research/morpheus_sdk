from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_cycle_count_body_assignments_item_status import CreateWMSCycleCountBodyAssignmentsItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSCycleCountBodyAssignmentsItem")


@_attrs_define
class CreateWMSCycleCountBodyAssignmentsItem:
    """
    Attributes:
        user_id (str): User identifier for count assignment Example: USER_001.
        user_name (str): User display name for assignment tracking Example: John Smith.
        assigned_bins (Union[Unset, list[str]]): Specific bins assigned to this user Example: ['BIN_ATL_A01_001',
            'BIN_ATL_A01_002'].
        status (Union[Unset, CreateWMSCycleCountBodyAssignmentsItemStatus]): Status of user assignment Example:
            ASSIGNED.
    """

    user_id: str
    user_name: str
    assigned_bins: Union[Unset, list[str]] = UNSET
    status: Union[Unset, CreateWMSCycleCountBodyAssignmentsItemStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        user_name = self.user_name

        assigned_bins: Union[Unset, list[str]] = UNSET
        if not isinstance(self.assigned_bins, Unset):
            assigned_bins = self.assigned_bins

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "userName": user_name,
            }
        )
        if assigned_bins is not UNSET:
            field_dict["assignedBins"] = assigned_bins
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId")

        user_name = d.pop("userName")

        assigned_bins = cast(list[str], d.pop("assignedBins", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateWMSCycleCountBodyAssignmentsItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateWMSCycleCountBodyAssignmentsItemStatus(_status)

        create_wms_cycle_count_body_assignments_item = cls(
            user_id=user_id,
            user_name=user_name,
            assigned_bins=assigned_bins,
            status=status,
        )

        create_wms_cycle_count_body_assignments_item.additional_properties = d
        return create_wms_cycle_count_body_assignments_item

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
