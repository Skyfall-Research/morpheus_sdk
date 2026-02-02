import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateERPOrderBodyLinesItem")


@_attrs_define
class CreateERPOrderBodyLinesItem:
    """
    Attributes:
        line_number (float): Line item sequence number Example: 1.
        sku (str): Product SKU identifier Example: PROD_WIDGET_001.
        quantity_ordered (float): Quantity ordered Example: 10.
        description (Union[Unset, str]): Line item description Example: Premium Widget - Blue.
        unit_price (Union[Unset, float]): Unit price per item Example: 99.99.
        line_total (Union[Unset, float]): Total line amount Example: 999.9.
        promised_date (Union[Unset, datetime.date]): Promised delivery date for this line Example: 2024-01-20.
    """

    line_number: float
    sku: str
    quantity_ordered: float
    description: Union[Unset, str] = UNSET
    unit_price: Union[Unset, float] = UNSET
    line_total: Union[Unset, float] = UNSET
    promised_date: Union[Unset, datetime.date] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        sku = self.sku

        quantity_ordered = self.quantity_ordered

        description = self.description

        unit_price = self.unit_price

        line_total = self.line_total

        promised_date: Union[Unset, str] = UNSET
        if not isinstance(self.promised_date, Unset):
            promised_date = self.promised_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNumber": line_number,
                "sku": sku,
                "quantityOrdered": quantity_ordered,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if unit_price is not UNSET:
            field_dict["unitPrice"] = unit_price
        if line_total is not UNSET:
            field_dict["lineTotal"] = line_total
        if promised_date is not UNSET:
            field_dict["promisedDate"] = promised_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("lineNumber")

        sku = d.pop("sku")

        quantity_ordered = d.pop("quantityOrdered")

        description = d.pop("description", UNSET)

        unit_price = d.pop("unitPrice", UNSET)

        line_total = d.pop("lineTotal", UNSET)

        _promised_date = d.pop("promisedDate", UNSET)
        promised_date: Union[Unset, datetime.date]
        if isinstance(_promised_date, Unset):
            promised_date = UNSET
        else:
            promised_date = isoparse(_promised_date).date()

        create_erp_order_body_lines_item = cls(
            line_number=line_number,
            sku=sku,
            quantity_ordered=quantity_ordered,
            description=description,
            unit_price=unit_price,
            line_total=line_total,
            promised_date=promised_date,
        )

        create_erp_order_body_lines_item.additional_properties = d
        return create_erp_order_body_lines_item

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
