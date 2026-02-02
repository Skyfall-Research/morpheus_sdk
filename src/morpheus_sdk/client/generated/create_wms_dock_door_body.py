from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_dock_door_body_door_type import CreateWMSDockDoorBodyDoorType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_dock_door_body_capabilities import CreateWMSDockDoorBodyCapabilities
    from ..models.create_wms_dock_door_body_equipment import CreateWMSDockDoorBodyEquipment
    from ..models.create_wms_dock_door_body_operating_hours import CreateWMSDockDoorBodyOperatingHours


T = TypeVar("T", bound="CreateWMSDockDoorBody")


@_attrs_define
class CreateWMSDockDoorBody:
    """
    Example:
        {'warehouseId': 'wms_warehouse_674565c1234567890abcdef', 'doorNumber': 'DOCK-01', 'doorType': 'INBOUND',
            'zoneId': 'wms_zone_674565c1234567890abcdef', 'capabilities': {'maxTrailerLength': 53, 'maxTrailerHeight': 13.5,
            'levelingDock': True, 'hydraulicLeveler': True, 'restraintSystem': True, 'weatherSeal': True}, 'equipment':
            {'forkliftAccess': True, 'conveyorSystem': False, 'scales': True, 'lightSystem': True}, 'operatingHours':
            {'monday': {'open': '06:00', 'close': '22:00'}, 'tuesday': {'open': '06:00', 'close': '22:00'}, 'wednesday':
            {'open': '06:00', 'close': '22:00'}, 'thursday': {'open': '06:00', 'close': '22:00'}, 'friday': {'open':
            '06:00', 'close': '22:00'}, 'saturday': {'open': '08:00', 'close': '18:00'}, 'sunday': {'open': '10:00',
            'close': '16:00'}}}

    Attributes:
        warehouse_id (str): Warehouse identifier where dock door is located Example:
            wms_warehouse_674565c1234567890abcdef.
        door_number (str): Physical door number or identifier Example: DOCK-01.
        door_type (CreateWMSDockDoorBodyDoorType): Operational type of dock door Example: INBOUND.
        zone_id (Union[Unset, str]): Zone identifier for dock door location Example: wms_zone_674565c1234567890abcdef.
        capabilities (Union[Unset, CreateWMSDockDoorBodyCapabilities]): Physical capabilities and specifications
        equipment (Union[Unset, CreateWMSDockDoorBodyEquipment]): Available equipment and systems
        operating_hours (Union[Unset, CreateWMSDockDoorBodyOperatingHours]): Daily operating hours schedule
    """

    warehouse_id: str
    door_number: str
    door_type: CreateWMSDockDoorBodyDoorType
    zone_id: Union[Unset, str] = UNSET
    capabilities: Union[Unset, "CreateWMSDockDoorBodyCapabilities"] = UNSET
    equipment: Union[Unset, "CreateWMSDockDoorBodyEquipment"] = UNSET
    operating_hours: Union[Unset, "CreateWMSDockDoorBodyOperatingHours"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        door_number = self.door_number

        door_type = self.door_type.value

        zone_id = self.zone_id

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        equipment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.equipment, Unset):
            equipment = self.equipment.to_dict()

        operating_hours: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.operating_hours, Unset):
            operating_hours = self.operating_hours.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "doorNumber": door_number,
                "doorType": door_type,
            }
        )
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if operating_hours is not UNSET:
            field_dict["operatingHours"] = operating_hours

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_dock_door_body_capabilities import CreateWMSDockDoorBodyCapabilities
        from ..models.create_wms_dock_door_body_equipment import CreateWMSDockDoorBodyEquipment
        from ..models.create_wms_dock_door_body_operating_hours import CreateWMSDockDoorBodyOperatingHours

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        door_number = d.pop("doorNumber")

        door_type = CreateWMSDockDoorBodyDoorType(d.pop("doorType"))

        zone_id = d.pop("zoneId", UNSET)

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, CreateWMSDockDoorBodyCapabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = CreateWMSDockDoorBodyCapabilities.from_dict(_capabilities)

        _equipment = d.pop("equipment", UNSET)
        equipment: Union[Unset, CreateWMSDockDoorBodyEquipment]
        if isinstance(_equipment, Unset):
            equipment = UNSET
        else:
            equipment = CreateWMSDockDoorBodyEquipment.from_dict(_equipment)

        _operating_hours = d.pop("operatingHours", UNSET)
        operating_hours: Union[Unset, CreateWMSDockDoorBodyOperatingHours]
        if isinstance(_operating_hours, Unset):
            operating_hours = UNSET
        else:
            operating_hours = CreateWMSDockDoorBodyOperatingHours.from_dict(_operating_hours)

        create_wms_dock_door_body = cls(
            warehouse_id=warehouse_id,
            door_number=door_number,
            door_type=door_type,
            zone_id=zone_id,
            capabilities=capabilities,
            equipment=equipment,
            operating_hours=operating_hours,
        )

        create_wms_dock_door_body.additional_properties = d
        return create_wms_dock_door_body

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
