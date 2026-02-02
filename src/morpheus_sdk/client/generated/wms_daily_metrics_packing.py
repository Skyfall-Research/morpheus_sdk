from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDailyMetricsPacking")


@_attrs_define
class WMSDailyMetricsPacking:
    """Packing operation metrics

    Attributes:
        orders_packed (Union[Unset, float]): Number of orders packed Example: 120.
        packages_packed (Union[Unset, float]): Number of packages packed Example: 98.
        packing_hours (Union[Unset, float]): Total packing labor hours Example: 24.
        orders_per_hour (Union[Unset, float]): Packing productivity - orders per hour Example: 5.
    """

    orders_packed: Union[Unset, float] = UNSET
    packages_packed: Union[Unset, float] = UNSET
    packing_hours: Union[Unset, float] = UNSET
    orders_per_hour: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders_packed = self.orders_packed

        packages_packed = self.packages_packed

        packing_hours = self.packing_hours

        orders_per_hour = self.orders_per_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders_packed is not UNSET:
            field_dict["ordersPacked"] = orders_packed
        if packages_packed is not UNSET:
            field_dict["packagesPacked"] = packages_packed
        if packing_hours is not UNSET:
            field_dict["packingHours"] = packing_hours
        if orders_per_hour is not UNSET:
            field_dict["ordersPerHour"] = orders_per_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        orders_packed = d.pop("ordersPacked", UNSET)

        packages_packed = d.pop("packagesPacked", UNSET)

        packing_hours = d.pop("packingHours", UNSET)

        orders_per_hour = d.pop("ordersPerHour", UNSET)

        wms_daily_metrics_packing = cls(
            orders_packed=orders_packed,
            packages_packed=packages_packed,
            packing_hours=packing_hours,
            orders_per_hour=orders_per_hour,
        )

        wms_daily_metrics_packing.additional_properties = d
        return wms_daily_metrics_packing

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
