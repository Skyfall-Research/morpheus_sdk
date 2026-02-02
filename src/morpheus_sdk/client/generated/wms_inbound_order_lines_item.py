import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_inbound_order_lines_item_line_status import WMSInboundOrderLinesItemLineStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSInboundOrderLinesItem")


@_attrs_define
class WMSInboundOrderLinesItem:
    """
    Attributes:
        line_number (Union[Unset, float]): Sequential line number for tracking and identification Example: 1.
        product_id (Union[Unset, str]): Product identifier from catalog for inventory management Example: PROD-
            WIDGET-001.
        sku (Union[Unset, str]): Stock keeping unit identifier for operational reference Example: SKU-WDG-BLU-SM.
        product_name (Union[Unset, str]): Human-readable product name for identification Example: Blue Widget Small.
        expected_quantity (Union[Unset, float]): Expected quantity to receive for planning and verification Example:
            300.
        received_quantity (Union[Unset, float]): Actual quantity received for progress tracking Example: 300.
        uom (Union[Unset, str]): Unit of measure (EA, CS, PLT, etc.) for quantity specification Example: EA.
        lot_number (Union[None, Unset, str]): Lot number for batch tracking and traceability compliance Example:
            LOT-2024-W47.
        expiration_date (Union[None, Unset, datetime.datetime]): Product expiration date for perishable item management
            Example: 2025-11-27T00:00:00Z.
        line_status (Union[Unset, WMSInboundOrderLinesItemLineStatus]): Current status of this specific product line
            Example: RECEIVED.
    """

    line_number: Union[Unset, float] = UNSET
    product_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    expected_quantity: Union[Unset, float] = UNSET
    received_quantity: Union[Unset, float] = UNSET
    uom: Union[Unset, str] = UNSET
    lot_number: Union[None, Unset, str] = UNSET
    expiration_date: Union[None, Unset, datetime.datetime] = UNSET
    line_status: Union[Unset, WMSInboundOrderLinesItemLineStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        product_id = self.product_id

        sku = self.sku

        product_name = self.product_name

        expected_quantity = self.expected_quantity

        received_quantity = self.received_quantity

        uom = self.uom

        lot_number: Union[None, Unset, str]
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        expiration_date: Union[None, Unset, str]
        if isinstance(self.expiration_date, Unset):
            expiration_date = UNSET
        elif isinstance(self.expiration_date, datetime.datetime):
            expiration_date = self.expiration_date.isoformat()
        else:
            expiration_date = self.expiration_date

        line_status: Union[Unset, str] = UNSET
        if not isinstance(self.line_status, Unset):
            line_status = self.line_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if expected_quantity is not UNSET:
            field_dict["expectedQuantity"] = expected_quantity
        if received_quantity is not UNSET:
            field_dict["receivedQuantity"] = received_quantity
        if uom is not UNSET:
            field_dict["uom"] = uom
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if line_status is not UNSET:
            field_dict["lineStatus"] = line_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("lineNumber", UNSET)

        product_id = d.pop("productId", UNSET)

        sku = d.pop("sku", UNSET)

        product_name = d.pop("productName", UNSET)

        expected_quantity = d.pop("expectedQuantity", UNSET)

        received_quantity = d.pop("receivedQuantity", UNSET)

        uom = d.pop("uom", UNSET)

        def _parse_lot_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))

        def _parse_expiration_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expiration_date_type_0 = isoparse(data)

                return expiration_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        expiration_date = _parse_expiration_date(d.pop("expirationDate", UNSET))

        _line_status = d.pop("lineStatus", UNSET)
        line_status: Union[Unset, WMSInboundOrderLinesItemLineStatus]
        if isinstance(_line_status, Unset):
            line_status = UNSET
        else:
            line_status = WMSInboundOrderLinesItemLineStatus(_line_status)

        wms_inbound_order_lines_item = cls(
            line_number=line_number,
            product_id=product_id,
            sku=sku,
            product_name=product_name,
            expected_quantity=expected_quantity,
            received_quantity=received_quantity,
            uom=uom,
            lot_number=lot_number,
            expiration_date=expiration_date,
            line_status=line_status,
        )

        wms_inbound_order_lines_item.additional_properties = d
        return wms_inbound_order_lines_item

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
