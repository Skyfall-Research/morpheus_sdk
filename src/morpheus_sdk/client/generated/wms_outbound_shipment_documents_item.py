from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSOutboundShipmentDocumentsItem")


@_attrs_define
class WMSOutboundShipmentDocumentsItem:
    """
    Attributes:
        type_ (str): Document type identifier Example: BOL.
        url (str): Document URL or file path Example: https://docs.example.com/bol123.pdf.
        document_type (Union[Unset, str]): File format Example: PDF.
    """

    type_: str
    url: str
    document_type: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url = self.url

        document_type = self.document_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "url": url,
            }
        )
        if document_type is not UNSET:
            field_dict["documentType"] = document_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type")

        url = d.pop("url")

        document_type = d.pop("documentType", UNSET)

        wms_outbound_shipment_documents_item = cls(
            type_=type_,
            url=url,
            document_type=document_type,
        )

        wms_outbound_shipment_documents_item.additional_properties = d
        return wms_outbound_shipment_documents_item

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
