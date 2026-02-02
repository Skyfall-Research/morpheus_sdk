import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_wms_outbound_order_status_body_status import UpdateWMSOutboundOrderStatusBodyStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWMSOutboundOrderStatusBody")


@_attrs_define
class UpdateWMSOutboundOrderStatusBody:
    """
    Attributes:
        status (UpdateWMSOutboundOrderStatusBodyStatus): New order status Example: ALLOCATED.
        status_date (Union[Unset, datetime.datetime]): Optional timestamp (defaults to current time) Example:
            2024-12-01T14:30:00.000Z.
    """

    status: UpdateWMSOutboundOrderStatusBodyStatus
    status_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        status_date: Union[Unset, str] = UNSET
        if not isinstance(self.status_date, Unset):
            status_date = self.status_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if status_date is not UNSET:
            field_dict["statusDate"] = status_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = UpdateWMSOutboundOrderStatusBodyStatus(d.pop("status"))

        _status_date = d.pop("statusDate", UNSET)
        status_date: Union[Unset, datetime.datetime]
        if isinstance(_status_date, Unset):
            status_date = UNSET
        else:
            status_date = isoparse(_status_date)

        update_wms_outbound_order_status_body = cls(
            status=status,
            status_date=status_date,
        )

        update_wms_outbound_order_status_body.additional_properties = d
        return update_wms_outbound_order_status_body

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
