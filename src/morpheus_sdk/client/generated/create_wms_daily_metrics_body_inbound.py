from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSDailyMetricsBodyInbound")


@_attrs_define
class CreateWMSDailyMetricsBodyInbound:
    """Inbound receiving metrics

    Attributes:
        po_received (Union[Unset, float]): Number of POs received Example: 45.
        lines_received (Union[Unset, float]): Number of lines received Example: 320.
        units_received (Union[Unset, float]): Total units received Example: 2450.
        pallets_received (Union[Unset, float]): Number of pallets received Example: 28.
        receiving_hours (Union[Unset, float]): Total receiving hours Example: 32.5.
        units_per_hour (Union[Unset, float]): Units processed per hour Example: 75.4.
    """

    po_received: Union[Unset, float] = UNSET
    lines_received: Union[Unset, float] = UNSET
    units_received: Union[Unset, float] = UNSET
    pallets_received: Union[Unset, float] = UNSET
    receiving_hours: Union[Unset, float] = UNSET
    units_per_hour: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        po_received = self.po_received

        lines_received = self.lines_received

        units_received = self.units_received

        pallets_received = self.pallets_received

        receiving_hours = self.receiving_hours

        units_per_hour = self.units_per_hour

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if po_received is not UNSET:
            field_dict["poReceived"] = po_received
        if lines_received is not UNSET:
            field_dict["linesReceived"] = lines_received
        if units_received is not UNSET:
            field_dict["unitsReceived"] = units_received
        if pallets_received is not UNSET:
            field_dict["palletsReceived"] = pallets_received
        if receiving_hours is not UNSET:
            field_dict["receivingHours"] = receiving_hours
        if units_per_hour is not UNSET:
            field_dict["unitsPerHour"] = units_per_hour

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        po_received = d.pop("poReceived", UNSET)

        lines_received = d.pop("linesReceived", UNSET)

        units_received = d.pop("unitsReceived", UNSET)

        pallets_received = d.pop("palletsReceived", UNSET)

        receiving_hours = d.pop("receivingHours", UNSET)

        units_per_hour = d.pop("unitsPerHour", UNSET)

        create_wms_daily_metrics_body_inbound = cls(
            po_received=po_received,
            lines_received=lines_received,
            units_received=units_received,
            pallets_received=pallets_received,
            receiving_hours=receiving_hours,
            units_per_hour=units_per_hour,
        )

        create_wms_daily_metrics_body_inbound.additional_properties = d
        return create_wms_daily_metrics_body_inbound

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
