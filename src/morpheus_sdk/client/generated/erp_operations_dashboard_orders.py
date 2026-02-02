from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_operations_dashboard_orders_purchase_orders import ERPOperationsDashboardOrdersPurchaseOrders
    from ..models.erp_operations_dashboard_orders_sales_orders import ERPOperationsDashboardOrdersSalesOrders


T = TypeVar("T", bound="ERPOperationsDashboardOrders")


@_attrs_define
class ERPOperationsDashboardOrders:
    """Order metrics split by purchase orders and sales orders

    Attributes:
        purchase_orders (Union[Unset, ERPOperationsDashboardOrdersPurchaseOrders]): Purchase order (inbound) metrics
        sales_orders (Union[Unset, ERPOperationsDashboardOrdersSalesOrders]): Sales order (outbound) metrics
    """

    purchase_orders: Union[Unset, "ERPOperationsDashboardOrdersPurchaseOrders"] = UNSET
    sales_orders: Union[Unset, "ERPOperationsDashboardOrdersSalesOrders"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        purchase_orders: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purchase_orders, Unset):
            purchase_orders = self.purchase_orders.to_dict()

        sales_orders: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sales_orders, Unset):
            sales_orders = self.sales_orders.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if purchase_orders is not UNSET:
            field_dict["purchaseOrders"] = purchase_orders
        if sales_orders is not UNSET:
            field_dict["salesOrders"] = sales_orders

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_operations_dashboard_orders_purchase_orders import ERPOperationsDashboardOrdersPurchaseOrders
        from ..models.erp_operations_dashboard_orders_sales_orders import ERPOperationsDashboardOrdersSalesOrders

        d = dict(src_dict)
        _purchase_orders = d.pop("purchaseOrders", UNSET)
        purchase_orders: Union[Unset, ERPOperationsDashboardOrdersPurchaseOrders]
        if isinstance(_purchase_orders, Unset):
            purchase_orders = UNSET
        else:
            purchase_orders = ERPOperationsDashboardOrdersPurchaseOrders.from_dict(_purchase_orders)

        _sales_orders = d.pop("salesOrders", UNSET)
        sales_orders: Union[Unset, ERPOperationsDashboardOrdersSalesOrders]
        if isinstance(_sales_orders, Unset):
            sales_orders = UNSET
        else:
            sales_orders = ERPOperationsDashboardOrdersSalesOrders.from_dict(_sales_orders)

        erp_operations_dashboard_orders = cls(
            purchase_orders=purchase_orders,
            sales_orders=sales_orders,
        )

        erp_operations_dashboard_orders.additional_properties = d
        return erp_operations_dashboard_orders

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
