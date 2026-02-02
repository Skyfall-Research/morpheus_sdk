from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AddERPShipmentDocumentBody")


@_attrs_define
class AddERPShipmentDocumentBody:
    """
    Attributes:
        document_url (str): URL to the document (required) Example: https://storage.example.com/documents/bill-of-
            lading-12345.pdf.
    """

    document_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_url = self.document_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "documentUrl": document_url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        document_url = d.pop("documentUrl")

        add_erp_shipment_document_body = cls(
            document_url=document_url,
        )

        add_erp_shipment_document_body.additional_properties = d
        return add_erp_shipment_document_body

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
