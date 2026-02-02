import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_erp_invoice_body_status import UpdateERPInvoiceBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_erp_invoice_body_allowances_item import UpdateERPInvoiceBodyAllowancesItem
    from ..models.update_erp_invoice_body_charges_item import UpdateERPInvoiceBodyChargesItem
    from ..models.update_erp_invoice_body_custom_fields import UpdateERPInvoiceBodyCustomFields
    from ..models.update_erp_invoice_body_lines_item import UpdateERPInvoiceBodyLinesItem


T = TypeVar("T", bound="UpdateERPInvoiceBody")


@_attrs_define
class UpdateERPInvoiceBody:
    """
    Attributes:
        due_date (Union[Unset, datetime.date]): Updated payment due date Example: 2024-03-01.
        subtotal (Union[Unset, float]): Updated subtotal amount Example: 1100.
        total_amount (Union[Unset, float]): Updated total amount Example: 1188.
        balance_due (Union[Unset, float]): Updated balance due Example: 1188.
        status (Union[Unset, UpdateERPInvoiceBodyStatus]): Updated invoice status Example: SENT.
        allowances (Union[Unset, list['UpdateERPInvoiceBodyAllowancesItem']]): Updated allowances and discounts
        charges (Union[Unset, list['UpdateERPInvoiceBodyChargesItem']]): Updated additional charges
        lines (Union[Unset, list['UpdateERPInvoiceBodyLinesItem']]): Updated invoice line items
        custom_fields (Union[Unset, UpdateERPInvoiceBodyCustomFields]): Updated custom fields
    """

    due_date: Union[Unset, datetime.date] = UNSET
    subtotal: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    balance_due: Union[Unset, float] = UNSET
    status: Union[Unset, UpdateERPInvoiceBodyStatus] = UNSET
    allowances: Union[Unset, list["UpdateERPInvoiceBodyAllowancesItem"]] = UNSET
    charges: Union[Unset, list["UpdateERPInvoiceBodyChargesItem"]] = UNSET
    lines: Union[Unset, list["UpdateERPInvoiceBodyLinesItem"]] = UNSET
    custom_fields: Union[Unset, "UpdateERPInvoiceBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        subtotal = self.subtotal

        total_amount = self.total_amount

        balance_due = self.balance_due

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

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

        lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if balance_due is not UNSET:
            field_dict["balanceDue"] = balance_due
        if status is not UNSET:
            field_dict["status"] = status
        if allowances is not UNSET:
            field_dict["allowances"] = allowances
        if charges is not UNSET:
            field_dict["charges"] = charges
        if lines is not UNSET:
            field_dict["lines"] = lines
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_erp_invoice_body_allowances_item import UpdateERPInvoiceBodyAllowancesItem
        from ..models.update_erp_invoice_body_charges_item import UpdateERPInvoiceBodyChargesItem
        from ..models.update_erp_invoice_body_custom_fields import UpdateERPInvoiceBodyCustomFields
        from ..models.update_erp_invoice_body_lines_item import UpdateERPInvoiceBodyLinesItem

        d = dict(src_dict)
        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        subtotal = d.pop("subtotal", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        balance_due = d.pop("balanceDue", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateERPInvoiceBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateERPInvoiceBodyStatus(_status)

        allowances = []
        _allowances = d.pop("allowances", UNSET)
        for allowances_item_data in _allowances or []:
            allowances_item = UpdateERPInvoiceBodyAllowancesItem.from_dict(allowances_item_data)

            allowances.append(allowances_item)

        charges = []
        _charges = d.pop("charges", UNSET)
        for charges_item_data in _charges or []:
            charges_item = UpdateERPInvoiceBodyChargesItem.from_dict(charges_item_data)

            charges.append(charges_item)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = UpdateERPInvoiceBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateERPInvoiceBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateERPInvoiceBodyCustomFields.from_dict(_custom_fields)

        update_erp_invoice_body = cls(
            due_date=due_date,
            subtotal=subtotal,
            total_amount=total_amount,
            balance_due=balance_due,
            status=status,
            allowances=allowances,
            charges=charges,
            lines=lines,
            custom_fields=custom_fields,
        )

        update_erp_invoice_body.additional_properties = d
        return update_erp_invoice_body

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
