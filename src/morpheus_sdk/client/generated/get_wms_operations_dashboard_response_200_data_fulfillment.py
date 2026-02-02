from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSOperationsDashboardResponse200DataFulfillment")


@_attrs_define
class GetWMSOperationsDashboardResponse200DataFulfillment:
    """
    Attributes:
        total (Union[Unset, int]):  Example: 2450.
        active (Union[Unset, int]):  Example: 125.
        created (Union[Unset, int]):  Example: 45.
        released (Union[Unset, int]):  Example: 30.
        allocated (Union[Unset, int]):  Example: 25.
        picking (Union[Unset, int]):  Example: 20.
        picked (Union[Unset, int]):  Example: 15.
        packing (Union[Unset, int]):  Example: 10.
        packed (Union[Unset, int]):  Example: 25.
        shipped (Union[Unset, int]):  Example: 2280.
        rush_orders (Union[Unset, int]):  Example: 8.
    """

    total: Union[Unset, int] = UNSET
    active: Union[Unset, int] = UNSET
    created: Union[Unset, int] = UNSET
    released: Union[Unset, int] = UNSET
    allocated: Union[Unset, int] = UNSET
    picking: Union[Unset, int] = UNSET
    picked: Union[Unset, int] = UNSET
    packing: Union[Unset, int] = UNSET
    packed: Union[Unset, int] = UNSET
    shipped: Union[Unset, int] = UNSET
    rush_orders: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        active = self.active

        created = self.created

        released = self.released

        allocated = self.allocated

        picking = self.picking

        picked = self.picked

        packing = self.packing

        packed = self.packed

        shipped = self.shipped

        rush_orders = self.rush_orders

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if active is not UNSET:
            field_dict["active"] = active
        if created is not UNSET:
            field_dict["created"] = created
        if released is not UNSET:
            field_dict["released"] = released
        if allocated is not UNSET:
            field_dict["allocated"] = allocated
        if picking is not UNSET:
            field_dict["picking"] = picking
        if picked is not UNSET:
            field_dict["picked"] = picked
        if packing is not UNSET:
            field_dict["packing"] = packing
        if packed is not UNSET:
            field_dict["packed"] = packed
        if shipped is not UNSET:
            field_dict["shipped"] = shipped
        if rush_orders is not UNSET:
            field_dict["rushOrders"] = rush_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        active = d.pop("active", UNSET)

        created = d.pop("created", UNSET)

        released = d.pop("released", UNSET)

        allocated = d.pop("allocated", UNSET)

        picking = d.pop("picking", UNSET)

        picked = d.pop("picked", UNSET)

        packing = d.pop("packing", UNSET)

        packed = d.pop("packed", UNSET)

        shipped = d.pop("shipped", UNSET)

        rush_orders = d.pop("rushOrders", UNSET)

        get_wms_operations_dashboard_response_200_data_fulfillment = cls(
            total=total,
            active=active,
            created=created,
            released=released,
            allocated=allocated,
            picking=picking,
            picked=picked,
            packing=packing,
            packed=packed,
            shipped=shipped,
            rush_orders=rush_orders,
        )

        get_wms_operations_dashboard_response_200_data_fulfillment.additional_properties = d
        return get_wms_operations_dashboard_response_200_data_fulfillment

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
