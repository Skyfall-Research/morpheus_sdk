from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkUpsertERPShipmentsBodyShipmentsItemLinesItem")


@_attrs_define
class BulkUpsertERPShipmentsBodyShipmentsItemLinesItem:
    """
    Attributes:
        sku (Union[Unset, str]):
        quantity_shipped (Union[Unset, float]):
    """

    sku: Union[Unset, str] = UNSET
    quantity_shipped: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku = self.sku

        quantity_shipped = self.quantity_shipped

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku is not UNSET:
            field_dict["sku"] = sku
        if quantity_shipped is not UNSET:
            field_dict["quantityShipped"] = quantity_shipped

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sku = d.pop("sku", UNSET)

        quantity_shipped = d.pop("quantityShipped", UNSET)

        bulk_upsert_erp_shipments_body_shipments_item_lines_item = cls(
            sku=sku,
            quantity_shipped=quantity_shipped,
        )

        bulk_upsert_erp_shipments_body_shipments_item_lines_item.additional_properties = d
        return bulk_upsert_erp_shipments_body_shipments_item_lines_item

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
