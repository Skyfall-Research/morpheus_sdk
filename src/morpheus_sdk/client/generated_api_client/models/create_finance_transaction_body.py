from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_finance_transaction_body_source_type import CreateFinanceTransactionBodySourceType
from ..models.create_finance_transaction_body_type import CreateFinanceTransactionBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_finance_transaction_body_metadata import CreateFinanceTransactionBodyMetadata


T = TypeVar("T", bound="CreateFinanceTransactionBody")


@_attrs_define
class CreateFinanceTransactionBody:
    """
    Attributes:
        type_ (CreateFinanceTransactionBodyType): Transaction direction (required) Example: payment_in.
        amount (float): Transaction amount - must be greater than 0 (required) Example: 1500.
        source_type (CreateFinanceTransactionBodySourceType): Source document type (required) Example: invoice.
        source_id (str): Source document identifier (required) Example: INV_507f1f77bcf86cd799439014.
        transaction_id (Union[Unset, str]): Optional custom transaction identifier (auto-generated if not provided)
            Example: TRANS_507f1f77bcf86cd799439012.
        partner_id (Union[Unset, str]): Partner identifier for transaction association Example:
            PARTNER_507f1f77bcf86cd799439013.
        metadata (Union[Unset, CreateFinanceTransactionBodyMetadata]): Additional transaction-specific data Example:
            {'paymentMethod': 'ACH', 'bankReference': 'REF123456', 'customerReference': 'CUST_PAY_001'}.
    """

    type_: CreateFinanceTransactionBodyType
    amount: float
    source_type: CreateFinanceTransactionBodySourceType
    source_id: str
    transaction_id: Union[Unset, str] = UNSET
    partner_id: Union[Unset, str] = UNSET
    metadata: Union[Unset, "CreateFinanceTransactionBodyMetadata"] = UNSET
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
        from ..models.create_finance_transaction_body_metadata import CreateFinanceTransactionBodyMetadata

        d = dict(src_dict)
        type_ = CreateFinanceTransactionBodyType(d.pop("type"))

        amount = d.pop("amount")

        source_type = CreateFinanceTransactionBodySourceType(d.pop("sourceType"))

        source_id = d.pop("sourceId")

        transaction_id = d.pop("transactionId", UNSET)

        partner_id = d.pop("partnerId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CreateFinanceTransactionBodyMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateFinanceTransactionBodyMetadata.from_dict(_metadata)

        create_finance_transaction_body = cls(
            type_=type_,
            amount=amount,
            source_type=source_type,
            source_id=source_id,
            transaction_id=transaction_id,
            partner_id=partner_id,
            metadata=metadata,
        )

        create_finance_transaction_body.additional_properties = d
        return create_finance_transaction_body

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
