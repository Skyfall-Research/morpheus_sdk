import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWMSOutboundShipmentBodyDates")


@_attrs_define
class CreateWMSOutboundShipmentBodyDates:
    """Scheduled dates and delivery requirements

    Attributes:
        ship_date (Union[Unset, datetime.datetime]): Planned ship date Example: 2024-12-02T09:00:00.000Z.
        estimated_delivery_date (Union[Unset, datetime.datetime]): Estimated delivery date Example:
            2024-12-04T17:00:00.000Z.
    """

    ship_date: Union[Unset, datetime.datetime] = UNSET
    estimated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.ship_date, Unset):
            ship_date = self.ship_date.isoformat()

        estimated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_delivery_date, Unset):
            estimated_delivery_date = self.estimated_delivery_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ship_date is not UNSET:
            field_dict["shipDate"] = ship_date
        if estimated_delivery_date is not UNSET:
            field_dict["estimatedDeliveryDate"] = estimated_delivery_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _ship_date = d.pop("shipDate", UNSET)
        ship_date: Union[Unset, datetime.datetime]
        if isinstance(_ship_date, Unset):
            ship_date = UNSET
        else:
            ship_date = isoparse(_ship_date)

        _estimated_delivery_date = d.pop("estimatedDeliveryDate", UNSET)
        estimated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_delivery_date, Unset):
            estimated_delivery_date = UNSET
        else:
            estimated_delivery_date = isoparse(_estimated_delivery_date)

        create_wms_outbound_shipment_body_dates = cls(
            ship_date=ship_date,
            estimated_delivery_date=estimated_delivery_date,
        )

        create_wms_outbound_shipment_body_dates.additional_properties = d
        return create_wms_outbound_shipment_body_dates

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
