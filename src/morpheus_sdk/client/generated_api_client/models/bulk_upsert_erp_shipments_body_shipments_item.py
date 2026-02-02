from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_upsert_erp_shipments_body_shipments_item_status import BulkUpsertERPShipmentsBodyShipmentsItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.bulk_upsert_erp_shipments_body_shipments_item_carrier import (
        BulkUpsertERPShipmentsBodyShipmentsItemCarrier,
    )
    from ..models.bulk_upsert_erp_shipments_body_shipments_item_lines_item import (
        BulkUpsertERPShipmentsBodyShipmentsItemLinesItem,
    )


T = TypeVar("T", bound="BulkUpsertERPShipmentsBodyShipmentsItem")


@_attrs_define
class BulkUpsertERPShipmentsBodyShipmentsItem:
    """
    Attributes:
        shipment_id (Union[Unset, str]):  Example: SHIP_001.
        po_number (Union[Unset, str]):  Example: PO_001.
        carrier (Union[Unset, BulkUpsertERPShipmentsBodyShipmentsItemCarrier]):
        tracking_number (Union[Unset, str]):  Example: 1Z999AA123456.
        status (Union[Unset, BulkUpsertERPShipmentsBodyShipmentsItemStatus]):
        to_address (Union[Unset, Address]): Physical address for billing, shipping, or remittance
        lines (Union[Unset, list['BulkUpsertERPShipmentsBodyShipmentsItemLinesItem']]):
    """

    shipment_id: Union[Unset, str] = UNSET
    po_number: Union[Unset, str] = UNSET
    carrier: Union[Unset, "BulkUpsertERPShipmentsBodyShipmentsItemCarrier"] = UNSET
    tracking_number: Union[Unset, str] = UNSET
    status: Union[Unset, BulkUpsertERPShipmentsBodyShipmentsItemStatus] = UNSET
    to_address: Union[Unset, "Address"] = UNSET
    lines: Union[Unset, list["BulkUpsertERPShipmentsBodyShipmentsItemLinesItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipment_id = self.shipment_id

        po_number = self.po_number

        carrier: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.carrier, Unset):
            carrier = self.carrier.to_dict()

        tracking_number = self.tracking_number

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        to_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to_address, Unset):
            to_address = self.to_address.to_dict()

        lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipment_id is not UNSET:
            field_dict["shipmentId"] = shipment_id
        if po_number is not UNSET:
            field_dict["poNumber"] = po_number
        if carrier is not UNSET:
            field_dict["carrier"] = carrier
        if tracking_number is not UNSET:
            field_dict["trackingNumber"] = tracking_number
        if status is not UNSET:
            field_dict["status"] = status
        if to_address is not UNSET:
            field_dict["toAddress"] = to_address
        if lines is not UNSET:
            field_dict["lines"] = lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address import Address
        from ..models.bulk_upsert_erp_shipments_body_shipments_item_carrier import (
            BulkUpsertERPShipmentsBodyShipmentsItemCarrier,
        )
        from ..models.bulk_upsert_erp_shipments_body_shipments_item_lines_item import (
            BulkUpsertERPShipmentsBodyShipmentsItemLinesItem,
        )

        d = dict(src_dict)
        shipment_id = d.pop("shipmentId", UNSET)

        po_number = d.pop("poNumber", UNSET)

        _carrier = d.pop("carrier", UNSET)
        carrier: Union[Unset, BulkUpsertERPShipmentsBodyShipmentsItemCarrier]
        if isinstance(_carrier, Unset):
            carrier = UNSET
        else:
            carrier = BulkUpsertERPShipmentsBodyShipmentsItemCarrier.from_dict(_carrier)

        tracking_number = d.pop("trackingNumber", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BulkUpsertERPShipmentsBodyShipmentsItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BulkUpsertERPShipmentsBodyShipmentsItemStatus(_status)

        _to_address = d.pop("toAddress", UNSET)
        to_address: Union[Unset, Address]
        if isinstance(_to_address, Unset):
            to_address = UNSET
        else:
            to_address = Address.from_dict(_to_address)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = BulkUpsertERPShipmentsBodyShipmentsItemLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        bulk_upsert_erp_shipments_body_shipments_item = cls(
            shipment_id=shipment_id,
            po_number=po_number,
            carrier=carrier,
            tracking_number=tracking_number,
            status=status,
            to_address=to_address,
            lines=lines,
        )

        bulk_upsert_erp_shipments_body_shipments_item.additional_properties = d
        return bulk_upsert_erp_shipments_body_shipments_item

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
