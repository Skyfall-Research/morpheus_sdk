from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateERPShipmentBodyCarrier")


@_attrs_define
class UpdateERPShipmentBodyCarrier:
    """Updated carrier information

    Attributes:
        name (Union[Unset, str]):  Example: UPS.
        scac (Union[Unset, str]):  Example: UPGF.
        mode (Union[Unset, str]):  Example: Ground.
    """

    name: Union[Unset, str] = UNSET
    scac: Union[Unset, str] = UNSET
    mode: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        scac = self.scac

        mode = self.mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if scac is not UNSET:
            field_dict["scac"] = scac
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        scac = d.pop("scac", UNSET)

        mode = d.pop("mode", UNSET)

        update_erp_shipment_body_carrier = cls(
            name=name,
            scac=scac,
            mode=mode,
        )

        update_erp_shipment_body_carrier.additional_properties = d
        return update_erp_shipment_body_carrier

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
