from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSInboundOrderTotalsType0")


@_attrs_define
class WMSInboundOrderTotalsType0:
    """Order totals for capacity planning and resource allocation

    Attributes:
        pallets (Union[Unset, float]): Total number of pallets expected for space planning Example: 5.
        cases (Union[Unset, float]): Total number of cases expected for handling planning Example: 120.
        units (Union[Unset, float]): Total number of individual units for inventory planning Example: 2400.
        expected_lines (Union[Unset, float]): Number of different product lines for processing planning Example: 8.
        received_lines (Union[Unset, float]): Number of product lines completely received Example: 6.
    """

    pallets: Union[Unset, float] = UNSET
    cases: Union[Unset, float] = UNSET
    units: Union[Unset, float] = UNSET
    expected_lines: Union[Unset, float] = UNSET
    received_lines: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pallets = self.pallets

        cases = self.cases

        units = self.units

        expected_lines = self.expected_lines

        received_lines = self.received_lines

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pallets is not UNSET:
            field_dict["pallets"] = pallets
        if cases is not UNSET:
            field_dict["cases"] = cases
        if units is not UNSET:
            field_dict["units"] = units
        if expected_lines is not UNSET:
            field_dict["expectedLines"] = expected_lines
        if received_lines is not UNSET:
            field_dict["receivedLines"] = received_lines

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pallets = d.pop("pallets", UNSET)

        cases = d.pop("cases", UNSET)

        units = d.pop("units", UNSET)

        expected_lines = d.pop("expectedLines", UNSET)

        received_lines = d.pop("receivedLines", UNSET)

        wms_inbound_order_totals_type_0 = cls(
            pallets=pallets,
            cases=cases,
            units=units,
            expected_lines=expected_lines,
            received_lines=received_lines,
        )

        wms_inbound_order_totals_type_0.additional_properties = d
        return wms_inbound_order_totals_type_0

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
