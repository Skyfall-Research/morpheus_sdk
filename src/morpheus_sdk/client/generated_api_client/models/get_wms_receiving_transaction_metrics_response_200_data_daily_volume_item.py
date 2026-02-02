import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSReceivingTransactionMetricsResponse200DataDailyVolumeItem")


@_attrs_define
class GetWMSReceivingTransactionMetricsResponse200DataDailyVolumeItem:
    """
    Attributes:
        date (Union[Unset, datetime.date]):  Example: 2024-11-15.
        transaction_count (Union[Unset, int]):  Example: 45.
        items_received (Union[Unset, int]):  Example: 580.
        accuracy (Union[Unset, float]):  Example: 97.8.
    """

    date: Union[Unset, datetime.date] = UNSET
    transaction_count: Union[Unset, int] = UNSET
    items_received: Union[Unset, int] = UNSET
    accuracy: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        transaction_count = self.transaction_count

        items_received = self.items_received

        accuracy = self.accuracy

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if transaction_count is not UNSET:
            field_dict["transactionCount"] = transaction_count
        if items_received is not UNSET:
            field_dict["itemsReceived"] = items_received
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        transaction_count = d.pop("transactionCount", UNSET)

        items_received = d.pop("itemsReceived", UNSET)

        accuracy = d.pop("accuracy", UNSET)

        get_wms_receiving_transaction_metrics_response_200_data_daily_volume_item = cls(
            date=date,
            transaction_count=transaction_count,
            items_received=items_received,
            accuracy=accuracy,
        )

        get_wms_receiving_transaction_metrics_response_200_data_daily_volume_item.additional_properties = d
        return get_wms_receiving_transaction_metrics_response_200_data_daily_volume_item

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
