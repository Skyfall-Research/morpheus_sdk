import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSCycleCountCountsItem")


@_attrs_define
class WMSCycleCountCountsItem:
    """
    Attributes:
        bin_id (Union[Unset, str]): Bin identifier where count was performed Example: BIN_ATL_A01_001.
        product_id (Union[Unset, str]): Product identifier for counted item Example: PROD_12345.
        sku (Union[Unset, str]): SKU identifier for product Example: SKU-WIDGET-001.
        lot_number (Union[Unset, str]): Lot number for batch tracking (if applicable) Example: LOT-2024-001.
        system_quantity (Union[Unset, float]): Expected quantity from system records Example: 150.
        counted_quantity (Union[Unset, float]): Actual counted quantity Example: 148.
        variance (Union[Unset, float]): Calculated variance (countedQuantity - systemQuantity) Example: -2.
        variance_percent (Union[Unset, float]): Variance as percentage of system quantity Example: -1.33.
        counted_by (Union[Unset, str]): User who performed the count Example: USER_001.
        counted_at (Union[Unset, datetime.datetime]): Timestamp when count was performed Example:
            2024-01-25T14:30:00.000Z.
        reconciled_by (Union[Unset, str]): User who reconciled variance (if applicable) Example: SUPERVISOR_001.
        reconciled_at (Union[Unset, datetime.datetime]): Timestamp when variance was reconciled Example:
            2024-01-25T16:15:00.000Z.
        notes (Union[Unset, str]): Notes about count or variance explanation Example: Found damaged units, excluded from
            count.
    """

    bin_id: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    system_quantity: Union[Unset, float] = UNSET
    counted_quantity: Union[Unset, float] = UNSET
    variance: Union[Unset, float] = UNSET
    variance_percent: Union[Unset, float] = UNSET
    counted_by: Union[Unset, str] = UNSET
    counted_at: Union[Unset, datetime.datetime] = UNSET
    reconciled_by: Union[Unset, str] = UNSET
    reconciled_at: Union[Unset, datetime.datetime] = UNSET
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_id = self.bin_id

        product_id = self.product_id

        sku = self.sku

        lot_number = self.lot_number

        system_quantity = self.system_quantity

        counted_quantity = self.counted_quantity

        variance = self.variance

        variance_percent = self.variance_percent

        counted_by = self.counted_by

        counted_at: Union[Unset, str] = UNSET
        if not isinstance(self.counted_at, Unset):
            counted_at = self.counted_at.isoformat()

        reconciled_by = self.reconciled_by

        reconciled_at: Union[Unset, str] = UNSET
        if not isinstance(self.reconciled_at, Unset):
            reconciled_at = self.reconciled_at.isoformat()

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_id is not UNSET:
            field_dict["binId"] = bin_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if system_quantity is not UNSET:
            field_dict["systemQuantity"] = system_quantity
        if counted_quantity is not UNSET:
            field_dict["countedQuantity"] = counted_quantity
        if variance is not UNSET:
            field_dict["variance"] = variance
        if variance_percent is not UNSET:
            field_dict["variancePercent"] = variance_percent
        if counted_by is not UNSET:
            field_dict["countedBy"] = counted_by
        if counted_at is not UNSET:
            field_dict["countedAt"] = counted_at
        if reconciled_by is not UNSET:
            field_dict["reconciledBy"] = reconciled_by
        if reconciled_at is not UNSET:
            field_dict["reconciledAt"] = reconciled_at
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bin_id = d.pop("binId", UNSET)

        product_id = d.pop("productId", UNSET)

        sku = d.pop("sku", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        system_quantity = d.pop("systemQuantity", UNSET)

        counted_quantity = d.pop("countedQuantity", UNSET)

        variance = d.pop("variance", UNSET)

        variance_percent = d.pop("variancePercent", UNSET)

        counted_by = d.pop("countedBy", UNSET)

        _counted_at = d.pop("countedAt", UNSET)
        counted_at: Union[Unset, datetime.datetime]
        if isinstance(_counted_at, Unset):
            counted_at = UNSET
        else:
            counted_at = isoparse(_counted_at)

        reconciled_by = d.pop("reconciledBy", UNSET)

        _reconciled_at = d.pop("reconciledAt", UNSET)
        reconciled_at: Union[Unset, datetime.datetime]
        if isinstance(_reconciled_at, Unset):
            reconciled_at = UNSET
        else:
            reconciled_at = isoparse(_reconciled_at)

        notes = d.pop("notes", UNSET)

        wms_cycle_count_counts_item = cls(
            bin_id=bin_id,
            product_id=product_id,
            sku=sku,
            lot_number=lot_number,
            system_quantity=system_quantity,
            counted_quantity=counted_quantity,
            variance=variance,
            variance_percent=variance_percent,
            counted_by=counted_by,
            counted_at=counted_at,
            reconciled_by=reconciled_by,
            reconciled_at=reconciled_at,
            notes=notes,
        )

        wms_cycle_count_counts_item.additional_properties = d
        return wms_cycle_count_counts_item

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
