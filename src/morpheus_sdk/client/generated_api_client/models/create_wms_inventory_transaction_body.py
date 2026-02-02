import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_wms_inventory_transaction_body_reference_type import CreateWMSInventoryTransactionBodyReferenceType
from ..models.create_wms_inventory_transaction_body_transaction_type import (
    CreateWMSInventoryTransactionBodyTransactionType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_inventory_transaction_body_custom_fields import (
        CreateWMSInventoryTransactionBodyCustomFields,
    )


T = TypeVar("T", bound="CreateWMSInventoryTransactionBody")


@_attrs_define
class CreateWMSInventoryTransactionBody:
    """
    Attributes:
        warehouse_id (str): Unique identifier of the warehouse facility Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (CreateWMSInventoryTransactionBodyTransactionType): Type of inventory transaction operation
            Example: PUTAWAY.
        product_id (str): Product identifier for the inventory transaction Example: prod_12345.
        quantity (float): Transaction quantity (positive for additions, negative for reductions) Example: 25.
        sku (Union[Unset, str]): Stock keeping unit code Example: ABC-123-XL.
        from_bin_id (Union[Unset, str]): Source bin identifier for movement transactions Example: BIN-RECV-001.
        to_bin_id (Union[Unset, str]): Destination bin identifier for movement transactions Example: BIN-A-01-01.
        lot_number (Union[Unset, str]): Lot number for batch tracking Example: LOT-2024-Q4-001.
        license_plate_number (Union[Unset, str]): Container or pallet identifier Example: LP-20241201-001.
        uom (Union[Unset, str]): Unit of measure Example: EA.
        reference_type (Union[Unset, CreateWMSInventoryTransactionBodyReferenceType]): Type of reference document
            Example: ORDER.
        reference_id (Union[Unset, str]): Reference document identifier Example: wms_outbound-
            order_674565c1234567890abcdef.
        transaction_date (Union[Unset, datetime.datetime]): Transaction timestamp (defaults to current time) Example:
            2024-12-01T14:30:00.000Z.
        user_id (Union[Unset, str]): User who performed the transaction Example: user_warehouse_worker_001.
        user_name (Union[Unset, str]): Human-readable user name Example: John Smith.
        reason_code (Union[Unset, str]): Reason code for adjustments or special transactions Example:
            CYCLE_COUNT_ADJUSTMENT.
        notes (Union[Unset, str]): Additional notes about the transaction Example: Putaway completed after quality
            inspection.
        custom_fields (Union[Unset, CreateWMSInventoryTransactionBodyCustomFields]): Additional custom transaction data
            Example: {'priority': 'HIGH', 'equipment': 'Forklift-002'}.
    """

    warehouse_id: str
    transaction_type: CreateWMSInventoryTransactionBodyTransactionType
    product_id: str
    quantity: float
    sku: Union[Unset, str] = UNSET
    from_bin_id: Union[Unset, str] = UNSET
    to_bin_id: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    license_plate_number: Union[Unset, str] = UNSET
    uom: Union[Unset, str] = UNSET
    reference_type: Union[Unset, CreateWMSInventoryTransactionBodyReferenceType] = UNSET
    reference_id: Union[Unset, str] = UNSET
    transaction_date: Union[Unset, datetime.datetime] = UNSET
    user_id: Union[Unset, str] = UNSET
    user_name: Union[Unset, str] = UNSET
    reason_code: Union[Unset, str] = UNSET
    notes: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "CreateWMSInventoryTransactionBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        transaction_type = self.transaction_type.value

        product_id = self.product_id

        quantity = self.quantity

        sku = self.sku

        from_bin_id = self.from_bin_id

        to_bin_id = self.to_bin_id

        lot_number = self.lot_number

        license_plate_number = self.license_plate_number

        uom = self.uom

        reference_type: Union[Unset, str] = UNSET
        if not isinstance(self.reference_type, Unset):
            reference_type = self.reference_type.value

        reference_id = self.reference_id

        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        user_id = self.user_id

        user_name = self.user_name

        reason_code = self.reason_code

        notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "transactionType": transaction_type,
                "productId": product_id,
                "quantity": quantity,
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
        if transaction_date is not UNSET:
            field_dict["transactionDate"] = transaction_date
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
        from ..models.create_wms_inventory_transaction_body_custom_fields import (
            CreateWMSInventoryTransactionBodyCustomFields,
        )

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        transaction_type = CreateWMSInventoryTransactionBodyTransactionType(d.pop("transactionType"))

        product_id = d.pop("productId")

        quantity = d.pop("quantity")

        sku = d.pop("sku", UNSET)

        from_bin_id = d.pop("fromBinId", UNSET)

        to_bin_id = d.pop("toBinId", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        license_plate_number = d.pop("licensePlateNumber", UNSET)

        uom = d.pop("uom", UNSET)

        _reference_type = d.pop("referenceType", UNSET)
        reference_type: Union[Unset, CreateWMSInventoryTransactionBodyReferenceType]
        if isinstance(_reference_type, Unset):
            reference_type = UNSET
        else:
            reference_type = CreateWMSInventoryTransactionBodyReferenceType(_reference_type)

        reference_id = d.pop("referenceId", UNSET)

        _transaction_date = d.pop("transactionDate", UNSET)
        transaction_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date, Unset):
            transaction_date = UNSET
        else:
            transaction_date = isoparse(_transaction_date)

        user_id = d.pop("userId", UNSET)

        user_name = d.pop("userName", UNSET)

        reason_code = d.pop("reasonCode", UNSET)

        notes = d.pop("notes", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateWMSInventoryTransactionBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateWMSInventoryTransactionBodyCustomFields.from_dict(_custom_fields)

        create_wms_inventory_transaction_body = cls(
            warehouse_id=warehouse_id,
            transaction_type=transaction_type,
            product_id=product_id,
            quantity=quantity,
            sku=sku,
            from_bin_id=from_bin_id,
            to_bin_id=to_bin_id,
            lot_number=lot_number,
            license_plate_number=license_plate_number,
            uom=uom,
            reference_type=reference_type,
            reference_id=reference_id,
            transaction_date=transaction_date,
            user_id=user_id,
            user_name=user_name,
            reason_code=reason_code,
            notes=notes,
            custom_fields=custom_fields,
        )

        create_wms_inventory_transaction_body.additional_properties = d
        return create_wms_inventory_transaction_body

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
