import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.patch_wms_inventory_body_inventory_status import PatchWMSInventoryBodyInventoryStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchWMSInventoryBody")


@_attrs_define
class PatchWMSInventoryBody:
    """
    Attributes:
        inventory_status (Union[Unset, PatchWMSInventoryBodyInventoryStatus]): New status for the inventory
        lot_number (Union[Unset, str]): Lot number for batch tracking Example: LOT-2024-001.
        expiration_date (Union[Unset, datetime.datetime]): Expiration date for perishable items Example:
            2025-06-30T00:00:00Z.
        bin_id (Union[Unset, str]): New bin location for the inventory Example: BIN-A01-01-01.
    """

    inventory_status: Union[Unset, PatchWMSInventoryBodyInventoryStatus] = UNSET
    lot_number: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    bin_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        inventory_status: Union[Unset, str] = UNSET
        if not isinstance(self.inventory_status, Unset):
            inventory_status = self.inventory_status.value

        lot_number = self.lot_number

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        bin_id = self.bin_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if inventory_status is not UNSET:
            field_dict["inventoryStatus"] = inventory_status
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if bin_id is not UNSET:
            field_dict["binId"] = bin_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _inventory_status = d.pop("inventoryStatus", UNSET)
        inventory_status: Union[Unset, PatchWMSInventoryBodyInventoryStatus]
        if isinstance(_inventory_status, Unset):
            inventory_status = UNSET
        else:
            inventory_status = PatchWMSInventoryBodyInventoryStatus(_inventory_status)

        lot_number = d.pop("lotNumber", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        bin_id = d.pop("binId", UNSET)

        patch_wms_inventory_body = cls(
            inventory_status=inventory_status,
            lot_number=lot_number,
            expiration_date=expiration_date,
            bin_id=bin_id,
        )

        patch_wms_inventory_body.additional_properties = d
        return patch_wms_inventory_body

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
