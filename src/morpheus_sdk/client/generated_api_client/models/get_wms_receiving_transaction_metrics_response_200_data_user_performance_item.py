from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSReceivingTransactionMetricsResponse200DataUserPerformanceItem")


@_attrs_define
class GetWMSReceivingTransactionMetricsResponse200DataUserPerformanceItem:
    """
    Attributes:
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        transaction_count (Union[Unset, int]):  Example: 125.
        accuracy (Union[Unset, float]):  Example: 99.2.
        average_processing_time (Union[Unset, float]):  Example: 18.7.
    """

    user_id: Union[Unset, str] = UNSET
    transaction_count: Union[Unset, int] = UNSET
    accuracy: Union[Unset, float] = UNSET
    average_processing_time: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        transaction_count = self.transaction_count

        accuracy = self.accuracy

        average_processing_time = self.average_processing_time

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if transaction_count is not UNSET:
            field_dict["transactionCount"] = transaction_count
        if accuracy is not UNSET:
            field_dict["accuracy"] = accuracy
        if average_processing_time is not UNSET:
            field_dict["averageProcessingTime"] = average_processing_time

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        user_id = d.pop("userId", UNSET)

        transaction_count = d.pop("transactionCount", UNSET)

        accuracy = d.pop("accuracy", UNSET)

        average_processing_time = d.pop("averageProcessingTime", UNSET)

        get_wms_receiving_transaction_metrics_response_200_data_user_performance_item = cls(
            user_id=user_id,
            transaction_count=transaction_count,
            accuracy=accuracy,
            average_processing_time=average_processing_time,
        )

        get_wms_receiving_transaction_metrics_response_200_data_user_performance_item.additional_properties = d
        return get_wms_receiving_transaction_metrics_response_200_data_user_performance_item

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
