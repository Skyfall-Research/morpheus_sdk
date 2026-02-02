import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_erp_shipment_body_status import CreateERPShipmentBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.create_erp_shipment_body_carrier import CreateERPShipmentBodyCarrier
    from ..models.create_erp_shipment_body_custom_fields import CreateERPShipmentBodyCustomFields
    from ..models.create_erp_shipment_body_lines_item import CreateERPShipmentBodyLinesItem
    from ..models.create_erp_shipment_body_packaging import CreateERPShipmentBodyPackaging


T = TypeVar("T", bound="CreateERPShipmentBody")


@_attrs_define
class CreateERPShipmentBody:
    """
    Attributes:
        to_address (Address): Physical address for billing, shipping, or remittance
        lines (list['CreateERPShipmentBodyLinesItem']): Shipment line items (required)
        shipment_id (Union[Unset, str]): Optional custom shipment identifier (auto-generated if not provided) Example:
            SHIP_507f1f77bcf86cd799439012.
        po_number (Union[Unset, str]): Related purchase order number Example: ORDER_507f1f77bcf86cd799439013.
        carrier (Union[Unset, CreateERPShipmentBodyCarrier]): Carrier information
        tracking_number (Union[Unset, str]): Carrier tracking number Example: 1Z999AA1234567890.
        ship_date (Union[Unset, datetime.date]): Shipment date Example: 2024-01-15.
        estimated_arrival (Union[Unset, datetime.date]): Estimated arrival date Example: 2024-01-17.
        status (Union[Unset, CreateERPShipmentBodyStatus]): Shipment status Default:
            CreateERPShipmentBodyStatus.CREATED. Example: CREATED.
        from_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        packaging (Union[Unset, CreateERPShipmentBodyPackaging]): Packaging information
        flow_id (Union[Unset, str]): Business flow identifier Example: FLOW_OUTBOUND_001.
        custom_fields (Union[Unset, CreateERPShipmentBodyCustomFields]): Additional shipment-specific fields Example:
            {'expedited': True, 'specialHandling': 'FRAGILE'}.
    """

    to_address: "Address"
    lines: list["CreateERPShipmentBodyLinesItem"]
    shipment_id: Union[Unset, str] = UNSET
    po_number: Union[Unset, str] = UNSET
    carrier: Union[Unset, "CreateERPShipmentBodyCarrier"] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    ship_date: Union[Unset, datetime.date] = UNSET
    estimated_arrival: Union[Unset, datetime.date] = UNSET
    status: Union[Unset, CreateERPShipmentBodyStatus] = CreateERPShipmentBodyStatus.CREATED
    from_address: Union[Unset, "Address"] = UNSET
    packaging: Union[Unset, "CreateERPShipmentBodyPackaging"] = UNSET
    flow_id: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "CreateERPShipmentBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to_address = self.to_address.to_dict()

        lines = []
        for lines_item_data in self.lines:
            lines_item = lines_item_data.to_dict()
            lines.append(lines_item)

        shipment_id = self.shipment_id

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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        from_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_address, Unset):
            from_address = self.from_address.to_dict()

        packaging: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.packaging, Unset):
            packaging = self.packaging.to_dict()

        flow_id = self.flow_id

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "toAddress": to_address,
                "lines": lines,
            }
        )
        if shipment_id is not UNSET:
            field_dict["shipmentId"] = shipment_id
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
        if status is not UNSET:
            field_dict["status"] = status
        if from_address is not UNSET:
            field_dict["fromAddress"] = from_address
        if packaging is not UNSET:
            field_dict["packaging"] = packaging
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.create_erp_shipment_body_carrier import CreateERPShipmentBodyCarrier
        from ..models.create_erp_shipment_body_custom_fields import CreateERPShipmentBodyCustomFields
        from ..models.create_erp_shipment_body_lines_item import CreateERPShipmentBodyLinesItem
        from ..models.create_erp_shipment_body_packaging import CreateERPShipmentBodyPackaging

        d = dict(src_dict)
        to_address = Address.from_dict(d.pop("toAddress"))

        lines = []
        _lines = d.pop("lines")
        for lines_item_data in _lines:
            lines_item = CreateERPShipmentBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        shipment_id = d.pop("shipmentId", UNSET)

        po_number = d.pop("poNumber", UNSET)

        _carrier = d.pop("carrier", UNSET)
        carrier: Union[Unset, CreateERPShipmentBodyCarrier]
        if isinstance(_carrier, Unset):
            carrier = UNSET
        else:
            carrier = CreateERPShipmentBodyCarrier.from_dict(_carrier)

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

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateERPShipmentBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateERPShipmentBodyStatus(_status)

        _from_address = d.pop("fromAddress", UNSET)
        from_address: Union[Unset, Address]
        if isinstance(_from_address, Unset):
            from_address = UNSET
        else:
            from_address = Address.from_dict(_from_address)

        _packaging = d.pop("packaging", UNSET)
        packaging: Union[Unset, CreateERPShipmentBodyPackaging]
        if isinstance(_packaging, Unset):
            packaging = UNSET
        else:
            packaging = CreateERPShipmentBodyPackaging.from_dict(_packaging)

        flow_id = d.pop("flowId", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateERPShipmentBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateERPShipmentBodyCustomFields.from_dict(_custom_fields)

        create_erp_shipment_body = cls(
            to_address=to_address,
            lines=lines,
            shipment_id=shipment_id,
            po_number=po_number,
            carrier=carrier,
            tracking_number=tracking_number,
            ship_date=ship_date,
            estimated_arrival=estimated_arrival,
            status=status,
            from_address=from_address,
            packaging=packaging,
            flow_id=flow_id,
            custom_fields=custom_fields,
        )

        create_erp_shipment_body.additional_properties = d
        return create_erp_shipment_body

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
