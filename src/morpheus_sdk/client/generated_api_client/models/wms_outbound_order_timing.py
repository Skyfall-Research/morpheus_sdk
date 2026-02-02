import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundOrderTiming")


@_attrs_define
class WMSOutboundOrderTiming:
    """Workflow timing tracking (automatically updated during status changes)

    Attributes:
        released_at (Union[Unset, datetime.datetime]): Timestamp when order released to WMS (status: RELEASED) Example:
            2024-12-01T10:15:00.000Z.
        allocated_at (Union[Unset, datetime.datetime]): Timestamp when inventory allocated (status: ALLOCATED) Example:
            2024-12-01T11:30:00.000Z.
        picking_started_at (Union[Unset, datetime.datetime]): Timestamp when picking began (status: PICKING) Example:
            2024-12-01T13:00:00.000Z.
        picked_at (Union[Unset, datetime.datetime]): Timestamp when picking completed (status: PICKED) Example:
            2024-12-01T14:45:00.000Z.
        packed_at (Union[Unset, datetime.datetime]): Timestamp when packing completed (status: PACKED) Example:
            2024-12-01T15:30:00.000Z.
        shipped_at (Union[Unset, datetime.datetime]): Timestamp when shipment dispatched (status: SHIPPED) Example:
            2024-12-01T16:00:00.000Z.
    """

    released_at: Union[Unset, datetime.datetime] = UNSET
    allocated_at: Union[Unset, datetime.datetime] = UNSET
    picking_started_at: Union[Unset, datetime.datetime] = UNSET
    picked_at: Union[Unset, datetime.datetime] = UNSET
    packed_at: Union[Unset, datetime.datetime] = UNSET
    shipped_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        released_at: Union[Unset, str] = UNSET
        if not isinstance(self.released_at, Unset):
            released_at = self.released_at.isoformat()

        allocated_at: Union[Unset, str] = UNSET
        if not isinstance(self.allocated_at, Unset):
            allocated_at = self.allocated_at.isoformat()

        picking_started_at: Union[Unset, str] = UNSET
        if not isinstance(self.picking_started_at, Unset):
            picking_started_at = self.picking_started_at.isoformat()

        picked_at: Union[Unset, str] = UNSET
        if not isinstance(self.picked_at, Unset):
            picked_at = self.picked_at.isoformat()

        packed_at: Union[Unset, str] = UNSET
        if not isinstance(self.packed_at, Unset):
            packed_at = self.packed_at.isoformat()

        shipped_at: Union[Unset, str] = UNSET
        if not isinstance(self.shipped_at, Unset):
            shipped_at = self.shipped_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if released_at is not UNSET:
            field_dict["releasedAt"] = released_at
        if allocated_at is not UNSET:
            field_dict["allocatedAt"] = allocated_at
        if picking_started_at is not UNSET:
            field_dict["pickingStartedAt"] = picking_started_at
        if picked_at is not UNSET:
            field_dict["pickedAt"] = picked_at
        if packed_at is not UNSET:
            field_dict["packedAt"] = packed_at
        if shipped_at is not UNSET:
            field_dict["shippedAt"] = shipped_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _released_at = d.pop("releasedAt", UNSET)
        released_at: Union[Unset, datetime.datetime]
        if isinstance(_released_at, Unset):
            released_at = UNSET
        else:
            released_at = isoparse(_released_at)

        _allocated_at = d.pop("allocatedAt", UNSET)
        allocated_at: Union[Unset, datetime.datetime]
        if isinstance(_allocated_at, Unset):
            allocated_at = UNSET
        else:
            allocated_at = isoparse(_allocated_at)

        _picking_started_at = d.pop("pickingStartedAt", UNSET)
        picking_started_at: Union[Unset, datetime.datetime]
        if isinstance(_picking_started_at, Unset):
            picking_started_at = UNSET
        else:
            picking_started_at = isoparse(_picking_started_at)

        _picked_at = d.pop("pickedAt", UNSET)
        picked_at: Union[Unset, datetime.datetime]
        if isinstance(_picked_at, Unset):
            picked_at = UNSET
        else:
            picked_at = isoparse(_picked_at)

        _packed_at = d.pop("packedAt", UNSET)
        packed_at: Union[Unset, datetime.datetime]
        if isinstance(_packed_at, Unset):
            packed_at = UNSET
        else:
            packed_at = isoparse(_packed_at)

        _shipped_at = d.pop("shippedAt", UNSET)
        shipped_at: Union[Unset, datetime.datetime]
        if isinstance(_shipped_at, Unset):
            shipped_at = UNSET
        else:
            shipped_at = isoparse(_shipped_at)

        wms_outbound_order_timing = cls(
            released_at=released_at,
            allocated_at=allocated_at,
            picking_started_at=picking_started_at,
            picked_at=picked_at,
            packed_at=packed_at,
            shipped_at=shipped_at,
        )

        wms_outbound_order_timing.additional_properties = d
        return wms_outbound_order_timing

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
