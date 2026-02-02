from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundShipmentTotals")


@_attrs_define
class WMSOutboundShipmentTotals:
    """Shipment totals and logistics metrics

    Attributes:
        packages (Union[Unset, float]): Total package count Example: 5.
        pallets (Union[Unset, float]): Total pallet count Example: 2.
        weight (Union[Unset, float]): Total shipment weight Example: 150.5.
        cube (Union[Unset, float]): Total cubic volume Example: 12.3.
        value (Union[Unset, float]): Total shipment value Example: 1249.99.
    """

    packages: Union[Unset, float] = UNSET
    pallets: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    cube: Union[Unset, float] = UNSET
    value: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        packages = self.packages

        pallets = self.pallets

        weight = self.weight

        cube = self.cube

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if packages is not UNSET:
            field_dict["packages"] = packages
        if pallets is not UNSET:
            field_dict["pallets"] = pallets
        if weight is not UNSET:
            field_dict["weight"] = weight
        if cube is not UNSET:
            field_dict["cube"] = cube
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        packages = d.pop("packages", UNSET)

        pallets = d.pop("pallets", UNSET)

        weight = d.pop("weight", UNSET)

        cube = d.pop("cube", UNSET)

        value = d.pop("value", UNSET)

        wms_outbound_shipment_totals = cls(
            packages=packages,
            pallets=pallets,
            weight=weight,
            cube=cube,
            value=value,
        )

        wms_outbound_shipment_totals.additional_properties = d
        return wms_outbound_shipment_totals

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
