from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.edi_transaction import EdiTransaction
    from ..models.list_edi_transactions_deprecated_response_200_meta import ListEdiTransactionsDeprecatedResponse200Meta
    from ..models.list_edi_transactions_deprecated_response_200_pagination import (
        ListEdiTransactionsDeprecatedResponse200Pagination,
    )


T = TypeVar("T", bound="ListEdiTransactionsDeprecatedResponse200")


@_attrs_define
class ListEdiTransactionsDeprecatedResponse200:
    """
    Attributes:
        success (bool):  Example: True.
        status (int):  Example: 200.
        data (list['EdiTransaction']): Array of EDI transaction objects for the requested page
        meta (ListEdiTransactionsDeprecatedResponse200Meta):
        pagination (Union[Unset, ListEdiTransactionsDeprecatedResponse200Pagination]): Pagination metadata. Note:
            nextCursor and previousCursor are always null in this deprecated endpoint.
    """

    success: bool
    status: int
    data: list["EdiTransaction"]
    meta: "ListEdiTransactionsDeprecatedResponse200Meta"
    pagination: Union[Unset, "ListEdiTransactionsDeprecatedResponse200Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
                "data": data,
                "meta": meta,
            }
        )
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edi_transaction import EdiTransaction
        from ..models.list_edi_transactions_deprecated_response_200_meta import (
            ListEdiTransactionsDeprecatedResponse200Meta,
        )
        from ..models.list_edi_transactions_deprecated_response_200_pagination import (
            ListEdiTransactionsDeprecatedResponse200Pagination,
        )

        d = dict(src_dict)
        success = d.pop("success")

        status = d.pop("status")

        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = EdiTransaction.from_dict(data_item_data)

            data.append(data_item)

        meta = ListEdiTransactionsDeprecatedResponse200Meta.from_dict(d.pop("meta"))

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, ListEdiTransactionsDeprecatedResponse200Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = ListEdiTransactionsDeprecatedResponse200Pagination.from_dict(_pagination)

        list_edi_transactions_deprecated_response_200 = cls(
            success=success,
            status=status,
            data=data,
            meta=meta,
            pagination=pagination,
        )

        list_edi_transactions_deprecated_response_200.additional_properties = d
        return list_edi_transactions_deprecated_response_200

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
