from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_operations_dashboard_response_200_data_inventory_by_status import (
        GetWMSOperationsDashboardResponse200DataInventoryByStatus,
    )


T = TypeVar("T", bound="GetWMSOperationsDashboardResponse200DataInventory")


@_attrs_define
class GetWMSOperationsDashboardResponse200DataInventory:
    """
    Attributes:
        total_items (Union[Unset, int]): Total inventory items on hand Example: 45890.
        by_status (Union[Unset, GetWMSOperationsDashboardResponse200DataInventoryByStatus]): Count of items by status
            Example: {'AVAILABLE': 42000, 'ALLOCATED': 3500, 'HOLD': 390}.
        low_stock_alerts (Union[Unset, int]): Number of low stock alerts Example: 12.
        expiring_alerts (Union[Unset, int]): Items expiring within 7 days Example: 45.
    """

    total_items: Union[Unset, int] = UNSET
    by_status: Union[Unset, "GetWMSOperationsDashboardResponse200DataInventoryByStatus"] = UNSET
    low_stock_alerts: Union[Unset, int] = UNSET
    expiring_alerts: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_items = self.total_items

        by_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.by_status, Unset):
            by_status = self.by_status.to_dict()

        low_stock_alerts = self.low_stock_alerts

        expiring_alerts = self.expiring_alerts

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_items is not UNSET:
            field_dict["totalItems"] = total_items
        if by_status is not UNSET:
            field_dict["byStatus"] = by_status
        if low_stock_alerts is not UNSET:
            field_dict["lowStockAlerts"] = low_stock_alerts
        if expiring_alerts is not UNSET:
            field_dict["expiringAlerts"] = expiring_alerts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_operations_dashboard_response_200_data_inventory_by_status import (
            GetWMSOperationsDashboardResponse200DataInventoryByStatus,
        )

        d = dict(src_dict)
        total_items = d.pop("totalItems", UNSET)

        _by_status = d.pop("byStatus", UNSET)
        by_status: Union[Unset, GetWMSOperationsDashboardResponse200DataInventoryByStatus]
        if isinstance(_by_status, Unset):
            by_status = UNSET
        else:
            by_status = GetWMSOperationsDashboardResponse200DataInventoryByStatus.from_dict(_by_status)

        low_stock_alerts = d.pop("lowStockAlerts", UNSET)

        expiring_alerts = d.pop("expiringAlerts", UNSET)

        get_wms_operations_dashboard_response_200_data_inventory = cls(
            total_items=total_items,
            by_status=by_status,
            low_stock_alerts=low_stock_alerts,
            expiring_alerts=expiring_alerts,
        )

        get_wms_operations_dashboard_response_200_data_inventory.additional_properties = d
        return get_wms_operations_dashboard_response_200_data_inventory

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
