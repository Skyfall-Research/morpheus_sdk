from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_dock_door_operating_hours_friday import WMSDockDoorOperatingHoursFriday
    from ..models.wms_dock_door_operating_hours_monday import WMSDockDoorOperatingHoursMonday
    from ..models.wms_dock_door_operating_hours_saturday import WMSDockDoorOperatingHoursSaturday
    from ..models.wms_dock_door_operating_hours_sunday import WMSDockDoorOperatingHoursSunday
    from ..models.wms_dock_door_operating_hours_thursday import WMSDockDoorOperatingHoursThursday
    from ..models.wms_dock_door_operating_hours_tuesday import WMSDockDoorOperatingHoursTuesday
    from ..models.wms_dock_door_operating_hours_wednesday import WMSDockDoorOperatingHoursWednesday


T = TypeVar("T", bound="WMSDockDoorOperatingHours")


@_attrs_define
class WMSDockDoorOperatingHours:
    """Daily operating hours schedule for appointment planning

    Attributes:
        monday (Union[Unset, WMSDockDoorOperatingHoursMonday]):
        tuesday (Union[Unset, WMSDockDoorOperatingHoursTuesday]):
        wednesday (Union[Unset, WMSDockDoorOperatingHoursWednesday]):
        thursday (Union[Unset, WMSDockDoorOperatingHoursThursday]):
        friday (Union[Unset, WMSDockDoorOperatingHoursFriday]):
        saturday (Union[Unset, WMSDockDoorOperatingHoursSaturday]):
        sunday (Union[Unset, WMSDockDoorOperatingHoursSunday]):
    """

    monday: Union[Unset, "WMSDockDoorOperatingHoursMonday"] = UNSET
    tuesday: Union[Unset, "WMSDockDoorOperatingHoursTuesday"] = UNSET
    wednesday: Union[Unset, "WMSDockDoorOperatingHoursWednesday"] = UNSET
    thursday: Union[Unset, "WMSDockDoorOperatingHoursThursday"] = UNSET
    friday: Union[Unset, "WMSDockDoorOperatingHoursFriday"] = UNSET
    saturday: Union[Unset, "WMSDockDoorOperatingHoursSaturday"] = UNSET
    sunday: Union[Unset, "WMSDockDoorOperatingHoursSunday"] = UNSET
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
        from ..models.wms_dock_door_operating_hours_friday import WMSDockDoorOperatingHoursFriday
        from ..models.wms_dock_door_operating_hours_monday import WMSDockDoorOperatingHoursMonday
        from ..models.wms_dock_door_operating_hours_saturday import WMSDockDoorOperatingHoursSaturday
        from ..models.wms_dock_door_operating_hours_sunday import WMSDockDoorOperatingHoursSunday
        from ..models.wms_dock_door_operating_hours_thursday import WMSDockDoorOperatingHoursThursday
        from ..models.wms_dock_door_operating_hours_tuesday import WMSDockDoorOperatingHoursTuesday
        from ..models.wms_dock_door_operating_hours_wednesday import WMSDockDoorOperatingHoursWednesday

        d = dict(src_dict)
        _monday = d.pop("monday", UNSET)
        monday: Union[Unset, WMSDockDoorOperatingHoursMonday]
        if isinstance(_monday, Unset):
            monday = UNSET
        else:
            monday = WMSDockDoorOperatingHoursMonday.from_dict(_monday)

        _tuesday = d.pop("tuesday", UNSET)
        tuesday: Union[Unset, WMSDockDoorOperatingHoursTuesday]
        if isinstance(_tuesday, Unset):
            tuesday = UNSET
        else:
            tuesday = WMSDockDoorOperatingHoursTuesday.from_dict(_tuesday)

        _wednesday = d.pop("wednesday", UNSET)
        wednesday: Union[Unset, WMSDockDoorOperatingHoursWednesday]
        if isinstance(_wednesday, Unset):
            wednesday = UNSET
        else:
            wednesday = WMSDockDoorOperatingHoursWednesday.from_dict(_wednesday)

        _thursday = d.pop("thursday", UNSET)
        thursday: Union[Unset, WMSDockDoorOperatingHoursThursday]
        if isinstance(_thursday, Unset):
            thursday = UNSET
        else:
            thursday = WMSDockDoorOperatingHoursThursday.from_dict(_thursday)

        _friday = d.pop("friday", UNSET)
        friday: Union[Unset, WMSDockDoorOperatingHoursFriday]
        if isinstance(_friday, Unset):
            friday = UNSET
        else:
            friday = WMSDockDoorOperatingHoursFriday.from_dict(_friday)

        _saturday = d.pop("saturday", UNSET)
        saturday: Union[Unset, WMSDockDoorOperatingHoursSaturday]
        if isinstance(_saturday, Unset):
            saturday = UNSET
        else:
            saturday = WMSDockDoorOperatingHoursSaturday.from_dict(_saturday)

        _sunday = d.pop("sunday", UNSET)
        sunday: Union[Unset, WMSDockDoorOperatingHoursSunday]
        if isinstance(_sunday, Unset):
            sunday = UNSET
        else:
            sunday = WMSDockDoorOperatingHoursSunday.from_dict(_sunday)

        wms_dock_door_operating_hours = cls(
            monday=monday,
            tuesday=tuesday,
            wednesday=wednesday,
            thursday=thursday,
            friday=friday,
            saturday=saturday,
            sunday=sunday,
        )

        wms_dock_door_operating_hours.additional_properties = d
        return wms_dock_door_operating_hours

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
