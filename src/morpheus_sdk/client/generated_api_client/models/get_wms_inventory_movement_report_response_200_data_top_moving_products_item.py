from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInventoryMovementReportResponse200DataTopMovingProductsItem")


@_attrs_define
class GetWMSInventoryMovementReportResponse200DataTopMovingProductsItem:
    """
    Attributes:
        product_id (Union[Unset, str]): Product identifier Example: prod_12345.
        sku (Union[Unset, str]): Stock keeping unit Example: ABC-123-XL.
        total_quantity (Union[Unset, float]): Total quantity moved for this product Example: 1847.
        transaction_count (Union[Unset, int]): Number of transactions for this product Example: 89.
    """

    product_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    total_quantity: Union[Unset, float] = UNSET
    transaction_count: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sku = self.sku

        total_quantity = self.total_quantity

        transaction_count = self.transaction_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity
        if transaction_count is not UNSET:
            field_dict["transactionCount"] = transaction_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("productId", UNSET)

        sku = d.pop("sku", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        transaction_count = d.pop("transactionCount", UNSET)

        get_wms_inventory_movement_report_response_200_data_top_moving_products_item = cls(
            product_id=product_id,
            sku=sku,
            total_quantity=total_quantity,
            transaction_count=transaction_count,
        )

        get_wms_inventory_movement_report_response_200_data_top_moving_products_item.additional_properties = d
        return get_wms_inventory_movement_report_response_200_data_top_moving_products_item

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
