from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_upsert_erp_products_body_products_item import BulkUpsertERPProductsBodyProductsItem


T = TypeVar("T", bound="BulkUpsertERPProductsBody")


@_attrs_define
class BulkUpsertERPProductsBody:
    """
    Attributes:
        products (list['BulkUpsertERPProductsBodyProductsItem']): Array of product objects to upsert Example:
            [{'productId': 'PROD_WIDGET_001', 'name': 'Premium Widget', 'status': 'ACTIVE', 'price': {'currency': 'USD',
            'amount': 99.99}}, {'productId': 'PROD_GADGET_002', 'name': 'Smart Gadget', 'status': 'ACTIVE', 'price':
            {'currency': 'USD', 'amount': 149.99}}].
    """

    products: list["BulkUpsertERPProductsBodyProductsItem"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        products = []
        for products_item_data in self.products:
            products_item = products_item_data.to_dict()
            products.append(products_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "products": products,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_upsert_erp_products_body_products_item import BulkUpsertERPProductsBodyProductsItem

        d = dict(src_dict)
        products = []
        _products = d.pop("products")
        for products_item_data in _products:
            products_item = BulkUpsertERPProductsBodyProductsItem.from_dict(products_item_data)

            products.append(products_item)

        bulk_upsert_erp_products_body = cls(
            products=products,
        )

        bulk_upsert_erp_products_body.additional_properties = d
        return bulk_upsert_erp_products_body

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
