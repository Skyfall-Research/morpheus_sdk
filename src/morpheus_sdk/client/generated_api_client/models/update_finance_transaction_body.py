from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_finance_transaction_body_source_type import UpdateFinanceTransactionBodySourceType
from ..models.update_finance_transaction_body_type import UpdateFinanceTransactionBodyType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_finance_transaction_body_metadata import UpdateFinanceTransactionBodyMetadata


T = TypeVar("T", bound="UpdateFinanceTransactionBody")


@_attrs_define
class UpdateFinanceTransactionBody:
    """
    Attributes:
        partner_id (Union[Unset, str]): Updated partner identifier Example: PARTNER_507f1f77bcf86cd799439015.
        type_ (Union[Unset, UpdateFinanceTransactionBodyType]): Updated transaction direction Example: payment_out.
        amount (Union[Unset, float]): Updated transaction amount Example: 1650.
        source_type (Union[Unset, UpdateFinanceTransactionBodySourceType]): Updated source document type Example: bill.
        source_id (Union[Unset, str]): Updated source document identifier Example: BILL_507f1f77bcf86cd799439016.
        metadata (Union[Unset, UpdateFinanceTransactionBodyMetadata]): Updated transaction metadata Example:
            {'paymentMethod': 'WIRE', 'correctionReason': 'Amount adjustment per accounting review'}.
    """

    partner_id: Union[Unset, str] = UNSET
    type_: Union[Unset, UpdateFinanceTransactionBodyType] = UNSET
    amount: Union[Unset, float] = UNSET
    source_type: Union[Unset, UpdateFinanceTransactionBodySourceType] = UNSET
    source_id: Union[Unset, str] = UNSET
    metadata: Union[Unset, "UpdateFinanceTransactionBodyMetadata"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        partner_id = self.partner_id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        amount = self.amount

        source_type: Union[Unset, str] = UNSET
        if not isinstance(self.source_type, Unset):
            source_type = self.source_type.value

        source_id = self.source_id

        metadata: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if partner_id is not UNSET:
            field_dict["partnerId"] = partner_id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if amount is not UNSET:
            field_dict["amount"] = amount
        if source_type is not UNSET:
            field_dict["sourceType"] = source_type
        if source_id is not UNSET:
            field_dict["sourceId"] = source_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_finance_transaction_body_metadata import UpdateFinanceTransactionBodyMetadata

        d = dict(src_dict)
        partner_id = d.pop("partnerId", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, UpdateFinanceTransactionBodyType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = UpdateFinanceTransactionBodyType(_type_)

        amount = d.pop("amount", UNSET)

        _source_type = d.pop("sourceType", UNSET)
        source_type: Union[Unset, UpdateFinanceTransactionBodySourceType]
        if isinstance(_source_type, Unset):
            source_type = UNSET
        else:
            source_type = UpdateFinanceTransactionBodySourceType(_source_type)

        source_id = d.pop("sourceId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, UpdateFinanceTransactionBodyMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = UpdateFinanceTransactionBodyMetadata.from_dict(_metadata)

        update_finance_transaction_body = cls(
            partner_id=partner_id,
            type_=type_,
            amount=amount,
            source_type=source_type,
            source_id=source_id,
            metadata=metadata,
        )

        update_finance_transaction_body.additional_properties = d
        return update_finance_transaction_body

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
