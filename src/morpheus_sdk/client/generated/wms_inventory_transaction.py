import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_inventory_transaction_reference_type import WMSInventoryTransactionReferenceType
from ..models.wms_inventory_transaction_transaction_type import WMSInventoryTransactionTransactionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_inventory_transaction_custom_fields import WMSInventoryTransactionCustomFields
    from ..models.wms_inventory_transaction_world_ref import WMSInventoryTransactionWorldRef


T = TypeVar("T", bound="WMSInventoryTransaction")


@_attrs_define
class WMSInventoryTransaction:
    """Complete inventory transaction record for warehouse inventory movements, adjustments, and operations tracking

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        transaction_id (str): Unique identifier for the inventory transaction (auto-generated with wms_inventory-
            transaction prefix) Example: wms_inventory-transaction_674565c1234567890abcdef.
        warehouse_id (str): Warehouse facility where the transaction occurred Example:
            wms_warehouse_674565c1234567890abcdef.
        transaction_type (WMSInventoryTransactionTransactionType): Type of inventory transaction operation Example:
            PUTAWAY.
        product_id (str): Product identifier for the transaction Example: prod_12345.
        quantity (float): Transaction quantity (positive for additions, negative for reductions) Example: 25.
        transaction_date (datetime.datetime): Timestamp when the transaction occurred (defaults to creation time)
            Example: 2024-12-01T14:30:00.000Z.
        world_ref (WMSInventoryTransactionWorldRef): Reference to the world environment for data isolation
        created_at (datetime.datetime): Timestamp when the transaction record was created Example:
            2024-12-01T14:30:00.000Z.
        updated_at (datetime.datetime): Timestamp when the transaction record was last updated Example:
            2024-12-01T14:30:00.000Z.
        sku (Union[None, Unset, str]): Stock keeping unit code for operational reference Example: ABC-123-XL.
        from_bin_id (Union[None, Unset, str]): Source bin identifier for movement transactions Example: BIN-RECV-001.
        to_bin_id (Union[None, Unset, str]): Destination bin identifier for movement transactions Example: BIN-A-01-01.
        lot_number (Union[None, Unset, str]): Lot number for batch tracking and traceability Example: LOT-2024-Q4-001.
        license_plate_number (Union[None, Unset, str]): Container or pallet identifier for tracking Example:
            LP-20241201-001.
        uom (Union[None, Unset, str]): Unit of measure for the transaction quantity Example: EA.
        reference_type (Union[Unset, WMSInventoryTransactionReferenceType]): Type of reference document that triggered
            the transaction Example: ORDER.
        reference_id (Union[None, Unset, str]): Reference document identifier Example: wms_outbound-
            order_674565c1234567890abcdef.
        user_id (Union[None, Unset, str]): User who performed the transaction Example: user_warehouse_worker_001.
        user_name (Union[None, Unset, str]): Human-readable name of the user who performed the transaction Example: John
            Smith.
        reason_code (Union[None, Unset, str]): Reason code for adjustments or special transactions Example:
            CYCLE_COUNT_ADJUSTMENT.
        notes (Union[None, Unset, str]): Additional notes about the transaction Example: Putaway completed after quality
            inspection.
        custom_fields (Union[Unset, WMSInventoryTransactionCustomFields]): Additional warehouse-specific transaction
            data Example: {'priority': 'HIGH', 'equipment': 'Forklift-002', 'temperatureZone': 'ambient',
            'handlingInstructions': 'Handle with care'}.
    """

    field_id: str
    transaction_id: str
    warehouse_id: str
    transaction_type: WMSInventoryTransactionTransactionType
    product_id: str
    quantity: float
    transaction_date: datetime.datetime
    world_ref: "WMSInventoryTransactionWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    sku: Union[None, Unset, str] = UNSET
    from_bin_id: Union[None, Unset, str] = UNSET
    to_bin_id: Union[None, Unset, str] = UNSET
    lot_number: Union[None, Unset, str] = UNSET
    license_plate_number: Union[None, Unset, str] = UNSET
    uom: Union[None, Unset, str] = UNSET
    reference_type: Union[Unset, WMSInventoryTransactionReferenceType] = UNSET
    reference_id: Union[None, Unset, str] = UNSET
    user_id: Union[None, Unset, str] = UNSET
    user_name: Union[None, Unset, str] = UNSET
    reason_code: Union[None, Unset, str] = UNSET
    notes: Union[None, Unset, str] = UNSET
    custom_fields: Union[Unset, "WMSInventoryTransactionCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        transaction_id = self.transaction_id

        warehouse_id = self.warehouse_id

        transaction_type = self.transaction_type.value

        product_id = self.product_id

        quantity = self.quantity

        transaction_date = self.transaction_date.isoformat()

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        sku: Union[None, Unset, str]
        if isinstance(self.sku, Unset):
            sku = UNSET
        else:
            sku = self.sku

        from_bin_id: Union[None, Unset, str]
        if isinstance(self.from_bin_id, Unset):
            from_bin_id = UNSET
        else:
            from_bin_id = self.from_bin_id

        to_bin_id: Union[None, Unset, str]
        if isinstance(self.to_bin_id, Unset):
            to_bin_id = UNSET
        else:
            to_bin_id = self.to_bin_id

        lot_number: Union[None, Unset, str]
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        license_plate_number: Union[None, Unset, str]
        if isinstance(self.license_plate_number, Unset):
            license_plate_number = UNSET
        else:
            license_plate_number = self.license_plate_number

        uom: Union[None, Unset, str]
        if isinstance(self.uom, Unset):
            uom = UNSET
        else:
            uom = self.uom

        reference_type: Union[Unset, str] = UNSET
        if not isinstance(self.reference_type, Unset):
            reference_type = self.reference_type.value

        reference_id: Union[None, Unset, str]
        if isinstance(self.reference_id, Unset):
            reference_id = UNSET
        else:
            reference_id = self.reference_id

        user_id: Union[None, Unset, str]
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        else:
            user_id = self.user_id

        user_name: Union[None, Unset, str]
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        reason_code: Union[None, Unset, str]
        if isinstance(self.reason_code, Unset):
            reason_code = UNSET
        else:
            reason_code = self.reason_code

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "transactionId": transaction_id,
                "warehouseId": warehouse_id,
                "transactionType": transaction_type,
                "productId": product_id,
                "quantity": quantity,
                "transactionDate": transaction_date,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if sku is not UNSET:
            field_dict["sku"] = sku
        if from_bin_id is not UNSET:
            field_dict["fromBinId"] = from_bin_id
        if to_bin_id is not UNSET:
            field_dict["toBinId"] = to_bin_id
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if license_plate_number is not UNSET:
            field_dict["licensePlateNumber"] = license_plate_number
        if uom is not UNSET:
            field_dict["uom"] = uom
        if reference_type is not UNSET:
            field_dict["referenceType"] = reference_type
        if reference_id is not UNSET:
            field_dict["referenceId"] = reference_id
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if reason_code is not UNSET:
            field_dict["reasonCode"] = reason_code
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_inventory_transaction_custom_fields import WMSInventoryTransactionCustomFields
        from ..models.wms_inventory_transaction_world_ref import WMSInventoryTransactionWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        transaction_id = d.pop("transactionId")

        warehouse_id = d.pop("warehouseId")

        transaction_type = WMSInventoryTransactionTransactionType(d.pop("transactionType"))

        product_id = d.pop("productId")

        quantity = d.pop("quantity")

        transaction_date = isoparse(d.pop("transactionDate"))

        world_ref = WMSInventoryTransactionWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_sku(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sku = _parse_sku(d.pop("sku", UNSET))

        def _parse_from_bin_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        from_bin_id = _parse_from_bin_id(d.pop("fromBinId", UNSET))

        def _parse_to_bin_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        to_bin_id = _parse_to_bin_id(d.pop("toBinId", UNSET))

        def _parse_lot_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))

        def _parse_license_plate_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        license_plate_number = _parse_license_plate_number(d.pop("licensePlateNumber", UNSET))

        def _parse_uom(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        uom = _parse_uom(d.pop("uom", UNSET))

        _reference_type = d.pop("referenceType", UNSET)
        reference_type: Union[Unset, WMSInventoryTransactionReferenceType]
        if isinstance(_reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = WMSInventoryTransactionReferenceType(_reference_type)

        def _parse_reference_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reference_id = _parse_reference_id(d.pop("referenceId", UNSET))

        def _parse_user_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_user_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        user_name = _parse_user_name(d.pop("userName", UNSET))

        def _parse_reason_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        reason_code = _parse_reason_code(d.pop("reasonCode", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSInventoryTransactionCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSInventoryTransactionCustomFields.from_dict(_custom_fields)

        wms_inventory_transaction = cls(
            field_id=field_id,
            transaction_id=transaction_id,
            warehouse_id=warehouse_id,
            transaction_type=transaction_type,
            product_id=product_id,
            quantity=quantity,
            transaction_date=transaction_date,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            sku=sku,
            from_bin_id=from_bin_id,
            to_bin_id=to_bin_id,
            lot_number=lot_number,
            license_plate_number=license_plate_number,
            uom=uom,
            reference_type=reference_type,
            reference_id=reference_id,
            user_id=user_id,
            user_name=user_name,
            reason_code=reason_code,
            notes=notes,
            custom_fields=custom_fields,
        )

        wms_inventory_transaction.additional_properties = d
        return wms_inventory_transaction

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
