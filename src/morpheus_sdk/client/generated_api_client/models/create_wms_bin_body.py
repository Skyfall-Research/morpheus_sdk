from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_bin_body_abc_classification import CreateWMSBinBodyAbcClassification
from ..models.create_wms_bin_body_bin_type import CreateWMSBinBodyBinType
from ..models.create_wms_bin_body_location_type import CreateWMSBinBodyLocationType
from ..models.create_wms_bin_body_status import CreateWMSBinBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_bin_body_capacity import CreateWMSBinBodyCapacity
    from ..models.create_wms_bin_body_custom_fields import CreateWMSBinBodyCustomFields
    from ..models.create_wms_bin_body_location import CreateWMSBinBodyLocation


T = TypeVar("T", bound="CreateWMSBinBody")


@_attrs_define
class CreateWMSBinBody:
    """
    Attributes:
        bin_code (str): Human-readable bin code Example: A01-B05-L02-P03.
        warehouse_id (str): Parent warehouse identifier Example: WH_ATL_001.
        zone_id (str): Zone identifier within warehouse Example: ZONE_PICK_A.
        bin_id (Union[Unset, str]): Unique bin identifier (auto-generated if not provided) Example: BIN_ATL_A01_001.
        aisle_id (Union[Unset, str]): Aisle identifier (optional) Example: AISLE_A01.
        location (Union[Unset, CreateWMSBinBodyLocation]):
        bin_type (Union[Unset, CreateWMSBinBodyBinType]): Type of bin for operational classification Example: PICK_FACE.
        location_type (Union[Unset, CreateWMSBinBodyLocationType]): Functional location type Example: STORAGE.
        capacity (Union[Unset, CreateWMSBinBodyCapacity]):
        status (Union[Unset, CreateWMSBinBodyStatus]): Initial operational status Example: AVAILABLE.
        abc_classification (Union[Unset, CreateWMSBinBodyAbcClassification]): ABC velocity classification for inventory
            management Example: A.
        pickable (Union[Unset, bool]): Whether bin is available for picking operations Example: True.
        custom_fields (Union[Unset, CreateWMSBinBodyCustomFields]): Additional warehouse-specific bin attributes
            Example: {'temperatureControlled': True, 'hazMatApproved': False}.
    """

    bin_code: str
    warehouse_id: str
    zone_id: str
    bin_id: Union[Unset, str] = UNSET
    aisle_id: Union[Unset, str] = UNSET
    location: Union[Unset, "CreateWMSBinBodyLocation"] = UNSET
    bin_type: Union[Unset, CreateWMSBinBodyBinType] = UNSET
    location_type: Union[Unset, CreateWMSBinBodyLocationType] = UNSET
    capacity: Union[Unset, "CreateWMSBinBodyCapacity"] = UNSET
    status: Union[Unset, CreateWMSBinBodyStatus] = UNSET
    abc_classification: Union[Unset, CreateWMSBinBodyAbcClassification] = UNSET
    pickable: Union[Unset, bool] = UNSET
    custom_fields: Union[Unset, "CreateWMSBinBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bin_code = self.bin_code

        warehouse_id = self.warehouse_id

        zone_id = self.zone_id

        bin_id = self.bin_id

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

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        abc_classification: Union[Unset, str] = UNSET
        if not isinstance(self.abc_classification, Unset):
            abc_classification = self.abc_classification.value

        pickable = self.pickable

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "binCode": bin_code,
                "warehouseId": warehouse_id,
                "zoneId": zone_id,
            }
        )
        if bin_id is not UNSET:
            field_dict["binId"] = bin_id
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
        if status is not UNSET:
            field_dict["status"] = status
        if abc_classification is not UNSET:
            field_dict["abcClassification"] = abc_classification
        if pickable is not UNSET:
            field_dict["pickable"] = pickable
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_bin_body_capacity import CreateWMSBinBodyCapacity
        from ..models.create_wms_bin_body_custom_fields import CreateWMSBinBodyCustomFields
        from ..models.create_wms_bin_body_location import CreateWMSBinBodyLocation

        d = dict(src_dict)
        bin_code = d.pop("binCode")

        warehouse_id = d.pop("warehouseId")

        zone_id = d.pop("zoneId")

        bin_id = d.pop("binId", UNSET)

        aisle_id = d.pop("aisleId", UNSET)

        _location = d.pop("location", UNSET)
        location: Union[Unset, CreateWMSBinBodyLocation]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = CreateWMSBinBodyLocation.from_dict(_location)

        _bin_type = d.pop("binType", UNSET)
        bin_type: Union[Unset, CreateWMSBinBodyBinType]
        if isinstance(_bin_type, Unset):
            bin_type = UNSET
        else:
            bin_type = CreateWMSBinBodyBinType(_bin_type)

        _location_type = d.pop("locationType", UNSET)
        location_type: Union[Unset, CreateWMSBinBodyLocationType]
        if isinstance(_location_type, Unset):
            location_type = UNSET
        else:
            location_type = CreateWMSBinBodyLocationType(_location_type)

        _capacity = d.pop("capacity", UNSET)
        capacity: Union[Unset, CreateWMSBinBodyCapacity]
        if isinstance(_capacity, Unset):
            capacity = UNSET
        else:
            capacity = CreateWMSBinBodyCapacity.from_dict(_capacity)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CreateWMSBinBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CreateWMSBinBodyStatus(_status)

        _abc_classification = d.pop("abcClassification", UNSET)
        abc_classification: Union[Unset, CreateWMSBinBodyAbcClassification]
        if isinstance(_abc_classification, Unset):
            abc_classification = UNSET
        else:
            abc_classification = CreateWMSBinBodyAbcClassification(_abc_classification)

        pickable = d.pop("pickable", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateWMSBinBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateWMSBinBodyCustomFields.from_dict(_custom_fields)

        create_wms_bin_body = cls(
            bin_code=bin_code,
            warehouse_id=warehouse_id,
            zone_id=zone_id,
            bin_id=bin_id,
            aisle_id=aisle_id,
            location=location,
            bin_type=bin_type,
            location_type=location_type,
            capacity=capacity,
            status=status,
            abc_classification=abc_classification,
            pickable=pickable,
            custom_fields=custom_fields,
        )

        create_wms_bin_body.additional_properties = d
        return create_wms_bin_body

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
