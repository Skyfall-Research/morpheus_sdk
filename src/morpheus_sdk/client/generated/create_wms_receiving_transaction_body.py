from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_receiving_transaction_body_receiving_status import (
    CreateWMSReceivingTransactionBodyReceivingStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_receiving_transaction_body_custom_fields import (
        CreateWMSReceivingTransactionBodyCustomFields,
    )
    from ..models.create_wms_receiving_transaction_body_damage import CreateWMSReceivingTransactionBodyDamage
    from ..models.create_wms_receiving_transaction_body_putaway import CreateWMSReceivingTransactionBodyPutaway
    from ..models.create_wms_receiving_transaction_body_quality import CreateWMSReceivingTransactionBodyQuality


T = TypeVar("T", bound="CreateWMSReceivingTransactionBody")


@_attrs_define
class CreateWMSReceivingTransactionBody:
    """
    Attributes:
        warehouse_id (str): Unique identifier of the warehouse facility Example: wms_warehouse_674565c1234567890abcdef.
        inbound_order_id (str): Reference to the inbound order being received Example: wms_inbound-
            order_674565c1234567890abcdef.
        product_id (str): Product being received Example: prod_12345.
        received_quantity (float): Quantity actually received Example: 50.
        inbound_line_id (Union[Unset, str]): Specific line item within the inbound order Example: line_001.
        sku (Union[Unset, str]): Stock keeping unit code Example: ABC-123-XL.
        product_name (Union[Unset, str]): Human-readable product name Example: Premium Wireless Headphones.
        license_plate_number (Union[Unset, str]): Container or pallet identifier Example: LP-20241201-001.
        lot_number (Union[Unset, str]): Lot number for batch tracking Example: LOT-2024-Q4-001.
        uom (Union[Unset, str]): Unit of measure Example: EA.
        dock_door_id (Union[Unset, str]): Dock door where goods were received Example: wms_dock-
            door_674565c1234567890abcdef.
        receiving_status (Union[Unset, CreateWMSReceivingTransactionBodyReceivingStatus]): Current status of the
            receiving transaction Example: RECEIVED.
        quality (Union[Unset, CreateWMSReceivingTransactionBodyQuality]): Quality control information
        damage (Union[Unset, CreateWMSReceivingTransactionBodyDamage]): Damage assessment information
        putaway (Union[Unset, CreateWMSReceivingTransactionBodyPutaway]): Putaway location assignment
        custom_fields (Union[Unset, CreateWMSReceivingTransactionBodyCustomFields]): Additional custom data Example:
            {'temperatureZone': 'ambient', 'vendorRefNumber': 'VEN-REF-12345'}.
    """

    warehouse_id: str
    inbound_order_id: str
    product_id: str
    received_quantity: float
    inbound_line_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    license_plate_number: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    uom: Union[Unset, str] = UNSET
    dock_door_id: Union[Unset, str] = UNSET
    receiving_status: Union[Unset, CreateWMSReceivingTransactionBodyReceivingStatus] = UNSET
    quality: Union[Unset, "CreateWMSReceivingTransactionBodyQuality"] = UNSET
    damage: Union[Unset, "CreateWMSReceivingTransactionBodyDamage"] = UNSET
    putaway: Union[Unset, "CreateWMSReceivingTransactionBodyPutaway"] = UNSET
    custom_fields: Union[Unset, "CreateWMSReceivingTransactionBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        inbound_order_id = self.inbound_order_id

        product_id = self.product_id

        received_quantity = self.received_quantity

        inbound_line_id = self.inbound_line_id

        sku = self.sku

        product_name = self.product_name

        license_plate_number = self.license_plate_number

        lot_number = self.lot_number

        uom = self.uom

        dock_door_id = self.dock_door_id

        receiving_status: Union[Unset, str] = UNSET
        if not isinstance(self.receiving_status, Unset):
            receiving_status = self.receiving_status.value

        quality: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quality, Unset):
            quality = self.quality.to_dict()

        damage: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.damage, Unset):
            damage = self.damage.to_dict()

        putaway: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.putaway, Unset):
            putaway = self.putaway.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "inboundOrderId": inbound_order_id,
                "productId": product_id,
                "receivedQuantity": received_quantity,
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
        if receiving_status is not UNSET:
            field_dict["receivingStatus"] = receiving_status
        if quality is not UNSET:
            field_dict["quality"] = quality
        if damage is not UNSET:
            field_dict["damage"] = damage
        if putaway is not UNSET:
            field_dict["putaway"] = putaway
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_receiving_transaction_body_custom_fields import (
            CreateWMSReceivingTransactionBodyCustomFields,
        )
        from ..models.create_wms_receiving_transaction_body_damage import CreateWMSReceivingTransactionBodyDamage
        from ..models.create_wms_receiving_transaction_body_putaway import CreateWMSReceivingTransactionBodyPutaway
        from ..models.create_wms_receiving_transaction_body_quality import CreateWMSReceivingTransactionBodyQuality

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        inbound_order_id = d.pop("inboundOrderId")

        product_id = d.pop("productId")

        received_quantity = d.pop("receivedQuantity")

        inbound_line_id = d.pop("inboundLineId", UNSET)

        sku = d.pop("sku", UNSET)

        product_name = d.pop("productName", UNSET)

        license_plate_number = d.pop("licensePlateNumber", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        uom = d.pop("uom", UNSET)

        dock_door_id = d.pop("dockDoorId", UNSET)

        _receiving_status = d.pop("receivingStatus", UNSET)
        receiving_status: Union[Unset, CreateWMSReceivingTransactionBodyReceivingStatus]
        if isinstance(_receiving_status, Unset):
            receiving_status = UNSET
        else:
            receiving_status = CreateWMSReceivingTransactionBodyReceivingStatus(_receiving_status)

        _quality = d.pop("quality", UNSET)
        quality: Union[Unset, CreateWMSReceivingTransactionBodyQuality]
        if isinstance(_quality, Unset):
            quality = UNSET
        else:
            quality = CreateWMSReceivingTransactionBodyQuality.from_dict(_quality)

        _damage = d.pop("damage", UNSET)
        damage: Union[Unset, CreateWMSReceivingTransactionBodyDamage]
        if isinstance(_damage, Unset):
            damage = UNSET
        else:
            damage = CreateWMSReceivingTransactionBodyDamage.from_dict(_damage)

        _putaway = d.pop("putaway", UNSET)
        putaway: Union[Unset, CreateWMSReceivingTransactionBodyPutaway]
        if isinstance(_putaway, Unset):
            putaway = UNSET
        else:
            putaway = CreateWMSReceivingTransactionBodyPutaway.from_dict(_putaway)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateWMSReceivingTransactionBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateWMSReceivingTransactionBodyCustomFields.from_dict(_custom_fields)

        create_wms_receiving_transaction_body = cls(
            warehouse_id=warehouse_id,
            inbound_order_id=inbound_order_id,
            product_id=product_id,
            received_quantity=received_quantity,
            inbound_line_id=inbound_line_id,
            sku=sku,
            product_name=product_name,
            license_plate_number=license_plate_number,
            lot_number=lot_number,
            uom=uom,
            dock_door_id=dock_door_id,
            receiving_status=receiving_status,
            quality=quality,
            damage=damage,
            putaway=putaway,
            custom_fields=custom_fields,
        )

        create_wms_receiving_transaction_body.additional_properties = d
        return create_wms_receiving_transaction_body

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
