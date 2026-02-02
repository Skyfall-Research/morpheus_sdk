import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInventoryListResponse200DataItemsItem")


@_attrs_define
class GetWMSInventoryListResponse200DataItemsItem:
    """
    Attributes:
        inventory_id (Union[Unset, str]):  Example: wms_inventory_674565c1234567890abcdef.
        sku (Union[Unset, str]):  Example: WIDGET-001.
        product_name (Union[Unset, str]):  Example: Premium Widget.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        bin_id (Union[Unset, str]):  Example: BIN-A01-01-01.
        quantity_on_hand (Union[Unset, int]):  Example: 150.
        quantity_allocated (Union[Unset, int]):  Example: 25.
        quantity_available (Union[Unset, int]):  Example: 125.
        inventory_status (Union[Unset, str]):  Example: AVAILABLE.
        lot_number (Union[Unset, str]):  Example: LOT-2024-001.
        expiration_date (Union[Unset, datetime.datetime]):  Example: 2025-06-30T00:00:00Z.
        last_movement_at (Union[Unset, datetime.datetime]):  Example: 2024-01-15T14:30:00Z.
    """

    inventory_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    warehouse_id: Union[Unset, str] = UNSET
    bin_id: Union[Unset, str] = UNSET
    quantity_on_hand: Union[Unset, int] = UNSET
    quantity_allocated: Union[Unset, int] = UNSET
    quantity_available: Union[Unset, int] = UNSET
    inventory_status: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    last_movement_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory_id = self.inventory_id

        sku = self.sku

        product_name = self.product_name

        warehouse_id = self.warehouse_id

        bin_id = self.bin_id

        quantity_on_hand = self.quantity_on_hand

        quantity_allocated = self.quantity_allocated

        quantity_available = self.quantity_available

        inventory_status = self.inventory_status

        lot_number = self.lot_number

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        last_movement_at: Union[Unset, str] = UNSET
        if not isinstance(self.last_movement_at, Unset):
            last_movement_at = self.last_movement_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory_id is not UNSET:
            field_dict["inventoryId"] = inventory_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if product_name is not UNSET:
            field_dict["productName"] = product_name
        if warehouse_id is not UNSET:
            field_dict["warehouseId"] = warehouse_id
        if bin_id is not UNSET:
            field_dict["binId"] = bin_id
        if quantity_on_hand is not UNSET:
            field_dict["quantityOnHand"] = quantity_on_hand
        if quantity_allocated is not UNSET:
            field_dict["quantityAllocated"] = quantity_allocated
        if quantity_available is not UNSET:
            field_dict["quantityAvailable"] = quantity_available
        if inventory_status is not UNSET:
            field_dict["inventoryStatus"] = inventory_status
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if last_movement_at is not UNSET:
            field_dict["lastMovementAt"] = last_movement_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        inventory_id = d.pop("inventoryId", UNSET)

        sku = d.pop("sku", UNSET)

        product_name = d.pop("productName", UNSET)

        warehouse_id = d.pop("warehouseId", UNSET)

        bin_id = d.pop("binId", UNSET)

        quantity_on_hand = d.pop("quantityOnHand", UNSET)

        quantity_allocated = d.pop("quantityAllocated", UNSET)

        quantity_available = d.pop("quantityAvailable", UNSET)

        inventory_status = d.pop("inventoryStatus", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        _last_movement_at = d.pop("lastMovementAt", UNSET)
        last_movement_at: Union[Unset, datetime.datetime]
        if isinstance(_last_movement_at, Unset):
            last_movement_at = UNSET
        else:
            last_movement_at = isoparse(_last_movement_at)

        get_wms_inventory_list_response_200_data_items_item = cls(
            inventory_id=inventory_id,
            sku=sku,
            product_name=product_name,
            warehouse_id=warehouse_id,
            bin_id=bin_id,
            quantity_on_hand=quantity_on_hand,
            quantity_allocated=quantity_allocated,
            quantity_available=quantity_available,
            inventory_status=inventory_status,
            lot_number=lot_number,
            expiration_date=expiration_date,
            last_movement_at=last_movement_at,
        )

        get_wms_inventory_list_response_200_data_items_item.additional_properties = d
        return get_wms_inventory_list_response_200_data_items_item

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
