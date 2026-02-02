from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_zone_body_zone_type import CreateZoneBodyZoneType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_zone_body_aisles_item import CreateZoneBodyAislesItem
    from ..models.create_zone_body_custom_fields import CreateZoneBodyCustomFields
    from ..models.create_zone_body_temperature_range import CreateZoneBodyTemperatureRange


T = TypeVar("T", bound="CreateZoneBody")


@_attrs_define
class CreateZoneBody:
    """
    Attributes:
        warehouse_id (str): Warehouse identifier Example: WH_ATL_001.
        zone_name (str): Human readable zone name Example: Picking Zone A.
        zone_type (Union[Unset, CreateZoneBodyZoneType]): Zone type classification Example: PICKING.
        temperature_controlled (Union[Unset, bool]): Temperature control flag
        temperature_range (Union[Unset, CreateZoneBodyTemperatureRange]): Temperature configuration for controlled zones
        capacity_cubic_feet (Union[Unset, float]): Zone storage capacity Example: 50000.
        aisles (Union[Unset, list['CreateZoneBodyAislesItem']]): Initial aisle configuration
        custom_fields (Union[Unset, CreateZoneBodyCustomFields]): Additional custom data
    """

    warehouse_id: str
    zone_name: str
    zone_type: Union[Unset, CreateZoneBodyZoneType] = UNSET
    temperature_controlled: Union[Unset, bool] = UNSET
    temperature_range: Union[Unset, "CreateZoneBodyTemperatureRange"] = UNSET
    capacity_cubic_feet: Union[Unset, float] = UNSET
    aisles: Union[Unset, list["CreateZoneBodyAislesItem"]] = UNSET
    custom_fields: Union[Unset, "CreateZoneBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        zone_name = self.zone_name

        zone_type: Union[Unset, str] = UNSET
        if not isinstance(self.zone_type, Unset):
            zone_type = self.zone_type.value

        temperature_controlled = self.temperature_controlled

        temperature_range: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.temperature_range, Unset):
            temperature_range = self.temperature_range.to_dict()

        capacity_cubic_feet = self.capacity_cubic_feet

        aisles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.aisles, Unset):
            aisles = []
            for aisles_item_data in self.aisles:
                aisles_item = aisles_item_data.to_dict()
                aisles.append(aisles_item)

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "zoneName": zone_name,
            }
        )
        if zone_type is not UNSET:
            field_dict["zoneType"] = zone_type
        if temperature_controlled is not UNSET:
            field_dict["temperatureControlled"] = temperature_controlled
        if temperature_range is not UNSET:
            field_dict["temperatureRange"] = temperature_range
        if capacity_cubic_feet is not UNSET:
            field_dict["capacityCubicFeet"] = capacity_cubic_feet
        if aisles is not UNSET:
            field_dict["aisles"] = aisles
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_zone_body_aisles_item import CreateZoneBodyAislesItem
        from ..models.create_zone_body_custom_fields import CreateZoneBodyCustomFields
        from ..models.create_zone_body_temperature_range import CreateZoneBodyTemperatureRange

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        zone_name = d.pop("zoneName")

        _zone_type = d.pop("zoneType", UNSET)
        zone_type: Union[Unset, CreateZoneBodyZoneType]
        if isinstance(_zone_type, Unset):
            zone_type = UNSET
        else:
            zone_type = CreateZoneBodyZoneType(_zone_type)

        temperature_controlled = d.pop("temperatureControlled", UNSET)

        _temperature_range = d.pop("temperatureRange", UNSET)
        temperature_range: Union[Unset, CreateZoneBodyTemperatureRange]
        if isinstance(_temperature_range, Unset):
            temperature_range = UNSET
        else:
            temperature_range = CreateZoneBodyTemperatureRange.from_dict(_temperature_range)

        capacity_cubic_feet = d.pop("capacityCubicFeet", UNSET)

        aisles = []
        _aisles = d.pop("aisles", UNSET)
        for aisles_item_data in _aisles or []:
            aisles_item = CreateZoneBodyAislesItem.from_dict(aisles_item_data)

            aisles.append(aisles_item)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateZoneBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateZoneBodyCustomFields.from_dict(_custom_fields)

        create_zone_body = cls(
            warehouse_id=warehouse_id,
            zone_name=zone_name,
            zone_type=zone_type,
            temperature_controlled=temperature_controlled,
            temperature_range=temperature_range,
            capacity_cubic_feet=capacity_cubic_feet,
            aisles=aisles,
            custom_fields=custom_fields,
        )

        create_zone_body.additional_properties = d
        return create_zone_body

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
