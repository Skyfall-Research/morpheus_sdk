from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_inbound_order_body_order_type import CreateWMSInboundOrderBodyOrderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_inbound_order_body_dates import CreateWMSInboundOrderBodyDates
    from ..models.create_wms_inbound_order_body_lines_item import CreateWMSInboundOrderBodyLinesItem
    from ..models.create_wms_inbound_order_body_totals import CreateWMSInboundOrderBodyTotals
    from ..models.create_wms_inbound_order_body_vendor import CreateWMSInboundOrderBodyVendor


T = TypeVar("T", bound="CreateWMSInboundOrderBody")


@_attrs_define
class CreateWMSInboundOrderBody:
    """
    Example:
        {'warehouseId': 'wms_warehouse_674565c1234567890abcdef', 'poNumber': 'PO-2024-001234', 'asnNumber': 'ASN-
            VND001-20241127', 'vendor': {'vendorId': 'VND-SWIFT-001', 'vendorName': 'Swift Manufacturing Co.',
            'contactEmail': 'receiving@swift-mfg.com', 'contactPhone': '+1-555-0123'}, 'orderType': 'PO', 'dates':
            {'expectedArrival': '2024-11-28T10:00:00Z'}, 'appointmentId': 'tms_appointment_674565c1234567890abcdef',
            'totals': {'pallets': 5, 'cases': 120, 'units': 2400, 'expectedLines': 8}, 'lines': [{'lineNumber': 1,
            'productId': 'PROD-WIDGET-001', 'sku': 'SKU-WDG-BLU-SM', 'productName': 'Blue Widget Small', 'expectedQuantity':
            300, 'uom': 'EA', 'lotNumber': 'LOT-2024-W47', 'expirationDate': '2025-11-27T00:00:00Z'}], 'receivingNotes':
            'Handle with care - fragile items. Check lot numbers carefully.'}

    Attributes:
        warehouse_id (str): Warehouse identifier where inventory will be received Example:
            wms_warehouse_674565c1234567890abcdef.
        lines (list['CreateWMSInboundOrderBodyLinesItem']): Product line items with receiving specifications
        po_number (Union[Unset, str]): Purchase order number for ERP integration Example: PO-2024-001234.
        asn_number (Union[Unset, str]): Advanced Ship Notice number from vendor Example: ASN-VND001-20241127.
        vendor (Union[Unset, CreateWMSInboundOrderBodyVendor]): Vendor information and contact details
        order_type (Union[Unset, CreateWMSInboundOrderBodyOrderType]): Type of inbound order for processing workflow
            Example: PO.
        dates (Union[Unset, CreateWMSInboundOrderBodyDates]): Important dates for receiving coordination
        appointment_id (Union[Unset, str]): Associated appointment ID for dock scheduling Example:
            tms_appointment_674565c1234567890abcdef.
        totals (Union[Unset, CreateWMSInboundOrderBodyTotals]): Order totals for capacity planning
        receiving_notes (Union[Unset, str]): Special instructions for receiving team Example: Handle with care - fragile
            items. Check lot numbers carefully..
    """

    warehouse_id: str
    lines: list["CreateWMSInboundOrderBodyLinesItem"]
    po_number: Union[Unset, str] = UNSET
    asn_number: Union[Unset, str] = UNSET
    vendor: Union[Unset, "CreateWMSInboundOrderBodyVendor"] = UNSET
    order_type: Union[Unset, CreateWMSInboundOrderBodyOrderType] = UNSET
    dates: Union[Unset, "CreateWMSInboundOrderBodyDates"] = UNSET
    appointment_id: Union[Unset, str] = UNSET
    totals: Union[Unset, "CreateWMSInboundOrderBodyTotals"] = UNSET
    receiving_notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        po_number = self.po_number

        asn_number = self.asn_number

        vendor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.vendor, Unset):
            vendor = self.vendor.to_dict()

        order_type: Union[Unset, str] = UNSET
        if not isinstance(self.order_type, Unset):
            order_type = self.order_type.value

        dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        appointment_id = self.appointment_id

        totals: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        receiving_notes = self.receiving_notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "lines": lines,
            }
        )
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number
        if asn_number is not UNSET:
            field_dict["asnNumber"] = asn_number
        if vendor is not UNSET:
            field_dict["vendor"] = vendor
        if order_type is not UNSET:
            field_dict["orderType"] = order_type
        if dates is not UNSET:
            field_dict["dates"] = dates
        if appointment_id is not UNSET:
            field_dict["appointmentId"] = appointment_id
        if totals is not UNSET:
            field_dict["totals"] = totals
        if receiving_notes is not UNSET:
            field_dict["receivingNotes"] = receiving_notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_inbound_order_body_dates import CreateWMSInboundOrderBodyDates
        from ..models.create_wms_inbound_order_body_lines_item import CreateWMSInboundOrderBodyLinesItem
        from ..models.create_wms_inbound_order_body_totals import CreateWMSInboundOrderBodyTotals
        from ..models.create_wms_inbound_order_body_vendor import CreateWMSInboundOrderBodyVendor

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = CreateWMSInboundOrderBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        po_number = d.pop("poNumber", UNSET)

        asn_number = d.pop("asnNumber", UNSET)

        _vendor = d.pop("vendor", UNSET)
        vendor: Union[Unset, CreateWMSInboundOrderBodyVendor]
        if isinstance(_vendor, Unset):
            vendor = UNSET
        else:
            vendor = CreateWMSInboundOrderBodyVendor.from_dict(_vendor)

        _order_type = d.pop("orderType", UNSET)
        order_type: Union[Unset, CreateWMSInboundOrderBodyOrderType]
        if isinstance(_order_type, Unset):
            order_type = UNSET
        else:
            order_type = CreateWMSInboundOrderBodyOrderType(_order_type)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, CreateWMSInboundOrderBodyDates]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = CreateWMSInboundOrderBodyDates.from_dict(_dates)

        appointment_id = d.pop("appointmentId", UNSET)

        _totals = d.pop("totals", UNSET)
        totals: Union[Unset, CreateWMSInboundOrderBodyTotals]
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = CreateWMSInboundOrderBodyTotals.from_dict(_totals)

        receiving_notes = d.pop("receivingNotes", UNSET)

        create_wms_inbound_order_body = cls(
            warehouse_id=warehouse_id,
            lines=lines,
            po_number=po_number,
            asn_number=asn_number,
            vendor=vendor,
            order_type=order_type,
            dates=dates,
            appointment_id=appointment_id,
            totals=totals,
            receiving_notes=receiving_notes,
        )

        create_wms_inbound_order_body.additional_properties = d
        return create_wms_inbound_order_body

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
