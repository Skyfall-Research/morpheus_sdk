from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ERPInvoiceReferencesItem")


@_attrs_define
class ERPInvoiceReferencesItem:
    """
    Attributes:
        doc_type (Union[Unset, str]):  Example: SHIPMENT.
        doc_id (Union[Unset, str]):  Example: SHIP_507f1f77bcf86cd799439012.
    """

    doc_type: Union[Unset, str] = UNSET
    doc_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        doc_type = self.doc_type

        doc_id = self.doc_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if doc_type is not UNSET:
            field_dict["docType"] = doc_type
        if doc_id is not UNSET:
            field_dict["docId"] = doc_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        doc_type = d.pop("docType", UNSET)

        doc_id = d.pop("docId", UNSET)

        erp_invoice_references_item = cls(
            doc_type=doc_type,
            doc_id=doc_id,
        )

        erp_invoice_references_item.additional_properties = d
        return erp_invoice_references_item

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
