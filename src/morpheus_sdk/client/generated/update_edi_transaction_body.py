from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_edi_transaction_body_payload import UpdateEdiTransactionBodyPayload


T = TypeVar("T", bound="UpdateEdiTransactionBody")


@_attrs_define
class UpdateEdiTransactionBody:
    """
    Attributes:
        business_document_number (Union[Unset, str]):
        flow_id (Union[Unset, str]):
        payload (Union[Unset, UpdateEdiTransactionBodyPayload]):
    """

    business_document_number: Union[Unset, str] = UNSET
    flow_id: Union[Unset, str] = UNSET
    payload: Union[Unset, "UpdateEdiTransactionBodyPayload"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_document_number = self.business_document_number

        flow_id = self.flow_id

        payload: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_document_number is not UNSET:
            field_dict["businessDocumentNumber"] = business_document_number
        if flow_id is not UNSET:
            field_dict["flowId"] = flow_id
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_edi_transaction_body_payload import UpdateEdiTransactionBodyPayload

        d = dict(src_dict)
        business_document_number = d.pop("businessDocumentNumber", UNSET)

        flow_id = d.pop("flowId", UNSET)

        _payload = d.pop("payload", UNSET)
        payload: Union[Unset, UpdateEdiTransactionBodyPayload]
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = UpdateEdiTransactionBodyPayload.from_dict(_payload)

        update_edi_transaction_body = cls(
            business_document_number=business_document_number,
            flow_id=flow_id,
            payload=payload,
        )

        update_edi_transaction_body.additional_properties = d
        return update_edi_transaction_body

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
