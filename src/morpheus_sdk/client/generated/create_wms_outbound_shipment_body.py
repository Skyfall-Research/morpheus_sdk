from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_outbound_shipment_body_carrier import CreateWMSOutboundShipmentBodyCarrier
    from ..models.create_wms_outbound_shipment_body_dates import CreateWMSOutboundShipmentBodyDates
    from ..models.create_wms_outbound_shipment_body_documents_item import CreateWMSOutboundShipmentBodyDocumentsItem
    from ..models.create_wms_outbound_shipment_body_from_address import CreateWMSOutboundShipmentBodyFromAddress
    from ..models.create_wms_outbound_shipment_body_lines_item import CreateWMSOutboundShipmentBodyLinesItem
    from ..models.create_wms_outbound_shipment_body_orders_item import CreateWMSOutboundShipmentBodyOrdersItem
    from ..models.create_wms_outbound_shipment_body_to_address import CreateWMSOutboundShipmentBodyToAddress
    from ..models.create_wms_outbound_shipment_body_totals import CreateWMSOutboundShipmentBodyTotals


T = TypeVar("T", bound="CreateWMSOutboundShipmentBody")


@_attrs_define
class CreateWMSOutboundShipmentBody:
    """
    Attributes:
        warehouse_id (str): Required - source warehouse identifier Example: WH-MAIN-001.
        lines (list['CreateWMSOutboundShipmentBodyLinesItem']): Shipment line items (required)
        to_address (CreateWMSOutboundShipmentBodyToAddress): Required destination address
        shipment_id (Union[Unset, str]): Business shipment identifier (auto-generated if not provided) Example:
            SHIP-2024-001234.
        carrier (Union[Unset, CreateWMSOutboundShipmentBodyCarrier]): Carrier information for shipment
        service_level (Union[Unset, str]): Carrier service level Example: GROUND.
        tracking_number (Union[Unset, str]): Carrier tracking number (if available) Example: 1Z999AA1234567890.
        trailer_number (Union[Unset, str]): Trailer identifier for LTL/TL shipments Example: TRL-001.
        dock_door_id (Union[Unset, str]): Assigned dock door for loading Example: DOCK-A-001.
        orders (Union[Unset, list['CreateWMSOutboundShipmentBodyOrdersItem']]): Orders included in this shipment
        from_address (Union[Unset, CreateWMSOutboundShipmentBodyFromAddress]): Origin address
        totals (Union[Unset, CreateWMSOutboundShipmentBodyTotals]): Shipment totals and metrics
        dates (Union[Unset, CreateWMSOutboundShipmentBodyDates]): Scheduled dates and delivery requirements
        documents (Union[Unset, list['CreateWMSOutboundShipmentBodyDocumentsItem']]): Shipment documents
    """

    warehouse_id: str
    lines: list["CreateWMSOutboundShipmentBodyLinesItem"]
    to_address: "CreateWMSOutboundShipmentBodyToAddress"
    shipment_id: Union[Unset, str] = UNSET
    carrier: Union[Unset, "CreateWMSOutboundShipmentBodyCarrier"] = UNSET
    service_level: Union[Unset, str] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    trailer_number: Union[Unset, str] = UNSET
    dock_door_id: Union[Unset, str] = UNSET
    orders: Union[Unset, list["CreateWMSOutboundShipmentBodyOrdersItem"]] = UNSET
    from_address: Union[Unset, "CreateWMSOutboundShipmentBodyFromAddress"] = UNSET
    totals: Union[Unset, "CreateWMSOutboundShipmentBodyTotals"] = UNSET
    dates: Union[Unset, "CreateWMSOutboundShipmentBodyDates"] = UNSET
    documents: Union[Unset, list["CreateWMSOutboundShipmentBodyDocumentsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        to_address = self.to_address.to_dict()

        shipment_id = self.shipment_id

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

        from_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_address, Unset):
            from_address = self.from_address.to_dict()

        totals: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.totals, Unset):
            totals = self.totals.to_dict()

        dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = []
            for documents_item_data in self.documents:
                documents_item = documents_item_data.to_dict()
                documents.append(documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "lines": lines,
                "toAddress": to_address,
            }
        )
        if shipment_id is not UNSET:
            field_dict["shipmentId"] = shipment_id
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
        if from_address is not UNSET:
            field_dict["fromAddress"] = from_address
        if totals is not UNSET:
            field_dict["totals"] = totals
        if dates is not UNSET:
            field_dict["dates"] = dates
        if documents is not UNSET:
            field_dict["documents"] = documents

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_outbound_shipment_body_carrier import CreateWMSOutboundShipmentBodyCarrier
        from ..models.create_wms_outbound_shipment_body_dates import CreateWMSOutboundShipmentBodyDates
        from ..models.create_wms_outbound_shipment_body_documents_item import CreateWMSOutboundShipmentBodyDocumentsItem
        from ..models.create_wms_outbound_shipment_body_from_address import CreateWMSOutboundShipmentBodyFromAddress
        from ..models.create_wms_outbound_shipment_body_lines_item import CreateWMSOutboundShipmentBodyLinesItem
        from ..models.create_wms_outbound_shipment_body_orders_item import CreateWMSOutboundShipmentBodyOrdersItem
        from ..models.create_wms_outbound_shipment_body_to_address import CreateWMSOutboundShipmentBodyToAddress
        from ..models.create_wms_outbound_shipment_body_totals import CreateWMSOutboundShipmentBodyTotals

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = CreateWMSOutboundShipmentBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        to_address = CreateWMSOutboundShipmentBodyToAddress.from_dict(d.pop("toAddress"))

        shipment_id = d.pop("shipmentId", UNSET)

        _carrier = d.pop("carrier", UNSET)
        carrier: Union[Unset, CreateWMSOutboundShipmentBodyCarrier]
        if isinstance(_carrier, Unset):
            carrier = UNSET
        else:
            carrier = CreateWMSOutboundShipmentBodyCarrier.from_dict(_carrier)

        service_level = d.pop("serviceLevel", UNSET)

        tracking_number = d.pop("trackingNumber", UNSET)

        trailer_number = d.pop("trailerNumber", UNSET)

        dock_door_id = d.pop("dockDoorId", UNSET)

        orders = []
        _orders = d.pop("orders", UNSET)
        for orders_item_data in _orders or []:
            orders_item = CreateWMSOutboundShipmentBodyOrdersItem.from_dict(orders_item_data)

            orders.append(orders_item)

        _from_address = d.pop("fromAddress", UNSET)
        from_address: Union[Unset, CreateWMSOutboundShipmentBodyFromAddress]
        if isinstance(_from_address, Unset):
            from_address = UNSET
        else:
            from_address = CreateWMSOutboundShipmentBodyFromAddress.from_dict(_from_address)

        _totals = d.pop("totals", UNSET)
        totals: Union[Unset, CreateWMSOutboundShipmentBodyTotals]
        if isinstance(_totals, Unset):
            totals = UNSET
        else:
            totals = CreateWMSOutboundShipmentBodyTotals.from_dict(_totals)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, CreateWMSOutboundShipmentBodyDates]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = CreateWMSOutboundShipmentBodyDates.from_dict(_dates)

        documents = []
        _documents = d.pop("documents", UNSET)
        for documents_item_data in _documents or []:
            documents_item = CreateWMSOutboundShipmentBodyDocumentsItem.from_dict(documents_item_data)

            documents.append(documents_item)

        create_wms_outbound_shipment_body = cls(
            warehouse_id=warehouse_id,
            lines=lines,
            to_address=to_address,
            shipment_id=shipment_id,
            carrier=carrier,
            service_level=service_level,
            tracking_number=tracking_number,
            trailer_number=trailer_number,
            dock_door_id=dock_door_id,
            orders=orders,
            from_address=from_address,
            totals=totals,
            dates=dates,
            documents=documents,
        )

        create_wms_outbound_shipment_body.additional_properties = d
        return create_wms_outbound_shipment_body

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
