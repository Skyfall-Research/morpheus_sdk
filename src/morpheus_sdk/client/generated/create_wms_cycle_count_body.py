from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_cycle_count_body_count_status import CreateWMSCycleCountBodyCountStatus
from ..models.create_wms_cycle_count_body_count_type import CreateWMSCycleCountBodyCountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_cycle_count_body_assignments_item import CreateWMSCycleCountBodyAssignmentsItem
    from ..models.create_wms_cycle_count_body_custom_fields import CreateWMSCycleCountBodyCustomFields
    from ..models.create_wms_cycle_count_body_schedule import CreateWMSCycleCountBodySchedule
    from ..models.create_wms_cycle_count_body_scope import CreateWMSCycleCountBodyScope


T = TypeVar("T", bound="CreateWMSCycleCountBody")


@_attrs_define
class CreateWMSCycleCountBody:
    """
    Attributes:
        warehouse_id (str): Target warehouse identifier Example: WH_ATL_001.
        count_type (CreateWMSCycleCountBodyCountType): Type of cycle count for methodology determination Example: ABC.
        schedule (CreateWMSCycleCountBodySchedule):
        cycle_count_id (Union[Unset, str]): Unique cycle count identifier (auto-generated if not provided) Example:
            CC_ATL_2024_001.
        count_status (Union[Unset, CreateWMSCycleCountBodyCountStatus]): Initial count status (defaults to SCHEDULED)
            Example: SCHEDULED.
        scope (Union[Unset, CreateWMSCycleCountBodyScope]):
        assignments (Union[Unset, list['CreateWMSCycleCountBodyAssignmentsItem']]): User assignments for count execution
        notes (Union[Unset, str]): Additional notes or instructions for count Example: Focus on high-value items in A
            classification.
        custom_fields (Union[Unset, CreateWMSCycleCountBodyCustomFields]): Additional warehouse-specific count
            attributes Example: {'priority': 'HIGH', 'countReason': 'Quarterly ABC Analysis', 'requiresApproval': True}.
    """

    warehouse_id: str
    count_type: CreateWMSCycleCountBodyCountType
    schedule: "CreateWMSCycleCountBodySchedule"
    cycle_count_id: Union[Unset, str] = UNSET
    count_status: Union[Unset, CreateWMSCycleCountBodyCountStatus] = UNSET
    scope: Union[Unset, "CreateWMSCycleCountBodyScope"] = UNSET
    assignments: Union[Unset, list["CreateWMSCycleCountBodyAssignmentsItem"]] = UNSET
    notes: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "CreateWMSCycleCountBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        count_type = self.count_type.value

        schedule = self.schedule.to_dict()

        cycle_count_id = self.cycle_count_id

        count_status: Union[Unset, str] = UNSET
        if not isinstance(self.count_status, Unset):
            count_status = self.count_status.value

        scope: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        assignments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.assignments, Unset):
            assignments = []
            for assignments_item_data in self.assignments:
                assignments_item = assignments_item_data.to_dict()
                assignments.append(assignments_item)

        notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "countType": count_type,
                "schedule": schedule,
            }
        )
        if cycle_count_id is not UNSET:
            field_dict["cycleCountId"] = cycle_count_id
        if count_status is not UNSET:
            field_dict["countStatus"] = count_status
        if scope is not UNSET:
            field_dict["scope"] = scope
        if assignments is not UNSET:
            field_dict["assignments"] = assignments
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_cycle_count_body_assignments_item import CreateWMSCycleCountBodyAssignmentsItem
        from ..models.create_wms_cycle_count_body_custom_fields import CreateWMSCycleCountBodyCustomFields
        from ..models.create_wms_cycle_count_body_schedule import CreateWMSCycleCountBodySchedule
        from ..models.create_wms_cycle_count_body_scope import CreateWMSCycleCountBodyScope

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        count_type = CreateWMSCycleCountBodyCountType(d.pop("countType"))

        schedule = CreateWMSCycleCountBodySchedule.from_dict(d.pop("schedule"))

        cycle_count_id = d.pop("cycleCountId", UNSET)

        _count_status = d.pop("countStatus", UNSET)
        count_status: Union[Unset, CreateWMSCycleCountBodyCountStatus]
        if isinstance(_count_status, Unset):
            count_status = UNSET
        else:
            count_status = CreateWMSCycleCountBodyCountStatus(_count_status)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, CreateWMSCycleCountBodyScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = CreateWMSCycleCountBodyScope.from_dict(_scope)

        assignments = []
        _assignments = d.pop("assignments", UNSET)
        for assignments_item_data in _assignments or []:
            assignments_item = CreateWMSCycleCountBodyAssignmentsItem.from_dict(assignments_item_data)

            assignments.append(assignments_item)

        notes = d.pop("notes", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, CreateWMSCycleCountBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = CreateWMSCycleCountBodyCustomFields.from_dict(_custom_fields)

        create_wms_cycle_count_body = cls(
            warehouse_id=warehouse_id,
            count_type=count_type,
            schedule=schedule,
            cycle_count_id=cycle_count_id,
            count_status=count_status,
            scope=scope,
            assignments=assignments,
            notes=notes,
            custom_fields=custom_fields,
        )

        create_wms_cycle_count_body.additional_properties = d
        return create_wms_cycle_count_body

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
