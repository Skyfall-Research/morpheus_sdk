import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_outbound_order_order_status import WMSOutboundOrderOrderStatus
from ..models.wms_outbound_order_order_type import WMSOutboundOrderOrderType
from ..models.wms_outbound_order_priority import WMSOutboundOrderPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_outbound_order_carrier_info import WMSOutboundOrderCarrierInfo
    from ..models.wms_outbound_order_lines_item import WMSOutboundOrderLinesItem
    from ..models.wms_outbound_order_shipping_address import WMSOutboundOrderShippingAddress
    from ..models.wms_outbound_order_timing import WMSOutboundOrderTiming
    from ..models.wms_outbound_order_world_ref import WMSOutboundOrderWorldRef


T = TypeVar("T", bound="WMSOutboundOrder")


@_attrs_define
class WMSOutboundOrder:
    """
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


        Attributes:
            field_id (str): MongoDB auto-generated primary key Example: 674565c1234567890abcdef0.
            order_id (str): Business primary identifier (consistent naming verified across all components) Example:
                ORD-2024-001234.
            order_number (str): Human-readable order number (unique per world, enforced by repository) Example:
                WO-20241201-001.
            world_ref (WMSOutboundOrderWorldRef): Multi-tenant world reference for data isolation
            warehouse_id (str): Required source warehouse identifier (validated in repository) Example: WH-MAIN-001.
            customer_id (str): Customer account identifier Example: CUST-ABC-123.
            customer_name (str): Customer display name Example: ABC Corporation.
            order_type (WMSOutboundOrderOrderType): Order classification affecting processing workflow Example: STANDARD.
            priority (WMSOutboundOrderPriority): Processing priority (affects sorting in ready-for-picking queries) Example:
                HIGH.
            order_status (WMSOutboundOrderOrderStatus): Current order state in fulfillment workflow Example: ALLOCATED.
            order_date (datetime.datetime): Order creation timestamp Example: 2024-12-01T09:00:00.000Z.
            requested_ship_date (datetime.datetime): Customer delivery requirement (used for on-time metrics) Example:
                2024-12-03T17:00:00.000Z.
            lines (list['WMSOutboundOrderLinesItem']): Order line items (required, validated length > 0 in repository)
            shipping_address (WMSOutboundOrderShippingAddress): Required delivery destination
            created_at (datetime.datetime): Document creation timestamp Example: 2024-12-01T09:00:00.000Z.
            updated_at (datetime.datetime): Last modification timestamp Example: 2024-12-01T14:45:00.000Z.
            carrier_info (Union[Unset, WMSOutboundOrderCarrierInfo]): Optional shipping carrier details
            special_instructions (Union[Unset, str]): Order-level handling and delivery notes Example: Deliver to loading
                dock, notify receiving department.
            timing (Union[Unset, WMSOutboundOrderTiming]): Workflow timing tracking (automatically updated during status
                changes)
    """

    field_id: str
    order_id: str
    order_number: str
    world_ref: "WMSOutboundOrderWorldRef"
    warehouse_id: str
    customer_id: str
    customer_name: str
    order_type: WMSOutboundOrderOrderType
    priority: WMSOutboundOrderPriority
    order_status: WMSOutboundOrderOrderStatus
    order_date: datetime.datetime
    requested_ship_date: datetime.datetime
    lines: list["WMSOutboundOrderLinesItem"]
    shipping_address: "WMSOutboundOrderShippingAddress"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    carrier_info: Union[Unset, "WMSOutboundOrderCarrierInfo"] = UNSET
    special_instructions: Union[Unset, str] = UNSET
    timing: Union[Unset, "WMSOutboundOrderTiming"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        order_id = self.order_id

        order_number = self.order_number

        world_ref = self.world_ref.to_dict()

        warehouse_id = self.warehouse_id

        customer_id = self.customer_id

        customer_name = self.customer_name

        order_type = self.order_type.value

        priority = self.priority.value

        order_status = self.order_status.value

        order_date = self.order_date.isoformat()

        requested_ship_date = self.requested_ship_date.isoformat()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        shipping_address = self.shipping_address.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        carrier_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier_info, Unset):
            carrier_info = self.carrier_info.to_dict()

        special_instructions = self.special_instructions

        timing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timing, Unset):
            timing = self.timing.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "orderId": order_id,
                "orderNumber": order_number,
                "worldRef": world_ref,
                "warehouseId": warehouse_id,
                "customerId": customer_id,
                "customerName": customer_name,
                "orderType": order_type,
                "priority": priority,
                "orderStatus": order_status,
                "orderDate": order_date,
                "requestedShipDate": requested_ship_date,
                "lines": lines,
                "shippingAddress": shipping_address,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if carrier_info is not UNSET:
            field_dict["carrierInfo"] = carrier_info
        if special_instructions is not UNSET:
            field_dict["specialInstructions"] = special_instructions
        if timing is not UNSET:
            field_dict["timing"] = timing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_outbound_order_carrier_info import WMSOutboundOrderCarrierInfo
        from ..models.wms_outbound_order_lines_item import WMSOutboundOrderLinesItem
        from ..models.wms_outbound_order_shipping_address import WMSOutboundOrderShippingAddress
        from ..models.wms_outbound_order_timing import WMSOutboundOrderTiming
        from ..models.wms_outbound_order_world_ref import WMSOutboundOrderWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        order_id = d.pop("orderId")

        order_number = d.pop("orderNumber")

        world_ref = WMSOutboundOrderWorldRef.from_dict(d.pop("worldRef"))

        warehouse_id = d.pop("warehouseId")

        customer_id = d.pop("customerId")

        customer_name = d.pop("customerName")

        order_type = WMSOutboundOrderOrderType(d.pop("orderType"))

        priority = WMSOutboundOrderPriority(d.pop("priority"))

        order_status = WMSOutboundOrderOrderStatus(d.pop("orderStatus"))

        order_date = isoparse(d.pop("orderDate"))

        requested_ship_date = isoparse(d.pop("requestedShipDate"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = WMSOutboundOrderLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        shipping_address = WMSOutboundOrderShippingAddress.from_dict(d.pop("shippingAddress"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _carrier_info = d.pop("carrierInfo", UNSET)
        carrier_info: Union[Unset, WMSOutboundOrderCarrierInfo]
        if isinstance(_carrier_info, Unset):
            carrier_info = UNSET
        else:
            carrier_info = WMSOutboundOrderCarrierInfo.from_dict(_carrier_info)

        special_instructions = d.pop("specialInstructions", UNSET)

        _timing = d.pop("timing", UNSET)
        timing: Union[Unset, WMSOutboundOrderTiming]
        if isinstance(_timing, Unset):
            timing = UNSET
        else:
            timing = WMSOutboundOrderTiming.from_dict(_timing)

        wms_outbound_order = cls(
            field_id=field_id,
            order_id=order_id,
            order_number=order_number,
            world_ref=world_ref,
            warehouse_id=warehouse_id,
            customer_id=customer_id,
            customer_name=customer_name,
            order_type=order_type,
            priority=priority,
            order_status=order_status,
            order_date=order_date,
            requested_ship_date=requested_ship_date,
            lines=lines,
            shipping_address=shipping_address,
            created_at=created_at,
            updated_at=updated_at,
            carrier_info=carrier_info,
            special_instructions=special_instructions,
            timing=timing,
        )

        wms_outbound_order.additional_properties = d
        return wms_outbound_order

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
