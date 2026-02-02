import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSInboundOrderBodyLinesItem")


@_attrs_define
class CreateWMSInboundOrderBodyLinesItem:
    """
    Attributes:
        product_id (str): Product identifier from catalog Example: PROD-WIDGET-001.
        expected_quantity (float): Expected quantity to receive Example: 300.
        line_number (Union[Unset, float]): Sequential line number for tracking Example: 1.
        sku (Union[Unset, str]): Stock keeping unit identifier Example: SKU-WDG-BLU-SM.
        product_name (Union[Unset, str]): Human-readable product name Example: Blue Widget Small.
        uom (Union[Unset, str]): Unit of measure (EA, CS, PLT, etc.) Example: EA.
        lot_number (Union[Unset, str]): Lot number for batch tracking Example: LOT-2024-W47.
        expiration_date (Union[Unset, datetime.datetime]): Product expiration date Example: 2025-11-27T00:00:00Z.
    """

    product_id: str
    expected_quantity: float
    line_number: Union[Unset, float] = UNSET
    sku: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    uom: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        expected_quantity = self.expected_quantity

        line_number = self.line_number

        sku = self.sku

        product_name = self.product_name

        uom = self.uom

        lot_number = self.lot_number

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "productId": product_id,
                "expectedQuantity": expected_quantity,
            }
        )
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if sku is not UNSET:
            field_dict["sku"] = sku
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if uom is not UNSET:
            field_dict["uom"] = uom
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("productId")

        expected_quantity = d.pop("expectedQuantity")

        line_number = d.pop("lineNumber", UNSET)

        sku = d.pop("sku", UNSET)

        product_name = d.pop("productName", UNSET)

        uom = d.pop("uom", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        create_wms_inbound_order_body_lines_item = cls(
            product_id=product_id,
            expected_quantity=expected_quantity,
            line_number=line_number,
            sku=sku,
            product_name=product_name,
            uom=uom,
            lot_number=lot_number,
            expiration_date=expiration_date,
        )

        create_wms_inbound_order_body_lines_item.additional_properties = d
        return create_wms_inbound_order_body_lines_item

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
