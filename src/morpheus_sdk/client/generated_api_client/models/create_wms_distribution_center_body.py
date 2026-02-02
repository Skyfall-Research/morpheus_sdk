from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_distribution_center_body_dc_type import CreateWMSDistributionCenterBodyDcType
from ..models.create_wms_distribution_center_body_operational_status import (
    CreateWMSDistributionCenterBodyOperationalStatus,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_distribution_center_body_address import CreateWMSDistributionCenterBodyAddress
    from ..models.create_wms_distribution_center_body_contact_info import CreateWMSDistributionCenterBodyContactInfo
    from ..models.create_wms_distribution_center_body_custom_fields import CreateWMSDistributionCenterBodyCustomFields
    from ..models.create_wms_distribution_center_body_operating_hours import (
        CreateWMSDistributionCenterBodyOperatingHours,
    )


T = TypeVar("T", bound="CreateWMSDistributionCenterBody")


@_attrs_define
class CreateWMSDistributionCenterBody:
    """
    Attributes:
        warehouse_id (str): Parent warehouse identifier Example: WH_ATL_001.
        dc_name (str): Distribution center name Example: Atlanta Fulfillment Center East.
        dc_type (Union[Unset, CreateWMSDistributionCenterBodyDcType]): Type of distribution center operation Example:
            FULFILLMENT.
        address (Union[Unset, CreateWMSDistributionCenterBodyAddress]): Physical address of the distribution center
        timezone (Union[Unset, str]): Timezone for facility operations Example: America/New_York.
        total_sq_footage (Union[Unset, float]): Total square footage of the facility Example: 250000.
        operational_status (Union[Unset, CreateWMSDistributionCenterBodyOperationalStatus]): Initial operational status
            Example: ACTIVE.
        operating_hours (Union[Unset, CreateWMSDistributionCenterBodyOperatingHours]): Weekly operating schedule
        contact_info (Union[Unset, CreateWMSDistributionCenterBodyContactInfo]): Contact information for the facility
        custom_fields (Union[Unset, CreateWMSDistributionCenterBodyCustomFields]): Additional facility-specific
            configuration Example: {'hazmatCertified': True, 'securityLevel': 'HIGH', 'temperatureControlZones': 4,
            'dockDoors': 24, 'certification': ['ISO9001', 'SOC2']}.
    """

    warehouse_id: str
    dc_name: str
    dc_type: Union[Unset, CreateWMSDistributionCenterBodyDcType] = UNSET
    address: Union[Unset, "CreateWMSDistributionCenterBodyAddress"] = UNSET
    timezone: Union[Unset, str] = UNSET
    total_sq_footage: Union[Unset, float] = UNSET
    operational_status: Union[Unset, CreateWMSDistributionCenterBodyOperationalStatus] = UNSET
    operating_hours: Union[Unset, "CreateWMSDistributionCenterBodyOperatingHours"] = UNSET
    contact_info: Union[Unset, "CreateWMSDistributionCenterBodyContactInfo"] = UNSET
    custom_fields: Union[Unset, "CreateWMSDistributionCenterBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        dc_name = self.dc_name

        dc_type: Union[Unset, str] = UNSET
        if not isinstance(self.dc_type, Unset):
            dc_type = self.dc_type.value

        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        timezone = self.timezone

        total_sq_footage = self.total_sq_footage

        operational_status: Union[Unset, str] = UNSET
        if not isinstance(self.operational_status, Unset):
            operational_status = self.operational_status.value

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
                "warehouseId": warehouse_id,
                "dcName": dc_name,
            }
        )
        if dc_type is not UNSET:
            field_dict["dcType"] = dc_type
        if address is not UNSET:
            field_dict["address"] = address
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if total_sq_footage is not UNSET:
            field_dict["totalSqFootage"] = total_sq_footage
        if operational_status is not UNSET:
            field_dict["operationalStatus"] = operational_status
        if operating_hours is not UNSET:
            field_dict["operatingHours"] = operating_hours
        if contact_info is not UNSET:
            field_dict["contactInfo"] = contact_info
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_distribution_center_body_address import CreateWMSDistributionCenterBodyAddress
        from ..models.create_wms_distribution_center_body_contact_info import CreateWMSDistributionCenterBodyContactInfo
        from ..models.create_wms_distribution_center_body_custom_fields import (
            CreateWMSDistributionCenterBodyCustomFields,
        )
        from ..models.create_wms_distribution_center_body_operating_hours import (
            CreateWMSDistributionCenterBodyOperatingHours,
        )

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        dc_name = d.pop("dcName")

        _dc_type = d.pop("dcType", UNSET)
        dc_type: Union[Unset, CreateWMSDistributionCenterBodyDcType]
        if isinstance(_dc_type, Unset):
            dc_type = UNSET
        else:
            dc_type = CreateWMSDistributionCenterBodyDcType(_dc_type)

        _address = d.pop("address", UNSET)
        address: Union[Unset, CreateWMSDistributionCenterBodyAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = CreateWMSDistributionCenterBodyAddress.from_dict(_address)

        timezone = d.pop("timezone", UNSET)

        total_sq_footage = d.pop("totalSqFootage", UNSET)

        _operational_status = d.pop("operationalStatus", UNSET)
        operational_status: Union[Unset, CreateWMSDistributionCenterBodyOperationalStatus]
        if isinstance(_operational_status, Unset):
            operational_status = UNSET
        else:
            operational_status = CreateWMSDistributionCenterBodyOperationalStatus(_operational_status)

        _operating_hours = d.pop("operatingHours", UNSET)
        operating_hours: Union[Unset, CreateWMSDistributionCenterBodyOperatingHours]
        if isinstance(_operating_hours, Unset):
            operating_hours = UNSET
        else:
            operating_hours = CreateWMSDistributionCenterBodyOperatingHours.from_dict(_operating_hours)

        _contact_info = d.pop("contactInfo", UNSET)
        contact_info: Union[Unset, CreateWMSDistributionCenterBodyContactInfo]
        if isinstance(_contact_info, Unset):
            contact_info = UNSET
        else:
            contact_info = CreateWMSDistributionCenterBodyContactInfo.from_dict(_contact_info)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateWMSDistributionCenterBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateWMSDistributionCenterBodyCustomFields.from_dict(_custom_fields)

        create_wms_distribution_center_body = cls(
            warehouse_id=warehouse_id,
            dc_name=dc_name,
            dc_type=dc_type,
            address=address,
            timezone=timezone,
            total_sq_footage=total_sq_footage,
            operational_status=operational_status,
            operating_hours=operating_hours,
            contact_info=contact_info,
            custom_fields=custom_fields,
        )

        create_wms_distribution_center_body.additional_properties = d
        return create_wms_distribution_center_body

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
