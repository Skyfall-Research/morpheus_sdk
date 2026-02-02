from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSDistributionCenterOperatingHoursMonday")


@_attrs_define
class WMSDistributionCenterOperatingHoursMonday:
    """Monday operating hours

    Attributes:
        open_ (Union[Unset, str]): Opening time in HH:MM format Example: 06:00.
        close (Union[Unset, str]): Closing time in HH:MM format Example: 22:00.
    """

    open_: Union[Unset, str] = UNSET
    close: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        close = self.close

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_ is not UNSET:
            field_dict["open"] = open_
        if close is not UNSET:
            field_dict["close"] = close

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        open_ = d.pop("open", UNSET)

        close = d.pop("close", UNSET)

        wms_distribution_center_operating_hours_monday = cls(
            open_=open_,
            close=close,
        )

        wms_distribution_center_operating_hours_monday.additional_properties = d
        return wms_distribution_center_operating_hours_monday

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
