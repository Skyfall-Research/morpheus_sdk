from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_friday import (
        GetWMSDistributionCenterCapacityResponse200DataOperationalHoursFriday,
    )
    from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_monday import (
        GetWMSDistributionCenterCapacityResponse200DataOperationalHoursMonday,
    )
    from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_saturday import (
        GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSaturday,
    )
    from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_sunday import (
        GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSunday,
    )
    from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_thursday import (
        GetWMSDistributionCenterCapacityResponse200DataOperationalHoursThursday,
    )
    from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_tuesday import (
        GetWMSDistributionCenterCapacityResponse200DataOperationalHoursTuesday,
    )
    from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_wednesday import (
        GetWMSDistributionCenterCapacityResponse200DataOperationalHoursWednesday,
    )


T = TypeVar("T", bound="GetWMSDistributionCenterCapacityResponse200DataOperationalHours")


@_attrs_define
class GetWMSDistributionCenterCapacityResponse200DataOperationalHours:
    """Facility operating hours schedule

    Attributes:
        monday (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursMonday]):
        tuesday (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursTuesday]):
        wednesday (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursWednesday]):
        thursday (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursThursday]):
        friday (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursFriday]):
        saturday (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSaturday]):
        sunday (Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSunday]):
    """

    monday: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataOperationalHoursMonday"] = UNSET
    tuesday: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataOperationalHoursTuesday"] = UNSET
    wednesday: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataOperationalHoursWednesday"] = UNSET
    thursday: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataOperationalHoursThursday"] = UNSET
    friday: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataOperationalHoursFriday"] = UNSET
    saturday: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSaturday"] = UNSET
    sunday: Union[Unset, "GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSunday"] = UNSET
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
        from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_friday import (
            GetWMSDistributionCenterCapacityResponse200DataOperationalHoursFriday,
        )
        from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_monday import (
            GetWMSDistributionCenterCapacityResponse200DataOperationalHoursMonday,
        )
        from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_saturday import (
            GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSaturday,
        )
        from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_sunday import (
            GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSunday,
        )
        from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_thursday import (
            GetWMSDistributionCenterCapacityResponse200DataOperationalHoursThursday,
        )
        from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_tuesday import (
            GetWMSDistributionCenterCapacityResponse200DataOperationalHoursTuesday,
        )
        from ..models.get_wms_distribution_center_capacity_response_200_data_operational_hours_wednesday import (
            GetWMSDistributionCenterCapacityResponse200DataOperationalHoursWednesday,
        )

        d = dict(src_dict)
        _monday = d.pop("monday", UNSET)
        monday: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursMonday]
        if isinstance(_monday, Unset):
            monday = UNSET
        else:
            monday = GetWMSDistributionCenterCapacityResponse200DataOperationalHoursMonday.from_dict(_monday)

        _tuesday = d.pop("tuesday", UNSET)
        tuesday: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursTuesday]
        if isinstance(_tuesday, Unset):
            tuesday = UNSET
        else:
            tuesday = GetWMSDistributionCenterCapacityResponse200DataOperationalHoursTuesday.from_dict(_tuesday)

        _wednesday = d.pop("wednesday", UNSET)
        wednesday: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursWednesday]
        if isinstance(_wednesday, Unset):
            wednesday = UNSET
        else:
            wednesday = GetWMSDistributionCenterCapacityResponse200DataOperationalHoursWednesday.from_dict(_wednesday)

        _thursday = d.pop("thursday", UNSET)
        thursday: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursThursday]
        if isinstance(_thursday, Unset):
            thursday = UNSET
        else:
            thursday = GetWMSDistributionCenterCapacityResponse200DataOperationalHoursThursday.from_dict(_thursday)

        _friday = d.pop("friday", UNSET)
        friday: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursFriday]
        if isinstance(_friday, Unset):
            friday = UNSET
        else:
            friday = GetWMSDistributionCenterCapacityResponse200DataOperationalHoursFriday.from_dict(_friday)

        _saturday = d.pop("saturday", UNSET)
        saturday: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSaturday]
        if isinstance(_saturday, Unset):
            saturday = UNSET
        else:
            saturday = GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSaturday.from_dict(_saturday)

        _sunday = d.pop("sunday", UNSET)
        sunday: Union[Unset, GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSunday]
        if isinstance(_sunday, Unset):
            sunday = UNSET
        else:
            sunday = GetWMSDistributionCenterCapacityResponse200DataOperationalHoursSunday.from_dict(_sunday)

        get_wms_distribution_center_capacity_response_200_data_operational_hours = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )

        get_wms_distribution_center_capacity_response_200_data_operational_hours.additional_properties = d
        return get_wms_distribution_center_capacity_response_200_data_operational_hours

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
