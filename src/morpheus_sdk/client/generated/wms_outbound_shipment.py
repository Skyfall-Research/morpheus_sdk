import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_outbound_shipment_shipment_status import WMSOutboundShipmentShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_outbound_shipment_carrier import WMSOutboundShipmentCarrier
    from ..models.wms_outbound_shipment_custom_fields import WMSOutboundShipmentCustomFields
    from ..models.wms_outbound_shipment_dates import WMSOutboundShipmentDates
    from ..models.wms_outbound_shipment_documents_item import WMSOutboundShipmentDocumentsItem
    from ..models.wms_outbound_shipment_events_item import WMSOutboundShipmentEventsItem
    from ..models.wms_outbound_shipment_from_address import WMSOutboundShipmentFromAddress
    from ..models.wms_outbound_shipment_lines_item import WMSOutboundShipmentLinesItem
    from ..models.wms_outbound_shipment_orders_item import WMSOutboundShipmentOrdersItem
    from ..models.wms_outbound_shipment_to_address import WMSOutboundShipmentToAddress
    from ..models.wms_outbound_shipment_totals import WMSOutboundShipmentTotals
    from ..models.wms_outbound_shipment_world_ref import WMSOutboundShipmentWorldRef


T = TypeVar("T", bound="WMSOutboundShipment")


