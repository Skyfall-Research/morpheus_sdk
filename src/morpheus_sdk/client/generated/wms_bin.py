import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_bin_abc_classification import WMSBinAbcClassification
from ..models.wms_bin_bin_type import WMSBinBinType
from ..models.wms_bin_location_type import WMSBinLocationType
from ..models.wms_bin_status import WMSBinStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_bin_capacity import WMSBinCapacity
    from ..models.wms_bin_custom_fields import WMSBinCustomFields
    from ..models.wms_bin_location import WMSBinLocation
    from ..models.wms_bin_world_ref import WMSBinWorldRef


T = TypeVar("T", bound="WMSBin")


@_attrs_define
class WMSBin:
    """Complete WMS warehouse bin record for inventory storage and location management

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        bin_id (str): Unique bin identifier Example: BIN_ATL_A01_001.
        bin_code (str): Human-readable bin code for operational identification Example: A01-B05-L02-P03.
        warehouse_id (str): Parent warehouse identifier Example: WH_ATL_001.
        zone_id (str): Zone identifier within warehouse hierarchy Example: ZONE_PICK_A.
        status (WMSBinStatus): Current operational status of the bin Example: AVAILABLE.
        world_ref (WMSBinWorldRef): World reference information for multi-tenant context
        created_at (datetime.datetime): Timestamp when the bin record was created Example: 2024-01-15T09:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the bin record was last updated Example:
            2024-01-20T14:30:00.000Z.
        id (Union[Unset, str]): Formatted document identifier for API responses Example: 507f1f77bcf86cd799439011.
        aisle_id (Union[Unset, str]): Aisle identifier for location organization Example: AISLE_A01.
        location (Union[Unset, WMSBinLocation]): Precise physical location within warehouse
        bin_type (Union[Unset, WMSBinBinType]): Type of bin for operational classification and workflow Example:
            PICK_FACE.
        location_type (Union[Unset, WMSBinLocationType]): Functional location type for operational context Example:
            STORAGE.
        capacity (Union[Unset, WMSBinCapacity]): Storage capacity constraints and limits
        abc_classification (Union[Unset, WMSBinAbcClassification]): ABC velocity classification for inventory management
            optimization Example: A.
        pickable (Union[Unset, bool]): Whether bin is available for picking operations Example: True.
        last_inventory_check (Union[Unset, datetime.datetime]): Timestamp of last inventory verification Example:
            2024-01-20T10:30:00.000Z.
        custom_fields (Union[Unset, WMSBinCustomFields]): Additional warehouse-specific bin attributes and metadata
            Example: {'temperatureControlled': True, 'hazMatApproved': False, 'cleaningRequired': False, 'equipmentType':
            'FORKLIFT_ACCESSIBLE'}.
    """

    field_id: str
    bin_id: str
    bin_code: str
    warehouse_id: str
    zone_id: str
    status: WMSBinStatus
    world_ref: "WMSBinWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, str] = UNSET
    aisle_id: Union[Unset, str] = UNSET
    location: Union[Unset, "WMSBinLocation"] = UNSET
    bin_type: Union[Unset, WMSBinBinType] = UNSET
    location_type: Union[Unset, WMSBinLocationType] = UNSET
    capacity: Union[Unset, "WMSBinCapacity"] = UNSET
    abc_classification: Union[Unset, WMSBinAbcClassification] = UNSET
    pickable: Union[Unset, bool] = UNSET
    last_inventory_check: Union[Unset, datetime.datetime] = UNSET
    custom_fields: Union[Unset, "WMSBinCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        bin_id = self.bin_id

        bin_code = self.bin_code

        warehouse_id = self.warehouse_id

        zone_id = self.zone_id

        status = self.status.value

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id

        aisle_id = self.aisle_id

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        bin_type: Union[Unset, str] = UNSET
        if not isinstance(self.bin_type, Unset):
            bin_type = self.bin_type.value

        location_type: Union[Unset, str] = UNSET
        if not isinstance(self.location_type, Unset):
            location_type = self.location_type.value

        capacity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.capacity, Unset):
            capacity = self.capacity.to_dict()

        abc_classification: Union[Unset, str] = UNSET
        if not isinstance(self.abc_classification, Unset):
            abc_classification = self.abc_classification.value

        pickable = self.pickable

        last_inventory_check: Union[Unset, str] = UNSET
        if not isinstance(self.last_inventory_check, Unset):
            last_inventory_check = self.last_inventory_check.isoformat()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "binId": bin_id,
                "binCode": bin_code,
                "warehouseId": warehouse_id,
                "zoneId": zone_id,
                "status": status,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if aisle_id is not UNSET:
            field_dict["aisleId"] = aisle_id
        if location is not UNSET:
            field_dict["location"] = location
        if bin_type is not UNSET:
            field_dict["binType"] = bin_type
        if location_type is not UNSET:
            field_dict["locationType"] = location_type
        if capacity is not UNSET:
            field_dict["capacity"] = capacity
        if abc_classification is not UNSET:
            field_dict["abcClassification"] = abc_classification
        if pickable is not UNSET:
            field_dict["pickable"] = pickable
        if last_inventory_check is not UNSET:
            field_dict["lastInventoryCheck"] = last_inventory_check
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_bin_capacity import WMSBinCapacity
        from ..models.wms_bin_custom_fields import WMSBinCustomFields
        from ..models.wms_bin_location import WMSBinLocation
        from ..models.wms_bin_world_ref import WMSBinWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        bin_id = d.pop("binId")

        bin_code = d.pop("binCode")

        warehouse_id = d.pop("warehouseId")

        zone_id = d.pop("zoneId")

        status = WMSBinStatus(d.pop("status"))

        world_ref = WMSBinWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        id = d.pop("id", UNSET)

        aisle_id = d.pop("aisleId", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, WMSBinLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = WMSBinLocation.from_dict(_location)

        _bin_type = d.pop("binType", UNSET)
        bin_type: Union[Unset, WMSBinBinType]
        if isinstance(_bin_type, Unset):
            bin_type = UNSET
        else:
            bin_type = WMSBinBinType(_bin_type)

        _location_type = d.pop("locationType", UNSET)
        location_type: Union[Unset, WMSBinLocationType]
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = WMSBinLocationType(_location_type)

        _capacity = d.pop("capacity", UNSET)
        capacity: Union[Unset, WMSBinCapacity]
        if isinstance(_capacity, Unset):
            capacity = UNSET
        else:
            capacity = WMSBinCapacity.from_dict(_capacity)

        _abc_classification = d.pop("abcClassification", UNSET)
        abc_classification: Union[Unset, WMSBinAbcClassification]
        if isinstance(_abc_classification, Unset):
            abc_classification = UNSET
        else:
            abc_classification = WMSBinAbcClassification(_abc_classification)

        pickable = d.pop("pickable", UNSET)

        _last_inventory_check = d.pop("lastInventoryCheck", UNSET)
        last_inventory_check: Union[Unset, datetime.datetime]
        if isinstance(_last_inventory_check, Unset):
            last_inventory_check = UNSET
        else:
            last_inventory_check = isoparse(_last_inventory_check)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSBinCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSBinCustomFields.from_dict(_custom_fields)

        wms_bin = cls(
            field_id=field_id,
            bin_id=bin_id,
            bin_code=bin_code,
            warehouse_id=warehouse_id,
            zone_id=zone_id,
            status=status,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            aisle_id=aisle_id,
            location=location,
            bin_type=bin_type,
            location_type=location_type,
            capacity=capacity,
            abc_classification=abc_classification,
            pickable=pickable,
            last_inventory_check=last_inventory_check,
            custom_fields=custom_fields,
        )

        wms_bin.additional_properties = d
        return wms_bin

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
