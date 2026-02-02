from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bulk_insert_finance_transactions_body_transactions_item_source_type import (
    BulkInsertFinanceTransactionsBodyTransactionsItemSourceType,
)
from ..models.bulk_insert_finance_transactions_body_transactions_item_type import (
    BulkInsertFinanceTransactionsBodyTransactionsItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_insert_finance_transactions_body_transactions_item_metadata import (
        BulkInsertFinanceTransactionsBodyTransactionsItemMetadata,
    )


T = TypeVar("T", bound="BulkInsertFinanceTransactionsBodyTransactionsItem")


@_attrs_define
class BulkInsertFinanceTransactionsBodyTransactionsItem:
    """
    Attributes:
        type_ (BulkInsertFinanceTransactionsBodyTransactionsItemType): Transaction direction Example: payment_in.
        amount (float): Transaction amount Example: 1500.
        source_type (BulkInsertFinanceTransactionsBodyTransactionsItemSourceType): Source document type Example:
            invoice.
        source_id (str): Source document identifier Example: INV_507f1f77bcf86cd799439014.
        transaction_id (Union[Unset, str]): Optional transaction identifier Example: TRANS_507f1f77bcf86cd799439012.
        partner_id (Union[Unset, str]): Partner identifier Example: PARTNER_507f1f77bcf86cd799439013.
        metadata (Union[Unset, BulkInsertFinanceTransactionsBodyTransactionsItemMetadata]): Additional transaction data
    """

    type_: BulkInsertFinanceTransactionsBodyTransactionsItemType
    amount: float
    source_type: BulkInsertFinanceTransactionsBodyTransactionsItemSourceType
    source_id: str
    transaction_id: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    metadata: Union[Unset, "BulkInsertFinanceTransactionsBodyTransactionsItemMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        amount = self.amount

        source_type = self.source_type.value

        source_id = self.source_id

        transaction_id = self.transaction_id

        partner_id = self.partner_id

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "amount": amount,
                "sourceType": source_type,
                "sourceId": source_id,
            }
        )
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_insert_finance_transactions_body_transactions_item_metadata import (
            BulkInsertFinanceTransactionsBodyTransactionsItemMetadata,
        )

        d = dict(src_dict)
        type_ = BulkInsertFinanceTransactionsBodyTransactionsItemType(d.pop("type"))

        amount = d.pop("amount")

        source_type = BulkInsertFinanceTransactionsBodyTransactionsItemSourceType(d.pop("sourceType"))

        source_id = d.pop("sourceId")

        transaction_id = d.pop("transactionId", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, BulkInsertFinanceTransactionsBodyTransactionsItemMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = BulkInsertFinanceTransactionsBodyTransactionsItemMetadata.from_dict(_metadata)

        bulk_insert_finance_transactions_body_transactions_item = cls(
            type_=type_,
            amount=amount,
            source_type=source_type,
            source_id=source_id,
            transaction_id=transaction_id,
            partner_id=partner_id,
            metadata=metadata,
        )

        bulk_insert_finance_transactions_body_transactions_item.additional_properties = d
        return bulk_insert_finance_transactions_body_transactions_item

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
