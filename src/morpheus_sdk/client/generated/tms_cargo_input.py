from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSCargoInput")


@_attrs_define
class TMSCargoInput:
    """Input data for TMS cargo

    Attributes:
        total_weight (Union[Unset, float]):  Example: 15000.
        total_weight_uom (Union[Unset, str]):  Example: LBS.
        total_volume (Union[Unset, float]):  Example: 800.
        total_volume_uom (Union[Unset, str]):  Example: CUFT.
        pallet_count (Union[Unset, int]):  Example: 20.
        package_count (Union[Unset, int]):  Example: 100.
        commodity_type (Union[Unset, str]):  Example: General Merchandise.
        hazmat (Union[Unset, bool]):
        temperature_controlled (Union[Unset, bool]):
    """

    total_weight: Union[Unset, float] = UNSET
    total_weight_uom: Union[Unset, str] = UNSET
    total_volume: Union[Unset, float] = UNSET
    total_volume_uom: Union[Unset, str] = UNSET
    pallet_count: Union[Unset, int] = UNSET
    package_count: Union[Unset, int] = UNSET
    commodity_type: Union[Unset, str] = UNSET
    hazmat: Union[Unset, bool] = UNSET
    temperature_controlled: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_weight = self.total_weight

        total_weight_uom = self.total_weight_uom

        total_volume = self.total_volume

        total_volume_uom = self.total_volume_uom

        pallet_count = self.pallet_count

        package_count = self.package_count

        commodity_type = self.commodity_type

        hazmat = self.hazmat

        temperature_controlled = self.temperature_controlled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_weight is not UNSET:
            field_dict["totalWeight"] = total_weight
        if total_weight_uom is not UNSET:
            field_dict["totalWeightUOM"] = total_weight_uom
        if total_volume is not UNSET:
            field_dict["totalVolume"] = total_volume
        if total_volume_uom is not UNSET:
            field_dict["totalVolumeUOM"] = total_volume_uom
        if pallet_count is not UNSET:
            field_dict["palletCount"] = pallet_count
        if package_count is not UNSET:
            field_dict["packageCount"] = package_count
        if commodity_type is not UNSET:
            field_dict["commodityType"] = commodity_type
        if hazmat is not UNSET:
            field_dict["hazmat"] = hazmat
        if temperature_controlled is not UNSET:
            field_dict["temperatureControlled"] = temperature_controlled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_weight = d.pop("totalWeight", UNSET)

        total_weight_uom = d.pop("totalWeightUOM", UNSET)

        total_volume = d.pop("totalVolume", UNSET)

        total_volume_uom = d.pop("totalVolumeUOM", UNSET)

        pallet_count = d.pop("palletCount", UNSET)

        package_count = d.pop("packageCount", UNSET)

        commodity_type = d.pop("commodityType", UNSET)

        hazmat = d.pop("hazmat", UNSET)

        temperature_controlled = d.pop("temperatureControlled", UNSET)

        tms_cargo_input = cls(
            total_weight=total_weight,
            total_weight_uom=total_weight_uom,
            total_volume=total_volume,
            total_volume_uom=total_volume_uom,
            pallet_count=pallet_count,
            package_count=package_count,
            commodity_type=commodity_type,
            hazmat=hazmat,
            temperature_controlled=temperature_controlled,
        )

        tms_cargo_input.additional_properties = d
        return tms_cargo_input

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
