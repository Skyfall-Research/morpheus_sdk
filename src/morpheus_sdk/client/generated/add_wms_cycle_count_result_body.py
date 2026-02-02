import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddWMSCycleCountResultBody")


@_attrs_define
class AddWMSCycleCountResultBody:
    """
    Attributes:
        bin_id (str): Bin identifier where count was performed Example: BIN_ATL_A01_001.
        product_id (str): Product identifier for counted item Example: PROD_12345.
        sku (str): SKU identifier for product identification Example: SKU-WIDGET-001.
        expected_quantity (float): Expected quantity from system records Example: 150.
        actual_quantity (float): Actual counted quantity Example: 148.
        variance (float): Calculated variance (actualQuantity - expectedQuantity) Example: -2.
        counted_by (str): User identifier who performed the count Example: USER_001.
        counted_at (datetime.datetime): Timestamp when count was performed Example: 2024-01-25T14:30:00.000Z.
        notes (Union[Unset, str]): Optional notes about count or observed discrepancies Example: Found damaged units,
            excluded from count.
    """

    bin_id: str
    product_id: str
    sku: str
    expected_quantity: float
    actual_quantity: float
    variance: float
    counted_by: str
    counted_at: datetime.datetime
    notes: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_id = self.bin_id

        product_id = self.product_id

        sku = self.sku

        expected_quantity = self.expected_quantity

        actual_quantity = self.actual_quantity

        variance = self.variance

        counted_by = self.counted_by

        counted_at = self.counted_at.isoformat()

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "binId": bin_id,
                "productId": product_id,
                "sku": sku,
                "expectedQuantity": expected_quantity,
                "actualQuantity": actual_quantity,
                "variance": variance,
                "countedBy": counted_by,
                "countedAt": counted_at,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bin_id = d.pop("binId")

        product_id = d.pop("productId")

        sku = d.pop("sku")

        expected_quantity = d.pop("expectedQuantity")

        actual_quantity = d.pop("actualQuantity")

        variance = d.pop("variance")

        counted_by = d.pop("countedBy")

        counted_at = isoparse(d.pop("countedAt"))

        notes = d.pop("notes", UNSET)

        add_wms_cycle_count_result_body = cls(
            bin_id=bin_id,
            product_id=product_id,
            sku=sku,
            expected_quantity=expected_quantity,
            actual_quantity=actual_quantity,
            variance=variance,
            counted_by=counted_by,
            counted_at=counted_at,
            notes=notes,
        )

        add_wms_cycle_count_result_body.additional_properties = d
        return add_wms_cycle_count_result_body

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
