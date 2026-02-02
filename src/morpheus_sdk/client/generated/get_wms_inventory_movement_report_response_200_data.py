from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_inventory_movement_report_response_200_data_movements_by_date_item import (
        GetWMSInventoryMovementReportResponse200DataMovementsByDateItem,
    )
    from ..models.get_wms_inventory_movement_report_response_200_data_top_moving_products_item import (
        GetWMSInventoryMovementReportResponse200DataTopMovingProductsItem,
    )
    from ..models.get_wms_inventory_movement_report_response_200_data_transactions_by_type_item import (
        GetWMSInventoryMovementReportResponse200DataTransactionsByTypeItem,
    )


T = TypeVar("T", bound="GetWMSInventoryMovementReportResponse200Data")


@_attrs_define
class GetWMSInventoryMovementReportResponse200Data:
    """
    Attributes:
        total_transactions (Union[Unset, int]): Total number of inventory transactions in period Example: 2847.
        transactions_by_type (Union[Unset, list['GetWMSInventoryMovementReportResponse200DataTransactionsByTypeItem']]):
        top_moving_products (Union[Unset, list['GetWMSInventoryMovementReportResponse200DataTopMovingProductsItem']]):
        movements_by_date (Union[Unset, list['GetWMSInventoryMovementReportResponse200DataMovementsByDateItem']]):
    """

    total_transactions: Union[Unset, int] = UNSET
    transactions_by_type: Union[Unset, list["GetWMSInventoryMovementReportResponse200DataTransactionsByTypeItem"]] = (
        UNSET
    )
    top_moving_products: Union[Unset, list["GetWMSInventoryMovementReportResponse200DataTopMovingProductsItem"]] = UNSET
    movements_by_date: Union[Unset, list["GetWMSInventoryMovementReportResponse200DataMovementsByDateItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_transactions = self.total_transactions

        transactions_by_type: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transactions_by_type, Unset):
            transactions_by_type = []
            for transactions_by_type_item_data in self.transactions_by_type:
                transactions_by_type_item = transactions_by_type_item_data.to_dict()
                transactions_by_type.append(transactions_by_type_item)

        top_moving_products: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.top_moving_products, Unset):
            top_moving_products = []
            for top_moving_products_item_data in self.top_moving_products:
                top_moving_products_item = top_moving_products_item_data.to_dict()
                top_moving_products.append(top_moving_products_item)

        movements_by_date: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.movements_by_date, Unset):
            movements_by_date = []
            for movements_by_date_item_data in self.movements_by_date:
                movements_by_date_item = movements_by_date_item_data.to_dict()
                movements_by_date.append(movements_by_date_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_transactions is not UNSET:
            field_dict["totalTransactions"] = total_transactions
        if transactions_by_type is not UNSET:
            field_dict["transactionsByType"] = transactions_by_type
        if top_moving_products is not UNSET:
            field_dict["topMovingProducts"] = top_moving_products
        if movements_by_date is not UNSET:
            field_dict["movementsByDate"] = movements_by_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_inventory_movement_report_response_200_data_movements_by_date_item import (
            GetWMSInventoryMovementReportResponse200DataMovementsByDateItem,
        )
        from ..models.get_wms_inventory_movement_report_response_200_data_top_moving_products_item import (
            GetWMSInventoryMovementReportResponse200DataTopMovingProductsItem,
        )
        from ..models.get_wms_inventory_movement_report_response_200_data_transactions_by_type_item import (
            GetWMSInventoryMovementReportResponse200DataTransactionsByTypeItem,
        )

        d = dict(src_dict)
        total_transactions = d.pop("totalTransactions", UNSET)

        transactions_by_type = []
        _transactions_by_type = d.pop("transactionsByType", UNSET)
        for transactions_by_type_item_data in _transactions_by_type or []:
            transactions_by_type_item = GetWMSInventoryMovementReportResponse200DataTransactionsByTypeItem.from_dict(
                transactions_by_type_item_data
            )

            transactions_by_type.append(transactions_by_type_item)

        top_moving_products = []
        _top_moving_products = d.pop("topMovingProducts", UNSET)
        for top_moving_products_item_data in _top_moving_products or []:
            top_moving_products_item = GetWMSInventoryMovementReportResponse200DataTopMovingProductsItem.from_dict(
                top_moving_products_item_data
            )

            top_moving_products.append(top_moving_products_item)

        movements_by_date = []
        _movements_by_date = d.pop("movementsByDate", UNSET)
        for movements_by_date_item_data in _movements_by_date or []:
            movements_by_date_item = GetWMSInventoryMovementReportResponse200DataMovementsByDateItem.from_dict(
                movements_by_date_item_data
            )

            movements_by_date.append(movements_by_date_item)

        get_wms_inventory_movement_report_response_200_data = cls(
            total_transactions=total_transactions,
            transactions_by_type=transactions_by_type,
            top_moving_products=top_moving_products,
            movements_by_date=movements_by_date,
        )

        get_wms_inventory_movement_report_response_200_data.additional_properties = d
        return get_wms_inventory_movement_report_response_200_data

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
