import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.erp_order_lines_item_custom_fields import ERPOrderLinesItemCustomFields
    from ..models.erp_order_lines_item_schedule_lines_item import ERPOrderLinesItemScheduleLinesItem
    from ..models.tax_detail import TaxDetail


T = TypeVar("T", bound="ERPOrderLinesItem")


@_attrs_define
class ERPOrderLinesItem:
    """
    Attributes:
        line_number (Union[Unset, float]):  Example: 1.
        sku (Union[Unset, str]):  Example: PROD_WIDGET_001.
        description (Union[Unset, str]):  Example: Premium Widget - Blue.
        quantity_ordered (Union[Unset, float]):  Example: 10.
        unit_price (Union[Unset, float]):  Example: 99.99.
        line_total (Union[Unset, float]):  Example: 999.9.
        promised_date (Union[Unset, datetime.date]):  Example: 2024-01-20.
        po_line_id (Union[Unset, str]): PO line identifier Example: PO_LINE_001.
        quantity_backordered (Union[Unset, float]): Quantity on backorder Default: 0.0.
        quantity_canceled (Union[Unset, float]): Quantity canceled Default: 0.0.
        unit_of_measure (Union[Unset, str]): Unit of measure Example: EA.
        ship_to_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        tax_details (Union[Unset, list['TaxDetail']]): Line-level tax details
        schedule_lines (Union[Unset, list['ERPOrderLinesItemScheduleLinesItem']]): Delivery schedule lines
        custom_fields (Union[Unset, ERPOrderLinesItemCustomFields]): Line-specific custom fields
    """

    line_number: Union[Unset, float] = UNSET
    sku: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    quantity_ordered: Union[Unset, float] = UNSET
    unit_price: Union[Unset, float] = UNSET
    line_total: Union[Unset, float] = UNSET
    promised_date: Union[Unset, datetime.date] = UNSET
    po_line_id: Union[Unset, str] = UNSET
    quantity_backordered: Union[Unset, float] = 0.0
    quantity_canceled: Union[Unset, float] = 0.0
    unit_of_measure: Union[Unset, str] = UNSET
    ship_to_address: Union[Unset, "Address"] = UNSET
    tax_details: Union[Unset, list["TaxDetail"]] = UNSET
    schedule_lines: Union[Unset, list["ERPOrderLinesItemScheduleLinesItem"]] = UNSET
    custom_fields: Union[Unset, "ERPOrderLinesItemCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        sku = self.sku

        description = self.description

        quantity_ordered = self.quantity_ordered

        unit_price = self.unit_price

        line_total = self.line_total

        promised_date: Union[Unset, str] = UNSET
        if not isinstance(self.promised_date, Unset):
            promised_date = self.promised_date.isoformat()

        po_line_id = self.po_line_id

        quantity_backordered = self.quantity_backordered

        quantity_canceled = self.quantity_canceled

        unit_of_measure = self.unit_of_measure

        ship_to_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ship_to_address, Unset):
            ship_to_address = self.ship_to_address.to_dict()

        tax_details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.tax_details, Unset):
            tax_details = []
            for tax_details_item_data in self.tax_details:
                tax_details_item = tax_details_item_data.to_dict()
                tax_details.append(tax_details_item)

        schedule_lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.schedule_lines, Unset):
            schedule_lines = []
            for schedule_lines_item_data in self.schedule_lines:
                schedule_lines_item = schedule_lines_item_data.to_dict()
                schedule_lines.append(schedule_lines_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if sku is not UNSET:
            field_dict["sku"] = sku
        if description is not UNSET:
            field_dict["description"] = description
        if quantity_ordered is not UNSET:
            field_dict["quantityOrdered"] = quantity_ordered
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if line_total is not UNSET:
            field_dict["lineTotal"] = line_total
        if promised_date is not UNSET:
            field_dict["promisedDate"] = promised_date
        if po_line_id is not UNSET:
            field_dict["poLineId"] = po_line_id
        if quantity_backordered is not UNSET:
            field_dict["quantityBackordered"] = quantity_backordered
        if quantity_canceled is not UNSET:
            field_dict["quantityCanceled"] = quantity_canceled
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if ship_to_address is not UNSET:
            field_dict["shipToAddress"] = ship_to_address
        if tax_details is not UNSET:
            field_dict["taxDetails"] = tax_details
        if schedule_lines is not UNSET:
            field_dict["scheduleLines"] = schedule_lines
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.erp_order_lines_item_custom_fields import ERPOrderLinesItemCustomFields
        from ..models.erp_order_lines_item_schedule_lines_item import ERPOrderLinesItemScheduleLinesItem
        from ..models.tax_detail import TaxDetail

        d = dict(src_dict)
        line_number = d.pop("lineNumber", UNSET)

        sku = d.pop("sku", UNSET)

        description = d.pop("description", UNSET)

        quantity_ordered = d.pop("quantityOrdered", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        line_total = d.pop("lineTotal", UNSET)

        _promised_date = d.pop("promisedDate", UNSET)
        promised_date: Union[Unset, datetime.date]
        if isinstance(_promised_date, Unset):
            promised_date = UNSET
        else:
            promised_date = isoparse(_promised_date).date()

        po_line_id = d.pop("poLineId", UNSET)

        quantity_backordered = d.pop("quantityBackordered", UNSET)

        quantity_canceled = d.pop("quantityCanceled", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        _ship_to_address = d.pop("shipToAddress", UNSET)
        ship_to_address: Union[Unset, Address]
        if isinstance(_ship_to_address, Unset):
            ship_to_address = UNSET
        else:
            ship_to_address = Address.from_dict(_ship_to_address)

        tax_details = []
        _tax_details = d.pop("taxDetails", UNSET)
        for tax_details_item_data in _tax_details or []:
            tax_details_item = TaxDetail.from_dict(tax_details_item_data)

            tax_details.append(tax_details_item)

        schedule_lines = []
        _schedule_lines = d.pop("scheduleLines", UNSET)
        for schedule_lines_item_data in _schedule_lines or []:
            schedule_lines_item = ERPOrderLinesItemScheduleLinesItem.from_dict(schedule_lines_item_data)

            schedule_lines.append(schedule_lines_item)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPOrderLinesItemCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPOrderLinesItemCustomFields.from_dict(_custom_fields)

        erp_order_lines_item = cls(
            line_number=line_number,
            sku=sku,
            description=description,
            quantity_ordered=quantity_ordered,
            unit_price=unit_price,
            line_total=line_total,
            promised_date=promised_date,
            po_line_id=po_line_id,
            quantity_backordered=quantity_backordered,
            quantity_canceled=quantity_canceled,
            unit_of_measure=unit_of_measure,
            ship_to_address=ship_to_address,
            tax_details=tax_details,
            schedule_lines=schedule_lines,
            custom_fields=custom_fields,
        )

        erp_order_lines_item.additional_properties = d
        return erp_order_lines_item

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
