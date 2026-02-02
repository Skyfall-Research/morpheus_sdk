from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_operations_dashboard_invoices_by_status import ERPOperationsDashboardInvoicesByStatus


T = TypeVar("T", bound="ERPOperationsDashboardInvoices")


@_attrs_define
class ERPOperationsDashboardInvoices:
    """Invoice metrics

    Attributes:
        total (Union[Unset, float]): Total number of invoices Example: 300.
        by_status (Union[Unset, ERPOperationsDashboardInvoicesByStatus]): Count of invoices by status Example: {'DRAFT':
            20, 'SENT': 50, 'PAID': 200, 'PARTIALLY_PAID': 30}.
        total_outstanding (Union[Unset, float]): Total outstanding balance Example: 45000.
        overdue_count (Union[Unset, float]): Number of overdue invoices Example: 12.
        paid_this_month (Union[Unset, float]): Number of invoices paid this month Example: 35.
    """

    total: Union[Unset, float] = UNSET
    by_status: Union[Unset, "ERPOperationsDashboardInvoicesByStatus"] = UNSET
    total_outstanding: Union[Unset, float] = UNSET
    overdue_count: Union[Unset, float] = UNSET
    paid_this_month: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        by_status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.by_status, Unset):
            by_status = self.by_status.to_dict()

        total_outstanding = self.total_outstanding

        overdue_count = self.overdue_count

        paid_this_month = self.paid_this_month

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if by_status is not UNSET:
            field_dict["byStatus"] = by_status
        if total_outstanding is not UNSET:
            field_dict["totalOutstanding"] = total_outstanding
        if overdue_count is not UNSET:
            field_dict["overdueCount"] = overdue_count
        if paid_this_month is not UNSET:
            field_dict["paidThisMonth"] = paid_this_month

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_operations_dashboard_invoices_by_status import ERPOperationsDashboardInvoicesByStatus

        d = dict(src_dict)
        total = d.pop("total", UNSET)

        _by_status = d.pop("byStatus", UNSET)
        by_status: Union[Unset, ERPOperationsDashboardInvoicesByStatus]
        if isinstance(_by_status, Unset):
            by_status = UNSET
        else:
            by_status = ERPOperationsDashboardInvoicesByStatus.from_dict(_by_status)

        total_outstanding = d.pop("totalOutstanding", UNSET)

        overdue_count = d.pop("overdueCount", UNSET)

        paid_this_month = d.pop("paidThisMonth", UNSET)

        erp_operations_dashboard_invoices = cls(
            total=total,
            by_status=by_status,
            total_outstanding=total_outstanding,
            overdue_count=overdue_count,
            paid_this_month=paid_this_month,
        )

        erp_operations_dashboard_invoices.additional_properties = d
        return erp_operations_dashboard_invoices

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
