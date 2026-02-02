from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_receiving_transaction_metrics_response_200_data_daily_volume_item import (
        GetWMSReceivingTransactionMetricsResponse200DataDailyVolumeItem,
    )
    from ..models.get_wms_receiving_transaction_metrics_response_200_data_user_performance_item import (
        GetWMSReceivingTransactionMetricsResponse200DataUserPerformanceItem,
    )


T = TypeVar("T", bound="GetWMSReceivingTransactionMetricsResponse200Data")


@_attrs_define
class GetWMSReceivingTransactionMetricsResponse200Data:
    """
    Attributes:
        total_transactions (Union[Unset, int]): Total number of receiving transactions Example: 1250.
        completed_transactions (Union[Unset, int]): Number of completed transactions Example: 1180.
        pending_transactions (Union[Unset, int]): Number of pending transactions Example: 70.
        discrepancies (Union[Unset, int]): Number of transactions with quantity discrepancies Example: 45.
        total_items_received (Union[Unset, int]): Total quantity of items received Example: 15750.
        total_items_expected (Union[Unset, int]): Total quantity of items expected Example: 16000.
        receiving_accuracy (Union[Unset, float]): Receiving accuracy percentage Example: 98.44.
        average_processing_time (Union[Unset, float]): Average processing time in minutes Example: 23.5.
        user_performance (Union[Unset, list['GetWMSReceivingTransactionMetricsResponse200DataUserPerformanceItem']]):
        daily_volume (Union[Unset, list['GetWMSReceivingTransactionMetricsResponse200DataDailyVolumeItem']]):
    """

    total_transactions: Union[Unset, int] = UNSET
    completed_transactions: Union[Unset, int] = UNSET
    pending_transactions: Union[Unset, int] = UNSET
    discrepancies: Union[Unset, int] = UNSET
    total_items_received: Union[Unset, int] = UNSET
    total_items_expected: Union[Unset, int] = UNSET
    receiving_accuracy: Union[Unset, float] = UNSET
    average_processing_time: Union[Unset, float] = UNSET
    user_performance: Union[Unset, list["GetWMSReceivingTransactionMetricsResponse200DataUserPerformanceItem"]] = UNSET
    daily_volume: Union[Unset, list["GetWMSReceivingTransactionMetricsResponse200DataDailyVolumeItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_transactions = self.total_transactions

        completed_transactions = self.completed_transactions

        pending_transactions = self.pending_transactions

        discrepancies = self.discrepancies

        total_items_received = self.total_items_received

        total_items_expected = self.total_items_expected

        receiving_accuracy = self.receiving_accuracy

        average_processing_time = self.average_processing_time

        user_performance: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.user_performance, Unset):
            user_performance = []
            for user_performance_item_data in self.user_performance:
                user_performance_item = user_performance_item_data.to_dict()
                user_performance.append(user_performance_item)

        daily_volume: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.daily_volume, Unset):
            daily_volume = []
            for daily_volume_item_data in self.daily_volume:
                daily_volume_item = daily_volume_item_data.to_dict()
                daily_volume.append(daily_volume_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_transactions is not UNSET:
            field_dict["totalTransactions"] = total_transactions
        if completed_transactions is not UNSET:
            field_dict["completedTransactions"] = completed_transactions
        if pending_transactions is not UNSET:
            field_dict["pendingTransactions"] = pending_transactions
        if discrepancies is not UNSET:
            field_dict["discrepancies"] = discrepancies
        if total_items_received is not UNSET:
            field_dict["totalItemsReceived"] = total_items_received
        if total_items_expected is not UNSET:
            field_dict["totalItemsExpected"] = total_items_expected
        if receiving_accuracy is not UNSET:
            field_dict["receivingAccuracy"] = receiving_accuracy
        if average_processing_time is not UNSET:
            field_dict["averageProcessingTime"] = average_processing_time
        if user_performance is not UNSET:
            field_dict["userPerformance"] = user_performance
        if daily_volume is not UNSET:
            field_dict["dailyVolume"] = daily_volume

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_wms_receiving_transaction_metrics_response_200_data_daily_volume_item import (
            GetWMSReceivingTransactionMetricsResponse200DataDailyVolumeItem,
        )
        from ..models.get_wms_receiving_transaction_metrics_response_200_data_user_performance_item import (
            GetWMSReceivingTransactionMetricsResponse200DataUserPerformanceItem,
        )

        d = dict(src_dict)
        total_transactions = d.pop("totalTransactions", UNSET)

        completed_transactions = d.pop("completedTransactions", UNSET)

        pending_transactions = d.pop("pendingTransactions", UNSET)

        discrepancies = d.pop("discrepancies", UNSET)

        total_items_received = d.pop("totalItemsReceived", UNSET)

        total_items_expected = d.pop("totalItemsExpected", UNSET)

        receiving_accuracy = d.pop("receivingAccuracy", UNSET)

        average_processing_time = d.pop("averageProcessingTime", UNSET)

        user_performance = []
        _user_performance = d.pop("userPerformance", UNSET)
        for user_performance_item_data in _user_performance or []:
            user_performance_item = GetWMSReceivingTransactionMetricsResponse200DataUserPerformanceItem.from_dict(
                user_performance_item_data
            )

            user_performance.append(user_performance_item)

        daily_volume = []
        _daily_volume = d.pop("dailyVolume", UNSET)
        for daily_volume_item_data in _daily_volume or []:
            daily_volume_item = GetWMSReceivingTransactionMetricsResponse200DataDailyVolumeItem.from_dict(
                daily_volume_item_data
            )

            daily_volume.append(daily_volume_item)

        get_wms_receiving_transaction_metrics_response_200_data = cls(
            total_transactions=total_transactions,
            completed_transactions=completed_transactions,
            pending_transactions=pending_transactions,
            discrepancies=discrepancies,
            total_items_received=total_items_received,
            total_items_expected=total_items_expected,
            receiving_accuracy=receiving_accuracy,
            average_processing_time=average_processing_time,
            user_performance=user_performance,
            daily_volume=daily_volume,
        )

        get_wms_receiving_transaction_metrics_response_200_data.additional_properties = d
        return get_wms_receiving_transaction_metrics_response_200_data

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
