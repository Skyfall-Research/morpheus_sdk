from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_distribution_center_operating_hours_friday import WMSDistributionCenterOperatingHoursFriday
    from ..models.wms_distribution_center_operating_hours_monday import WMSDistributionCenterOperatingHoursMonday
    from ..models.wms_distribution_center_operating_hours_saturday import WMSDistributionCenterOperatingHoursSaturday
    from ..models.wms_distribution_center_operating_hours_sunday import WMSDistributionCenterOperatingHoursSunday
    from ..models.wms_distribution_center_operating_hours_thursday import WMSDistributionCenterOperatingHoursThursday
    from ..models.wms_distribution_center_operating_hours_tuesday import WMSDistributionCenterOperatingHoursTuesday
    from ..models.wms_distribution_center_operating_hours_wednesday import WMSDistributionCenterOperatingHoursWednesday


T = TypeVar("T", bound="WMSDistributionCenterOperatingHours")


@_attrs_define
class WMSDistributionCenterOperatingHours:
    """Weekly operating schedule for the facility

    Attributes:
        monday (Union[Unset, WMSDistributionCenterOperatingHoursMonday]): Monday operating hours
        tuesday (Union[Unset, WMSDistributionCenterOperatingHoursTuesday]): Tuesday operating hours
        wednesday (Union[Unset, WMSDistributionCenterOperatingHoursWednesday]): Wednesday operating hours
        thursday (Union[Unset, WMSDistributionCenterOperatingHoursThursday]): Thursday operating hours
        friday (Union[Unset, WMSDistributionCenterOperatingHoursFriday]): Friday operating hours
        saturday (Union[Unset, WMSDistributionCenterOperatingHoursSaturday]): Saturday operating hours
        sunday (Union[Unset, WMSDistributionCenterOperatingHoursSunday]): Sunday operating hours
    """

    monday: Union[Unset, "WMSDistributionCenterOperatingHoursMonday"] = UNSET
    tuesday: Union[Unset, "WMSDistributionCenterOperatingHoursTuesday"] = UNSET
    wednesday: Union[Unset, "WMSDistributionCenterOperatingHoursWednesday"] = UNSET
    thursday: Union[Unset, "WMSDistributionCenterOperatingHoursThursday"] = UNSET
    friday: Union[Unset, "WMSDistributionCenterOperatingHoursFriday"] = UNSET
    saturday: Union[Unset, "WMSDistributionCenterOperatingHoursSaturday"] = UNSET
    sunday: Union[Unset, "WMSDistributionCenterOperatingHoursSunday"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        monday: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.monday, Unset):
            monday = self.monday.to_dict()

        tuesday: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tuesday, Unset):
            tuesday = self.tuesday.to_dict()

        wednesday: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.wednesday, Unset):
            wednesday = self.wednesday.to_dict()

        thursday: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.thursday, Unset):
            thursday = self.thursday.to_dict()

        friday: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.friday, Unset):
            friday = self.friday.to_dict()

        saturday: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.saturday, Unset):
            saturday = self.saturday.to_dict()

        sunday: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.sunday, Unset):
            sunday = self.sunday.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if monday is not UNSET:
            field_dict["monday"] = monday
        if tuesday is not UNSET:
            field_dict["tuesday"] = tuesday
        if wednesday is not UNSET:
            field_dict["wednesday"] = wednesday
        if thursday is not UNSET:
            field_dict["thursday"] = thursday
        if friday is not UNSET:
            field_dict["friday"] = friday
        if saturday is not UNSET:
            field_dict["saturday"] = saturday
        if sunday is not UNSET:
            field_dict["sunday"] = sunday

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_distribution_center_operating_hours_friday import WMSDistributionCenterOperatingHoursFriday
        from ..models.wms_distribution_center_operating_hours_monday import WMSDistributionCenterOperatingHoursMonday
        from ..models.wms_distribution_center_operating_hours_saturday import (
            WMSDistributionCenterOperatingHoursSaturday,
        )
        from ..models.wms_distribution_center_operating_hours_sunday import WMSDistributionCenterOperatingHoursSunday
        from ..models.wms_distribution_center_operating_hours_thursday import (
            WMSDistributionCenterOperatingHoursThursday,
        )
        from ..models.wms_distribution_center_operating_hours_tuesday import WMSDistributionCenterOperatingHoursTuesday
        from ..models.wms_distribution_center_operating_hours_wednesday import (
            WMSDistributionCenterOperatingHoursWednesday,
        )

        d = dict(src_dict)
        _monday = d.pop("monday", UNSET)
        monday: Union[Unset, WMSDistributionCenterOperatingHoursMonday]
        if isinstance(_monday, Unset):
            monday = UNSET
        else:
            monday = WMSDistributionCenterOperatingHoursMonday.from_dict(_monday)

        _tuesday = d.pop("tuesday", UNSET)
        tuesday: Union[Unset, WMSDistributionCenterOperatingHoursTuesday]
        if isinstance(_tuesday, Unset):
            tuesday = UNSET
        else:
            tuesday = WMSDistributionCenterOperatingHoursTuesday.from_dict(_tuesday)

        _wednesday = d.pop("wednesday", UNSET)
        wednesday: Union[Unset, WMSDistributionCenterOperatingHoursWednesday]
        if isinstance(_wednesday, Unset):
            wednesday = UNSET
        else:
            wednesday = WMSDistributionCenterOperatingHoursWednesday.from_dict(_wednesday)

        _thursday = d.pop("thursday", UNSET)
        thursday: Union[Unset, WMSDistributionCenterOperatingHoursThursday]
        if isinstance(_thursday, Unset):
            thursday = UNSET
        else:
            thursday = WMSDistributionCenterOperatingHoursThursday.from_dict(_thursday)

        _friday = d.pop("friday", UNSET)
        friday: Union[Unset, WMSDistributionCenterOperatingHoursFriday]
        if isinstance(_friday, Unset):
            friday = UNSET
        else:
            friday = WMSDistributionCenterOperatingHoursFriday.from_dict(_friday)

        _saturday = d.pop("saturday", UNSET)
        saturday: Union[Unset, WMSDistributionCenterOperatingHoursSaturday]
        if isinstance(_saturday, Unset):
            saturday = UNSET
        else:
            saturday = WMSDistributionCenterOperatingHoursSaturday.from_dict(_saturday)

        _sunday = d.pop("sunday", UNSET)
        sunday: Union[Unset, WMSDistributionCenterOperatingHoursSunday]
        if isinstance(_sunday, Unset):
            sunday = UNSET
        else:
            sunday = WMSDistributionCenterOperatingHoursSunday.from_dict(_sunday)

        wms_distribution_center_operating_hours = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )

        wms_distribution_center_operating_hours.additional_properties = d
        return wms_distribution_center_operating_hours

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
