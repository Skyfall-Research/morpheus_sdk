from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSBinCapacity")


@_attrs_define
class WMSBinCapacity:
    """Storage capacity constraints and limits

    Attributes:
        max_weight_lbs (Union[Unset, float]): Maximum weight capacity in pounds Example: 2000.
        max_cubic_feet (Union[Unset, float]): Maximum volume capacity in cubic feet Example: 50.5.
        max_pallets (Union[Unset, int]): Maximum pallet capacity Example: 1.
    """

    max_weight_lbs: Union[Unset, float] = UNSET
    max_cubic_feet: Union[Unset, float] = UNSET
    max_pallets: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_weight_lbs = self.max_weight_lbs

        max_cubic_feet = self.max_cubic_feet

        max_pallets = self.max_pallets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_weight_lbs is not UNSET:
            field_dict["maxWeightLbs"] = max_weight_lbs
        if max_cubic_feet is not UNSET:
            field_dict["maxCubicFeet"] = max_cubic_feet
        if max_pallets is not UNSET:
            field_dict["maxPallets"] = max_pallets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        max_weight_lbs = d.pop("maxWeightLbs", UNSET)

        max_cubic_feet = d.pop("maxCubicFeet", UNSET)

        max_pallets = d.pop("maxPallets", UNSET)

        wms_bin_capacity = cls(
            max_weight_lbs=max_weight_lbs,
            max_cubic_feet=max_cubic_feet,
            max_pallets=max_pallets,
        )

        wms_bin_capacity.additional_properties = d
        return wms_bin_capacity

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
