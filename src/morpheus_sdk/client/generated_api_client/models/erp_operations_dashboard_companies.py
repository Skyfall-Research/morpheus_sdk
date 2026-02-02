from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_operations_dashboard_companies_by_type import ERPOperationsDashboardCompaniesByType


T = TypeVar("T", bound="ERPOperationsDashboardCompanies")


@_attrs_define
class ERPOperationsDashboardCompanies:
    """Company metrics

    Attributes:
        total (Union[Unset, float]): Total number of companies Example: 500.
        by_type (Union[Unset, ERPOperationsDashboardCompaniesByType]): Count of companies by type Example: {'CUSTOMER':
            350, 'SUPPLIER': 120, 'PARTNER': 30}.
        active_customers (Union[Unset, float]): Number of active customers Example: 300.
        active_suppliers (Union[Unset, float]): Number of active suppliers Example: 100.
        active_companies (Union[Unset, float]): Total active companies Example: 420.
    """

    total: Union[Unset, float] = UNSET
    by_type: Union[Unset, "ERPOperationsDashboardCompaniesByType"] = UNSET
    active_customers: Union[Unset, float] = UNSET
    active_suppliers: Union[Unset, float] = UNSET
    active_companies: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        by_type: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.by_type, Unset):
            by_type = self.by_type.to_dict()

        active_customers = self.active_customers

        active_suppliers = self.active_suppliers

        active_companies = self.active_companies

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if by_type is not UNSET:
            field_dict["byType"] = by_type
        if active_customers is not UNSET:
            field_dict["activeCustomers"] = active_customers
        if active_suppliers is not UNSET:
            field_dict["activeSuppliers"] = active_suppliers
        if active_companies is not UNSET:
            field_dict["activeCompanies"] = active_companies

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_operations_dashboard_companies_by_type import ERPOperationsDashboardCompaniesByType

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        _by_type = d.pop("byType", UNSET)
        by_type: Union[Unset, ERPOperationsDashboardCompaniesByType]
        if isinstance(_by_type, Unset):
            by_type = UNSET
        else:
            by_type = ERPOperationsDashboardCompaniesByType.from_dict(_by_type)

        active_customers = d.pop("activeCustomers", UNSET)

        active_suppliers = d.pop("activeSuppliers", UNSET)

        active_companies = d.pop("activeCompanies", UNSET)

        erp_operations_dashboard_companies = cls(
            total=total,
            by_type=by_type,
            active_customers=active_customers,
            active_suppliers=active_suppliers,
            active_companies=active_companies,
        )

        erp_operations_dashboard_companies.additional_properties = d
        return erp_operations_dashboard_companies

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
