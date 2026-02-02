from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSReplenishmentBodyFromBin")


@_attrs_define
class CreateWMSReplenishmentBodyFromBin:
    """Source bin details with availability

    Attributes:
        bin_id (Union[Unset, str]):  Example: BIN-A001.
        bin_code (Union[Unset, str]):  Example: A-001.
        available_quantity (Union[Unset, float]):  Example: 500.
        current_quantity (Union[Unset, float]):  Example: 1000.
    """

    bin_id: Union[Unset, str] = UNSET
    bin_code: Union[Unset, str] = UNSET
    available_quantity: Union[Unset, float] = UNSET
    current_quantity: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_id = self.bin_id

        bin_code = self.bin_code

        available_quantity = self.available_quantity

        current_quantity = self.current_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bin_id is not UNSET:
            field_dict["binId"] = bin_id
        if bin_code is not UNSET:
            field_dict["binCode"] = bin_code
        if available_quantity is not UNSET:
            field_dict["availableQuantity"] = available_quantity
        if current_quantity is not UNSET:
            field_dict["currentQuantity"] = current_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bin_id = d.pop("binId", UNSET)

        bin_code = d.pop("binCode", UNSET)

        available_quantity = d.pop("availableQuantity", UNSET)

        current_quantity = d.pop("currentQuantity", UNSET)

        create_wms_replenishment_body_from_bin = cls(
            bin_id=bin_id,
            bin_code=bin_code,
            available_quantity=available_quantity,
            current_quantity=current_quantity,
        )

        create_wms_replenishment_body_from_bin.additional_properties = d
        return create_wms_replenishment_body_from_bin

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