@_attrs_define
class WMSOutboundShipment:
    """
    **Complete WMS Outbound Shipment Schema**

    Comprehensive outbound shipment management with multi-carrier support, tracking integration, and logistics workflow.

    **Key Features:**
    - Multi-line shipment support with order references and line-level details
    - Carrier integration with SCAC codes, modes, and service levels
    - Comprehensive address management for origin and destination
    - Status workflow tracking from creation to delivery
    - Event-driven tracking with timestamps and location data
    - Document management for shipping documentation
    - Performance analytics and metrics tracking

    **Field Consistency Verified:**
    - Primary identifier: `shipmentId` (consistent across model, controller, repository)
    - Status field: `shipmentStatus` (enum-driven workflow)
    - All repository methods align with controller parameter expectations

    **🚨 CRITICAL BUGS DOCUMENTED:**
    1. Route parameter missing in ready-to-ship endpoint
    2. Field mapping issue in warehouse filtering (status vs shipmentStatus)

    **Status Workflow:**
    CREATED → MANIFESTED → LOADING → LOADED → SHIPPED → IN_TRANSIT → DELIVERED


        Attributes:
            field_id (str): MongoDB auto-generated primary key Example: 674565c1234567890abcdef0.
            shipment_id (str): Business shipment identifier (consistent naming verified across all components) Example:
                SHIP-2024-001234.
            world_ref (WMSOutboundShipmentWorldRef): Multi-tenant world reference for data isolation
            warehouse_id (str): Required source warehouse identifier (validated in repository) Example: WH-MAIN-001.
            shipment_status (WMSOutboundShipmentShipmentStatus): Current shipment state in logistics workflow Example:
                SHIPPED.
            lines (list['WMSOutboundShipmentLinesItem']): Shipment line items with order references (required, validated
                length > 0 in repository)
            to_address (WMSOutboundShipmentToAddress): Required destination address (validated in repository)
            created_at (datetime.datetime): Document creation timestamp Example: 2024-12-01T09:00:00.000Z.
            updated_at (datetime.datetime): Last modification timestamp Example: 2024-12-01T16:00:00.000Z.
            carrier (Union[Unset, WMSOutboundShipmentCarrier]): Carrier information for transportation
            service_level (Union[Unset, str]): Carrier service level (GROUND, EXPRESS, etc.) Example: GROUND.
            tracking_number (Union[Unset, str]): Carrier tracking number for customer visibility Example: 1Z999AA1234567890.
            trailer_number (Union[Unset, str]): Trailer identifier for LTL/TL shipments Example: TRL-001.
            dock_door_id (Union[Unset, str]): Assigned dock door for loading operations Example: DOCK-A-001.
            orders (Union[Unset, list['WMSOutboundShipmentOrdersItem']]): Orders consolidated in this shipment
            totals (Union[Unset, WMSOutboundShipmentTotals]): Shipment totals and logistics metrics
            dates (Union[Unset, WMSOutboundShipmentDates]): Logistics timeline and delivery requirements
            from_address (Union[Unset, WMSOutboundShipmentFromAddress]): Origin address (typically warehouse)
            documents (Union[Unset, list['WMSOutboundShipmentDocumentsItem']]): Shipment documentation and attachments
            events (Union[Unset, list['WMSOutboundShipmentEventsItem']]): Tracking event history (updated via
                addTrackingEvent)
            custom_fields (Union[Unset, WMSOutboundShipmentCustomFields]): Additional shipment-specific attributes Example:
                {'expedited': True, 'specialHandling': 'FRAGILE', 'customerReference': 'PO-12345'}.
    """

    field_id: str
    shipment_id: str
    world_ref: "WMSOutboundShipmentWorldRef"
    warehouse_id: str
    shipment_status: WMSOutboundShipmentShipmentStatus
    lines: list["WMSOutboundShipmentLinesItem"]
    to_address: "WMSOutboundShipmentToAddress"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    carrier: Union[Unset, "WMSOutboundShipmentCarrier"] = UNSET
    service_level: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    trailer_number: Union[Unset, str] = UNSET
    dock_door_id: Union[Unset, str] = UNSET
    orders: Union[Unset, list["WMSOutboundShipmentOrdersItem"]] = UNSET
    totals: Union[Unset, "WMSOutboundShipmentTotals"] = UNSET
    dates: Union[Unset, "WMSOutboundShipmentDates"] = UNSET
    from_address: Union[Unset, "WMSOutboundShipmentFromAddress"] = UNSET
    documents: Union[Unset, list["WMSOutboundShipmentDocumentsItem"]] = UNSET
    events: Union[Unset, list["WMSOutboundShipmentEventsItem"]] = UNSET
    custom_fields: Union[Unset, "WMSOutboundShipmentCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        shipment_id = self.shipment_id

        world_ref = self.world_ref.to_dict()

        warehouse_id = self.warehouse_id

        shipment_status = self.shipment_status.value

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        to_address = self.to_address.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        carrier: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier, Unset):
            carrier = self.carrier.to_dict()

        service_level = self.service_level

        tracking_number = self.tracking_number

        trailer_number = self.trailer_number

        dock_door_id = self.dock_door_id

        orders: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = []
            for orders_item_data in self.orders:
                orders_item = orders_item_data.to_dict()
                orders.append(orders_item)

        totals: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        from_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_address, Unset):
            from_address = self.from_address.to_dict()

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "shipmentId": shipment_id,
                "worldRef": world_ref,
                "warehouseId": warehouse_id,
                "shipmentStatus": shipment_status,
                "lines": lines,
                "toAddress": to_address,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if service_level is not UNSET:
            field_dict["serviceLevel"] = service_level
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if trailer_number is not UNSET:
            field_dict["trailerNumber"] = trailer_number
        if dock_door_id is not UNSET:
            field_dict["dockDoorId"] = dock_door_id
        if orders is not UNSET:
            field_dict["orders"] = orders
        if totals is not UNSET:
            field_dict["totals"] = totals
        if dates is not UNSET:
            field_dict["dates"] = dates
        if from_address is not UNSET:
            field_dict["fromAddress"] = from_address
        if documents is not UNSET:
            field_dict["documents"] = documents
        if events is not UNSET:
            field_dict["events"] = events
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_outbound_shipment_carrier import WMSOutboundShipmentCarrier
        from ..models.wms_outbound_shipment_custom_fields import WMSOutboundShipmentCustomFields
        from ..models.wms_outbound_shipment_dates import WMSOutboundShipmentDates
        from ..models.wms_outbound_shipment_documents_item import WMSOutboundShipmentDocumentsItem
        from ..models.wms_outbound_shipment_events_item import WMSOutboundShipmentEventsItem
        from ..models.wms_outbound_shipment_from_address import WMSOutboundShipmentFromAddress
        from ..models.wms_outbound_shipment_lines_item import WMSOutboundShipmentLinesItem
        from ..models.wms_outbound_shipment_orders_item import WMSOutboundShipmentOrdersItem
        from ..models.wms_outbound_shipment_to_address import WMSOutboundShipmentToAddress
        from ..models.wms_outbound_shipment_totals import WMSOutboundShipmentTotals
        from ..models.wms_outbound_shipment_world_ref import WMSOutboundShipmentWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        shipment_id = d.pop("shipmentId")

        world_ref = WMSOutboundShipmentWorldRef.from_dict(d.pop("worldRef"))

        warehouse_id = d.pop("warehouseId")

        shipment_status = WMSOutboundShipmentShipmentStatus(d.pop("shipmentStatus"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = WMSOutboundShipmentLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        to_address = WMSOutboundShipmentToAddress.from_dict(d.pop("toAddress"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _carrier = d.pop("carrier", UNSET)
        carrier: Union[Unset, WMSOutboundShipmentCarrier]
        if isinstance(_carrier, Unset):
            carrier = UNSET
        else:
            carrier = WMSOutboundShipmentCarrier.from_dict(_carrier)

        service_level = d.pop("serviceLevel", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        trailer_number = d.pop("trailerNumber", UNSET)

        dock_door_id = d.pop("dockDoorId", UNSET)

        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = WMSOutboundShipmentOrdersItem.from_dict(orders_item_data)

            orders.append(orders_item)

        _totals = d.pop("totals", UNSET)
        totals: Union[Unset, WMSOutboundShipmentTotals]
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = WMSOutboundShipmentTotals.from_dict(_totals)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, WMSOutboundShipmentDates]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = WMSOutboundShipmentDates.from_dict(_dates)

        _from_address = d.pop("fromAddress", UNSET)
        from_address: Union[Unset, WMSOutboundShipmentFromAddress]
        if isinstance(_from_address, Unset):
            from_address = UNSET
        else:
            from_address = WMSOutboundShipmentFromAddress.from_dict(_from_address)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = WMSOutboundShipmentDocumentsItem.from_dict(documents_item_data)

            documents.append(documents_item)

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = WMSOutboundShipmentEventsItem.from_dict(events_item_data)

            events.append(events_item)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSOutboundShipmentCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSOutboundShipmentCustomFields.from_dict(_custom_fields)

        wms_outbound_shipment = cls(
            field_id=field_id,
            shipment_id=shipment_id,
            world_ref=world_ref,
            warehouse_id=warehouse_id,
            shipment_status=shipment_status,
            lines=lines,
            to_address=to_address,
            created_at=created_at,
            updated_at=updated_at,
            carrier=carrier,
            service_level=service_level,
            tracking_number=tracking_number,
            trailer_number=trailer_number,
            dock_door_id=dock_door_id,
            orders=orders,
            totals=totals,
            dates=dates,
            from_address=from_address,
            documents=documents,
            events=events,
            custom_fields=custom_fields,
        )

        wms_outbound_shipment.additional_properties = d
        return wms_outbound_shipment

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
