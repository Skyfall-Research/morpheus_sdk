from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSReplenishmentMetricsResponse200DataTopReplenishedProductsItem")


@_attrs_define
class GetWMSReplenishmentMetricsResponse200DataTopReplenishedProductsItem:
    """
    Attributes:
        product_id (Union[Unset, str]):  Example: PROD-12345.
        sku (Union[Unset, str]):  Example: ABC-XYZ-001.
        replenishment_count (Union[Unset, float]):  Example: 45.
        total_quantity (Union[Unset, float]):  Example: 6750.
    """

    product_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    replenishment_count: Union[Unset, float] = UNSET
    total_quantity: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sku = self.sku

        replenishment_count = self.replenishment_count

        total_quantity = self.total_quantity

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if replenishment_count is not UNSET:
            field_dict["replenishmentCount"] = replenishment_count
        if total_quantity is not UNSET:
            field_dict["totalQuantity"] = total_quantity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("productId", UNSET)

        sku = d.pop("sku", UNSET)

        replenishment_count = d.pop("replenishmentCount", UNSET)

        total_quantity = d.pop("totalQuantity", UNSET)

        get_wms_replenishment_metrics_response_200_data_top_replenished_products_item = cls(
            product_id=product_id,
            sku=sku,
            replenishment_count=replenishment_count,
            total_quantity=total_quantity,
        )

        get_wms_replenishment_metrics_response_200_data_top_replenished_products_item.additional_properties = d
        return get_wms_replenishment_metrics_response_200_data_top_replenished_products_item

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
