from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_operations_dashboard_orders_sales_orders_by_status import (
        ERPOperationsDashboardOrdersSalesOrdersByStatus,
    )


T = TypeVar("T", bound="ERPOperationsDashboardOrdersSalesOrders")


@_attrs_define
class ERPOperationsDashboardOrdersSalesOrders:
    """Sales order (outbound) metrics

    Attributes:
        total (Union[Unset, float]): Total number of sales orders Example: 200.
        by_status (Union[Unset, ERPOperationsDashboardOrdersSalesOrdersByStatus]): Count of orders by status Example:
            {'RECEIVED': 40, 'IN_PROGRESS': 60, 'COMPLETED': 100}.
        recent_orders (Union[Unset, float]): Orders in the last 30 days Example: 45.
        total_value (Union[Unset, float]): Total value of all orders Example: 250000.
        average_order_value (Union[Unset, float]): Average order value Example: 1250.
    """

    total: Union[Unset, float] = UNSET
    by_status: Union[Unset, "ERPOperationsDashboardOrdersSalesOrdersByStatus"] = UNSET
    recent_orders: Union[Unset, float] = UNSET
    total_value: Union[Unset, float] = UNSET
    average_order_value: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        by_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.by_status, Unset):
            by_status = self.by_status.to_dict()

        recent_orders = self.recent_orders

        total_value = self.total_value

        average_order_value = self.average_order_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if by_status is not UNSET:
            field_dict["byStatus"] = by_status
        if recent_orders is not UNSET:
            field_dict["recentOrders"] = recent_orders
        if total_value is not UNSET:
            field_dict["totalValue"] = total_value
        if average_order_value is not UNSET:
            field_dict["averageOrderValue"] = average_order_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_operations_dashboard_orders_sales_orders_by_status import (
            ERPOperationsDashboardOrdersSalesOrdersByStatus,
        )

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        _by_status = d.pop("byStatus", UNSET)
        by_status: Union[Unset, ERPOperationsDashboardOrdersSalesOrdersByStatus]
        if isinstance(_by_status, Unset):
            by_status = UNSET
        else:
            by_status = ERPOperationsDashboardOrdersSalesOrdersByStatus.from_dict(_by_status)

        recent_orders = d.pop("recentOrders", UNSET)

        total_value = d.pop("totalValue", UNSET)

        average_order_value = d.pop("averageOrderValue", UNSET)

        erp_operations_dashboard_orders_sales_orders = cls(
            total=total,
            by_status=by_status,
            recent_orders=recent_orders,
            total_value=total_value,
            average_order_value=average_order_value,
        )

        erp_operations_dashboard_orders_sales_orders.additional_properties = d
        return erp_operations_dashboard_orders_sales_orders

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
