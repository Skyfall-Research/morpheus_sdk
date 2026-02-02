from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_distribution_center_body_operating_hours_friday import (
        CreateWMSDistributionCenterBodyOperatingHoursFriday,
    )
    from ..models.create_wms_distribution_center_body_operating_hours_monday import (
        CreateWMSDistributionCenterBodyOperatingHoursMonday,
    )
    from ..models.create_wms_distribution_center_body_operating_hours_saturday import (
        CreateWMSDistributionCenterBodyOperatingHoursSaturday,
    )
    from ..models.create_wms_distribution_center_body_operating_hours_sunday import (
        CreateWMSDistributionCenterBodyOperatingHoursSunday,
    )
    from ..models.create_wms_distribution_center_body_operating_hours_thursday import (
        CreateWMSDistributionCenterBodyOperatingHoursThursday,
    )
    from ..models.create_wms_distribution_center_body_operating_hours_tuesday import (
        CreateWMSDistributionCenterBodyOperatingHoursTuesday,
    )
    from ..models.create_wms_distribution_center_body_operating_hours_wednesday import (
        CreateWMSDistributionCenterBodyOperatingHoursWednesday,
    )


T = TypeVar("T", bound="CreateWMSDistributionCenterBodyOperatingHours")


@_attrs_define
class CreateWMSDistributionCenterBodyOperatingHours:
    """Weekly operating schedule

    Attributes:
        monday (Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursMonday]):
        tuesday (Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursTuesday]):
        wednesday (Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursWednesday]):
        thursday (Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursThursday]):
        friday (Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursFriday]):
        saturday (Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursSaturday]):
        sunday (Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursSunday]):
    """

    monday: Union[Unset, "CreateWMSDistributionCenterBodyOperatingHoursMonday"] = UNSET
    tuesday: Union[Unset, "CreateWMSDistributionCenterBodyOperatingHoursTuesday"] = UNSET
    wednesday: Union[Unset, "CreateWMSDistributionCenterBodyOperatingHoursWednesday"] = UNSET
    thursday: Union[Unset, "CreateWMSDistributionCenterBodyOperatingHoursThursday"] = UNSET
    friday: Union[Unset, "CreateWMSDistributionCenterBodyOperatingHoursFriday"] = UNSET
    saturday: Union[Unset, "CreateWMSDistributionCenterBodyOperatingHoursSaturday"] = UNSET
    sunday: Union[Unset, "CreateWMSDistributionCenterBodyOperatingHoursSunday"] = UNSET
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
        from ..models.create_wms_distribution_center_body_operating_hours_friday import (
            CreateWMSDistributionCenterBodyOperatingHoursFriday,
        )
        from ..models.create_wms_distribution_center_body_operating_hours_monday import (
            CreateWMSDistributionCenterBodyOperatingHoursMonday,
        )
        from ..models.create_wms_distribution_center_body_operating_hours_saturday import (
            CreateWMSDistributionCenterBodyOperatingHoursSaturday,
        )
        from ..models.create_wms_distribution_center_body_operating_hours_sunday import (
            CreateWMSDistributionCenterBodyOperatingHoursSunday,
        )
        from ..models.create_wms_distribution_center_body_operating_hours_thursday import (
            CreateWMSDistributionCenterBodyOperatingHoursThursday,
        )
        from ..models.create_wms_distribution_center_body_operating_hours_tuesday import (
            CreateWMSDistributionCenterBodyOperatingHoursTuesday,
        )
        from ..models.create_wms_distribution_center_body_operating_hours_wednesday import (
            CreateWMSDistributionCenterBodyOperatingHoursWednesday,
        )

        d = dict(src_dict)
        _monday = d.pop("monday", UNSET)
        monday: Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursMonday]
        if isinstance(_monday, Unset):
            monday = UNSET
        else:
            monday = CreateWMSDistributionCenterBodyOperatingHoursMonday.from_dict(_monday)

        _tuesday = d.pop("tuesday", UNSET)
        tuesday: Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursTuesday]
        if isinstance(_tuesday, Unset):
            tuesday = UNSET
        else:
            tuesday = CreateWMSDistributionCenterBodyOperatingHoursTuesday.from_dict(_tuesday)

        _wednesday = d.pop("wednesday", UNSET)
        wednesday: Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursWednesday]
        if isinstance(_wednesday, Unset):
            wednesday = UNSET
        else:
            wednesday = CreateWMSDistributionCenterBodyOperatingHoursWednesday.from_dict(_wednesday)

        _thursday = d.pop("thursday", UNSET)
        thursday: Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursThursday]
        if isinstance(_thursday, Unset):
            thursday = UNSET
        else:
            thursday = CreateWMSDistributionCenterBodyOperatingHoursThursday.from_dict(_thursday)

        _friday = d.pop("friday", UNSET)
        friday: Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursFriday]
        if isinstance(_friday, Unset):
            friday = UNSET
        else:
            friday = CreateWMSDistributionCenterBodyOperatingHoursFriday.from_dict(_friday)

        _saturday = d.pop("saturday", UNSET)
        saturday: Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursSaturday]
        if isinstance(_saturday, Unset):
            saturday = UNSET
        else:
            saturday = CreateWMSDistributionCenterBodyOperatingHoursSaturday.from_dict(_saturday)

        _sunday = d.pop("sunday", UNSET)
        sunday: Union[Unset, CreateWMSDistributionCenterBodyOperatingHoursSunday]
        if isinstance(_sunday, Unset):
            sunday = UNSET
        else:
            sunday = CreateWMSDistributionCenterBodyOperatingHoursSunday.from_dict(_sunday)

        create_wms_distribution_center_body_operating_hours = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )

        create_wms_distribution_center_body_operating_hours.additional_properties = d
        return create_wms_distribution_center_body_operating_hours

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
