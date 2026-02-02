from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDailyMetricsInventory")


@_attrs_define
class WMSDailyMetricsInventory:
    """Inventory management metrics

    Attributes:
        on_hand_units (Union[Unset, float]): Total units on hand Example: 45890.
        inventory_value (Union[Unset, float]): Total inventory value in dollars Example: 2456780.5.
        turnover_rate (Union[Unset, float]): Inventory turnover rate Example: 8.4.
    """

    on_hand_units: Union[Unset, float] = UNSET
    inventory_value: Union[Unset, float] = UNSET
    turnover_rate: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on_hand_units = self.on_hand_units

        inventory_value = self.inventory_value

        turnover_rate = self.turnover_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if on_hand_units is not UNSET:
            field_dict["onHandUnits"] = on_hand_units
        if inventory_value is not UNSET:
            field_dict["inventoryValue"] = inventory_value
        if turnover_rate is not UNSET:
            field_dict["turnoverRate"] = turnover_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        on_hand_units = d.pop("onHandUnits", UNSET)

        inventory_value = d.pop("inventoryValue", UNSET)

        turnover_rate = d.pop("turnoverRate", UNSET)

        wms_daily_metrics_inventory = cls(
            on_hand_units=on_hand_units,
            inventory_value=inventory_value,
            turnover_rate=turnover_rate,
        )

        wms_daily_metrics_inventory.additional_properties = d
        return wms_daily_metrics_inventory

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
