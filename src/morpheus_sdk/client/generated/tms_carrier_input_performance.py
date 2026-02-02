from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSCarrierInputPerformance")


@_attrs_define
class TMSCarrierInputPerformance:
    """Initial performance metrics (optional)

    Attributes:
        on_time_delivery_rate (Union[Unset, float]): Percentage of on-time deliveries (0-1) Example: 0.95.
        damage_claim_rate (Union[Unset, float]): Percentage of shipments with damage claims (0-1) Example: 0.002.
        total_shipments_completed (Union[Unset, int]): Total number of completed shipments
    """

    on_time_delivery_rate: Union[Unset, float] = UNSET
    damage_claim_rate: Union[Unset, float] = UNSET
    total_shipments_completed: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        on_time_delivery_rate = self.on_time_delivery_rate

        damage_claim_rate = self.damage_claim_rate

        total_shipments_completed = self.total_shipments_completed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if on_time_delivery_rate is not UNSET:
            field_dict["onTimeDeliveryRate"] = on_time_delivery_rate
        if damage_claim_rate is not UNSET:
            field_dict["damageClaimRate"] = damage_claim_rate
        if total_shipments_completed is not UNSET:
            field_dict["totalShipmentsCompleted"] = total_shipments_completed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        on_time_delivery_rate = d.pop("onTimeDeliveryRate", UNSET)

        damage_claim_rate = d.pop("damageClaimRate", UNSET)

        total_shipments_completed = d.pop("totalShipmentsCompleted", UNSET)

        tms_carrier_input_performance = cls(
            on_time_delivery_rate=on_time_delivery_rate,
            damage_claim_rate=damage_claim_rate,
            total_shipments_completed=total_shipments_completed,
        )

        tms_carrier_input_performance.additional_properties = d
        return tms_carrier_input_performance

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
