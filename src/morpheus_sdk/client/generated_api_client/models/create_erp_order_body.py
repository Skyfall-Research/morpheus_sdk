import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_erp_order_body_po_type import CreateERPOrderBodyPoType
from ..models.create_erp_order_body_status import CreateERPOrderBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_erp_order_body_buyer import CreateERPOrderBodyBuyer
    from ..models.create_erp_order_body_custom_fields import CreateERPOrderBodyCustomFields
    from ..models.create_erp_order_body_discounts_item import CreateERPOrderBodyDiscountsItem
    from ..models.create_erp_order_body_lines_item import CreateERPOrderBodyLinesItem


T = TypeVar("T", bound="CreateERPOrderBody")


@_attrs_define
class CreateERPOrderBody:
    """
    Attributes:
        customer_id (str): Customer identifier (required) Example: CUST_507f1f77bcf86cd799439013.
        order_date (datetime.date): Order placement date (required) Example: 2024-01-15.
        lines (list['CreateERPOrderBodyLinesItem']): Order line items (required)
        order_id (Union[Unset, str]): Optional custom order identifier (auto-generated if not provided) Example:
            ORDER_507f1f77bcf86cd799439012.
        po_type (Union[Unset, CreateERPOrderBodyPoType]): Purchase order type for business logic Default:
            CreateERPOrderBodyPoType.STANDARD. Example: STANDARD.
        partner_id (Union[Unset, str]): Partner identifier for B2B relationships Example:
            PARTNER_507f1f77bcf86cd799439014.
        requested_date (Union[Unset, datetime.date]): Requested delivery date Example: 2024-01-25.
        due_date (Union[Unset, datetime.date]): Due date for order completion Example: 2024-01-30.
        buyer (Union[Unset, CreateERPOrderBodyBuyer]): Buyer information
        currency (Union[Unset, str]): Order currency Default: 'USD'. Example: USD.
        subtotal (Union[Unset, float]): Order subtotal before taxes and fees Example: 1250.
        discounts (Union[Unset, list['CreateERPOrderBodyDiscountsItem']]): Order-level discounts
        total_amount (Union[Unset, float]): Total order amount including taxes and fees Example: 1335.
        status (Union[Unset, CreateERPOrderBodyStatus]): Order processing status Default:
            CreateERPOrderBodyStatus.RECEIVED. Example: RECEIVED.
        notes (Union[Unset, str]): Order notes and special instructions Example: Please deliver to dock 3.
        custom_fields (Union[Unset, CreateERPOrderBodyCustomFields]): Additional order-specific fields Example:
            {'salesRep': 'JOHN_DOE', 'priority': 'HIGH'}.
    """

    customer_id: str
    order_date: datetime.date
    lines: list["CreateERPOrderBodyLinesItem"]
    order_id: Union[Unset, str] = UNSET
    po_type: Union[Unset, CreateERPOrderBodyPoType] = CreateERPOrderBodyPoType.STANDARD
    partner_id: Union[Unset, str] = UNSET
    requested_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    buyer: Union[Unset, "CreateERPOrderBodyBuyer"] = UNSET
    currency: Union[Unset, str] = "USD"
    subtotal: Union[Unset, float] = UNSET
    discounts: Union[Unset, list["CreateERPOrderBodyDiscountsItem"]] = UNSET
    total_amount: Union[Unset, float] = UNSET
    status: Union[Unset, CreateERPOrderBodyStatus] = CreateERPOrderBodyStatus.RECEIVED
    notes: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "CreateERPOrderBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        order_date = self.order_date.isoformat()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        order_id = self.order_id

        po_type: Union[Unset, str] = UNSET
        if not isinstance(self.po_type, Unset):
            po_type = self.po_type.value

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

        total_amount = self.total_amount

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
                "orderDate": order_date,
                "lines": lines,
            }
        )
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if po_type is not UNSET:
            field_dict["poType"] = po_type
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
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if status is not UNSET:
            field_dict["status"] = status
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_erp_order_body_buyer import CreateERPOrderBodyBuyer
        from ..models.create_erp_order_body_custom_fields import CreateERPOrderBodyCustomFields
        from ..models.create_erp_order_body_discounts_item import CreateERPOrderBodyDiscountsItem
        from ..models.create_erp_order_body_lines_item import CreateERPOrderBodyLinesItem

        d = dict(src_dict)
        customer_id = d.pop("customerId")

        order_date = isoparse(d.pop("orderDate")).date()

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = CreateERPOrderBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        order_id = d.pop("orderId", UNSET)

        _po_type = d.pop("poType", UNSET)
        po_type: Union[Unset, CreateERPOrderBodyPoType]
        if isinstance(_po_type, Unset):
            po_type = UNSET
        else:
            po_type = CreateERPOrderBodyPoType(_po_type)

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
        buyer: Union[Unset, CreateERPOrderBodyBuyer]
        if isinstance(_buyer, Unset):
            buyer = UNSET
        else:
            buyer = CreateERPOrderBodyBuyer.from_dict(_buyer)

        currency = d.pop("currency", UNSET)

        subtotal = d.pop("subtotal", UNSET)

        discounts = []
        _discounts = d.pop("discounts", UNSET)
        for discounts_item_data in _discounts or []:
            discounts_item = CreateERPOrderBodyDiscountsItem.from_dict(discounts_item_data)

            discounts.append(discounts_item)

        total_amount = d.pop("totalAmount", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateERPOrderBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateERPOrderBodyStatus(_status)

        notes = d.pop("notes", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateERPOrderBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateERPOrderBodyCustomFields.from_dict(_custom_fields)

        create_erp_order_body = cls(
            customer_id=customer_id,
            order_date=order_date,
            lines=lines,
            order_id=order_id,
            po_type=po_type,
            partner_id=partner_id,
            requested_date=requested_date,
            due_date=due_date,
            buyer=buyer,
            currency=currency,
            subtotal=subtotal,
            discounts=discounts,
            total_amount=total_amount,
            status=status,
            notes=notes,
            custom_fields=custom_fields,
        )

        create_erp_order_body.additional_properties = d
        return create_erp_order_body

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
