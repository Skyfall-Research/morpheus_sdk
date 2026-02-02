from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateERPShipmentBodyPackaging")


@_attrs_define
class UpdateERPShipmentBodyPackaging:
    """Updated packaging information

    Attributes:
        pallet_count (Union[Unset, float]):  Example: 3.
        total_packages (Union[Unset, float]):  Example: 12.
        packaging_type (Union[Unset, str]):  Example: PALLET.
    """

    pallet_count: Union[Unset, float] = UNSET
    total_packages: Union[Unset, float] = UNSET
    packaging_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pallet_count = self.pallet_count

        total_packages = self.total_packages

        packaging_type = self.packaging_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pallet_count is not UNSET:
            field_dict["palletCount"] = pallet_count
        if total_packages is not UNSET:
            field_dict["totalPackages"] = total_packages
        if packaging_type is not UNSET:
            field_dict["packagingType"] = packaging_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pallet_count = d.pop("palletCount", UNSET)

        total_packages = d.pop("totalPackages", UNSET)

        packaging_type = d.pop("packagingType", UNSET)

        update_erp_shipment_body_packaging = cls(
            pallet_count=pallet_count,
            total_packages=total_packages,
            packaging_type=packaging_type,
        )

        update_erp_shipment_body_packaging.additional_properties = d
        return update_erp_shipment_body_packaging

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
