import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TMSShipmentDates")


@_attrs_define
class TMSShipmentDates:
    """Important shipment dates

    Attributes:
        planned_pickup_date (Union[Unset, datetime.datetime]):  Example: 2024-11-27T08:00:00.000Z.
        actual_pickup_date (Union[None, Unset, datetime.datetime]): Actual pickup timestamp (null until pickup occurs)
            Example: 2024-11-27T08:15:00.000Z.
        planned_delivery_date (Union[Unset, datetime.datetime]):  Example: 2024-11-29T17:00:00.000Z.
        estimated_delivery_date (Union[Unset, datetime.datetime]):  Example: 2024-11-29T16:30:00.000Z.
        actual_delivery_date (Union[None, Unset, datetime.datetime]): Actual delivery timestamp (null until delivery
            occurs) Example: 2024-11-29T16:45:00.000Z.
    """

    planned_pickup_date: Union[Unset, datetime.datetime] = UNSET
    actual_pickup_date: Union[None, Unset, datetime.datetime] = UNSET
    planned_delivery_date: Union[Unset, datetime.datetime] = UNSET
    estimated_delivery_date: Union[Unset, datetime.datetime] = UNSET
    actual_delivery_date: Union[None, Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        planned_pickup_date: Union[Unset, str] = UNSET
        if not isinstance(self.planned_pickup_date, Unset):
            planned_pickup_date = self.planned_pickup_date.isoformat()

        actual_pickup_date: Union[None, Unset, str]
        if isinstance(self.actual_pickup_date, Unset):
            actual_pickup_date = UNSET
        elif isinstance(self.actual_pickup_date, datetime.datetime):
            actual_pickup_date = self.actual_pickup_date.isoformat()
        else:
            actual_pickup_date = self.actual_pickup_date

        planned_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.planned_delivery_date, Unset):
            planned_delivery_date = self.planned_delivery_date.isoformat()

        estimated_delivery_date: Union[Unset, str] = UNSET
        if not isinstance(self.estimated_delivery_date, Unset):
            estimated_delivery_date = self.estimated_delivery_date.isoformat()

        actual_delivery_date: Union[None, Unset, str]
        if isinstance(self.actual_delivery_date, Unset):
            actual_delivery_date = UNSET
        elif isinstance(self.actual_delivery_date, datetime.datetime):
            actual_delivery_date = self.actual_delivery_date.isoformat()
        else:
            actual_delivery_date = self.actual_delivery_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if planned_pickup_date is not UNSET:
            field_dict["plannedPickupDate"] = planned_pickup_date
        if actual_pickup_date is not UNSET:
            field_dict["actualPickupDate"] = actual_pickup_date
        if planned_delivery_date is not UNSET:
            field_dict["plannedDeliveryDate"] = planned_delivery_date
        if estimated_delivery_date is not UNSET:
            field_dict["estimatedDeliveryDate"] = estimated_delivery_date
        if actual_delivery_date is not UNSET:
            field_dict["actualDeliveryDate"] = actual_delivery_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _planned_pickup_date = d.pop("plannedPickupDate", UNSET)
        planned_pickup_date: Union[Unset, datetime.datetime]
        if isinstance(_planned_pickup_date, Unset):
            planned_pickup_date = UNSET
        else:
            planned_pickup_date = isoparse(_planned_pickup_date)

        def _parse_actual_pickup_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actual_pickup_date_type_0 = isoparse(data)

                return actual_pickup_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        actual_pickup_date = _parse_actual_pickup_date(d.pop("actualPickupDate", UNSET))

        _planned_delivery_date = d.pop("plannedDeliveryDate", UNSET)
        planned_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_planned_delivery_date, Unset):
            planned_delivery_date = UNSET
        else:
            planned_delivery_date = isoparse(_planned_delivery_date)

        _estimated_delivery_date = d.pop("estimatedDeliveryDate", UNSET)
        estimated_delivery_date: Union[Unset, datetime.datetime]
        if isinstance(_estimated_delivery_date, Unset):
            estimated_delivery_date = UNSET
        else:
            estimated_delivery_date = isoparse(_estimated_delivery_date)

        def _parse_actual_delivery_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                actual_delivery_date_type_0 = isoparse(data)

                return actual_delivery_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        actual_delivery_date = _parse_actual_delivery_date(d.pop("actualDeliveryDate", UNSET))

        tms_shipment_dates = cls(
            planned_pickup_date=planned_pickup_date,
            actual_pickup_date=actual_pickup_date,
            planned_delivery_date=planned_delivery_date,
            estimated_delivery_date=estimated_delivery_date,
            actual_delivery_date=actual_delivery_date,
        )

        tms_shipment_dates.additional_properties = d
        return tms_shipment_dates

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
