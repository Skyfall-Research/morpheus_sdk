from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_outbound_order import WMSOutboundOrder


T = TypeVar("T", bound="UpdateWMSPickingProgressResponse200")


@_attrs_define
class UpdateWMSPickingProgressResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 200.
        message (Union[Unset, str]):  Example: Picking progress updated successfully.
        data (Union[Unset, WMSOutboundOrder]):
            **Complete WMS Outbound Order Schema**

            Comprehensive outbound order management with multi-line support, customer integration, and workflow tracking.

            **Key Features:**
            - Complex nested line item structure with allocation tracking
            - Customer and shipping address management
            - Priority-based order classification
            - Comprehensive timing workflow with automatic status updates
            - Warehouse-scoped order processing
            - Integrated carrier and tracking information

            **Field Consistency Verified:**
            - Primary identifier: `orderId` (consistent across model, controller, repository)
            - Business identifier: `orderNumber` (unique per world)
            - All repository methods align with controller parameter expectations

            **Status Workflow:**
            PENDING → RELEASED → ALLOCATED → PICKING → PICKED → PACKED → SHIPPED

    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    data: Union[Unset, "WMSOutboundOrder"] = UNSET
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
        from ..models.wms_outbound_order import WMSOutboundOrder

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, WMSOutboundOrder]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WMSOutboundOrder.from_dict(_data)

        update_wms_picking_progress_response_200 = cls(
            success=success,
            status=status,
            message=message,
            data=data,
        )

        update_wms_picking_progress_response_200.additional_properties = d
        return update_wms_picking_progress_response_200

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
