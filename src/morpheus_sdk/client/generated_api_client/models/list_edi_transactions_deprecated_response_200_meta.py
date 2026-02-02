import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="ListEdiTransactionsDeprecatedResponse200Meta")


@_attrs_define
class ListEdiTransactionsDeprecatedResponse200Meta:
    """
    Attributes:
        event (Union[Unset, str]):  Example: message.
        timestamp (Union[Unset, datetime.datetime]):  Example: 2024-01-15T10:30:00.123Z.
        deprecation_warning (Union[Unset, str]):  Example: This endpoint is deprecated. Please migrate to GET
            /{worldId}/edi with cursor-based pagination..
    """

    event: Union[Unset, str] = UNSET
    timestamp: Union[Unset, datetime.datetime] = UNSET
    deprecation_warning: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        event = self.event

        timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.timestamp, Unset):
            timestamp = self.timestamp.isoformat()

        deprecation_warning = self.deprecation_warning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if event is not UNSET:
            field_dict["event"] = event
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if deprecation_warning is not UNSET:
            field_dict["deprecationWarning"] = deprecation_warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        event = d.pop("event", UNSET)

        _timestamp = d.pop("timestamp", UNSET)
        timestamp: Union[Unset, datetime.datetime]
        if isinstance(_timestamp, Unset):
            timestamp = UNSET
        else:
            timestamp = isoparse(_timestamp)

        deprecation_warning = d.pop("deprecationWarning", UNSET)

        list_edi_transactions_deprecated_response_200_meta = cls(
            event=event,
            timestamp=timestamp,
            deprecation_warning=deprecation_warning,
        )

        list_edi_transactions_deprecated_response_200_meta.additional_properties = d
        return list_edi_transactions_deprecated_response_200_meta

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
