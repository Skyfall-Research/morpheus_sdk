from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_replenishment import WMSReplenishment


T = TypeVar("T", bound="CancelWMSReplenishmentResponse200")


@_attrs_define
class CancelWMSReplenishmentResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 200.
        message (Union[Unset, str]):  Example: Replenishment cancelled successfully.
        data (Union[Unset, WMSReplenishment]):
            **WMS Inventory Replenishment Management**

            Complete replenishment operation tracking from suggestion through completion, managing bin-to-bin inventory
            movement with approval workflows.

            **⚠️ CRITICAL IMPLEMENTATION BUGS:**

            > **BUG #5**: Repository approval method sets `approvedQuantity` field but model expects `quantity.approved`
            structure
            >
            > **BUG #6**: Metrics aggregation references `suggestedQuantity` field but model stores `quantity.suggested`
            >
            > **Impact**: Approval functionality and metrics will fail or return incorrect data
            > **Required Fixes**:
            > - Update `approveReplenishment` method to set `quantity.approved` not `approvedQuantity`
            > - Update metrics aggregation to use `"$quantity.suggested"` not `"$suggestedQuantity"`

            **Business Process Flow:**
            1. **SUGGESTED** - Initial replenishment request created
            2. **APPROVED** - Management approval with quantity validation
            3. **TASK_CREATED** - Work order generated for execution
            4. **IN_PROGRESS** - Active execution by warehouse staff
            5. **COMPLETED** - Successfully finished with actual quantities
            6. **CANCELLED** - Process terminated with reason

            **Key Features:**
            - Complex bin-to-bin movement tracking
            - Multi-level quantity management (suggested/approved/actual)
            - Priority-based processing with workflow integration
            - Comprehensive audit trail with approval/cancellation metadata

    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    data: Union[Unset, "WMSReplenishment"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        message = self.message

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_replenishment import WMSReplenishment

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WMSReplenishment]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WMSReplenishment.from_dict(_data)

        cancel_wms_replenishment_response_200 = cls(
            success=success,
            status=status,
            message=message,
            data=data,
        )

        cancel_wms_replenishment_response_200.additional_properties = d
        return cancel_wms_replenishment_response_200

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
