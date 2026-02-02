import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_zone_zone_type import WMSZoneZoneType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_zone_aisles_item import WMSZoneAislesItem
    from ..models.wms_zone_custom_fields_type_0 import WMSZoneCustomFieldsType0
    from ..models.wms_zone_temperature_range_type_0 import WMSZoneTemperatureRangeType0
    from ..models.wms_zone_world_ref import WMSZoneWorldRef


T = TypeVar("T", bound="WMSZone")


@_attrs_define
class WMSZone:
    """Warehouse zone configuration and management data

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        world_ref (WMSZoneWorldRef): Reference to the world environment
        zone_id (str): Unique auto-generated zone identifier Example: ZNE_507f1f77bcf86cd799439012.
        warehouse_id (str): Associated warehouse identifier Example: WH_ATL_001.
        zone_code (str): Auto-generated zone code from zone name (slugified) Example: picking-zone-a.
        zone_name (str): Human readable zone name Example: Picking Zone A.
        temperature_controlled (bool): Temperature control requirement flag Default: False.
        created_at (datetime.datetime): Timestamp when the zone record was created Example: 2024-11-27T09:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the zone record was last updated Example:
            2024-11-27T09:35:00.000Z.
        zone_type (Union[Unset, WMSZoneZoneType]): Zone operational type classification Example: PICKING.
        temperature_range (Union['WMSZoneTemperatureRangeType0', None, Unset]): Temperature configuration for controlled
            zones
        capacity_cubic_feet (Union[None, Unset, float]): Zone storage capacity in cubic feet Example: 50000.
        aisles (Union[Unset, list['WMSZoneAislesItem']]): Aisle configuration within the zone
        custom_fields (Union['WMSZoneCustomFieldsType0', None, Unset]): Additional custom data fields Example:
            {'shiftCode': 'DAY-1', 'supervisor': 'SUP-001', 'specialHandling': ['FRAGILE']}.
    """

    field_id: str
    world_ref: "WMSZoneWorldRef"
    zone_id: str
    warehouse_id: str
    zone_code: str
    zone_name: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    temperature_controlled: bool = False
    zone_type: Union[Unset, WMSZoneZoneType] = UNSET
    temperature_range: Union["WMSZoneTemperatureRangeType0", None, Unset] = UNSET
    capacity_cubic_feet: Union[None, Unset, float] = UNSET
    aisles: Union[Unset, list["WMSZoneAislesItem"]] = UNSET
    custom_fields: Union["WMSZoneCustomFieldsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wms_zone_custom_fields_type_0 import WMSZoneCustomFieldsType0
        from ..models.wms_zone_temperature_range_type_0 import WMSZoneTemperatureRangeType0

        field_id = self.field_id

        world_ref = self.world_ref.to_dict()

        zone_id = self.zone_id

        warehouse_id = self.warehouse_id

        zone_code = self.zone_code

        zone_name = self.zone_name

        temperature_controlled = self.temperature_controlled

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        zone_type: Union[Unset, str] = UNSET
        if not isinstance(self.zone_type, Unset):
            zone_type = self.zone_type.value

        temperature_range: Union[None, Unset, dict[str, Any]]
        if isinstance(self.temperature_range, Unset):
            temperature_range = UNSET
        elif isinstance(self.temperature_range, WMSZoneTemperatureRangeType0):
            temperature_range = self.temperature_range.to_dict()
        else:
            temperature_range = self.temperature_range

        capacity_cubic_feet: Union[None, Unset, float]
        if isinstance(self.capacity_cubic_feet, Unset):
            capacity_cubic_feet = UNSET
        else:
            capacity_cubic_feet = self.capacity_cubic_feet

        aisles: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.aisles, Unset):
            aisles = []
            for aisles_item_data in self.aisles:
                aisles_item = aisles_item_data.to_dict()
                aisles.append(aisles_item)

        custom_fields: Union[None, Unset, dict[str, Any]]
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, WMSZoneCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "worldRef": world_ref,
                "zoneId": zone_id,
                "warehouseId": warehouse_id,
                "zoneCode": zone_code,
                "zoneName": zone_name,
                "temperatureControlled": temperature_controlled,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if zone_type is not UNSET:
            field_dict["zoneType"] = zone_type
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
        from ..models.wms_zone_aisles_item import WMSZoneAislesItem
        from ..models.wms_zone_custom_fields_type_0 import WMSZoneCustomFieldsType0
        from ..models.wms_zone_temperature_range_type_0 import WMSZoneTemperatureRangeType0
        from ..models.wms_zone_world_ref import WMSZoneWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        world_ref = WMSZoneWorldRef.from_dict(d.pop("worldRef"))

        zone_id = d.pop("zoneId")

        warehouse_id = d.pop("warehouseId")

        zone_code = d.pop("zoneCode")

        zone_name = d.pop("zoneName")

        temperature_controlled = d.pop("temperatureControlled")

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _zone_type = d.pop("zoneType", UNSET)
        zone_type: Union[Unset, WMSZoneZoneType]
        if isinstance(_zone_type, Unset):
            zone_type = UNSET
        else:
            zone_type = WMSZoneZoneType(_zone_type)

        def _parse_temperature_range(data: object) -> Union["WMSZoneTemperatureRangeType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                temperature_range_type_0 = WMSZoneTemperatureRangeType0.from_dict(data)

                return temperature_range_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSZoneTemperatureRangeType0", None, Unset], data)

        temperature_range = _parse_temperature_range(d.pop("temperatureRange", UNSET))

        def _parse_capacity_cubic_feet(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        capacity_cubic_feet = _parse_capacity_cubic_feet(d.pop("capacityCubicFeet", UNSET))

        aisles = []
        _aisles = d.pop("aisles", UNSET)
        for aisles_item_data in _aisles or []:
            aisles_item = WMSZoneAislesItem.from_dict(aisles_item_data)

            aisles.append(aisles_item)

        def _parse_custom_fields(data: object) -> Union["WMSZoneCustomFieldsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = WMSZoneCustomFieldsType0.from_dict(data)

                return custom_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSZoneCustomFieldsType0", None, Unset], data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))

        wms_zone = cls(
            field_id=field_id,
            world_ref=world_ref,
            zone_id=zone_id,
            warehouse_id=warehouse_id,
            zone_code=zone_code,
            zone_name=zone_name,
            temperature_controlled=temperature_controlled,
            created_at=created_at,
            updated_at=updated_at,
            zone_type=zone_type,
            temperature_range=temperature_range,
            capacity_cubic_feet=capacity_cubic_feet,
            aisles=aisles,
            custom_fields=custom_fields,
        )

        wms_zone.additional_properties = d
        return wms_zone

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
