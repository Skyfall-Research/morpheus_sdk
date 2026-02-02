import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompleteTMSTrailerUnloadingBody")


@_attrs_define
class CompleteTMSTrailerUnloadingBody:
    """
    Attributes:
        completion_time (datetime.datetime): Timestamp when unloading was completed Example: 2024-01-20T15:30:00.000Z.
        actual_pallets (Union[Unset, int]): Actual number of pallets received Example: 18.
    """

    completion_time: datetime.datetime
    actual_pallets: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        completion_time = self.completion_time.isoformat()

        actual_pallets = self.actual_pallets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completionTime": completion_time,
            }
        )
        if actual_pallets is not UNSET:
            field_dict["actualPallets"] = actual_pallets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        completion_time = isoparse(d.pop("completionTime"))

        actual_pallets = d.pop("actualPallets", UNSET)

        complete_tms_trailer_unloading_body = cls(
            completion_time=completion_time,
            actual_pallets=actual_pallets,
        )

        complete_tms_trailer_unloading_body.additional_properties = d
        return complete_tms_trailer_unloading_body

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
