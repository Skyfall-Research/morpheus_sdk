import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_receiving_transaction_receiving_status import WMSReceivingTransactionReceivingStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_receiving_transaction_custom_fields import WMSReceivingTransactionCustomFields
    from ..models.wms_receiving_transaction_damage_type_0 import WMSReceivingTransactionDamageType0
    from ..models.wms_receiving_transaction_items_item import WMSReceivingTransactionItemsItem
    from ..models.wms_receiving_transaction_putaway_type_0 import WMSReceivingTransactionPutawayType0
    from ..models.wms_receiving_transaction_quality_type_0 import WMSReceivingTransactionQualityType0
    from ..models.wms_receiving_transaction_world_ref import WMSReceivingTransactionWorldRef


T = TypeVar("T", bound="WMSReceivingTransaction")


@_attrs_define
class WMSReceivingTransaction:
    """Complete receiving transaction record for goods receipt with quality control, damage assessment, and putaway
    management

        Attributes:
            field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
            receiving_id (str): Unique identifier for the receiving transaction (auto-generated with wms_receiving-
                transaction prefix) Example: wms_receiving-transaction_674565c1234567890abcdef.
            warehouse_id (str): Warehouse facility where goods are received Example: wms_warehouse_674565c1234567890abcdef.
            inbound_order_id (str): Reference to the inbound order being received Example: wms_inbound-
                order_674565c1234567890abcdef.
            product_id (str): Product identifier for the received goods Example: prod_12345.
            received_quantity (float): Quantity actually received and documented Example: 50.
            receiving_status (WMSReceivingTransactionReceivingStatus): Current status of the receiving transaction workflow
                Example: RECEIVED.
            world_ref (WMSReceivingTransactionWorldRef): Reference to the world environment for data isolation
            created_at (datetime.datetime): Timestamp when the receiving transaction was created Example:
                2024-12-01T10:30:00.000Z.
            updated_at (datetime.datetime): Timestamp when the receiving transaction was last updated Example:
                2024-12-01T11:15:00.000Z.
            inbound_line_id (Union[None, Unset, str]): Specific line item within the inbound order Example: line_001.
            sku (Union[None, Unset, str]): Stock keeping unit code for operational reference Example: ABC-123-XL.
            product_name (Union[None, Unset, str]): Human-readable product name for identification Example: Premium Wireless
                Headphones.
            license_plate_number (Union[None, Unset, str]): Container or pallet identifier for tracking Example:
                LP-20241201-001.
            lot_number (Union[None, Unset, str]): Lot number for batch tracking and traceability Example: LOT-2024-Q4-001.
            uom (Union[None, Unset, str]): Unit of measure for received quantities (EA, CS, PLT, etc.) Example: EA.
            dock_door_id (Union[None, Unset, str]): Dock door identifier where goods were received Example: wms_dock-
                door_674565c1234567890abcdef.
            quality (Union['WMSReceivingTransactionQualityType0', None, Unset]): Quality control and inspection information
            damage (Union['WMSReceivingTransactionDamageType0', None, Unset]): Damage assessment and documentation
            putaway (Union['WMSReceivingTransactionPutawayType0', None, Unset]): Putaway location assignment and management
            items (Union[Unset, list['WMSReceivingTransactionItemsItem']]): Array of individual items within this receiving
                transaction
            custom_fields (Union[Unset, WMSReceivingTransactionCustomFields]): Additional warehouse-specific receiving
                transaction data Example: {'temperatureZone': 'ambient', 'vendorRefNumber': 'VEN-REF-12345', 'priority': 'HIGH',
                'specialHandling': 'FRAGILE'}.
            status_updated_at (Union[None, Unset, datetime.datetime]): Timestamp when the status was last updated Example:
                2024-12-01T11:15:00.000Z.
    """

    field_id: str
    receiving_id: str
    warehouse_id: str
    inbound_order_id: str
    product_id: str
    received_quantity: float
    receiving_status: WMSReceivingTransactionReceivingStatus
    world_ref: "WMSReceivingTransactionWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    inbound_line_id: Union[None, Unset, str] = UNSET
    sku: Union[None, Unset, str] = UNSET
    product_name: Union[None, Unset, str] = UNSET
    license_plate_number: Union[None, Unset, str] = UNSET
    lot_number: Union[None, Unset, str] = UNSET
    uom: Union[None, Unset, str] = UNSET
    dock_door_id: Union[None, Unset, str] = UNSET
    quality: Union["WMSReceivingTransactionQualityType0", None, Unset] = UNSET
    damage: Union["WMSReceivingTransactionDamageType0", None, Unset] = UNSET
    putaway: Union["WMSReceivingTransactionPutawayType0", None, Unset] = UNSET
    items: Union[Unset, list["WMSReceivingTransactionItemsItem"]] = UNSET
    custom_fields: Union[Unset, "WMSReceivingTransactionCustomFields"] = UNSET
    status_updated_at: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wms_receiving_transaction_damage_type_0 import WMSReceivingTransactionDamageType0
        from ..models.wms_receiving_transaction_putaway_type_0 import WMSReceivingTransactionPutawayType0
        from ..models.wms_receiving_transaction_quality_type_0 import WMSReceivingTransactionQualityType0

        field_id = self.field_id

        receiving_id = self.receiving_id

        warehouse_id = self.warehouse_id

        inbound_order_id = self.inbound_order_id

        product_id = self.product_id

        received_quantity = self.received_quantity

        receiving_status = self.receiving_status.value

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        inbound_line_id: Union[None, Unset, str]
        if isinstance(self.inbound_line_id, Unset):
            inbound_line_id = UNSET
        else:
            inbound_line_id = self.inbound_line_id

        sku: Union[None, Unset, str]
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        product_name: Union[None, Unset, str]
        if isinstance(self.product_name, Unset):
            product_name = UNSET
        else:
            product_name = self.product_name

        license_plate_number: Union[None, Unset, str]
        if isinstance(self.license_plate_number, Unset):
            license_plate_number = UNSET
        else:
            license_plate_number = self.license_plate_number

        lot_number: Union[None, Unset, str]
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        uom: Union[None, Unset, str]
        if isinstance(self.uom, Unset):
            uom = UNSET
        else:
            uom = self.uom

        dock_door_id: Union[None, Unset, str]
        if isinstance(self.dock_door_id, Unset):
            dock_door_id = UNSET
        else:
            dock_door_id = self.dock_door_id

        quality: Union[None, Unset, dict[str, Any]]
        if isinstance(self.quality, Unset):
            quality = UNSET
        elif isinstance(self.quality, WMSReceivingTransactionQualityType0):
            quality = self.quality.to_dict()
        else:
            quality = self.quality

        damage: Union[None, Unset, dict[str, Any]]
        if isinstance(self.damage, Unset):
            damage = UNSET
        elif isinstance(self.damage, WMSReceivingTransactionDamageType0):
            damage = self.damage.to_dict()
        else:
            damage = self.damage

        putaway: Union[None, Unset, dict[str, Any]]
        if isinstance(self.putaway, Unset):
            putaway = UNSET
        elif isinstance(self.putaway, WMSReceivingTransactionPutawayType0):
            putaway = self.putaway.to_dict()
        else:
            putaway = self.putaway

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        status_updated_at: Union[None, Unset, str]
        if isinstance(self.status_updated_at, Unset):
            status_updated_at = UNSET
        elif isinstance(self.status_updated_at, datetime.datetime):
            status_updated_at = self.status_updated_at.isoformat()
        else:
            status_updated_at = self.status_updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "receivingId": receiving_id,
                "warehouseId": warehouse_id,
                "inboundOrderId": inbound_order_id,
                "productId": product_id,
                "receivedQuantity": received_quantity,
                "receivingStatus": receiving_status,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if inbound_line_id is not UNSET:
            field_dict["inboundLineId"] = inbound_line_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if license_plate_number is not UNSET:
            field_dict["licensePlateNumber"] = license_plate_number
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if uom is not UNSET:
            field_dict["uom"] = uom
        if dock_door_id is not UNSET:
            field_dict["dockDoorId"] = dock_door_id
        if quality is not UNSET:
            field_dict["quality"] = quality
        if damage is not UNSET:
            field_dict["damage"] = damage
        if putaway is not UNSET:
            field_dict["putaway"] = putaway
        if items is not UNSET:
            field_dict["items"] = items
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if status_updated_at is not UNSET:
            field_dict["statusUpdatedAt"] = status_updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_receiving_transaction_custom_fields import WMSReceivingTransactionCustomFields
        from ..models.wms_receiving_transaction_damage_type_0 import WMSReceivingTransactionDamageType0
        from ..models.wms_receiving_transaction_items_item import WMSReceivingTransactionItemsItem
        from ..models.wms_receiving_transaction_putaway_type_0 import WMSReceivingTransactionPutawayType0
        from ..models.wms_receiving_transaction_quality_type_0 import WMSReceivingTransactionQualityType0
        from ..models.wms_receiving_transaction_world_ref import WMSReceivingTransactionWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        receiving_id = d.pop("receivingId")

        warehouse_id = d.pop("warehouseId")

        inbound_order_id = d.pop("inboundOrderId")

        product_id = d.pop("productId")

        received_quantity = d.pop("receivedQuantity")

        receiving_status = WMSReceivingTransactionReceivingStatus(d.pop("receivingStatus"))

        world_ref = WMSReceivingTransactionWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_inbound_line_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        inbound_line_id = _parse_inbound_line_id(d.pop("inboundLineId", UNSET))

        def _parse_sku(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_product_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        product_name = _parse_product_name(d.pop("productName", UNSET))

        def _parse_license_plate_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        license_plate_number = _parse_license_plate_number(d.pop("licensePlateNumber", UNSET))

        def _parse_lot_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))

        def _parse_uom(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        uom = _parse_uom(d.pop("uom", UNSET))

        def _parse_dock_door_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        dock_door_id = _parse_dock_door_id(d.pop("dockDoorId", UNSET))

        def _parse_quality(data: object) -> Union["WMSReceivingTransactionQualityType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                quality_type_0 = WMSReceivingTransactionQualityType0.from_dict(data)

                return quality_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSReceivingTransactionQualityType0", None, Unset], data)

        quality = _parse_quality(d.pop("quality", UNSET))

        def _parse_damage(data: object) -> Union["WMSReceivingTransactionDamageType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                damage_type_0 = WMSReceivingTransactionDamageType0.from_dict(data)

                return damage_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSReceivingTransactionDamageType0", None, Unset], data)

        damage = _parse_damage(d.pop("damage", UNSET))

        def _parse_putaway(data: object) -> Union["WMSReceivingTransactionPutawayType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                putaway_type_0 = WMSReceivingTransactionPutawayType0.from_dict(data)

                return putaway_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSReceivingTransactionPutawayType0", None, Unset], data)

        putaway = _parse_putaway(d.pop("putaway", UNSET))

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = WMSReceivingTransactionItemsItem.from_dict(items_item_data)

            items.append(items_item)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSReceivingTransactionCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSReceivingTransactionCustomFields.from_dict(_custom_fields)

        def _parse_status_updated_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_updated_at_type_0 = isoparse(data)

                return status_updated_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        status_updated_at = _parse_status_updated_at(d.pop("statusUpdatedAt", UNSET))

        wms_receiving_transaction = cls(
            field_id=field_id,
            receiving_id=receiving_id,
            warehouse_id=warehouse_id,
            inbound_order_id=inbound_order_id,
            product_id=product_id,
            received_quantity=received_quantity,
            receiving_status=receiving_status,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            inbound_line_id=inbound_line_id,
            sku=sku,
            product_name=product_name,
            license_plate_number=license_plate_number,
            lot_number=lot_number,
            uom=uom,
            dock_door_id=dock_door_id,
            quality=quality,
            damage=damage,
            putaway=putaway,
            items=items,
            custom_fields=custom_fields,
            status_updated_at=status_updated_at,
        )

        wms_receiving_transaction.additional_properties = d
        return wms_receiving_transaction

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
