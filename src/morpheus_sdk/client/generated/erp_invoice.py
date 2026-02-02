import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.erp_invoice_invoice_type import ERPInvoiceInvoiceType
from ..models.erp_invoice_status import ERPInvoiceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.erp_invoice_accounting import ERPInvoiceAccounting
    from ..models.erp_invoice_allowances_item import ERPInvoiceAllowancesItem
    from ..models.erp_invoice_attachments_item import ERPInvoiceAttachmentsItem
    from ..models.erp_invoice_charges_item import ERPInvoiceChargesItem
    from ..models.erp_invoice_correction_history_item import ERPInvoiceCorrectionHistoryItem
    from ..models.erp_invoice_custom_fields import ERPInvoiceCustomFields
    from ..models.erp_invoice_disputes_item import ERPInvoiceDisputesItem
    from ..models.erp_invoice_lines_item import ERPInvoiceLinesItem
    from ..models.erp_invoice_references_item import ERPInvoiceReferencesItem
    from ..models.erp_invoice_tax_summary import ERPInvoiceTaxSummary
    from ..models.tax_detail import TaxDetail


T = TypeVar("T", bound="ERPInvoice")


@_attrs_define
class ERPInvoice:
    """ERP invoice with comprehensive billing information and line item details

    Attributes:
        field_id (str): MongoDB unique identifier Example: 507f1f77bcf86cd799439015.
        world_id (str): World environment identifier Example: 507f1f77bcf86cd799439011.
        invoice_id (str): Unique invoice identifier (NOTE: Route parameter 'invoiceNumber' maps to this field) Example:
            INV_507f1f77bcf86cd799439012.
        customer_id (str): Customer identifier Example: CUST_507f1f77bcf86cd799439014.
        issue_date (datetime.date): Invoice issue date Example: 2024-01-15.
        total_amount (float): Total invoice amount Example: 1080.
        status (ERPInvoiceStatus): Invoice status Example: DRAFT.
        lines (list['ERPInvoiceLinesItem']): Invoice line items
        field_v (Union[Unset, float]): MongoDB version key
        invoice_type (Union[Unset, ERPInvoiceInvoiceType]): Invoice type Example: STANDARD.
        po_number (Union[Unset, str]): Related purchase order number Example: ORDER_507f1f77bcf86cd799439013.
        order_id (Union[Unset, str]): Reference to order ID Example: ORDER_507f1f77bcf86cd799439013.
        partner_id (Union[Unset, str]): Partner identifier Example: PARTNER_507f1f77bcf86cd799439015.
        bill_to (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        remit_to (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        due_date (Union[Unset, datetime.date]): Payment due date Example: 2024-02-15.
        currency (Union[Unset, str]): Invoice currency Example: USD.
        subtotal (Union[Unset, float]): Invoice subtotal Example: 1000.
        allowances (Union[Unset, list['ERPInvoiceAllowancesItem']]): Invoice allowances and discounts
        charges (Union[Unset, list['ERPInvoiceChargesItem']]): Additional charges and fees
        taxes (Union[Unset, list['TaxDetail']]): Invoice-level tax details
        balance_due (Union[Unset, float]): Outstanding balance due Example: 1080.
        references (Union[Unset, list['ERPInvoiceReferencesItem']]): Document references
        edi_transaction_id (Union[Unset, str]): Reference to EDI transaction ID Example: 507f1f77bcf86cd799439021.
        tax_summary (Union[Unset, ERPInvoiceTaxSummary]): Tax summary data Example: {'totalTax': 80, 'taxBreakdown':
            [{'taxType': 'STATE', 'amount': 60}, {'taxType': 'LOCAL', 'amount': 20}]}.
        accounting (Union[Unset, ERPInvoiceAccounting]): Accounting configuration
        disputes (Union[Unset, list['ERPInvoiceDisputesItem']]): Invoice disputes
        correction_history (Union[Unset, list['ERPInvoiceCorrectionHistoryItem']]): Invoice correction history
        attachments (Union[Unset, list['ERPInvoiceAttachmentsItem']]): Invoice attachments and documents
        flow_id (Union[Unset, str]): Business flow identifier for workflow tracking Example: FLOW_INV_001.
        payment_terms (Union[Unset, str]): Payment terms Example: NET30.
        custom_fields (Union[Unset, ERPInvoiceCustomFields]): Additional invoice fields Example: {'salesRep':
            'JANE_DOE', 'region': 'NORTHEAST'}.
        created_at (Union[Unset, datetime.datetime]): Invoice creation timestamp Example: 2024-01-15T09:00:00.000Z.
        updated_at (Union[Unset, datetime.datetime]): Last update timestamp Example: 2024-01-15T14:30:00.000Z.
    """

    field_id: str
    world_id: str
    invoice_id: str
    customer_id: str
    issue_date: datetime.date
    total_amount: float
    status: ERPInvoiceStatus
    lines: list["ERPInvoiceLinesItem"]
    field_v: Union[Unset, float] = UNSET
    invoice_type: Union[Unset, ERPInvoiceInvoiceType] = UNSET
    po_number: Union[Unset, str] = UNSET
    order_id: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    bill_to: Union[Unset, "Address"] = UNSET
    remit_to: Union[Unset, "Address"] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    currency: Union[Unset, str] = UNSET
    subtotal: Union[Unset, float] = UNSET
    allowances: Union[Unset, list["ERPInvoiceAllowancesItem"]] = UNSET
    charges: Union[Unset, list["ERPInvoiceChargesItem"]] = UNSET
    taxes: Union[Unset, list["TaxDetail"]] = UNSET
    balance_due: Union[Unset, float] = UNSET
    references: Union[Unset, list["ERPInvoiceReferencesItem"]] = UNSET
    edi_transaction_id: Union[Unset, str] = UNSET
    tax_summary: Union[Unset, "ERPInvoiceTaxSummary"] = UNSET
    accounting: Union[Unset, "ERPInvoiceAccounting"] = UNSET
    disputes: Union[Unset, list["ERPInvoiceDisputesItem"]] = UNSET
    correction_history: Union[Unset, list["ERPInvoiceCorrectionHistoryItem"]] = UNSET
    attachments: Union[Unset, list["ERPInvoiceAttachmentsItem"]] = UNSET
    flow_id: Union[Unset, str] = UNSET
    payment_terms: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "ERPInvoiceCustomFields"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_id = self.world_id

        invoice_id = self.invoice_id

        customer_id = self.customer_id

        issue_date = self.issue_date.isoformat()

        total_amount = self.total_amount

        status = self.status.value

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        field_v = self.field_v

        invoice_type: Union[Unset, str] = UNSET
        if not isinstance(self.invoice_type, Unset):
            invoice_type = self.invoice_type.value

        po_number = self.po_number

        order_id = self.order_id

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

        taxes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.taxes, Unset):
            taxes = []
            for taxes_item_data in self.taxes:
                taxes_item = taxes_item_data.to_dict()
                taxes.append(taxes_item)

        balance_due = self.balance_due

        references: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.references, Unset):
            references = []
            for references_item_data in self.references:
                references_item = references_item_data.to_dict()
                references.append(references_item)

        edi_transaction_id = self.edi_transaction_id

        tax_summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_summary, Unset):
            tax_summary = self.tax_summary.to_dict()

        accounting: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.accounting, Unset):
            accounting = self.accounting.to_dict()

        disputes: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.disputes, Unset):
            disputes = []
            for disputes_item_data in self.disputes:
                disputes_item = disputes_item_data.to_dict()
                disputes.append(disputes_item)

        correction_history: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.correction_history, Unset):
            correction_history = []
            for correction_history_item_data in self.correction_history:
                correction_history_item = correction_history_item_data.to_dict()
                correction_history.append(correction_history_item)

        attachments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)

        flow_id = self.flow_id

        payment_terms = self.payment_terms

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
                "invoiceId": invoice_id,
                "customerId": customer_id,
                "issueDate": issue_date,
                "totalAmount": total_amount,
                "status": status,
                "lines": lines,
            }
        )
        if field_v is not UNSET:
            field_dict["__v"] = field_v
        if invoice_type is not UNSET:
            field_dict["invoiceType"] = invoice_type
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
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
        if taxes is not UNSET:
            field_dict["taxes"] = taxes
        if balance_due is not UNSET:
            field_dict["balanceDue"] = balance_due
        if references is not UNSET:
            field_dict["references"] = references
        if edi_transaction_id is not UNSET:
            field_dict["ediTransactionId"] = edi_transaction_id
        if tax_summary is not UNSET:
            field_dict["taxSummary"] = tax_summary
        if accounting is not UNSET:
            field_dict["accounting"] = accounting
        if disputes is not UNSET:
            field_dict["disputes"] = disputes
        if correction_history is not UNSET:
            field_dict["correctionHistory"] = correction_history
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if payment_terms is not UNSET:
            field_dict["paymentTerms"] = payment_terms
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.erp_invoice_accounting import ERPInvoiceAccounting
        from ..models.erp_invoice_allowances_item import ERPInvoiceAllowancesItem
        from ..models.erp_invoice_attachments_item import ERPInvoiceAttachmentsItem
        from ..models.erp_invoice_charges_item import ERPInvoiceChargesItem
        from ..models.erp_invoice_correction_history_item import ERPInvoiceCorrectionHistoryItem
        from ..models.erp_invoice_custom_fields import ERPInvoiceCustomFields
        from ..models.erp_invoice_disputes_item import ERPInvoiceDisputesItem
        from ..models.erp_invoice_lines_item import ERPInvoiceLinesItem
        from ..models.erp_invoice_references_item import ERPInvoiceReferencesItem
        from ..models.erp_invoice_tax_summary import ERPInvoiceTaxSummary
        from ..models.tax_detail import TaxDetail

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_id = d.pop("worldId")

        invoice_id = d.pop("invoiceId")

        customer_id = d.pop("customerId")

        issue_date = isoparse(d.pop("issueDate")).date()

        total_amount = d.pop("totalAmount")

        status = ERPInvoiceStatus(d.pop("status"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = ERPInvoiceLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        field_v = d.pop("__v", UNSET)

        _invoice_type = d.pop("invoiceType", UNSET)
        invoice_type: Union[Unset, ERPInvoiceInvoiceType]
        if isinstance(_invoice_type, Unset):
            invoice_type = UNSET
        else:
            invoice_type = ERPInvoiceInvoiceType(_invoice_type)

        po_number = d.pop("poNumber", UNSET)

        order_id = d.pop("orderId", UNSET)

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
            allowances_item = ERPInvoiceAllowancesItem.from_dict(allowances_item_data)

            allowances.append(allowances_item)

        charges = []
        _charges = d.pop("charges", UNSET)
        for charges_item_data in _charges or []:
            charges_item = ERPInvoiceChargesItem.from_dict(charges_item_data)

            charges.append(charges_item)

        taxes = []
        _taxes = d.pop("taxes", UNSET)
        for taxes_item_data in _taxes or []:
            taxes_item = TaxDetail.from_dict(taxes_item_data)

            taxes.append(taxes_item)

        balance_due = d.pop("balanceDue", UNSET)

        references = []
        _references = d.pop("references", UNSET)
        for references_item_data in _references or []:
            references_item = ERPInvoiceReferencesItem.from_dict(references_item_data)

            references.append(references_item)

        edi_transaction_id = d.pop("ediTransactionId", UNSET)

        _tax_summary = d.pop("taxSummary", UNSET)
        tax_summary: Union[Unset, ERPInvoiceTaxSummary]
        if isinstance(_tax_summary, Unset):
            tax_summary = UNSET
        else:
            tax_summary = ERPInvoiceTaxSummary.from_dict(_tax_summary)

        _accounting = d.pop("accounting", UNSET)
        accounting: Union[Unset, ERPInvoiceAccounting]
        if isinstance(_accounting, Unset):
            accounting = UNSET
        else:
            accounting = ERPInvoiceAccounting.from_dict(_accounting)

        disputes = []
        _disputes = d.pop("disputes", UNSET)
        for disputes_item_data in _disputes or []:
            disputes_item = ERPInvoiceDisputesItem.from_dict(disputes_item_data)

            disputes.append(disputes_item)

        correction_history = []
        _correction_history = d.pop("correctionHistory", UNSET)
        for correction_history_item_data in _correction_history or []:
            correction_history_item = ERPInvoiceCorrectionHistoryItem.from_dict(correction_history_item_data)

            correction_history.append(correction_history_item)

        attachments = []
        _attachments = d.pop("attachments", UNSET)
        for attachments_item_data in _attachments or []:
            attachments_item = ERPInvoiceAttachmentsItem.from_dict(attachments_item_data)

            attachments.append(attachments_item)

        flow_id = d.pop("flowId", UNSET)

        payment_terms = d.pop("paymentTerms", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPInvoiceCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPInvoiceCustomFields.from_dict(_custom_fields)

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

        erp_invoice = cls(
            field_id=field_id,
            world_id=world_id,
            invoice_id=invoice_id,
            customer_id=customer_id,
            issue_date=issue_date,
            total_amount=total_amount,
            status=status,
            lines=lines,
            field_v=field_v,
            invoice_type=invoice_type,
            po_number=po_number,
            order_id=order_id,
            partner_id=partner_id,
            bill_to=bill_to,
            remit_to=remit_to,
            due_date=due_date,
            currency=currency,
            subtotal=subtotal,
            allowances=allowances,
            charges=charges,
            taxes=taxes,
            balance_due=balance_due,
            references=references,
            edi_transaction_id=edi_transaction_id,
            tax_summary=tax_summary,
            accounting=accounting,
            disputes=disputes,
            correction_history=correction_history,
            attachments=attachments,
            flow_id=flow_id,
            payment_terms=payment_terms,
            custom_fields=custom_fields,
            created_at=created_at,
            updated_at=updated_at,
        )

        erp_invoice.additional_properties = d
        return erp_invoice

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
