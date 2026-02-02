from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_task import WMSTask


T = TypeVar("T", bound="AddWMSTaskScanResponse200")


@_attrs_define
class AddWMSTaskScanResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 200.
        message (Union[Unset, str]):  Example: Task scan added successfully.
        data (Union[Unset, WMSTask]):
            **WMS Task Management System**

            Comprehensive warehouse task orchestration with detailed tracking, performance measurement, and workflow
            automation.

            **⚠️ CRITICAL IMPLEMENTATION BUG:**

            > **BUG #7**: Aggregation pipeline uses `avgDuration` but return value expects `averageDuration`
            >
            > **Impact**: Inconsistent field naming in metrics response causing client-side failures
            > **Required Fix**: Align aggregation field name with expected return value or update interface

            **Task Types Supported:**
            - **PICK**: Order fulfillment picking operations
            - **PUTAWAY**: Inbound inventory storage tasks
            - **REPLENISHMENT**: Stock movement for bin replenishment
            - **CYCLE_COUNT**: Inventory counting and verification
            - **MOVE**: General inventory relocation
            - **LOAD/UNLOAD**: Dock and trailer operations
            - **PACK**: Order packaging and preparation
            - **SORT**: Product and order sorting operations

            **Status Workflow:**
            1. **CREATED** - Task generated but not yet available
            2. **RELEASED** - Task available for assignment
            3. **ASSIGNED** - Task assigned to specific user
            4. **IN_PROGRESS** - Task execution in progress
            5. **COMPLETED** - Task successfully finished
            6. **CANCELLED/SUSPENDED** - Task terminated or paused

            **Key Features:**
            - Priority-based task sequencing and assignment
            - Comprehensive timing and performance tracking
            - Detailed scan validation and audit trails
            - Flexible task detail and product tracking
            - Equipment and resource assignment
            - Real-time status monitoring and reporting

    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    data: Union[Unset, "WMSTask"] = UNSET
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
        from ..models.wms_task import WMSTask

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WMSTask]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WMSTask.from_dict(_data)

        add_wms_task_scan_response_200 = cls(
            success=success,
            status=status,
            message=message,
            data=data,
        )

        add_wms_task_scan_response_200.additional_properties = d
        return add_wms_task_scan_response_200

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
