import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSInboundOrderRelationsResponse200DataFinanceTransaction")


@_attrs_define
class GetWMSInboundOrderRelationsResponse200DataFinanceTransaction:
    """Related finance transaction

    Attributes:
        transaction_id (Union[Unset, str]):  Example: fin_txn_674565c1234567890abcdef.
        type_ (Union[Unset, str]):  Example: payment_out.
        amount (Union[Unset, float]):  Example: 15000.
        status (Union[Unset, str]):  Example: COMPLETED.
        processed_at (Union[Unset, datetime.datetime]):  Example: 2024-01-20T14:30:00Z.
    """

    transaction_id: Union[Unset, str] = UNSET
    type_: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    status: Union[Unset, str] = UNSET
    processed_at: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transaction_id = self.transaction_id

        type_ = self.type_

        amount = self.amount

        status = self.status

        processed_at: Union[Unset, str] = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if amount is not UNSET:
            field_dict["amount"] = amount
        if status is not UNSET:
            field_dict["status"] = status
        if processed_at is not UNSET:
            field_dict["processedAt"] = processed_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        transaction_id = d.pop("transactionId", UNSET)

        type_ = d.pop("type", UNSET)

        amount = d.pop("amount", UNSET)

        status = d.pop("status", UNSET)

        _processed_at = d.pop("processedAt", UNSET)
        processed_at: Union[Unset, datetime.datetime]
        if isinstance(_processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = isoparse(_processed_at)

        get_wms_inbound_order_relations_response_200_data_finance_transaction = cls(
            transaction_id=transaction_id,
            type_=type_,
            amount=amount,
            status=status,
            processed_at=processed_at,
        )

        get_wms_inbound_order_relations_response_200_data_finance_transaction.additional_properties = d
        return get_wms_inbound_order_relations_response_200_data_finance_transaction

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
