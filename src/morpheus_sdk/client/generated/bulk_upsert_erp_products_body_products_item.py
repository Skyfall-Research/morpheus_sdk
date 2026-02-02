from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_upsert_erp_products_body_products_item_status import BulkUpsertERPProductsBodyProductsItemStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkUpsertERPProductsBodyProductsItem")


@_attrs_define
class BulkUpsertERPProductsBodyProductsItem:
    """Product data (same as create product schema)

    Attributes:
        product_id (Union[Unset, str]): Product identifier for upsert matching Example: PROD_WIDGET_001.
        name (Union[Unset, str]): Product name Example: Premium Widget.
        status (Union[Unset, BulkUpsertERPProductsBodyProductsItemStatus]):  Example: ACTIVE.
    """

    product_id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    status: Union[Unset, BulkUpsertERPProductsBodyProductsItemStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        name = self.name

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if name is not UNSET:
            field_dict["name"] = name
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("productId", UNSET)

        name = d.pop("name", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, BulkUpsertERPProductsBodyProductsItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = BulkUpsertERPProductsBodyProductsItemStatus(_status)

        bulk_upsert_erp_products_body_products_item = cls(
            product_id=product_id,
            name=name,
            status=status,
        )

        bulk_upsert_erp_products_body_products_item.additional_properties = d
        return bulk_upsert_erp_products_body_products_item

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
