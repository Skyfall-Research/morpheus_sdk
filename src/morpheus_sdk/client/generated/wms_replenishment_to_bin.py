from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSReplenishmentToBin")


@_attrs_define
class WMSReplenishmentToBin:
    """Destination bin details with capacity constraints

    Attributes:
        bin_id (str): Destination bin identifier Example: BIN-P001.
        bin_code (Union[Unset, str]): Human-readable bin location code Example: P-001.
        current_quantity (Union[Unset, float]): Current quantity in destination bin Example: 50.
        min_quantity (Union[Unset, float]): Minimum quantity threshold triggering replenishment Example: 100.
        max_quantity (Union[Unset, float]): Maximum capacity of destination bin Example: 200.
    """

    bin_id: str
    bin_code: Union[Unset, str] = UNSET
    current_quantity: Union[Unset, float] = UNSET
    min_quantity: Union[Unset, float] = UNSET
    max_quantity: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_id = self.bin_id

        bin_code = self.bin_code

        current_quantity = self.current_quantity

        min_quantity = self.min_quantity

        max_quantity = self.max_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "binId": bin_id,
            }
        )
        if bin_code is not UNSET:
            field_dict["binCode"] = bin_code
        if current_quantity is not UNSET:
            field_dict["currentQuantity"] = current_quantity
        if min_quantity is not UNSET:
            field_dict["minQuantity"] = min_quantity
        if max_quantity is not UNSET:
            field_dict["maxQuantity"] = max_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bin_id = d.pop("binId")

        bin_code = d.pop("binCode", UNSET)

        current_quantity = d.pop("currentQuantity", UNSET)

        min_quantity = d.pop("minQuantity", UNSET)

        max_quantity = d.pop("maxQuantity", UNSET)

        wms_replenishment_to_bin = cls(
            bin_id=bin_id,
            bin_code=bin_code,
            current_quantity=current_quantity,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
        )

        wms_replenishment_to_bin.additional_properties = d
        return wms_replenishment_to_bin

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
