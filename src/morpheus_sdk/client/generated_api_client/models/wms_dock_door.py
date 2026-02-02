import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_dock_door_door_type import WMSDockDoorDoorType
from ..models.wms_dock_door_status import WMSDockDoorStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_dock_door_capabilities import WMSDockDoorCapabilities
    from ..models.wms_dock_door_current_appointment_type_0 import WMSDockDoorCurrentAppointmentType0
    from ..models.wms_dock_door_current_trailer_type_0 import WMSDockDoorCurrentTrailerType0
    from ..models.wms_dock_door_custom_fields import WMSDockDoorCustomFields
    from ..models.wms_dock_door_equipment import WMSDockDoorEquipment
    from ..models.wms_dock_door_maintenance import WMSDockDoorMaintenance
    from ..models.wms_dock_door_operating_hours import WMSDockDoorOperatingHours
    from ..models.wms_dock_door_safety import WMSDockDoorSafety
    from ..models.wms_dock_door_world_ref import WMSDockDoorWorldRef


T = TypeVar("T", bound="WMSDockDoor")


@_attrs_define
class WMSDockDoor:
    """Warehouse dock door for trailer loading/unloading operations and appointment scheduling

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        dock_door_id (str): Unique identifier for the dock door, auto-generated using WMS service prefix Example:
            wms_dock-door_674565c1234567890abcdef.
        warehouse_id (str): Warehouse identifier where dock door is located Example:
            wms_warehouse_674565c1234567890abcdef.
        door_number (str): Physical door number or identifier for operational reference Example: DOCK-01.
        door_type (WMSDockDoorDoorType): Operational type of dock door determining traffic flow and usage Example:
            INBOUND.
        status (WMSDockDoorStatus): Current operational status affecting appointment scheduling availability Example:
            AVAILABLE.
        world_ref (WMSDockDoorWorldRef): Reference to the world environment containing this dock door
        created_at (datetime.datetime): Timestamp when the dock door record was created Example:
            2024-11-27T10:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the dock door record was last updated Example:
            2024-11-27T15:30:00.000Z.
        zone_id (Union[None, Unset, str]): Zone identifier for dock door location within warehouse facility Example:
            wms_zone_674565c1234567890abcdef.
        capabilities (Union[Unset, WMSDockDoorCapabilities]): Physical capabilities and specifications for trailer
            compatibility
        equipment (Union[Unset, WMSDockDoorEquipment]): Available equipment and systems supporting dock operations
        current_appointment (Union['WMSDockDoorCurrentAppointmentType0', None, Unset]): Current active appointment
            assigned to dock door
        current_trailer (Union['WMSDockDoorCurrentTrailerType0', None, Unset]): Current trailer positioned at dock door
            for operations
        operating_hours (Union[Unset, WMSDockDoorOperatingHours]): Daily operating hours schedule for appointment
            planning
        safety (Union[Unset, WMSDockDoorSafety]): Safety equipment and inspection schedules for compliance management
        maintenance (Union[Unset, WMSDockDoorMaintenance]): Maintenance schedules and documentation for operational
            continuity
        custom_fields (Union[Unset, WMSDockDoorCustomFields]): Additional facility-specific configuration and
            operational data Example: {'doorCode': 'DOCK-INBOUND-01', 'operatorCertificationRequired': True, 'maxWeight':
            80000, 'priorityLevel': 'HIGH', 'associatedWarehouseZones': ['RECEIVING', 'STAGING']}.
    """

    field_id: str
    dock_door_id: str
    warehouse_id: str
    door_number: str
    door_type: WMSDockDoorDoorType
    status: WMSDockDoorStatus
    world_ref: "WMSDockDoorWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    zone_id: Union[None, Unset, str] = UNSET
    capabilities: Union[Unset, "WMSDockDoorCapabilities"] = UNSET
    equipment: Union[Unset, "WMSDockDoorEquipment"] = UNSET
    current_appointment: Union["WMSDockDoorCurrentAppointmentType0", None, Unset] = UNSET
    current_trailer: Union["WMSDockDoorCurrentTrailerType0", None, Unset] = UNSET
    operating_hours: Union[Unset, "WMSDockDoorOperatingHours"] = UNSET
    safety: Union[Unset, "WMSDockDoorSafety"] = UNSET
    maintenance: Union[Unset, "WMSDockDoorMaintenance"] = UNSET
    custom_fields: Union[Unset, "WMSDockDoorCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wms_dock_door_current_appointment_type_0 import WMSDockDoorCurrentAppointmentType0
        from ..models.wms_dock_door_current_trailer_type_0 import WMSDockDoorCurrentTrailerType0

        field_id = self.field_id

        dock_door_id = self.dock_door_id

        warehouse_id = self.warehouse_id

        door_number = self.door_number

        door_type = self.door_type.value

        status = self.status.value

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        zone_id: Union[None, Unset, str]
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        else:
            zone_id = self.zone_id

        capabilities: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = self.capabilities.to_dict()

        equipment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.equipment, Unset):
            equipment = self.equipment.to_dict()

        current_appointment: Union[None, Unset, dict[str, Any]]
        if isinstance(self.current_appointment, Unset):
            current_appointment = UNSET
        elif isinstance(self.current_appointment, WMSDockDoorCurrentAppointmentType0):
            current_appointment = self.current_appointment.to_dict()
        else:
            current_appointment = self.current_appointment

        current_trailer: Union[None, Unset, dict[str, Any]]
        if isinstance(self.current_trailer, Unset):
            current_trailer = UNSET
        elif isinstance(self.current_trailer, WMSDockDoorCurrentTrailerType0):
            current_trailer = self.current_trailer.to_dict()
        else:
            current_trailer = self.current_trailer

        operating_hours: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.operating_hours, Unset):
            operating_hours = self.operating_hours.to_dict()

        safety: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.safety, Unset):
            safety = self.safety.to_dict()

        maintenance: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.maintenance, Unset):
            maintenance = self.maintenance.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "dockDoorId": dock_door_id,
                "warehouseId": warehouse_id,
                "doorNumber": door_number,
                "doorType": door_type,
                "status": status,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if equipment is not UNSET:
            field_dict["equipment"] = equipment
        if current_appointment is not UNSET:
            field_dict["currentAppointment"] = current_appointment
        if current_trailer is not UNSET:
            field_dict["currentTrailer"] = current_trailer
        if operating_hours is not UNSET:
            field_dict["operatingHours"] = operating_hours
        if safety is not UNSET:
            field_dict["safety"] = safety
        if maintenance is not UNSET:
            field_dict["maintenance"] = maintenance
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_dock_door_capabilities import WMSDockDoorCapabilities
        from ..models.wms_dock_door_current_appointment_type_0 import WMSDockDoorCurrentAppointmentType0
        from ..models.wms_dock_door_current_trailer_type_0 import WMSDockDoorCurrentTrailerType0
        from ..models.wms_dock_door_custom_fields import WMSDockDoorCustomFields
        from ..models.wms_dock_door_equipment import WMSDockDoorEquipment
        from ..models.wms_dock_door_maintenance import WMSDockDoorMaintenance
        from ..models.wms_dock_door_operating_hours import WMSDockDoorOperatingHours
        from ..models.wms_dock_door_safety import WMSDockDoorSafety
        from ..models.wms_dock_door_world_ref import WMSDockDoorWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        dock_door_id = d.pop("dockDoorId")

        warehouse_id = d.pop("warehouseId")

        door_number = d.pop("doorNumber")

        door_type = WMSDockDoorDoorType(d.pop("doorType"))

        status = WMSDockDoorStatus(d.pop("status"))

        world_ref = WMSDockDoorWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        def _parse_zone_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zone_id = _parse_zone_id(d.pop("zoneId", UNSET))

        _capabilities = d.pop("capabilities", UNSET)
        capabilities: Union[Unset, WMSDockDoorCapabilities]
        if isinstance(_capabilities, Unset):
            capabilities = UNSET
        else:
            capabilities = WMSDockDoorCapabilities.from_dict(_capabilities)

        _equipment = d.pop("equipment", UNSET)
        equipment: Union[Unset, WMSDockDoorEquipment]
        if isinstance(_equipment, Unset):
            equipment = UNSET
        else:
            equipment = WMSDockDoorEquipment.from_dict(_equipment)

        def _parse_current_appointment(data: object) -> Union["WMSDockDoorCurrentAppointmentType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_appointment_type_0 = WMSDockDoorCurrentAppointmentType0.from_dict(data)

                return current_appointment_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSDockDoorCurrentAppointmentType0", None, Unset], data)

        current_appointment = _parse_current_appointment(d.pop("currentAppointment", UNSET))

        def _parse_current_trailer(data: object) -> Union["WMSDockDoorCurrentTrailerType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                current_trailer_type_0 = WMSDockDoorCurrentTrailerType0.from_dict(data)

                return current_trailer_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSDockDoorCurrentTrailerType0", None, Unset], data)

        current_trailer = _parse_current_trailer(d.pop("currentTrailer", UNSET))

        _operating_hours = d.pop("operatingHours", UNSET)
        operating_hours: Union[Unset, WMSDockDoorOperatingHours]
        if isinstance(_operating_hours, Unset):
            operating_hours = UNSET
        else:
            operating_hours = WMSDockDoorOperatingHours.from_dict(_operating_hours)

        _safety = d.pop("safety", UNSET)
        safety: Union[Unset, WMSDockDoorSafety]
        if isinstance(_safety, Unset):
            safety = UNSET
        else:
            safety = WMSDockDoorSafety.from_dict(_safety)

        _maintenance = d.pop("maintenance", UNSET)
        maintenance: Union[Unset, WMSDockDoorMaintenance]
        if isinstance(_maintenance, Unset):
            maintenance = UNSET
        else:
            maintenance = WMSDockDoorMaintenance.from_dict(_maintenance)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSDockDoorCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSDockDoorCustomFields.from_dict(_custom_fields)

        wms_dock_door = cls(
            field_id=field_id,
            dock_door_id=dock_door_id,
            warehouse_id=warehouse_id,
            door_number=door_number,
            door_type=door_type,
            status=status,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            zone_id=zone_id,
            capabilities=capabilities,
            equipment=equipment,
            current_appointment=current_appointment,
            current_trailer=current_trailer,
            operating_hours=operating_hours,
            safety=safety,
            maintenance=maintenance,
            custom_fields=custom_fields,
        )

        wms_dock_door.additional_properties = d
        return wms_dock_door

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
