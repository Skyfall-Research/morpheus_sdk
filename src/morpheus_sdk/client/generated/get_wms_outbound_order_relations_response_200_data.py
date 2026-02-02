from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_outbound_order_relations_response_200_data_edi_documents_item import (
        GetWMSOutboundOrderRelationsResponse200DataEdiDocumentsItem,
    )
    from ..models.get_wms_outbound_order_relations_response_200_data_erp_order import (
        GetWMSOutboundOrderRelationsResponse200DataErpOrder,
    )
    from ..models.get_wms_outbound_order_relations_response_200_data_finance_transaction import (
        GetWMSOutboundOrderRelationsResponse200DataFinanceTransaction,
    )


T = TypeVar("T", bound="GetWMSOutboundOrderRelationsResponse200Data")


@_attrs_define
class GetWMSOutboundOrderRelationsResponse200Data:
    """
    Attributes:
        erp_order (Union[Unset, GetWMSOutboundOrderRelationsResponse200DataErpOrder]): Related ERP sales order
        edi_documents (Union[Unset, list['GetWMSOutboundOrderRelationsResponse200DataEdiDocumentsItem']]): Related EDI
            documents
        finance_transaction (Union[Unset, GetWMSOutboundOrderRelationsResponse200DataFinanceTransaction]): Related
            finance transaction
    """

    erp_order: Union[Unset, "GetWMSOutboundOrderRelationsResponse200DataErpOrder"] = UNSET
    edi_documents: Union[Unset, list["GetWMSOutboundOrderRelationsResponse200DataEdiDocumentsItem"]] = UNSET
    finance_transaction: Union[Unset, "GetWMSOutboundOrderRelationsResponse200DataFinanceTransaction"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        erp_order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.erp_order, Unset):
            erp_order = self.erp_order.to_dict()

        edi_documents: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.edi_documents, Unset):
            edi_documents = []
            for edi_documents_item_data in self.edi_documents:
                edi_documents_item = edi_documents_item_data.to_dict()
                edi_documents.append(edi_documents_item)

        finance_transaction: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.finance_transaction, Unset):
            finance_transaction = self.finance_transaction.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if erp_order is not UNSET:
            field_dict["erpOrder"] = erp_order
        if edi_documents is not UNSET:
            field_dict["ediDocuments"] = edi_documents
        if finance_transaction is not UNSET:
            field_dict["financeTransaction"] = finance_transaction

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_outbound_order_relations_response_200_data_edi_documents_item import (
            GetWMSOutboundOrderRelationsResponse200DataEdiDocumentsItem,
        )
        from ..models.get_wms_outbound_order_relations_response_200_data_erp_order import (
            GetWMSOutboundOrderRelationsResponse200DataErpOrder,
        )
        from ..models.get_wms_outbound_order_relations_response_200_data_finance_transaction import (
            GetWMSOutboundOrderRelationsResponse200DataFinanceTransaction,
        )

        d = dict(src_dict)
        _erp_order = d.pop("erpOrder", UNSET)
        erp_order: Union[Unset, GetWMSOutboundOrderRelationsResponse200DataErpOrder]
        if isinstance(_erp_order, Unset):
            erp_order = UNSET
        else:
            erp_order = GetWMSOutboundOrderRelationsResponse200DataErpOrder.from_dict(_erp_order)

        edi_documents = []
        _edi_documents = d.pop("ediDocuments", UNSET)
        for edi_documents_item_data in _edi_documents or []:
            edi_documents_item = GetWMSOutboundOrderRelationsResponse200DataEdiDocumentsItem.from_dict(
                edi_documents_item_data
            )

            edi_documents.append(edi_documents_item)

        _finance_transaction = d.pop("financeTransaction", UNSET)
        finance_transaction: Union[Unset, GetWMSOutboundOrderRelationsResponse200DataFinanceTransaction]
        if isinstance(_finance_transaction, Unset):
            finance_transaction = UNSET
        else:
            finance_transaction = GetWMSOutboundOrderRelationsResponse200DataFinanceTransaction.from_dict(
                _finance_transaction
            )

        get_wms_outbound_order_relations_response_200_data = cls(
            erp_order=erp_order,
            edi_documents=edi_documents,
            finance_transaction=finance_transaction,
        )

        get_wms_outbound_order_relations_response_200_data.additional_properties = d
        return get_wms_outbound_order_relations_response_200_data

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
