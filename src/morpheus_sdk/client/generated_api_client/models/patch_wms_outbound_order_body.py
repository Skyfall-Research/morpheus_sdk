import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.patch_wms_outbound_order_body_order_priority import PatchWMSOutboundOrderBodyOrderPriority
from ..models.patch_wms_outbound_order_body_order_status import PatchWMSOutboundOrderBodyOrderStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_wms_outbound_order_body_dates import PatchWMSOutboundOrderBodyDates


T = TypeVar("T", bound="PatchWMSOutboundOrderBody")


@_attrs_define
class PatchWMSOutboundOrderBody:
    """
    Attributes:
        order_status (Union[Unset, PatchWMSOutboundOrderBodyOrderStatus]): New status for the order
        order_priority (Union[Unset, PatchWMSOutboundOrderBodyOrderPriority]): New priority for the order
        dates (Union[Unset, PatchWMSOutboundOrderBodyDates]):
        dates_required_ship_date (Union[Unset, datetime.datetime]): Updated required ship date (dot notation)
        dates_actual_ship_date (Union[Unset, datetime.datetime]): Actual ship date (dot notation)
    """

    order_status: Union[Unset, PatchWMSOutboundOrderBodyOrderStatus] = UNSET
    order_priority: Union[Unset, PatchWMSOutboundOrderBodyOrderPriority] = UNSET
    dates: Union[Unset, "PatchWMSOutboundOrderBodyDates"] = UNSET
    dates_required_ship_date: Union[Unset, datetime.datetime] = UNSET
    dates_actual_ship_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_status: Union[Unset, str] = UNSET
        if not isinstance(self.order_status, Unset):
            order_status = self.order_status.value

        order_priority: Union[Unset, str] = UNSET
        if not isinstance(self.order_priority, Unset):
            order_priority = self.order_priority.value

        dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        dates_required_ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.dates_required_ship_date, Unset):
            dates_required_ship_date = self.dates_required_ship_date.isoformat()

        dates_actual_ship_date: Union[Unset, str] = UNSET
        if not isinstance(self.dates_actual_ship_date, Unset):
            dates_actual_ship_date = self.dates_actual_ship_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_status is not UNSET:
            field_dict["orderStatus"] = order_status
        if order_priority is not UNSET:
            field_dict["orderPriority"] = order_priority
        if dates is not UNSET:
            field_dict["dates"] = dates
        if dates_required_ship_date is not UNSET:
            field_dict["dates.requiredShipDate"] = dates_required_ship_date
        if dates_actual_ship_date is not UNSET:
            field_dict["dates.actualShipDate"] = dates_actual_ship_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_wms_outbound_order_body_dates import PatchWMSOutboundOrderBodyDates

        d = dict(src_dict)
        _order_status = d.pop("orderStatus", UNSET)
        order_status: Union[Unset, PatchWMSOutboundOrderBodyOrderStatus]
        if isinstance(_order_status, Unset):
            order_status = UNSET
        else:
            order_status = PatchWMSOutboundOrderBodyOrderStatus(_order_status)

        _order_priority = d.pop("orderPriority", UNSET)
        order_priority: Union[Unset, PatchWMSOutboundOrderBodyOrderPriority]
        if isinstance(_order_priority, Unset):
            order_priority = UNSET
        else:
            order_priority = PatchWMSOutboundOrderBodyOrderPriority(_order_priority)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, PatchWMSOutboundOrderBodyDates]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = PatchWMSOutboundOrderBodyDates.from_dict(_dates)

        _dates_required_ship_date = d.pop("dates.requiredShipDate", UNSET)
        dates_required_ship_date: Union[Unset, datetime.datetime]
        if isinstance(_dates_required_ship_date, Unset):
            dates_required_ship_date = UNSET
        else:
            dates_required_ship_date = isoparse(_dates_required_ship_date)

        _dates_actual_ship_date = d.pop("dates.actualShipDate", UNSET)
        dates_actual_ship_date: Union[Unset, datetime.datetime]
        if isinstance(_dates_actual_ship_date, Unset):
            dates_actual_ship_date = UNSET
        else:
            dates_actual_ship_date = isoparse(_dates_actual_ship_date)

        patch_wms_outbound_order_body = cls(
            order_status=order_status,
            order_priority=order_priority,
            dates=dates,
            dates_required_ship_date=dates_required_ship_date,
            dates_actual_ship_date=dates_actual_ship_date,
        )

        patch_wms_outbound_order_body.additional_properties = d
        return patch_wms_outbound_order_body

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
