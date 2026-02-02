import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_erp_invoice_body_invoice_type import CreateERPInvoiceBodyInvoiceType
from ..models.create_erp_invoice_body_status import CreateERPInvoiceBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.create_erp_invoice_body_allowances_item import CreateERPInvoiceBodyAllowancesItem
    from ..models.create_erp_invoice_body_charges_item import CreateERPInvoiceBodyChargesItem
    from ..models.create_erp_invoice_body_custom_fields import CreateERPInvoiceBodyCustomFields
    from ..models.create_erp_invoice_body_lines_item import CreateERPInvoiceBodyLinesItem


T = TypeVar("T", bound="CreateERPInvoiceBody")


@_attrs_define
class CreateERPInvoiceBody:
    """
    Attributes:
        customer_id (str): Customer identifier (required) Example: CUST_507f1f77bcf86cd799439014.
        issue_date (datetime.date): Invoice issue date (required) Example: 2024-01-15.
        total_amount (float): Total invoice amount including taxes and adjustments (required) Example: 1080.
        lines (list['CreateERPInvoiceBodyLinesItem']): Invoice line items (required)
        invoice_id (Union[Unset, str]): Optional custom invoice identifier (auto-generated if not provided) Example:
            INV_507f1f77bcf86cd799439012.
        invoice_type (Union[Unset, CreateERPInvoiceBodyInvoiceType]): Invoice type for business processing Default:
            CreateERPInvoiceBodyInvoiceType.STANDARD. Example: STANDARD.
        po_number (Union[Unset, str]): Related purchase order number Example: ORDER_507f1f77bcf86cd799439013.
        partner_id (Union[Unset, str]): Partner identifier for B2B relationships Example:
            PARTNER_507f1f77bcf86cd799439015.
        bill_to (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        remit_to (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        due_date (Union[Unset, datetime.date]): Payment due date Example: 2024-02-15.
        currency (Union[Unset, str]): Invoice currency Default: 'USD'. Example: USD.
        subtotal (Union[Unset, float]): Invoice subtotal before adjustments Example: 1000.
        allowances (Union[Unset, list['CreateERPInvoiceBodyAllowancesItem']]): Invoice allowances and discounts
        charges (Union[Unset, list['CreateERPInvoiceBodyChargesItem']]): Additional charges and fees
        balance_due (Union[Unset, float]): Outstanding balance due Example: 1080.
        status (Union[Unset, CreateERPInvoiceBodyStatus]): Invoice processing status Default:
            CreateERPInvoiceBodyStatus.DRAFT. Example: DRAFT.
        payment_terms (Union[Unset, str]): Payment terms and conditions Example: NET30.
        custom_fields (Union[Unset, CreateERPInvoiceBodyCustomFields]): Additional invoice-specific fields Example:
            {'salesRep': 'JANE_DOE', 'region': 'NORTHEAST'}.
    """

    customer_id: str
    issue_date: datetime.date
    total_amount: float
    lines: list["CreateERPInvoiceBodyLinesItem"]
    invoice_id: Union[Unset, str] = UNSET
    invoice_type: Union[Unset, CreateERPInvoiceBodyInvoiceType] = CreateERPInvoiceBodyInvoiceType.STANDARD
    po_number: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    bill_to: Union[Unset, "Address"] = UNSET
    remit_to: Union[Unset, "Address"] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    currency: Union[Unset, str] = "USD"
    subtotal: Union[Unset, float] = UNSET
    allowances: Union[Unset, list["CreateERPInvoiceBodyAllowancesItem"]] = UNSET
    charges: Union[Unset, list["CreateERPInvoiceBodyChargesItem"]] = UNSET
    balance_due: Union[Unset, float] = UNSET
    status: Union[Unset, CreateERPInvoiceBodyStatus] = CreateERPInvoiceBodyStatus.DRAFT
    payment_terms: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "CreateERPInvoiceBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        issue_date = self.issue_date.isoformat()

        total_amount = self.total_amount

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        invoice_id = self.invoice_id

        invoice_type: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_type, Unset):
            invoice_type = self.invoice_type.value

        po_number = self.po_number

        partner_id = self.partner_id

        bill_to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bill_to, Unset):
            bill_to = self.bill_to.to_dict()

        remit_to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.remit_to, Unset):
            remit_to = self.remit_to.to_dict()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        currency = self.currency

        subtotal = self.subtotal

        allowances: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.allowances, Unset):
            allowances = []
            for allowances_item_data in self.allowances:
                allowances_item = allowances_item_data.to_dict()
                allowances.append(allowances_item)

        charges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.charges, Unset):
            charges = []
            for charges_item_data in self.charges:
                charges_item = charges_item_data.to_dict()
                charges.append(charges_item)

        balance_due = self.balance_due

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        payment_terms = self.payment_terms

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customerId": customer_id,
                "issueDate": issue_date,
                "totalAmount": total_amount,
                "lines": lines,
            }
        )
        if invoice_id is not UNSET:
            field_dict["invoiceId"] = invoice_id
        if invoice_type is not UNSET:
            field_dict["invoiceType"] = invoice_type
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if bill_to is not UNSET:
            field_dict["billTo"] = bill_to
        if remit_to is not UNSET:
            field_dict["remitTo"] = remit_to
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if currency is not UNSET:
            field_dict["currency"] = currency
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if allowances is not UNSET:
            field_dict["allowances"] = allowances
        if charges is not UNSET:
            field_dict["charges"] = charges
        if balance_due is not UNSET:
            field_dict["balanceDue"] = balance_due
        if status is not UNSET:
            field_dict["status"] = status
        if payment_terms is not UNSET:
            field_dict["paymentTerms"] = payment_terms
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.create_erp_invoice_body_allowances_item import CreateERPInvoiceBodyAllowancesItem
        from ..models.create_erp_invoice_body_charges_item import CreateERPInvoiceBodyChargesItem
        from ..models.create_erp_invoice_body_custom_fields import CreateERPInvoiceBodyCustomFields
        from ..models.create_erp_invoice_body_lines_item import CreateERPInvoiceBodyLinesItem

        d = dict(src_dict)
        customer_id = d.pop("customerId")

        issue_date = isoparse(d.pop("issueDate")).date()

        total_amount = d.pop("totalAmount")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = CreateERPInvoiceBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        invoice_id = d.pop("invoiceId", UNSET)

        _invoice_type = d.pop("invoiceType", UNSET)
        invoice_type: Union[Unset, CreateERPInvoiceBodyInvoiceType]
        if isinstance(_invoice_type, Unset):
            invoice_type = UNSET
        else:
            invoice_type = CreateERPInvoiceBodyInvoiceType(_invoice_type)

        po_number = d.pop("poNumber", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        _bill_to = d.pop("billTo", UNSET)
        bill_to: Union[Unset, Address]
        if isinstance(_bill_to, Unset):
            bill_to = UNSET
        else:
            bill_to = Address.from_dict(_bill_to)

        _remit_to = d.pop("remitTo", UNSET)
        remit_to: Union[Unset, Address]
        if isinstance(_remit_to, Unset):
            remit_to = UNSET
        else:
            remit_to = Address.from_dict(_remit_to)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        currency = d.pop("currency", UNSET)

        subtotal = d.pop("subtotal", UNSET)

        allowances = []
        _allowances = d.pop("allowances", UNSET)
        for allowances_item_data in _allowances or []:
            allowances_item = CreateERPInvoiceBodyAllowancesItem.from_dict(allowances_item_data)

            allowances.append(allowances_item)

        charges = []
        _charges = d.pop("charges", UNSET)
        for charges_item_data in _charges or []:
            charges_item = CreateERPInvoiceBodyChargesItem.from_dict(charges_item_data)

            charges.append(charges_item)

        balance_due = d.pop("balanceDue", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateERPInvoiceBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateERPInvoiceBodyStatus(_status)

        payment_terms = d.pop("paymentTerms", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateERPInvoiceBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateERPInvoiceBodyCustomFields.from_dict(_custom_fields)

        create_erp_invoice_body = cls(
            customer_id=customer_id,
            issue_date=issue_date,
            total_amount=total_amount,
            lines=lines,
            invoice_id=invoice_id,
            invoice_type=invoice_type,
            po_number=po_number,
            partner_id=partner_id,
            bill_to=bill_to,
            remit_to=remit_to,
            due_date=due_date,
            currency=currency,
            subtotal=subtotal,
            allowances=allowances,
            charges=charges,
            balance_due=balance_due,
            status=status,
            payment_terms=payment_terms,
            custom_fields=custom_fields,
        )

        create_erp_invoice_body.additional_properties = d
        return create_erp_invoice_body

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
