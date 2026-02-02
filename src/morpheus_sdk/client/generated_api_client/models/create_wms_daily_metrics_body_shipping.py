from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSDailyMetricsBodyShipping")


@_attrs_define
class CreateWMSDailyMetricsBodyShipping:
    """Shipping operation metrics

    Attributes:
        shipments_created (Union[Unset, float]): Number of shipments created Example: 85.
        carriers_dispatched (Union[Unset, float]): Number of carriers dispatched Example: 12.
        packages_shipped (Union[Unset, float]): Total packages shipped Example: 96.
    """

    shipments_created: Union[Unset, float] = UNSET
    carriers_dispatched: Union[Unset, float] = UNSET
    packages_shipped: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        shipments_created = self.shipments_created

        carriers_dispatched = self.carriers_dispatched

        packages_shipped = self.packages_shipped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if shipments_created is not UNSET:
            field_dict["shipmentsCreated"] = shipments_created
        if carriers_dispatched is not UNSET:
            field_dict["carriersDispatched"] = carriers_dispatched
        if packages_shipped is not UNSET:
            field_dict["packagesShipped"] = packages_shipped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        shipments_created = d.pop("shipmentsCreated", UNSET)

        carriers_dispatched = d.pop("carriersDispatched", UNSET)

        packages_shipped = d.pop("packagesShipped", UNSET)

        create_wms_daily_metrics_body_shipping = cls(
            shipments_created=shipments_created,
            carriers_dispatched=carriers_dispatched,
            packages_shipped=packages_shipped,
        )

        create_wms_daily_metrics_body_shipping.additional_properties = d
        return create_wms_daily_metrics_body_shipping

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
