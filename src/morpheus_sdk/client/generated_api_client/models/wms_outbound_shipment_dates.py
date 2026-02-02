import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundShipmentDates")


@_attrs_define
class WMSOutboundShipmentDates:
    """Logistics timeline and delivery requirements

    Attributes:
        ship_date (Union[Unset, datetime.datetime]): Planned ship date Example: 2024-12-02T09:00:00.000Z.
        manifest_date (Union[Unset, datetime.datetime]): Carrier manifest date (set on MANIFESTED status) Example:
            2024-12-02T08:30:00.000Z.
        load_start_time (Union[Unset, datetime.datetime]): Loading start timestamp Example: 2024-12-02T10:00:00.000Z.
        load_end_time (Union[Unset, datetime.datetime]): Loading completion timestamp Example: 2024-12-02T11:30:00.000Z.
        actual_ship_time (Union[Unset, datetime.datetime]): Actual dispatch timestamp (set on SHIPPED status) Example:
            2024-12-02T12:00:00.000Z.
        estimated_delivery_date (Union[Unset, datetime.datetime]): Carrier estimated delivery date Example:
            2024-12-04T17:00:00.000Z.
        actual_delivery_date (Union[Unset, datetime.datetime]): Actual delivery timestamp (set on DELIVERED status)
            Example: 2024-12-04T15:45:00.000Z.
    """

    ship_date: Union[Unset, datetime.datetime] = UNSET
    manifest_date: Union[Unset, datetime.datetime] = UNSET
    load_start_time: Union[Unset, datetime.datetime] = UNSET
    load_end_time: Union[Unset, datetime.datetime] = UNSET
    actual_ship_time: Union[Unset, datetime.datetime] = UNSET
    estimated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    actual_delivery_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.ship_date, Unset):
            ship_date = self.ship_date.isoformat()

        manifest_date: Union[Unset, str] = UNSET
        if not isinstance(self.manifest_date, Unset):
            manifest_date = self.manifest_date.isoformat()

        load_start_time: Union[Unset, str] = UNSET
        if not isinstance(self.load_start_time, Unset):
            load_start_time = self.load_start_time.isoformat()

        load_end_time: Union[Unset, str] = UNSET
        if not isinstance(self.load_end_time, Unset):
            load_end_time = self.load_end_time.isoformat()

        actual_ship_time: Union[Unset, str] = UNSET
        if not isinstance(self.actual_ship_time, Unset):
            actual_ship_time = self.actual_ship_time.isoformat()

        estimated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_delivery_date, Unset):
            estimated_delivery_date = self.estimated_delivery_date.isoformat()

        actual_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.actual_delivery_date, Unset):
            actual_delivery_date = self.actual_delivery_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ship_date is not UNSET:
            field_dict["shipDate"] = ship_date
        if manifest_date is not UNSET:
            field_dict["manifestDate"] = manifest_date
        if load_start_time is not UNSET:
            field_dict["loadStartTime"] = load_start_time
        if load_end_time is not UNSET:
            field_dict["loadEndTime"] = load_end_time
        if actual_ship_time is not UNSET:
            field_dict["actualShipTime"] = actual_ship_time
        if estimated_delivery_date is not UNSET:
            field_dict["estimatedDeliveryDate"] = estimated_delivery_date
        if actual_delivery_date is not UNSET:
            field_dict["actualDeliveryDate"] = actual_delivery_date

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

        _manifest_date = d.pop("manifestDate", UNSET)
        manifest_date: Union[Unset, datetime.datetime]
        if isinstance(_manifest_date, Unset):
            manifest_date = UNSET
        else:
            manifest_date = isoparse(_manifest_date)

        _load_start_time = d.pop("loadStartTime", UNSET)
        load_start_time: Union[Unset, datetime.datetime]
        if isinstance(_load_start_time, Unset):
            load_start_time = UNSET
        else:
            load_start_time = isoparse(_load_start_time)

        _load_end_time = d.pop("loadEndTime", UNSET)
        load_end_time: Union[Unset, datetime.datetime]
        if isinstance(_load_end_time, Unset):
            load_end_time = UNSET
        else:
            load_end_time = isoparse(_load_end_time)

        _actual_ship_time = d.pop("actualShipTime", UNSET)
        actual_ship_time: Union[Unset, datetime.datetime]
        if isinstance(_actual_ship_time, Unset):
            actual_ship_time = UNSET
        else:
            actual_ship_time = isoparse(_actual_ship_time)

        _estimated_delivery_date = d.pop("estimatedDeliveryDate", UNSET)
        estimated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_delivery_date, Unset):
            estimated_delivery_date = UNSET
        else:
            estimated_delivery_date = isoparse(_estimated_delivery_date)

        _actual_delivery_date = d.pop("actualDeliveryDate", UNSET)
        actual_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_actual_delivery_date, Unset):
            actual_delivery_date = UNSET
        else:
            actual_delivery_date = isoparse(_actual_delivery_date)

        wms_outbound_shipment_dates = cls(
            ship_date=ship_date,
            manifest_date=manifest_date,
            load_start_time=load_start_time,
            load_end_time=load_end_time,
            actual_ship_time=actual_ship_time,
            estimated_delivery_date=estimated_delivery_date,
            actual_delivery_date=actual_delivery_date,
        )

        wms_outbound_shipment_dates.additional_properties = d
        return wms_outbound_shipment_dates

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
