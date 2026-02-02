from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetWMSOperationsDashboardResponse200DataReceiving")


@_attrs_define
class GetWMSOperationsDashboardResponse200DataReceiving:
    """
    Attributes:
        total (Union[Unset, int]):  Example: 156.
        pending (Union[Unset, int]):  Example: 23.
        expected (Union[Unset, int]):  Example: 15.
        in_transit (Union[Unset, int]):  Example: 5.
        receiving (Union[Unset, int]):  Example: 3.
        received (Union[Unset, int]):  Example: 133.
        due_today (Union[Unset, int]):  Example: 8.
    """

    total: Union[Unset, int] = UNSET
    pending: Union[Unset, int] = UNSET
    expected: Union[Unset, int] = UNSET
    in_transit: Union[Unset, int] = UNSET
    receiving: Union[Unset, int] = UNSET
    received: Union[Unset, int] = UNSET
    due_today: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        pending = self.pending

        expected = self.expected

        in_transit = self.in_transit

        receiving = self.receiving

        received = self.received

        due_today = self.due_today

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if pending is not UNSET:
            field_dict["pending"] = pending
        if expected is not UNSET:
            field_dict["expected"] = expected
        if in_transit is not UNSET:
            field_dict["inTransit"] = in_transit
        if receiving is not UNSET:
            field_dict["receiving"] = receiving
        if received is not UNSET:
            field_dict["received"] = received
        if due_today is not UNSET:
            field_dict["dueToday"] = due_today

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        pending = d.pop("pending", UNSET)

        expected = d.pop("expected", UNSET)

        in_transit = d.pop("inTransit", UNSET)

        receiving = d.pop("receiving", UNSET)

        received = d.pop("received", UNSET)

        due_today = d.pop("dueToday", UNSET)

        get_wms_operations_dashboard_response_200_data_receiving = cls(
            total=total,
            pending=pending,
            expected=expected,
            in_transit=in_transit,
            receiving=receiving,
            received=received,
            due_today=due_today,
        )

        get_wms_operations_dashboard_response_200_data_receiving.additional_properties = d
        return get_wms_operations_dashboard_response_200_data_receiving

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
