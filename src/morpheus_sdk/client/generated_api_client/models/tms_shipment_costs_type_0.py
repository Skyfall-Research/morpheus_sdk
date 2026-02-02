from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentCostsType0")


@_attrs_define
class TMSShipmentCostsType0:
    """Shipment cost breakdown (optional, may be null if costs not yet calculated)

    Attributes:
        base_cost (Union[None, Unset, float]): Base freight cost Example: 1250.
        fuel_surcharge (Union[None, Unset, float]): Fuel surcharge amount Example: 125.5.
        accessorial_charges (Union[None, Unset, float]): Additional accessorial charges Example: 75.25.
        total_cost (Union[None, Unset, float]): Total shipment cost Example: 1450.75.
        currency (Union[Unset, str]): Currency code (ISO 4217) Example: USD.
        cost_per_mile (Union[None, Unset, float]): Cost per mile Example: 2.15.
    """

    base_cost: Union[None, Unset, float] = UNSET
    fuel_surcharge: Union[None, Unset, float] = UNSET
    accessorial_charges: Union[None, Unset, float] = UNSET
    total_cost: Union[None, Unset, float] = UNSET
    currency: Union[Unset, str] = UNSET
    cost_per_mile: Union[None, Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base_cost: Union[None, Unset, float]
        if isinstance(self.base_cost, Unset):
            base_cost = UNSET
        else:
            base_cost = self.base_cost

        fuel_surcharge: Union[None, Unset, float]
        if isinstance(self.fuel_surcharge, Unset):
            fuel_surcharge = UNSET
        else:
            fuel_surcharge = self.fuel_surcharge

        accessorial_charges: Union[None, Unset, float]
        if isinstance(self.accessorial_charges, Unset):
            accessorial_charges = UNSET
        else:
            accessorial_charges = self.accessorial_charges

        total_cost: Union[None, Unset, float]
        if isinstance(self.total_cost, Unset):
            total_cost = UNSET
        else:
            total_cost = self.total_cost

        currency = self.currency

        cost_per_mile: Union[None, Unset, float]
        if isinstance(self.cost_per_mile, Unset):
            cost_per_mile = UNSET
        else:
            cost_per_mile = self.cost_per_mile

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base_cost is not UNSET:
            field_dict["baseCost"] = base_cost
        if fuel_surcharge is not UNSET:
            field_dict["fuelSurcharge"] = fuel_surcharge
        if accessorial_charges is not UNSET:
            field_dict["accessorialCharges"] = accessorial_charges
        if total_cost is not UNSET:
            field_dict["totalCost"] = total_cost
        if currency is not UNSET:
            field_dict["currency"] = currency
        if cost_per_mile is not UNSET:
            field_dict["costPerMile"] = cost_per_mile

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_base_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        base_cost = _parse_base_cost(d.pop("baseCost", UNSET))

        def _parse_fuel_surcharge(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        fuel_surcharge = _parse_fuel_surcharge(d.pop("fuelSurcharge", UNSET))

        def _parse_accessorial_charges(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        accessorial_charges = _parse_accessorial_charges(d.pop("accessorialCharges", UNSET))

        def _parse_total_cost(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        total_cost = _parse_total_cost(d.pop("totalCost", UNSET))

        currency = d.pop("currency", UNSET)

        def _parse_cost_per_mile(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_per_mile = _parse_cost_per_mile(d.pop("costPerMile", UNSET))

        tms_shipment_costs_type_0 = cls(
            base_cost=base_cost,
            fuel_surcharge=fuel_surcharge,
            accessorial_charges=accessorial_charges,
            total_cost=total_cost,
            currency=currency,
            cost_per_mile=cost_per_mile,
        )

        tms_shipment_costs_type_0.additional_properties = d
        return tms_shipment_costs_type_0

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
