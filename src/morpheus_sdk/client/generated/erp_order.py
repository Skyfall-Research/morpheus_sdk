import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.erp_order_direction import ERPOrderDirection
from ..models.erp_order_po_type import ERPOrderPoType
from ..models.erp_order_status import ERPOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_order_attachments_item import ERPOrderAttachmentsItem
    from ..models.erp_order_buyer import ERPOrderBuyer
    from ..models.erp_order_custom_fields import ERPOrderCustomFields
    from ..models.erp_order_discounts_item import ERPOrderDiscountsItem
    from ..models.erp_order_lines_item import ERPOrderLinesItem
    from ..models.tax_detail import TaxDetail


T = TypeVar("T", bound="ERPOrder")


@_attrs_define
class ERPOrder:
    """ERP purchase order with comprehensive order information and line item details

    Attributes:
        field_id (str): MongoDB unique identifier Example: 507f1f77bcf86cd799439012.
        world_id (str): World environment identifier Example: 507f1f77bcf86cd799439011.
        order_id (str): Unique order identifier (CRITICAL: Route parameter 'poNumber' maps to this field) Example:
            ORDER_507f1f77bcf86cd799439012.
        customer_id (str): Customer identifier Example: CUST_507f1f77bcf86cd799439013.
        order_date (datetime.date): Order placement date Example: 2024-01-15.
        status (ERPOrderStatus): Order processing status Example: RECEIVED.
        lines (list['ERPOrderLinesItem']): Order line items
        field_v (Union[Unset, float]): MongoDB version key
        po_type (Union[Unset, ERPOrderPoType]): Purchase order type Example: STANDARD.
        direction (Union[Unset, ERPOrderDirection]): Order direction - INBOUND for purchase orders, OUTBOUND for sales
            orders Default: ERPOrderDirection.INBOUND. Example: INBOUND.
        partner_id (Union[Unset, str]): Partner identifier Example: PARTNER_507f1f77bcf86cd799439014.
        requested_date (Union[Unset, datetime.date]): Requested delivery date Example: 2024-01-25.
        due_date (Union[Unset, datetime.date]): Due date for order completion Example: 2024-01-30.
        buyer (Union[Unset, ERPOrderBuyer]): Buyer information
        currency (Union[Unset, str]): Order currency Example: USD.
        subtotal (Union[Unset, float]): Order subtotal before taxes and fees Example: 1250.
        discounts (Union[Unset, list['ERPOrderDiscountsItem']]): Order-level discounts
        taxes (Union[Unset, list['TaxDetail']]): Order-level tax details
        total_amount (Union[Unset, float]): Total order amount Example: 1335.
        attachments (Union[Unset, list['ERPOrderAttachmentsItem']]): Order attachments and documents
        edi_transaction_id (Union[Unset, str]): Reference to EDI transaction ID Example: 507f1f77bcf86cd799439021.
        flow_id (Union[Unset, str]): Business flow identifier for workflow tracking Example: FLOW_PO_001.
        notes (Union[Unset, str]): Order notes and instructions Example: Please deliver to dock 3.
        custom_fields (Union[Unset, ERPOrderCustomFields]): Additional order-specific fields Example: {'salesRep':
            'JOHN_DOE', 'priority': 'HIGH'}.
        created_at (Union[Unset, datetime.datetime]): Order creation timestamp Example: 2024-01-15T10:00:00.000Z.
        updated_at (Union[Unset, datetime.datetime]): Last update timestamp Example: 2024-01-15T15:30:00.000Z.
    """

    field_id: str
    world_id: str
    order_id: str
    customer_id: str
    order_date: datetime.date
    status: ERPOrderStatus
    lines: list["ERPOrderLinesItem"]
    field_v: Union[Unset, float] = UNSET
    po_type: Union[Unset, ERPOrderPoType] = UNSET
    direction: Union[Unset, ERPOrderDirection] = ERPOrderDirection.INBOUND
    partner_id: Union[Unset, str] = UNSET
    requested_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    buyer: Union[Unset, "ERPOrderBuyer"] = UNSET
    currency: Union[Unset, str] = UNSET
    subtotal: Union[Unset, float] = UNSET
    discounts: Union[Unset, list["ERPOrderDiscountsItem"]] = UNSET
    taxes: Union[Unset, list["TaxDetail"]] = UNSET
    total_amount: Union[Unset, float] = UNSET
    attachments: Union[Unset, list["ERPOrderAttachmentsItem"]] = UNSET
    edi_transaction_id: Union[Unset, str] = UNSET
    flow_id: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "ERPOrderCustomFields"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_id = self.world_id

        order_id = self.order_id

        customer_id = self.customer_id

        order_date = self.order_date.isoformat()

        status = self.status.value

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        field_v = self.field_v

        po_type: Union[Unset, str] = UNSET
        if not isinstance(self.po_type, Unset):
            po_type = self.po_type.value

        direction: Union[Unset, str] = UNSET
        if not isinstance(self.direction, Unset):
            direction = self.direction.value

        partner_id = self.partner_id

        requested_date: Union[Unset, str] = UNSET
        if not isinstance(self.requested_date, Unset):
            requested_date = self.requested_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        buyer: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.buyer, Unset):
            buyer = self.buyer.to_dict()

        currency = self.currency

        subtotal = self.subtotal

        discounts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.discounts, Unset):
            discounts = []
            for discounts_item_data in self.discounts:
                discounts_item = discounts_item_data.to_dict()
                discounts.append(discounts_item)

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        total_amount = self.total_amount

        attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        edi_transaction_id = self.edi_transaction_id

        flow_id = self.flow_id

        notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "worldId": world_id,
                "orderId": order_id,
                "customerId": customer_id,
                "orderDate": order_date,
                "status": status,
                "lines": lines,
            }
        )
        if field_v is not UNSET:
            field_dict["__v"] = field_v
        if po_type is not UNSET:
            field_dict["poType"] = po_type
        if direction is not UNSET:
            field_dict["direction"] = direction
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if requested_date is not UNSET:
            field_dict["requestedDate"] = requested_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if buyer is not UNSET:
            field_dict["buyer"] = buyer
        if currency is not UNSET:
            field_dict["currency"] = currency
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if discounts is not UNSET:
            field_dict["discounts"] = discounts
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if edi_transaction_id is not UNSET:
            field_dict["ediTransactionId"] = edi_transaction_id
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_order_attachments_item import ERPOrderAttachmentsItem
        from ..models.erp_order_buyer import ERPOrderBuyer
        from ..models.erp_order_custom_fields import ERPOrderCustomFields
        from ..models.erp_order_discounts_item import ERPOrderDiscountsItem
        from ..models.erp_order_lines_item import ERPOrderLinesItem
        from ..models.tax_detail import TaxDetail

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_id = d.pop("worldId")

        order_id = d.pop("orderId")

        customer_id = d.pop("customerId")

        order_date = isoparse(d.pop("orderDate")).date()

        status = ERPOrderStatus(d.pop("status"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = ERPOrderLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        field_v = d.pop("__v", UNSET)

        _po_type = d.pop("poType", UNSET)
        po_type: Union[Unset, ERPOrderPoType]
        if isinstance(_po_type, Unset):
            po_type = UNSET
        else:
            po_type = ERPOrderPoType(_po_type)

        _direction = d.pop("direction", UNSET)
        direction: Union[Unset, ERPOrderDirection]
        if isinstance(_direction, Unset):
            direction = UNSET
        else:
            direction = ERPOrderDirection(_direction)

        partner_id = d.pop("partnerId", UNSET)

        _requested_date = d.pop("requestedDate", UNSET)
        requested_date: Union[Unset, datetime.date]
        if isinstance(_requested_date, Unset):
            requested_date = UNSET
        else:
            requested_date = isoparse(_requested_date).date()

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        _buyer = d.pop("buyer", UNSET)
        buyer: Union[Unset, ERPOrderBuyer]
        if isinstance(_buyer, Unset):
            buyer = UNSET
        else:
            buyer = ERPOrderBuyer.from_dict(_buyer)

        currency = d.pop("currency", UNSET)

        subtotal = d.pop("subtotal", UNSET)

        discounts = []
        _discounts = d.pop("discounts", UNSET)
        for discounts_item_data in _discounts or []:
            discounts_item = ERPOrderDiscountsItem.from_dict(discounts_item_data)

            discounts.append(discounts_item)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = TaxDetail.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        total_amount = d.pop("totalAmount", UNSET)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = ERPOrderAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        edi_transaction_id = d.pop("ediTransactionId", UNSET)

        flow_id = d.pop("flowId", UNSET)

        notes = d.pop("notes", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPOrderCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPOrderCustomFields.from_dict(_custom_fields)

        _created_at = d.pop("createdAt", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updatedAt", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        erp_order = cls(
            field_id=field_id,
            world_id=world_id,
            order_id=order_id,
            customer_id=customer_id,
            order_date=order_date,
            status=status,
            lines=lines,
            field_v=field_v,
            po_type=po_type,
            direction=direction,
            partner_id=partner_id,
            requested_date=requested_date,
            due_date=due_date,
            buyer=buyer,
            currency=currency,
            subtotal=subtotal,
            discounts=discounts,
            taxes=taxes,
            total_amount=total_amount,
            attachments=attachments,
            edi_transaction_id=edi_transaction_id,
            flow_id=flow_id,
            notes=notes,
            custom_fields=custom_fields,
            created_at=created_at,
            updated_at=updated_at,
        )

        erp_order.additional_properties = d
        return erp_order

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
