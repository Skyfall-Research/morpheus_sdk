import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_inbound_order_order_status import WMSInboundOrderOrderStatus
from ..models.wms_inbound_order_order_type import WMSInboundOrderOrderType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_inbound_order_custom_fields import WMSInboundOrderCustomFields
    from ..models.wms_inbound_order_dates_type_0 import WMSInboundOrderDatesType0
    from ..models.wms_inbound_order_lines_item import WMSInboundOrderLinesItem
    from ..models.wms_inbound_order_totals_type_0 import WMSInboundOrderTotalsType0
    from ..models.wms_inbound_order_vendor_type_0 import WMSInboundOrderVendorType0
    from ..models.wms_inbound_order_world_ref import WMSInboundOrderWorldRef


T = TypeVar("T", bound="WMSInboundOrder")


@_attrs_define
class WMSInboundOrder:
    """Complete inbound order for receiving inventory into the warehouse with vendor coordination and line-item tracking

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str): Unique identifier for the inbound order, auto-generated using WMS service prefix
            Example: wms_inbound-order_674565c1234567890abcdef.
        warehouse_id (str): Warehouse identifier where inventory will be received Example:
            wms_warehouse_674565c1234567890abcdef.
        order_status (WMSInboundOrderOrderStatus): Current operational status affecting receiving operations Example:
            EXPECTED.
        lines (list['WMSInboundOrderLinesItem']): Product line items with receiving specifications and progress tracking
        world_ref (WMSInboundOrderWorldRef): Reference to the world environment containing this inbound order
        created_at (datetime.datetime): Timestamp when the inbound order record was created Example:
            2024-11-27T10:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the inbound order record was last updated Example:
            2024-11-27T15:30:00.000Z.
        po_number (Union[None, Unset, str]): Purchase order number for ERP integration and vendor coordination Example:
            PO-2024-001234.
        asn_number (Union[None, Unset, str]): Advanced Ship Notice number from vendor for delivery coordination Example:
            ASN-VND001-20241127.
        vendor (Union['WMSInboundOrderVendorType0', None, Unset]): Complete vendor information and contact details for
            coordination
        order_type (Union[Unset, WMSInboundOrderOrderType]): Type of inbound order determining processing workflow
            Example: PO.
        dates (Union['WMSInboundOrderDatesType0', None, Unset]): Important dates for receiving coordination and timeline
            tracking
        appointment_id (Union[None, Unset, str]): Associated appointment ID for dock scheduling coordination Example:
            tms_appointment_674565c1234567890abcdef.
        totals (Union['WMSInboundOrderTotalsType0', None, Unset]): Order totals for capacity planning and resource
            allocation
        receiving_notes (Union[None, Unset, str]): Special instructions and notes for receiving team coordination
            Example: Handle with care - fragile items. Check lot numbers carefully..
        damage_report (Union[None, Unset, str]): Documentation of any damage found during receiving Example: Minor
            packaging damage on 3 units, product integrity maintained..
        custom_fields (Union[Unset, WMSInboundOrderCustomFields]): Additional order-specific configuration and
            operational data Example: {'priority': 'HIGH', 'specialHandling': 'FRAGILE', 'temperatureRequired': 'AMBIENT',
            'qualityInspectionRequired': True, 'crossDockCandidate': False, 'carrierInstructions': 'Call 30 minutes before
            arrival'}.
    """

    field_id: str
    inbound_order_id: str
    warehouse_id: str
    order_status: WMSInboundOrderOrderStatus
    lines: list["WMSInboundOrderLinesItem"]
    world_ref: "WMSInboundOrderWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    po_number: Union[None, Unset, str] = UNSET
    asn_number: Union[None, Unset, str] = UNSET
    vendor: Union["WMSInboundOrderVendorType0", None, Unset] = UNSET
    order_type: Union[Unset, WMSInboundOrderOrderType] = UNSET
    dates: Union["WMSInboundOrderDatesType0", None, Unset] = UNSET
    appointment_id: Union[None, Unset, str] = UNSET
    totals: Union["WMSInboundOrderTotalsType0", None, Unset] = UNSET
    receiving_notes: Union[None, Unset, str] = UNSET
    damage_report: Union[None, Unset, str] = UNSET
    custom_fields: Union[Unset, "WMSInboundOrderCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wms_inbound_order_dates_type_0 import WMSInboundOrderDatesType0
        from ..models.wms_inbound_order_totals_type_0 import WMSInboundOrderTotalsType0
        from ..models.wms_inbound_order_vendor_type_0 import WMSInboundOrderVendorType0

        field_id = self.field_id

        inbound_order_id = self.inbound_order_id

        warehouse_id = self.warehouse_id

        order_status = self.order_status.value

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        po_number: Union[None, Unset, str]
        if isinstance(self.po_number, Unset):
            po_number = UNSET
        else:
            po_number = self.po_number

        asn_number: Union[None, Unset, str]
        if isinstance(self.asn_number, Unset):
            asn_number = UNSET
        else:
            asn_number = self.asn_number

        vendor: Union[None, Unset, dict[str, Any]]
        if isinstance(self.vendor, Unset):
            vendor = UNSET
        elif isinstance(self.vendor, WMSInboundOrderVendorType0):
            vendor = self.vendor.to_dict()
        else:
            vendor = self.vendor

        order_type: Union[Unset, str] = UNSET
        if not isinstance(self.order_type, Unset):
            order_type = self.order_type.value

        dates: Union[None, Unset, dict[str, Any]]
        if isinstance(self.dates, Unset):
            dates = UNSET
        elif isinstance(self.dates, WMSInboundOrderDatesType0):
            dates = self.dates.to_dict()
        else:
            dates = self.dates

        appointment_id: Union[None, Unset, str]
        if isinstance(self.appointment_id, Unset):
            appointment_id = UNSET
        else:
            appointment_id = self.appointment_id

        totals: Union[None, Unset, dict[str, Any]]
        if isinstance(self.totals, Unset):
            totals = UNSET
        elif isinstance(self.totals, WMSInboundOrderTotalsType0):
            totals = self.totals.to_dict()
        else:
            totals = self.totals

        receiving_notes: Union[None, Unset, str]
        if isinstance(self.receiving_notes, Unset):
            receiving_notes = UNSET
        else:
            receiving_notes = self.receiving_notes

        damage_report: Union[None, Unset, str]
        if isinstance(self.damage_report, Unset):
            damage_report = UNSET
        else:
            damage_report = self.damage_report

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "inboundOrderId": inbound_order_id,
                "warehouseId": warehouse_id,
                "orderStatus": order_status,
                "lines": lines,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
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
        if damage_report is not UNSET:
            field_dict["damageReport"] = damage_report
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_inbound_order_custom_fields import WMSInboundOrderCustomFields
        from ..models.wms_inbound_order_dates_type_0 import WMSInboundOrderDatesType0
        from ..models.wms_inbound_order_lines_item import WMSInboundOrderLinesItem
        from ..models.wms_inbound_order_totals_type_0 import WMSInboundOrderTotalsType0
        from ..models.wms_inbound_order_vendor_type_0 import WMSInboundOrderVendorType0
        from ..models.wms_inbound_order_world_ref import WMSInboundOrderWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        inbound_order_id = d.pop("inboundOrderId")

        warehouse_id = d.pop("warehouseId")

        order_status = WMSInboundOrderOrderStatus(d.pop("orderStatus"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = WMSInboundOrderLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        world_ref = WMSInboundOrderWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_po_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        po_number = _parse_po_number(d.pop("poNumber", UNSET))

        def _parse_asn_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        asn_number = _parse_asn_number(d.pop("asnNumber", UNSET))

        def _parse_vendor(data: object) -> Union["WMSInboundOrderVendorType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                vendor_type_0 = WMSInboundOrderVendorType0.from_dict(data)

                return vendor_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSInboundOrderVendorType0", None, Unset], data)

        vendor = _parse_vendor(d.pop("vendor", UNSET))

        _order_type = d.pop("orderType", UNSET)
        order_type: Union[Unset, WMSInboundOrderOrderType]
        if isinstance(_order_type, Unset):
            order_type = UNSET
        else:
            order_type = WMSInboundOrderOrderType(_order_type)

        def _parse_dates(data: object) -> Union["WMSInboundOrderDatesType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                dates_type_0 = WMSInboundOrderDatesType0.from_dict(data)

                return dates_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSInboundOrderDatesType0", None, Unset], data)

        dates = _parse_dates(d.pop("dates", UNSET))

        def _parse_appointment_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        appointment_id = _parse_appointment_id(d.pop("appointmentId", UNSET))

        def _parse_totals(data: object) -> Union["WMSInboundOrderTotalsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                totals_type_0 = WMSInboundOrderTotalsType0.from_dict(data)

                return totals_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSInboundOrderTotalsType0", None, Unset], data)

        totals = _parse_totals(d.pop("totals", UNSET))

        def _parse_receiving_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        receiving_notes = _parse_receiving_notes(d.pop("receivingNotes", UNSET))

        def _parse_damage_report(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        damage_report = _parse_damage_report(d.pop("damageReport", UNSET))

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSInboundOrderCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSInboundOrderCustomFields.from_dict(_custom_fields)

        wms_inbound_order = cls(
            field_id=field_id,
            inbound_order_id=inbound_order_id,
            warehouse_id=warehouse_id,
            order_status=order_status,
            lines=lines,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            po_number=po_number,
            asn_number=asn_number,
            vendor=vendor,
            order_type=order_type,
            dates=dates,
            appointment_id=appointment_id,
            totals=totals,
            receiving_notes=receiving_notes,
            damage_report=damage_report,
            custom_fields=custom_fields,
        )

        wms_inbound_order.additional_properties = d
        return wms_inbound_order

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
