import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_wms_outbound_order_body_order_type import CreateWMSOutboundOrderBodyOrderType
from ..models.create_wms_outbound_order_body_priority import CreateWMSOutboundOrderBodyPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_outbound_order_body_carrier_info import CreateWMSOutboundOrderBodyCarrierInfo
    from ..models.create_wms_outbound_order_body_lines_item import CreateWMSOutboundOrderBodyLinesItem
    from ..models.create_wms_outbound_order_body_shipping_address import CreateWMSOutboundOrderBodyShippingAddress


T = TypeVar("T", bound="CreateWMSOutboundOrderBody")


@_attrs_define
class CreateWMSOutboundOrderBody:
    """
    Attributes:
        order_id (str): Business primary identifier (consistent naming verified) Example: ORD-2024-001234.
        order_number (str): Human-readable order number (unique per world) Example: WO-20241201-001.
        warehouse_id (str): Required - source warehouse identifier Example: WH-MAIN-001.
        customer_id (str): Customer account identifier Example: CUST-ABC-123.
        customer_name (str): Customer display name Example: ABC Corporation.
        order_date (datetime.datetime): Order creation timestamp Example: 2024-12-01T09:00:00.000Z.
        requested_ship_date (datetime.datetime): Customer delivery requirement Example: 2024-12-03T17:00:00.000Z.
        priority (CreateWMSOutboundOrderBodyPriority): Order processing priority Example: HIGH.
        order_type (CreateWMSOutboundOrderBodyOrderType): Order classification type Example: STANDARD.
        lines (list['CreateWMSOutboundOrderBodyLinesItem']): Order line items (required, length > 0)
        shipping_address (CreateWMSOutboundOrderBodyShippingAddress): Delivery destination
        carrier_info (Union[Unset, CreateWMSOutboundOrderBodyCarrierInfo]): Optional shipping carrier details
        special_instructions (Union[Unset, str]): Order-level notes Example: Deliver to loading dock.
    """

    order_id: str
    order_number: str
    warehouse_id: str
    customer_id: str
    customer_name: str
    order_date: datetime.datetime
    requested_ship_date: datetime.datetime
    priority: CreateWMSOutboundOrderBodyPriority
    order_type: CreateWMSOutboundOrderBodyOrderType
    lines: list["CreateWMSOutboundOrderBodyLinesItem"]
    shipping_address: "CreateWMSOutboundOrderBodyShippingAddress"
    carrier_info: Union[Unset, "CreateWMSOutboundOrderBodyCarrierInfo"] = UNSET
    special_instructions: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_id = self.order_id

        order_number = self.order_number

        warehouse_id = self.warehouse_id

        customer_id = self.customer_id

        customer_name = self.customer_name

        order_date = self.order_date.isoformat()

        requested_ship_date = self.requested_ship_date.isoformat()

        priority = self.priority.value

        order_type = self.order_type.value

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        shipping_address = self.shipping_address.to_dict()

        carrier_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier_info, Unset):
            carrier_info = self.carrier_info.to_dict()

        special_instructions = self.special_instructions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "orderId": order_id,
                "orderNumber": order_number,
                "warehouseId": warehouse_id,
                "customerId": customer_id,
                "customerName": customer_name,
                "orderDate": order_date,
                "requestedShipDate": requested_ship_date,
                "priority": priority,
                "orderType": order_type,
                "lines": lines,
                "shippingAddress": shipping_address,
            }
        )
        if carrier_info is not UNSET:
            field_dict["carrierInfo"] = carrier_info
        if special_instructions is not UNSET:
            field_dict["specialInstructions"] = special_instructions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_outbound_order_body_carrier_info import CreateWMSOutboundOrderBodyCarrierInfo
        from ..models.create_wms_outbound_order_body_lines_item import CreateWMSOutboundOrderBodyLinesItem
        from ..models.create_wms_outbound_order_body_shipping_address import CreateWMSOutboundOrderBodyShippingAddress

        d = dict(src_dict)
        order_id = d.pop("orderId")

        order_number = d.pop("orderNumber")

        warehouse_id = d.pop("warehouseId")

        customer_id = d.pop("customerId")

        customer_name = d.pop("customerName")

        order_date = isoparse(d.pop("orderDate"))

        requested_ship_date = isoparse(d.pop("requestedShipDate"))

        priority = CreateWMSOutboundOrderBodyPriority(d.pop("priority"))

        order_type = CreateWMSOutboundOrderBodyOrderType(d.pop("orderType"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = CreateWMSOutboundOrderBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        shipping_address = CreateWMSOutboundOrderBodyShippingAddress.from_dict(d.pop("shippingAddress"))

        _carrier_info = d.pop("carrierInfo", UNSET)
        carrier_info: Union[Unset, CreateWMSOutboundOrderBodyCarrierInfo]
        if isinstance(_carrier_info, Unset):
            carrier_info = UNSET
        else:
            carrier_info = CreateWMSOutboundOrderBodyCarrierInfo.from_dict(_carrier_info)

        special_instructions = d.pop("specialInstructions", UNSET)

        create_wms_outbound_order_body = cls(
            order_id=order_id,
            order_number=order_number,
            warehouse_id=warehouse_id,
            customer_id=customer_id,
            customer_name=customer_name,
            order_date=order_date,
            requested_ship_date=requested_ship_date,
            priority=priority,
            order_type=order_type,
            lines=lines,
            shipping_address=shipping_address,
            carrier_info=carrier_info,
            special_instructions=special_instructions,
        )

        create_wms_outbound_order_body.additional_properties = d
        return create_wms_outbound_order_body

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
