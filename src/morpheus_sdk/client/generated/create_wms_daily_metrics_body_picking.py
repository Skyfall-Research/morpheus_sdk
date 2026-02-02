from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSDailyMetricsBodyPicking")


@_attrs_define
class CreateWMSDailyMetricsBodyPicking:
    """Picking operation metrics

    Attributes:
        orders_shipped (Union[Unset, float]): Number of orders shipped Example: 125.
        lines_picked (Union[Unset, float]): Number of lines picked Example: 890.
        units_picked (Union[Unset, float]): Total units picked Example: 2240.
        picking_hours (Union[Unset, float]): Total picking hours Example: 45.5.
        lines_per_hour (Union[Unset, float]): Lines picked per hour Example: 19.6.
        units_per_hour (Union[Unset, float]): Units picked per hour Example: 49.2.
        pick_accuracy (Union[Unset, float]): Pick accuracy percentage Example: 99.2.
    """

    orders_shipped: Union[Unset, float] = UNSET
    lines_picked: Union[Unset, float] = UNSET
    units_picked: Union[Unset, float] = UNSET
    picking_hours: Union[Unset, float] = UNSET
    lines_per_hour: Union[Unset, float] = UNSET
    units_per_hour: Union[Unset, float] = UNSET
    pick_accuracy: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders_shipped = self.orders_shipped

        lines_picked = self.lines_picked

        units_picked = self.units_picked

        picking_hours = self.picking_hours

        lines_per_hour = self.lines_per_hour

        units_per_hour = self.units_per_hour

        pick_accuracy = self.pick_accuracy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders_shipped is not UNSET:
            field_dict["ordersShipped"] = orders_shipped
        if lines_picked is not UNSET:
            field_dict["linesPicked"] = lines_picked
        if units_picked is not UNSET:
            field_dict["unitsPicked"] = units_picked
        if picking_hours is not UNSET:
            field_dict["pickingHours"] = picking_hours
        if lines_per_hour is not UNSET:
            field_dict["linesPerHour"] = lines_per_hour
        if units_per_hour is not UNSET:
            field_dict["unitsPerHour"] = units_per_hour
        if pick_accuracy is not UNSET:
            field_dict["pickAccuracy"] = pick_accuracy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        orders_shipped = d.pop("ordersShipped", UNSET)

        lines_picked = d.pop("linesPicked", UNSET)

        units_picked = d.pop("unitsPicked", UNSET)

        picking_hours = d.pop("pickingHours", UNSET)

        lines_per_hour = d.pop("linesPerHour", UNSET)

        units_per_hour = d.pop("unitsPerHour", UNSET)

        pick_accuracy = d.pop("pickAccuracy", UNSET)

        create_wms_daily_metrics_body_picking = cls(
            orders_shipped=orders_shipped,
            lines_picked=lines_picked,
            units_picked=units_picked,
            picking_hours=picking_hours,
            lines_per_hour=lines_per_hour,
            units_per_hour=units_per_hour,
            pick_accuracy=pick_accuracy,
        )

        create_wms_daily_metrics_body_picking.additional_properties = d
        return create_wms_daily_metrics_body_picking

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
