from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWMSDailyMetricsBodyPicking")


@_attrs_define
class UpdateWMSDailyMetricsBodyPicking:
    """Updated picking operation metrics

    Attributes:
        pick_accuracy (Union[Unset, float]):  Example: 99.4.
        orders_shipped (Union[Unset, float]):  Example: 128.
    """

    pick_accuracy: Union[Unset, float] = UNSET
    orders_shipped: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pick_accuracy = self.pick_accuracy

        orders_shipped = self.orders_shipped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pick_accuracy is not UNSET:
            field_dict["pickAccuracy"] = pick_accuracy
        if orders_shipped is not UNSET:
            field_dict["ordersShipped"] = orders_shipped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pick_accuracy = d.pop("pickAccuracy", UNSET)

        orders_shipped = d.pop("ordersShipped", UNSET)

        update_wms_daily_metrics_body_picking = cls(
            pick_accuracy=pick_accuracy,
            orders_shipped=orders_shipped,
        )

        update_wms_daily_metrics_body_picking.additional_properties = d
        return update_wms_daily_metrics_body_picking

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
