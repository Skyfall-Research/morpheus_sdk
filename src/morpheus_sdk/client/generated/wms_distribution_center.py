import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_distribution_center_dc_type import WMSDistributionCenterDcType
from ..models.wms_distribution_center_operational_status import WMSDistributionCenterOperationalStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_distribution_center_address import WMSDistributionCenterAddress
    from ..models.wms_distribution_center_contact_info import WMSDistributionCenterContactInfo
    from ..models.wms_distribution_center_custom_fields import WMSDistributionCenterCustomFields
    from ..models.wms_distribution_center_operating_hours import WMSDistributionCenterOperatingHours
    from ..models.wms_distribution_center_world_ref import WMSDistributionCenterWorldRef


T = TypeVar("T", bound="WMSDistributionCenter")


@_attrs_define
class WMSDistributionCenter:
    """Complete WMS distribution center record for comprehensive facility management and operational coordination

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        dc_id (str): Unique distribution center identifier Example: wms_distribution-center_674565c1234567890abcdef.
        warehouse_id (str): Parent warehouse identifier Example: WH_ATL_001.
        dc_name (str): Distribution center name Example: Atlanta Fulfillment Center East.
        operational_status (WMSDistributionCenterOperationalStatus): Current operational status of the facility Example:
            ACTIVE.
        world_ref (WMSDistributionCenterWorldRef): World reference information for multi-tenant context
        created_at (datetime.datetime): Timestamp when the distribution center record was created Example:
            2024-11-27T10:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the distribution center record was last updated Example:
            2024-11-27T15:30:00.000Z.
        id (Union[Unset, str]): Formatted document identifier for API responses Example: 507f1f77bcf86cd799439011.
        dc_type (Union[Unset, WMSDistributionCenterDcType]): Type of distribution center operation Example: FULFILLMENT.
        address (Union[Unset, WMSDistributionCenterAddress]): Physical address of the distribution center
        timezone (Union[Unset, str]): Timezone for facility operations Example: America/New_York.
        total_sq_footage (Union[Unset, float]): Total square footage of the facility Example: 250000.
        operating_hours (Union[Unset, WMSDistributionCenterOperatingHours]): Weekly operating schedule for the facility
        contact_info (Union[Unset, WMSDistributionCenterContactInfo]): Contact information for the facility
        custom_fields (Union[Unset, WMSDistributionCenterCustomFields]): Additional facility-specific configuration and
            operational data Example: {'hazmatCertified': True, 'securityLevel': 'HIGH', 'temperatureControlZones': 4,
            'dockDoors': 24, 'certification': ['ISO9001', 'SOC2'], 'sustainabilityMetrics': {'energyEfficiencyRating': 'A+',
            'solarPowerCapacity': '500kW', 'wasteRecyclingRate': 95.5}}.
    """

    field_id: str
    dc_id: str
    warehouse_id: str
    dc_name: str
    operational_status: WMSDistributionCenterOperationalStatus
    world_ref: "WMSDistributionCenterWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, str] = UNSET
    dc_type: Union[Unset, WMSDistributionCenterDcType] = UNSET
    address: Union[Unset, "WMSDistributionCenterAddress"] = UNSET
    timezone: Union[Unset, str] = UNSET
    total_sq_footage: Union[Unset, float] = UNSET
    operating_hours: Union[Unset, "WMSDistributionCenterOperatingHours"] = UNSET
    contact_info: Union[Unset, "WMSDistributionCenterContactInfo"] = UNSET
    custom_fields: Union[Unset, "WMSDistributionCenterCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        dc_id = self.dc_id

        warehouse_id = self.warehouse_id

        dc_name = self.dc_name

        operational_status = self.operational_status.value

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id

        dc_type: Union[Unset, str] = UNSET
        if not isinstance(self.dc_type, Unset):
            dc_type = self.dc_type.value

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        timezone = self.timezone

        total_sq_footage = self.total_sq_footage

        operating_hours: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.operating_hours, Unset):
            operating_hours = self.operating_hours.to_dict()

        contact_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.contact_info, Unset):
            contact_info = self.contact_info.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "dcId": dc_id,
                "warehouseId": warehouse_id,
                "dcName": dc_name,
                "operationalStatus": operational_status,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if dc_type is not UNSET:
            field_dict["dcType"] = dc_type
        if address is not UNSET:
            field_dict["address"] = address
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if total_sq_footage is not UNSET:
            field_dict["totalSqFootage"] = total_sq_footage
        if operating_hours is not UNSET:
            field_dict["operatingHours"] = operating_hours
        if contact_info is not UNSET:
            field_dict["contactInfo"] = contact_info
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_distribution_center_address import WMSDistributionCenterAddress
        from ..models.wms_distribution_center_contact_info import WMSDistributionCenterContactInfo
        from ..models.wms_distribution_center_custom_fields import WMSDistributionCenterCustomFields
        from ..models.wms_distribution_center_operating_hours import WMSDistributionCenterOperatingHours
        from ..models.wms_distribution_center_world_ref import WMSDistributionCenterWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        dc_id = d.pop("dcId")

        warehouse_id = d.pop("warehouseId")

        dc_name = d.pop("dcName")

        operational_status = WMSDistributionCenterOperationalStatus(d.pop("operationalStatus"))

        world_ref = WMSDistributionCenterWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        id = d.pop("id", UNSET)

        _dc_type = d.pop("dcType", UNSET)
        dc_type: Union[Unset, WMSDistributionCenterDcType]
        if isinstance(_dc_type, Unset):
            dc_type = UNSET
        else:
            dc_type = WMSDistributionCenterDcType(_dc_type)

        _address = d.pop("address", UNSET)
        address: Union[Unset, WMSDistributionCenterAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = WMSDistributionCenterAddress.from_dict(_address)

        timezone = d.pop("timezone", UNSET)

        total_sq_footage = d.pop("totalSqFootage", UNSET)

        _operating_hours = d.pop("operatingHours", UNSET)
        operating_hours: Union[Unset, WMSDistributionCenterOperatingHours]
        if isinstance(_operating_hours, Unset):
            operating_hours = UNSET
        else:
            operating_hours = WMSDistributionCenterOperatingHours.from_dict(_operating_hours)

        _contact_info = d.pop("contactInfo", UNSET)
        contact_info: Union[Unset, WMSDistributionCenterContactInfo]
        if isinstance(_contact_info, Unset):
            contact_info = UNSET
        else:
            contact_info = WMSDistributionCenterContactInfo.from_dict(_contact_info)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSDistributionCenterCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSDistributionCenterCustomFields.from_dict(_custom_fields)

        wms_distribution_center = cls(
            field_id=field_id,
            dc_id=dc_id,
            warehouse_id=warehouse_id,
            dc_name=dc_name,
            operational_status=operational_status,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            dc_type=dc_type,
            address=address,
            timezone=timezone,
            total_sq_footage=total_sq_footage,
            operating_hours=operating_hours,
            contact_info=contact_info,
            custom_fields=custom_fields,
        )

        wms_distribution_center.additional_properties = d
        return wms_distribution_center

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
