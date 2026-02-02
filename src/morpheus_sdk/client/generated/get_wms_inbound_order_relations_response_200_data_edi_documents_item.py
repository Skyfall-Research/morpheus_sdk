import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInboundOrderRelationsResponse200DataEdiDocumentsItem")


@_attrs_define
class GetWMSInboundOrderRelationsResponse200DataEdiDocumentsItem:
    """
    Attributes:
        transaction_id (Union[Unset, str]):  Example: edi_txn_674565c1234567890abcdef.
        doc_type (Union[Unset, str]):  Example: 856.
        status (Union[Unset, str]):  Example: PROCESSED.
        direction (Union[Unset, str]):  Example: INBOUND.
        timestamp (Union[Unset, datetime.datetime]):  Example: 2024-01-15T10:30:00Z.
        business_document_number (Union[Unset, str]):  Example: PO-2024-001234.
    """

    transaction_id: Union[Unset, str] = UNSET
    doc_type: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    direction: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    business_document_number: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_id = self.transaction_id

        doc_type = self.doc_type

        status = self.status

        direction = self.direction

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        business_document_number = self.business_document_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if doc_type is not UNSET:
            field_dict["docType"] = doc_type
        if status is not UNSET:
            field_dict["status"] = status
        if direction is not UNSET:
            field_dict["direction"] = direction
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if business_document_number is not UNSET:
            field_dict["businessDocumentNumber"] = business_document_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_id = d.pop("transactionId", UNSET)

        doc_type = d.pop("docType", UNSET)

        status = d.pop("status", UNSET)

        direction = d.pop("direction", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        business_document_number = d.pop("businessDocumentNumber", UNSET)

        get_wms_inbound_order_relations_response_200_data_edi_documents_item = cls(
            transaction_id=transaction_id,
            doc_type=doc_type,
            status=status,
            direction=direction,
            timestamp=timestamp,
            business_document_number=business_document_number,
        )

        get_wms_inbound_order_relations_response_200_data_edi_documents_item.additional_properties = d
        return get_wms_inbound_order_relations_response_200_data_edi_documents_item

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
