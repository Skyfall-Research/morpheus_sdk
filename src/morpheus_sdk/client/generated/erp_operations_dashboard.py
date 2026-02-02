from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_operations_dashboard_companies import ERPOperationsDashboardCompanies
    from ..models.erp_operations_dashboard_invoices import ERPOperationsDashboardInvoices
    from ..models.erp_operations_dashboard_orders import ERPOperationsDashboardOrders
    from ..models.erp_operations_dashboard_products import ERPOperationsDashboardProducts


T = TypeVar("T", bound="ERPOperationsDashboard")


@_attrs_define
class ERPOperationsDashboard:
    """Aggregated metrics for the ERP Command Center dashboard

    Attributes:
        orders (Union[Unset, ERPOperationsDashboardOrders]): Order metrics split by purchase orders and sales orders
        invoices (Union[Unset, ERPOperationsDashboardInvoices]): Invoice metrics
        companies (Union[Unset, ERPOperationsDashboardCompanies]): Company metrics
        products (Union[Unset, ERPOperationsDashboardProducts]): Product metrics
    """

    orders: Union[Unset, "ERPOperationsDashboardOrders"] = UNSET
    invoices: Union[Unset, "ERPOperationsDashboardInvoices"] = UNSET
    companies: Union[Unset, "ERPOperationsDashboardCompanies"] = UNSET
    products: Union[Unset, "ERPOperationsDashboardProducts"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        orders: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.orders, Unset):
            orders = self.orders.to_dict()

        invoices: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.invoices, Unset):
            invoices = self.invoices.to_dict()

        companies: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.companies, Unset):
            companies = self.companies.to_dict()

        products: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.products, Unset):
            products = self.products.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if orders is not UNSET:
            field_dict["orders"] = orders
        if invoices is not UNSET:
            field_dict["invoices"] = invoices
        if companies is not UNSET:
            field_dict["companies"] = companies
        if products is not UNSET:
            field_dict["products"] = products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_operations_dashboard_companies import ERPOperationsDashboardCompanies
        from ..models.erp_operations_dashboard_invoices import ERPOperationsDashboardInvoices
        from ..models.erp_operations_dashboard_orders import ERPOperationsDashboardOrders
        from ..models.erp_operations_dashboard_products import ERPOperationsDashboardProducts

        d = dict(src_dict)
        _orders = d.pop("orders", UNSET)
        orders: Union[Unset, ERPOperationsDashboardOrders]
        if isinstance(_orders, Unset):
            orders = UNSET
        else:
            orders = ERPOperationsDashboardOrders.from_dict(_orders)

        _invoices = d.pop("invoices", UNSET)
        invoices: Union[Unset, ERPOperationsDashboardInvoices]
        if isinstance(_invoices, Unset):
            invoices = UNSET
        else:
            invoices = ERPOperationsDashboardInvoices.from_dict(_invoices)

        _companies = d.pop("companies", UNSET)
        companies: Union[Unset, ERPOperationsDashboardCompanies]
        if isinstance(_companies, Unset):
            companies = UNSET
        else:
            companies = ERPOperationsDashboardCompanies.from_dict(_companies)

        _products = d.pop("products", UNSET)
        products: Union[Unset, ERPOperationsDashboardProducts]
        if isinstance(_products, Unset):
            products = UNSET
        else:
            products = ERPOperationsDashboardProducts.from_dict(_products)

        erp_operations_dashboard = cls(
            orders=orders,
            invoices=invoices,
            companies=companies,
            products=products,
        )

        erp_operations_dashboard.additional_properties = d
        return erp_operations_dashboard

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
