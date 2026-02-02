import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.erp_shipment_status import ERPShipmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.erp_shipment_carrier import ERPShipmentCarrier
    from ..models.erp_shipment_custom_fields import ERPShipmentCustomFields
    from ..models.erp_shipment_events_item import ERPShipmentEventsItem
    from ..models.erp_shipment_lines_item import ERPShipmentLinesItem
    from ..models.erp_shipment_packaging import ERPShipmentPackaging


T = TypeVar("T", bound="ERPShipment")


@_attrs_define
class ERPShipment:
    """ERP shipment with comprehensive logistics and tracking information

    Attributes:
        field_id (str): MongoDB unique identifier Example: 507f1f77bcf86cd799439020.
        world_id (str): World environment identifier Example: 507f1f77bcf86cd799439011.
        shipment_id (str): Unique shipment identifier (auto-generated) Example: SHIP_507f1f77bcf86cd799439012.
        status (ERPShipmentStatus): Shipment status Example: CREATED.
        to_address (Address): Physical address for billing, shipping, or remittance
        lines (list['ERPShipmentLinesItem']): Shipment line items
        field_v (Union[Unset, float]): MongoDB version key
        po_number (Union[Unset, str]): Related purchase order number Example: ORDER_507f1f77bcf86cd799439013.
        carrier (Union[Unset, ERPShipmentCarrier]): Carrier information
        tracking_number (Union[Unset, str]): Carrier tracking number Example: 1Z999AA1234567890.
        ship_date (Union[Unset, datetime.date]): Shipment date Example: 2024-01-15.
        estimated_arrival (Union[Unset, datetime.date]): Estimated arrival date Example: 2024-01-17.
        actual_arrival (Union[Unset, datetime.date]): Actual arrival date Example: 2024-01-17.
        from_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        packaging (Union[Unset, ERPShipmentPackaging]): Packaging information
        edi_transaction_id (Union[Unset, str]): Related EDI transaction ID Example: 507f1f77bcf86cd799439021.
        documents (Union[Unset, list[str]]): Document URLs for bills of lading, labels, etc. Example:
            ['https://storage.example.com/bill-of-lading.pdf', 'https://storage.example.com/shipping-label.pdf'].
        events (Union[Unset, list['ERPShipmentEventsItem']]): Shipment tracking events
        flow_id (Union[Unset, str]): Business flow identifier Example: FLOW_OUTBOUND_001.
        custom_fields (Union[Unset, ERPShipmentCustomFields]): Additional shipment fields Example: {'expedited': True,
            'specialHandling': 'FRAGILE'}.
        created_at (Union[Unset, datetime.datetime]): Shipment creation timestamp Example: 2024-01-15T08:00:00.000Z.
        updated_at (Union[Unset, datetime.datetime]): Last update timestamp Example: 2024-01-15T16:45:00.000Z.
    """

    field_id: str
    world_id: str
    shipment_id: str
    status: ERPShipmentStatus
    to_address: "Address"
    lines: list["ERPShipmentLinesItem"]
    field_v: Union[Unset, float] = UNSET
    po_number: Union[Unset, str] = UNSET
    carrier: Union[Unset, "ERPShipmentCarrier"] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    ship_date: Union[Unset, datetime.date] = UNSET
    estimated_arrival: Union[Unset, datetime.date] = UNSET
    actual_arrival: Union[Unset, datetime.date] = UNSET
    from_address: Union[Unset, "Address"] = UNSET
    packaging: Union[Unset, "ERPShipmentPackaging"] = UNSET
    edi_transaction_id: Union[Unset, str] = UNSET
    documents: Union[Unset, list[str]] = UNSET
    events: Union[Unset, list["ERPShipmentEventsItem"]] = UNSET
    flow_id: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "ERPShipmentCustomFields"] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        world_id = self.world_id

        shipment_id = self.shipment_id

        status = self.status.value

        to_address = self.to_address.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        field_v = self.field_v

        po_number = self.po_number

        carrier: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier, Unset):
            carrier = self.carrier.to_dict()

        tracking_number = self.tracking_number

        ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.ship_date, Unset):
            ship_date = self.ship_date.isoformat()

        estimated_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_arrival, Unset):
            estimated_arrival = self.estimated_arrival.isoformat()

        actual_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.actual_arrival, Unset):
            actual_arrival = self.actual_arrival.isoformat()

        from_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_address, Unset):
            from_address = self.from_address.to_dict()

        packaging: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.packaging, Unset):
            packaging = self.packaging.to_dict()

        edi_transaction_id = self.edi_transaction_id

        documents: Union[Unset, list[str]] = UNSET
        if not isinstance(self.documents, Unset):
            documents = self.documents

        events: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.events, Unset):
            events = []
            for events_item_data in self.events:
                events_item = events_item_data.to_dict()
                events.append(events_item)

        flow_id = self.flow_id

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
                "shipmentId": shipment_id,
                "status": status,
                "toAddress": to_address,
                "lines": lines,
            }
        )
        if field_v is not UNSET:
            field_dict["__v"] = field_v
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if ship_date is not UNSET:
            field_dict["shipDate"] = ship_date
        if estimated_arrival is not UNSET:
            field_dict["estimatedArrival"] = estimated_arrival
        if actual_arrival is not UNSET:
            field_dict["actualArrival"] = actual_arrival
        if from_address is not UNSET:
            field_dict["fromAddress"] = from_address
        if packaging is not UNSET:
            field_dict["packaging"] = packaging
        if edi_transaction_id is not UNSET:
            field_dict["ediTransactionId"] = edi_transaction_id
        if documents is not UNSET:
            field_dict["documents"] = documents
        if events is not UNSET:
            field_dict["events"] = events
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
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
        from ..models.erp_shipment_carrier import ERPShipmentCarrier
        from ..models.erp_shipment_custom_fields import ERPShipmentCustomFields
        from ..models.erp_shipment_events_item import ERPShipmentEventsItem
        from ..models.erp_shipment_lines_item import ERPShipmentLinesItem
        from ..models.erp_shipment_packaging import ERPShipmentPackaging

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_id = d.pop("worldId")

        shipment_id = d.pop("shipmentId")

        status = ERPShipmentStatus(d.pop("status"))

        to_address = Address.from_dict(d.pop("toAddress"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = ERPShipmentLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        field_v = d.pop("__v", UNSET)

        po_number = d.pop("poNumber", UNSET)

        _carrier = d.pop("carrier", UNSET)
        carrier: Union[Unset, ERPShipmentCarrier]
        if isinstance(_carrier, Unset):
            carrier = UNSET
        else:
            carrier = ERPShipmentCarrier.from_dict(_carrier)

        tracking_number = d.pop("trackingNumber", UNSET)

        _ship_date = d.pop("shipDate", UNSET)
        ship_date: Union[Unset, datetime.date]
        if isinstance(_ship_date, Unset):
            ship_date = UNSET
        else:
            ship_date = isoparse(_ship_date).date()

        _estimated_arrival = d.pop("estimatedArrival", UNSET)
        estimated_arrival: Union[Unset, datetime.date]
        if isinstance(_estimated_arrival, Unset):
            estimated_arrival = UNSET
        else:
            estimated_arrival = isoparse(_estimated_arrival).date()

        _actual_arrival = d.pop("actualArrival", UNSET)
        actual_arrival: Union[Unset, datetime.date]
        if isinstance(_actual_arrival, Unset):
            actual_arrival = UNSET
        else:
            actual_arrival = isoparse(_actual_arrival).date()

        _from_address = d.pop("fromAddress", UNSET)
        from_address: Union[Unset, Address]
        if isinstance(_from_address, Unset):
            from_address = UNSET
        else:
            from_address = Address.from_dict(_from_address)

        _packaging = d.pop("packaging", UNSET)
        packaging: Union[Unset, ERPShipmentPackaging]
        if isinstance(_packaging, Unset):
            packaging = UNSET
        else:
            packaging = ERPShipmentPackaging.from_dict(_packaging)

        edi_transaction_id = d.pop("ediTransactionId", UNSET)

        documents = cast(list[str], d.pop("documents", UNSET))

        events = []
        _events = d.pop("events", UNSET)
        for events_item_data in _events or []:
            events_item = ERPShipmentEventsItem.from_dict(events_item_data)

            events.append(events_item)

        flow_id = d.pop("flowId", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPShipmentCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPShipmentCustomFields.from_dict(_custom_fields)

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

        erp_shipment = cls(
            field_id=field_id,
            world_id=world_id,
            shipment_id=shipment_id,
            status=status,
            to_address=to_address,
            lines=lines,
            field_v=field_v,
            po_number=po_number,
            carrier=carrier,
            tracking_number=tracking_number,
            ship_date=ship_date,
            estimated_arrival=estimated_arrival,
            actual_arrival=actual_arrival,
            from_address=from_address,
            packaging=packaging,
            edi_transaction_id=edi_transaction_id,
            documents=documents,
            events=events,
            flow_id=flow_id,
            custom_fields=custom_fields,
            created_at=created_at,
            updated_at=updated_at,
        )

        erp_shipment.additional_properties = d
        return erp_shipment

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
