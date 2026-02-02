import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_cycle_count_count_status import WMSCycleCountCountStatus
from ..models.wms_cycle_count_count_type import WMSCycleCountCountType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_cycle_count_assignments_item import WMSCycleCountAssignmentsItem
    from ..models.wms_cycle_count_counts_item import WMSCycleCountCountsItem
    from ..models.wms_cycle_count_custom_fields import WMSCycleCountCustomFields
    from ..models.wms_cycle_count_schedule import WMSCycleCountSchedule
    from ..models.wms_cycle_count_scope import WMSCycleCountScope
    from ..models.wms_cycle_count_summary import WMSCycleCountSummary
    from ..models.wms_cycle_count_world_ref import WMSCycleCountWorldRef


T = TypeVar("T", bound="WMSCycleCount")


@_attrs_define
class WMSCycleCount:
    """Complete WMS cycle count record for inventory accuracy verification and variance analysis

    Attributes:
        field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str): Unique cycle count identifier Example: CC_ATL_2024_001.
        warehouse_id (str): Target warehouse identifier for count execution Example: WH_ATL_001.
        count_type (WMSCycleCountCountType): Type of cycle count for methodology determination Example: ABC.
        count_status (WMSCycleCountCountStatus): Current operational status of the cycle count Example: IN_PROGRESS.
        schedule (WMSCycleCountSchedule): Scheduling information and execution timeline
        world_ref (WMSCycleCountWorldRef): World reference information for multi-tenant context
        created_at (datetime.datetime): Timestamp when the cycle count record was created Example:
            2024-01-24T16:00:00.000Z.
        updated_at (datetime.datetime): Timestamp when the cycle count record was last updated Example:
            2024-01-25T17:00:00.000Z.
        id (Union[Unset, str]): Formatted document identifier for API responses Example: 507f1f77bcf86cd799439011.
        scope (Union[Unset, WMSCycleCountScope]): Count scope definition and targeting criteria
        assignments (Union[Unset, list['WMSCycleCountAssignmentsItem']]): User assignments and workload distribution
        counts (Union[Unset, list['WMSCycleCountCountsItem']]): Individual count results and variance details
        summary (Union[Unset, WMSCycleCountSummary]): Count summary and accuracy metrics
        approved_by (Union[Unset, str]): User who approved the count results Example: MANAGER_001.
        approved_at (Union[Unset, datetime.datetime]): Timestamp when count was approved Example:
            2024-01-25T17:00:00.000Z.
        notes (Union[Unset, str]): General notes about the count Example: Focus on high-value items in A classification.
            Some damaged inventory excluded..
        custom_fields (Union[Unset, WMSCycleCountCustomFields]): Additional warehouse-specific count attributes and
            metadata Example: {'priority': 'HIGH', 'countReason': 'Quarterly ABC Analysis', 'requiresApproval': True,
            'auditRequired': False}.
    """

    field_id: str
    cycle_count_id: str
    warehouse_id: str
    count_type: WMSCycleCountCountType
    count_status: WMSCycleCountCountStatus
    schedule: "WMSCycleCountSchedule"
    world_ref: "WMSCycleCountWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: Union[Unset, str] = UNSET
    scope: Union[Unset, "WMSCycleCountScope"] = UNSET
    assignments: Union[Unset, list["WMSCycleCountAssignmentsItem"]] = UNSET
    counts: Union[Unset, list["WMSCycleCountCountsItem"]] = UNSET
    summary: Union[Unset, "WMSCycleCountSummary"] = UNSET
    approved_by: Union[Unset, str] = UNSET
    approved_at: Union[Unset, datetime.datetime] = UNSET
    notes: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "WMSCycleCountCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        cycle_count_id = self.cycle_count_id

        warehouse_id = self.warehouse_id

        count_type = self.count_type.value

        count_status = self.count_status.value

        schedule = self.schedule.to_dict()

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id = self.id

        scope: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        assignments: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.assignments, Unset):
            assignments = []
            for assignments_item_data in self.assignments:
                assignments_item = assignments_item_data.to_dict()
                assignments.append(assignments_item)

        counts: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.counts, Unset):
            counts = []
            for counts_item_data in self.counts:
                counts_item = counts_item_data.to_dict()
                counts.append(counts_item)

        summary: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.summary, Unset):
            summary = self.summary.to_dict()

        approved_by = self.approved_by

        approved_at: Union[Unset, str] = UNSET
        if not isinstance(self.approved_at, Unset):
            approved_at = self.approved_at.isoformat()

        notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "cycleCountId": cycle_count_id,
                "warehouseId": warehouse_id,
                "countType": count_type,
                "countStatus": count_status,
                "schedule": schedule,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if scope is not UNSET:
            field_dict["scope"] = scope
        if assignments is not UNSET:
            field_dict["assignments"] = assignments
        if counts is not UNSET:
            field_dict["counts"] = counts
        if summary is not UNSET:
            field_dict["summary"] = summary
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by
        if approved_at is not UNSET:
            field_dict["approvedAt"] = approved_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_cycle_count_assignments_item import WMSCycleCountAssignmentsItem
        from ..models.wms_cycle_count_counts_item import WMSCycleCountCountsItem
        from ..models.wms_cycle_count_custom_fields import WMSCycleCountCustomFields
        from ..models.wms_cycle_count_schedule import WMSCycleCountSchedule
        from ..models.wms_cycle_count_scope import WMSCycleCountScope
        from ..models.wms_cycle_count_summary import WMSCycleCountSummary
        from ..models.wms_cycle_count_world_ref import WMSCycleCountWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        cycle_count_id = d.pop("cycleCountId")

        warehouse_id = d.pop("warehouseId")

        count_type = WMSCycleCountCountType(d.pop("countType"))

        count_status = WMSCycleCountCountStatus(d.pop("countStatus"))

        schedule = WMSCycleCountSchedule.from_dict(d.pop("schedule"))

        world_ref = WMSCycleCountWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        id = d.pop("id", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Union[Unset, WMSCycleCountScope]
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = WMSCycleCountScope.from_dict(_scope)

        assignments = []
        _assignments = d.pop("assignments", UNSET)
        for assignments_item_data in _assignments or []:
            assignments_item = WMSCycleCountAssignmentsItem.from_dict(assignments_item_data)

            assignments.append(assignments_item)

        counts = []
        _counts = d.pop("counts", UNSET)
        for counts_item_data in _counts or []:
            counts_item = WMSCycleCountCountsItem.from_dict(counts_item_data)

            counts.append(counts_item)

        _summary = d.pop("summary", UNSET)
        summary: Union[Unset, WMSCycleCountSummary]
        if isinstance(_summary, Unset):
            summary = UNSET
        else:
            summary = WMSCycleCountSummary.from_dict(_summary)

        approved_by = d.pop("approvedBy", UNSET)

        _approved_at = d.pop("approvedAt", UNSET)
        approved_at: Union[Unset, datetime.datetime]
        if isinstance(_approved_at, Unset):
            approved_at = UNSET
        else:
            approved_at = isoparse(_approved_at)

        notes = d.pop("notes", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSCycleCountCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSCycleCountCustomFields.from_dict(_custom_fields)

        wms_cycle_count = cls(
            field_id=field_id,
            cycle_count_id=cycle_count_id,
            warehouse_id=warehouse_id,
            count_type=count_type,
            count_status=count_status,
            schedule=schedule,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            scope=scope,
            assignments=assignments,
            counts=counts,
            summary=summary,
            approved_by=approved_by,
            approved_at=approved_at,
            notes=notes,
            custom_fields=custom_fields,
        )

        wms_cycle_count.additional_properties = d
        return wms_cycle_count

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
