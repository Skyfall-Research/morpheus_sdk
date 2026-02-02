import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.patch_wms_inbound_order_body_order_status import PatchWMSInboundOrderBodyOrderStatus
from ..models.patch_wms_inbound_order_body_priority import PatchWMSInboundOrderBodyPriority
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_wms_inbound_order_body_dates import PatchWMSInboundOrderBodyDates


T = TypeVar("T", bound="PatchWMSInboundOrderBody")


@_attrs_define
class PatchWMSInboundOrderBody:
    """
    Attributes:
        order_status (Union[Unset, PatchWMSInboundOrderBodyOrderStatus]): New status for the order
        priority (Union[Unset, PatchWMSInboundOrderBodyPriority]): New priority for the order
        dates (Union[Unset, PatchWMSInboundOrderBodyDates]):
        dates_expected_arrival (Union[Unset, datetime.datetime]): Updated expected arrival date (dot notation)
    """

    order_status: Union[Unset, PatchWMSInboundOrderBodyOrderStatus] = UNSET
    priority: Union[Unset, PatchWMSInboundOrderBodyPriority] = UNSET
    dates: Union[Unset, "PatchWMSInboundOrderBodyDates"] = UNSET
    dates_expected_arrival: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        order_status: Union[Unset, str] = UNSET
        if not isinstance(self.order_status, Unset):
            order_status = self.order_status.value

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dates, Unset):
            dates = self.dates.to_dict()

        dates_expected_arrival: Union[Unset, str] = UNSET
        if not isinstance(self.dates_expected_arrival, Unset):
            dates_expected_arrival = self.dates_expected_arrival.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if order_status is not UNSET:
            field_dict["orderStatus"] = order_status
        if priority is not UNSET:
            field_dict["priority"] = priority
        if dates is not UNSET:
            field_dict["dates"] = dates
        if dates_expected_arrival is not UNSET:
            field_dict["dates.expectedArrival"] = dates_expected_arrival

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_wms_inbound_order_body_dates import PatchWMSInboundOrderBodyDates

        d = dict(src_dict)
        _order_status = d.pop("orderStatus", UNSET)
        order_status: Union[Unset, PatchWMSInboundOrderBodyOrderStatus]
        if isinstance(_order_status, Unset):
            order_status = UNSET
        else:
            order_status = PatchWMSInboundOrderBodyOrderStatus(_order_status)

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, PatchWMSInboundOrderBodyPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = PatchWMSInboundOrderBodyPriority(_priority)

        _dates = d.pop("dates", UNSET)
        dates: Union[Unset, PatchWMSInboundOrderBodyDates]
        if isinstance(_dates, Unset):
            dates = UNSET
        else:
            dates = PatchWMSInboundOrderBodyDates.from_dict(_dates)

        _dates_expected_arrival = d.pop("dates.expectedArrival", UNSET)
        dates_expected_arrival: Union[Unset, datetime.datetime]
        if isinstance(_dates_expected_arrival, Unset):
            dates_expected_arrival = UNSET
        else:
            dates_expected_arrival = isoparse(_dates_expected_arrival)

        patch_wms_inbound_order_body = cls(
            order_status=order_status,
            priority=priority,
            dates=dates,
            dates_expected_arrival=dates_expected_arrival,
        )

        patch_wms_inbound_order_body.additional_properties = d
        return patch_wms_inbound_order_body

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
