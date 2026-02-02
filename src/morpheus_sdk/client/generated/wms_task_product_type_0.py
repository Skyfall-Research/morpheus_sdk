from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSTaskProductType0")


@_attrs_define
class WMSTaskProductType0:
    """Product information associated with the task

    Attributes:
        product_id (Union[Unset, str]): Product identifier Example: PROD-12345.
        sku (Union[Unset, str]): Stock keeping unit code Example: ABC-XYZ-001.
        product_name (Union[Unset, str]): Human-readable product name Example: Widget Premium.
    """

    product_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        product_id = self.product_id

        sku = self.sku

        product_name = self.product_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if product_name is not UNSET:
            field_dict["productName"] = product_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        product_id = d.pop("productId", UNSET)

        sku = d.pop("sku", UNSET)

        product_name = d.pop("productName", UNSET)

        wms_task_product_type_0 = cls(
            product_id=product_id,
            sku=sku,
            product_name=product_name,
        )

        wms_task_product_type_0.additional_properties = d
        return wms_task_product_type_0

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
