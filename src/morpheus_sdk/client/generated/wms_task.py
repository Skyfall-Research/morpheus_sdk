import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_task_task_status import WMSTaskTaskStatus
from ..models.wms_task_task_subtype import WMSTaskTaskSubtype
from ..models.wms_task_task_type import WMSTaskTaskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_task_assignment_type_0 import WMSTaskAssignmentType0
    from ..models.wms_task_custom_fields_type_0 import WMSTaskCustomFieldsType0
    from ..models.wms_task_details_item import WMSTaskDetailsItem
    from ..models.wms_task_from_type_0 import WMSTaskFromType0
    from ..models.wms_task_performance_type_0 import WMSTaskPerformanceType0
    from ..models.wms_task_product_type_0 import WMSTaskProductType0
    from ..models.wms_task_quantity_type_0 import WMSTaskQuantityType0
    from ..models.wms_task_reference_type_0 import WMSTaskReferenceType0
    from ..models.wms_task_scans_item import WMSTaskScansItem
    from ..models.wms_task_timing_type_0 import WMSTaskTimingType0
    from ..models.wms_task_to_type_0 import WMSTaskToType0
    from ..models.wms_task_world_ref import WMSTaskWorldRef


T = TypeVar("T", bound="WMSTask")


@_attrs_define
class WMSTask:
    """
    **WMS Task Management System**

    Comprehensive warehouse task orchestration with detailed tracking, performance measurement, and workflow automation.

    **⚠️ CRITICAL IMPLEMENTATION BUG:**

    > **BUG #7**: Aggregation pipeline uses `avgDuration` but return value expects `averageDuration`
    >
    > **Impact**: Inconsistent field naming in metrics response causing client-side failures
    > **Required Fix**: Align aggregation field name with expected return value or update interface

    **Task Types Supported:**
    - **PICK**: Order fulfillment picking operations
    - **PUTAWAY**: Inbound inventory storage tasks
    - **REPLENISHMENT**: Stock movement for bin replenishment
    - **CYCLE_COUNT**: Inventory counting and verification
    - **MOVE**: General inventory relocation
    - **LOAD/UNLOAD**: Dock and trailer operations
    - **PACK**: Order packaging and preparation
    - **SORT**: Product and order sorting operations

    **Status Workflow:**
    1. **CREATED** - Task generated but not yet available
    2. **RELEASED** - Task available for assignment
    3. **ASSIGNED** - Task assigned to specific user
    4. **IN_PROGRESS** - Task execution in progress
    5. **COMPLETED** - Task successfully finished
    6. **CANCELLED/SUSPENDED** - Task terminated or paused

    **Key Features:**
    - Priority-based task sequencing and assignment
    - Comprehensive timing and performance tracking
    - Detailed scan validation and audit trails
    - Flexible task detail and product tracking
    - Equipment and resource assignment
    - Real-time status monitoring and reporting


        Attributes:
            field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
            task_id (str): Unique business identifier for the task, auto-generated using WMS service prefix Example:
                wms_task_674565c1234567890abcdef.
            warehouse_id (str): Warehouse identifier where task occurs Example: WH001.
            task_type (WMSTaskTaskType): Type of warehouse operation to be performed Example: PICK.
            priority (float): Task priority level for sequencing (higher values = higher priority) Default: 50.0. Example:
                75.
            task_status (WMSTaskTaskStatus): Current status in the task lifecycle Default: WMSTaskTaskStatus.CREATED.
                Example: IN_PROGRESS.
            world_ref (WMSTaskWorldRef): Reference to the world environment containing this task
            created_at (datetime.datetime): Timestamp when the task record was created Example: 2024-11-27T09:00:00.000Z.
            updated_at (datetime.datetime): Timestamp when the task record was last updated Example:
                2024-11-27T09:35:00.000Z.
            task_subtype (Union[Unset, WMSTaskTaskSubtype]): Task execution methodology and grouping strategy Example:
                DISCRETE.
            reference (Union['WMSTaskReferenceType0', None, Unset]): Reference to originating business document
            product (Union['WMSTaskProductType0', None, Unset]): Product information associated with the task
            from_ (Union['WMSTaskFromType0', None, Unset]): Source location for the task
            to (Union['WMSTaskToType0', None, Unset]): Destination location for the task
            lot_number (Union[None, Unset, str]): Lot or batch number for traceability Example: LOT-20241127-001.
            license_plate_number (Union[None, Unset, str]): License plate number for pallet tracking Example: LPN-987654321.
            quantity (Union['WMSTaskQuantityType0', None, Unset]): Quantity requirements and tracking
            assignment (Union['WMSTaskAssignmentType0', None, Unset]): Task assignment and resource allocation
            zone_id (Union[None, Unset, str]): Primary zone identifier for the task Example: ZONE-PICK.
            timing (Union['WMSTaskTimingType0', None, Unset]): Comprehensive timing and performance tracking
            completed_by (Union[None, Unset, str]): User identifier who completed the task Example: USER-001.
            details (Union[Unset, list['WMSTaskDetailsItem']]): Task-specific detail items and sub-operations
            scans (Union[Unset, list['WMSTaskScansItem']]): Scan validation history and audit trail
            performance (Union['WMSTaskPerformanceType0', None, Unset]): Performance metrics and productivity data
            notes (Union[None, Unset, str]): Additional operational notes and instructions Example: Customer requested
                expedited processing.
            custom_fields (Union['WMSTaskCustomFieldsType0', None, Unset]): Additional business-specific data and
                configuration Example: {'shiftCode': 'DAY-1', 'supervisorId': 'SUP-001', 'customerPriority': 'HIGH',
                'specialInstructions': ['FRAGILE', 'HEAVY_LIFT']}.
    """

    field_id: str
    task_id: str
    warehouse_id: str
    task_type: WMSTaskTaskType
    world_ref: "WMSTaskWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    priority: float = 50.0
    task_status: WMSTaskTaskStatus = WMSTaskTaskStatus.CREATED
    task_subtype: Union[Unset, WMSTaskTaskSubtype] = UNSET
    reference: Union["WMSTaskReferenceType0", None, Unset] = UNSET
    product: Union["WMSTaskProductType0", None, Unset] = UNSET
    from_: Union["WMSTaskFromType0", None, Unset] = UNSET
    to: Union["WMSTaskToType0", None, Unset] = UNSET
    lot_number: Union[None, Unset, str] = UNSET
    license_plate_number: Union[None, Unset, str] = UNSET
    quantity: Union["WMSTaskQuantityType0", None, Unset] = UNSET
    assignment: Union["WMSTaskAssignmentType0", None, Unset] = UNSET
    zone_id: Union[None, Unset, str] = UNSET
    timing: Union["WMSTaskTimingType0", None, Unset] = UNSET
    completed_by: Union[None, Unset, str] = UNSET
    details: Union[Unset, list["WMSTaskDetailsItem"]] = UNSET
    scans: Union[Unset, list["WMSTaskScansItem"]] = UNSET
    performance: Union["WMSTaskPerformanceType0", None, Unset] = UNSET
    notes: Union[None, Unset, str] = UNSET
    custom_fields: Union["WMSTaskCustomFieldsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.wms_task_assignment_type_0 import WMSTaskAssignmentType0
        from ..models.wms_task_custom_fields_type_0 import WMSTaskCustomFieldsType0
        from ..models.wms_task_from_type_0 import WMSTaskFromType0
        from ..models.wms_task_performance_type_0 import WMSTaskPerformanceType0
        from ..models.wms_task_product_type_0 import WMSTaskProductType0
        from ..models.wms_task_quantity_type_0 import WMSTaskQuantityType0
        from ..models.wms_task_reference_type_0 import WMSTaskReferenceType0
        from ..models.wms_task_timing_type_0 import WMSTaskTimingType0
        from ..models.wms_task_to_type_0 import WMSTaskToType0

        field_id = self.field_id

        task_id = self.task_id

        warehouse_id = self.warehouse_id

        task_type = self.task_type.value

        priority = self.priority

        task_status = self.task_status.value

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        task_subtype: Union[Unset, str] = UNSET
        if not isinstance(self.task_subtype, Unset):
            task_subtype = self.task_subtype.value

        reference: Union[None, Unset, dict[str, Any]]
        if isinstance(self.reference, Unset):
            reference = UNSET
        elif isinstance(self.reference, WMSTaskReferenceType0):
            reference = self.reference.to_dict()
        else:
            reference = self.reference

        product: Union[None, Unset, dict[str, Any]]
        if isinstance(self.product, Unset):
            product = UNSET
        elif isinstance(self.product, WMSTaskProductType0):
            product = self.product.to_dict()
        else:
            product = self.product

        from_: Union[None, Unset, dict[str, Any]]
        if isinstance(self.from_, Unset):
            from_ = UNSET
        elif isinstance(self.from_, WMSTaskFromType0):
            from_ = self.from_.to_dict()
        else:
            from_ = self.from_

        to: Union[None, Unset, dict[str, Any]]
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, WMSTaskToType0):
            to = self.to.to_dict()
        else:
            to = self.to

        lot_number: Union[None, Unset, str]
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        license_plate_number: Union[None, Unset, str]
        if isinstance(self.license_plate_number, Unset):
            license_plate_number = UNSET
        else:
            license_plate_number = self.license_plate_number

        quantity: Union[None, Unset, dict[str, Any]]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        elif isinstance(self.quantity, WMSTaskQuantityType0):
            quantity = self.quantity.to_dict()
        else:
            quantity = self.quantity

        assignment: Union[None, Unset, dict[str, Any]]
        if isinstance(self.assignment, Unset):
            assignment = UNSET
        elif isinstance(self.assignment, WMSTaskAssignmentType0):
            assignment = self.assignment.to_dict()
        else:
            assignment = self.assignment

        zone_id: Union[None, Unset, str]
        if isinstance(self.zone_id, Unset):
            zone_id = UNSET
        else:
            zone_id = self.zone_id

        timing: Union[None, Unset, dict[str, Any]]
        if isinstance(self.timing, Unset):
            timing = UNSET
        elif isinstance(self.timing, WMSTaskTimingType0):
            timing = self.timing.to_dict()
        else:
            timing = self.timing

        completed_by: Union[None, Unset, str]
        if isinstance(self.completed_by, Unset):
            completed_by = UNSET
        else:
            completed_by = self.completed_by

        details: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()
                details.append(details_item)

        scans: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.scans, Unset):
            scans = []
            for scans_item_data in self.scans:
                scans_item = scans_item_data.to_dict()
                scans.append(scans_item)

        performance: Union[None, Unset, dict[str, Any]]
        if isinstance(self.performance, Unset):
            performance = UNSET
        elif isinstance(self.performance, WMSTaskPerformanceType0):
            performance = self.performance.to_dict()
        else:
            performance = self.performance

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        custom_fields: Union[None, Unset, dict[str, Any]]
        if isinstance(self.custom_fields, Unset):
            custom_fields = UNSET
        elif isinstance(self.custom_fields, WMSTaskCustomFieldsType0):
            custom_fields = self.custom_fields.to_dict()
        else:
            custom_fields = self.custom_fields

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "taskId": task_id,
                "warehouseId": warehouse_id,
                "taskType": task_type,
                "priority": priority,
                "taskStatus": task_status,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if task_subtype is not UNSET:
            field_dict["taskSubtype"] = task_subtype
        if reference is not UNSET:
            field_dict["reference"] = reference
        if product is not UNSET:
            field_dict["product"] = product
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if license_plate_number is not UNSET:
            field_dict["licensePlateNumber"] = license_plate_number
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if assignment is not UNSET:
            field_dict["assignment"] = assignment
        if zone_id is not UNSET:
            field_dict["zoneId"] = zone_id
        if timing is not UNSET:
            field_dict["timing"] = timing
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by
        if details is not UNSET:
            field_dict["details"] = details
        if scans is not UNSET:
            field_dict["scans"] = scans
        if performance is not UNSET:
            field_dict["performance"] = performance
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_task_assignment_type_0 import WMSTaskAssignmentType0
        from ..models.wms_task_custom_fields_type_0 import WMSTaskCustomFieldsType0
        from ..models.wms_task_details_item import WMSTaskDetailsItem
        from ..models.wms_task_from_type_0 import WMSTaskFromType0
        from ..models.wms_task_performance_type_0 import WMSTaskPerformanceType0
        from ..models.wms_task_product_type_0 import WMSTaskProductType0
        from ..models.wms_task_quantity_type_0 import WMSTaskQuantityType0
        from ..models.wms_task_reference_type_0 import WMSTaskReferenceType0
        from ..models.wms_task_scans_item import WMSTaskScansItem
        from ..models.wms_task_timing_type_0 import WMSTaskTimingType0
        from ..models.wms_task_to_type_0 import WMSTaskToType0
        from ..models.wms_task_world_ref import WMSTaskWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        task_id = d.pop("taskId")

        warehouse_id = d.pop("warehouseId")

        task_type = WMSTaskTaskType(d.pop("taskType"))

        priority = d.pop("priority")

        task_status = WMSTaskTaskStatus(d.pop("taskStatus"))

        world_ref = WMSTaskWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        _task_subtype = d.pop("taskSubtype", UNSET)
        task_subtype: Union[Unset, WMSTaskTaskSubtype]
        if isinstance(_task_subtype, Unset):
            task_subtype = UNSET
        else:
            task_subtype = WMSTaskTaskSubtype(_task_subtype)

        def _parse_reference(data: object) -> Union["WMSTaskReferenceType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reference_type_0 = WMSTaskReferenceType0.from_dict(data)

                return reference_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskReferenceType0", None, Unset], data)

        reference = _parse_reference(d.pop("reference", UNSET))

        def _parse_product(data: object) -> Union["WMSTaskProductType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                product_type_0 = WMSTaskProductType0.from_dict(data)

                return product_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskProductType0", None, Unset], data)

        product = _parse_product(d.pop("product", UNSET))

        def _parse_from_(data: object) -> Union["WMSTaskFromType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                from_type_0 = WMSTaskFromType0.from_dict(data)

                return from_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskFromType0", None, Unset], data)

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(data: object) -> Union["WMSTaskToType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                to_type_0 = WMSTaskToType0.from_dict(data)

                return to_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskToType0", None, Unset], data)

        to = _parse_to(d.pop("to", UNSET))

        def _parse_lot_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))

        def _parse_license_plate_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        license_plate_number = _parse_license_plate_number(d.pop("licensePlateNumber", UNSET))

        def _parse_quantity(data: object) -> Union["WMSTaskQuantityType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                quantity_type_0 = WMSTaskQuantityType0.from_dict(data)

                return quantity_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskQuantityType0", None, Unset], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        def _parse_assignment(data: object) -> Union["WMSTaskAssignmentType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                assignment_type_0 = WMSTaskAssignmentType0.from_dict(data)

                return assignment_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskAssignmentType0", None, Unset], data)

        assignment = _parse_assignment(d.pop("assignment", UNSET))

        def _parse_zone_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zone_id = _parse_zone_id(d.pop("zoneId", UNSET))

        def _parse_timing(data: object) -> Union["WMSTaskTimingType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                timing_type_0 = WMSTaskTimingType0.from_dict(data)

                return timing_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskTimingType0", None, Unset], data)

        timing = _parse_timing(d.pop("timing", UNSET))

        def _parse_completed_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completed_by = _parse_completed_by(d.pop("completedBy", UNSET))

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = WMSTaskDetailsItem.from_dict(details_item_data)

            details.append(details_item)

        scans = []
        _scans = d.pop("scans", UNSET)
        for scans_item_data in _scans or []:
            scans_item = WMSTaskScansItem.from_dict(scans_item_data)

            scans.append(scans_item)

        def _parse_performance(data: object) -> Union["WMSTaskPerformanceType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                performance_type_0 = WMSTaskPerformanceType0.from_dict(data)

                return performance_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskPerformanceType0", None, Unset], data)

        performance = _parse_performance(d.pop("performance", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        def _parse_custom_fields(data: object) -> Union["WMSTaskCustomFieldsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                custom_fields_type_0 = WMSTaskCustomFieldsType0.from_dict(data)

                return custom_fields_type_0
            except:  # noqa: E722
                pass
            return cast(Union["WMSTaskCustomFieldsType0", None, Unset], data)

        custom_fields = _parse_custom_fields(d.pop("customFields", UNSET))

        wms_task = cls(
            field_id=field_id,
            task_id=task_id,
            warehouse_id=warehouse_id,
            task_type=task_type,
            priority=priority,
            task_status=task_status,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            task_subtype=task_subtype,
            reference=reference,
            product=product,
            from_=from_,
            to=to,
            lot_number=lot_number,
            license_plate_number=license_plate_number,
            quantity=quantity,
            assignment=assignment,
            zone_id=zone_id,
            timing=timing,
            completed_by=completed_by,
            details=details,
            scans=scans,
            performance=performance,
            notes=notes,
            custom_fields=custom_fields,
        )

        wms_task.additional_properties = d
        return wms_task

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
