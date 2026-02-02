from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ERPOperationsDashboardProducts")


@_attrs_define
class ERPOperationsDashboardProducts:
    """Product metrics

    Attributes:
        total (Union[Unset, float]): Total number of products Example: 1000.
        active_products (Union[Unset, float]): Number of active products Example: 850.
        discontinued_products (Union[Unset, float]): Number of discontinued products Example: 150.
    """

    total: Union[Unset, float] = UNSET
    active_products: Union[Unset, float] = UNSET
    discontinued_products: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        active_products = self.active_products

        discontinued_products = self.discontinued_products

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if active_products is not UNSET:
            field_dict["activeProducts"] = active_products
        if discontinued_products is not UNSET:
            field_dict["discontinuedProducts"] = discontinued_products

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        active_products = d.pop("activeProducts", UNSET)

        discontinued_products = d.pop("discontinuedProducts", UNSET)

        erp_operations_dashboard_products = cls(
            total=total,
            active_products=active_products,
            discontinued_products=discontinued_products,
        )

        erp_operations_dashboard_products.additional_properties = d
        return erp_operations_dashboard_products

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
