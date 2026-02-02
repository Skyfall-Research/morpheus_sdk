from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_edi_transaction_body_direction import CreateEdiTransactionBodyDirection
from ..models.create_edi_transaction_body_doc_type import CreateEdiTransactionBodyDocType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEdiTransactionBody")


@_attrs_define
class CreateEdiTransactionBody:
    """
    Attributes:
        partner_id (str): Trading partner identifier Example: PARTNER_WALMART_001.
        doc_type (CreateEdiTransactionBodyDocType):  Example: 810.
        direction (CreateEdiTransactionBodyDirection):  Example: OUTBOUND.
        raw_edi (Union[Unset, str]): Raw EDI document text Example: ISA*00*          *00*          *ZZ*SENDER....
    """

    partner_id: str
    doc_type: CreateEdiTransactionBodyDocType
    direction: CreateEdiTransactionBodyDirection
    raw_edi: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partner_id = self.partner_id

        doc_type = self.doc_type.value

        direction = self.direction.value

        raw_edi = self.raw_edi

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "partnerId": partner_id,
                "docType": doc_type,
                "direction": direction,
            }
        )
        if raw_edi is not UNSET:
            field_dict["rawEdi"] = raw_edi

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        partner_id = d.pop("partnerId")

        doc_type = CreateEdiTransactionBodyDocType(d.pop("docType"))

        direction = CreateEdiTransactionBodyDirection(d.pop("direction"))

        raw_edi = d.pop("rawEdi", UNSET)

        create_edi_transaction_body = cls(
            partner_id=partner_id,
            doc_type=doc_type,
            direction=direction,
            raw_edi=raw_edi,
        )

        create_edi_transaction_body.additional_properties = d
        return create_edi_transaction_body

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
