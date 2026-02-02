import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.wms_replenishment_replenishment_type import WMSReplenishmentReplenishmentType
from ..models.wms_replenishment_status import WMSReplenishmentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_replenishment_custom_fields import WMSReplenishmentCustomFields
    from ..models.wms_replenishment_from_bin import WMSReplenishmentFromBin
    from ..models.wms_replenishment_quantity import WMSReplenishmentQuantity
    from ..models.wms_replenishment_to_bin import WMSReplenishmentToBin
    from ..models.wms_replenishment_world_ref import WMSReplenishmentWorldRef


T = TypeVar("T", bound="WMSReplenishment")


@_attrs_define
class WMSReplenishment:
    """
    **WMS Inventory Replenishment Management**

    Complete replenishment operation tracking from suggestion through completion, managing bin-to-bin inventory movement
    with approval workflows.

    **⚠️ CRITICAL IMPLEMENTATION BUGS:**

    > **BUG #5**: Repository approval method sets `approvedQuantity` field but model expects `quantity.approved`
    structure
    >
    > **BUG #6**: Metrics aggregation references `suggestedQuantity` field but model stores `quantity.suggested`
    >
    > **Impact**: Approval functionality and metrics will fail or return incorrect data
    > **Required Fixes**:
    > - Update `approveReplenishment` method to set `quantity.approved` not `approvedQuantity`
    > - Update metrics aggregation to use `"$quantity.suggested"` not `"$suggestedQuantity"`

    **Business Process Flow:**
    1. **SUGGESTED** - Initial replenishment request created
    2. **APPROVED** - Management approval with quantity validation
    3. **TASK_CREATED** - Work order generated for execution
    4. **IN_PROGRESS** - Active execution by warehouse staff
    5. **COMPLETED** - Successfully finished with actual quantities
    6. **CANCELLED** - Process terminated with reason

    **Key Features:**
    - Complex bin-to-bin movement tracking
    - Multi-level quantity management (suggested/approved/actual)
    - Priority-based processing with workflow integration
    - Comprehensive audit trail with approval/cancellation metadata


        Attributes:
            field_id (str): MongoDB document identifier Example: 507f1f77bcf86cd799439011.
            replenishment_id (str): Unique business identifier for the replenishment request, auto-generated using WMS
                service prefix Example: wms_replenishment_674565c1234567890abcdef.
            warehouse_id (str): Source warehouse identifier where replenishment occurs Example: WH001.
            product_id (str): Product identifier being replenished Example: PROD-12345.
            from_bin (WMSReplenishmentFromBin): Source bin details with current availability information
            to_bin (WMSReplenishmentToBin): Destination bin details with capacity constraints
            quantity (WMSReplenishmentQuantity): Multi-level quantity tracking throughout replenishment lifecycle
            replenishment_type (WMSReplenishmentReplenishmentType): Type of replenishment strategy triggering this request
                Example: MIN_MAX.
            priority (float): Priority level for processing order (1-10, 10 being highest priority) Example: 5.
            status (WMSReplenishmentStatus): Current status in the replenishment workflow Example: SUGGESTED.
            world_ref (WMSReplenishmentWorldRef): Reference to the world environment containing this replenishment
            created_at (datetime.datetime): Timestamp when the replenishment record was created Example:
                2024-11-27T10:00:00.000Z.
            updated_at (datetime.datetime): Timestamp when the replenishment record was last updated Example:
                2024-11-27T15:30:00.000Z.
            sku (Union[Unset, str]): Product SKU for operational reference and identification Example: ABC-XYZ-001.
            due_date (Union[None, Unset, datetime.datetime]): Target completion date for the replenishment Example:
                2024-11-28T10:00:00Z.
            task_id (Union[None, Unset, str]): Associated task identifier when status becomes TASK_CREATED Example:
                TASK-12345.
            approved_by (Union[None, Unset, str]): User identifier of the approving manager Example: MGR-001.
            approved_date (Union[None, Unset, datetime.datetime]): Timestamp when replenishment was approved Example:
                2024-11-27T14:30:00Z.
            completed_by (Union[None, Unset, str]): User identifier of the completing operator Example: OP-007.
            completed_date (Union[None, Unset, datetime.datetime]): Timestamp when replenishment execution was completed
                Example: 2024-11-27T16:45:00Z.
            cancel_reason (Union[None, Unset, str]): Reason provided when replenishment was cancelled Example: Product
                discontinued.
            cancelled_by (Union[None, Unset, str]): User identifier who cancelled the replenishment Example: MGR-002.
            cancelled_date (Union[None, Unset, datetime.datetime]): Timestamp when replenishment was cancelled Example:
                2024-11-27T15:00:00Z.
            notes (Union[None, Unset, str]): Additional operational notes and instructions Example: Handle with care -
                fragile items.
            custom_fields (Union[Unset, WMSReplenishmentCustomFields]): Additional business-specific data and configuration
                Example: {'urgencyLevel': 'HIGH', 'costCenter': 'DC001', 'shiftAssignment': 'DAY', 'equipmentRequired':
                ['FORKLIFT', 'SCANNER']}.
    """

    field_id: str
    replenishment_id: str
    warehouse_id: str
    product_id: str
    from_bin: "WMSReplenishmentFromBin"
    to_bin: "WMSReplenishmentToBin"
    quantity: "WMSReplenishmentQuantity"
    replenishment_type: WMSReplenishmentReplenishmentType
    priority: float
    status: WMSReplenishmentStatus
    world_ref: "WMSReplenishmentWorldRef"
    created_at: datetime.datetime
    updated_at: datetime.datetime
    sku: Union[Unset, str] = UNSET
    due_date: Union[None, Unset, datetime.datetime] = UNSET
    task_id: Union[None, Unset, str] = UNSET
    approved_by: Union[None, Unset, str] = UNSET
    approved_date: Union[None, Unset, datetime.datetime] = UNSET
    completed_by: Union[None, Unset, str] = UNSET
    completed_date: Union[None, Unset, datetime.datetime] = UNSET
    cancel_reason: Union[None, Unset, str] = UNSET
    cancelled_by: Union[None, Unset, str] = UNSET
    cancelled_date: Union[None, Unset, datetime.datetime] = UNSET
    notes: Union[None, Unset, str] = UNSET
    custom_fields: Union[Unset, "WMSReplenishmentCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        replenishment_id = self.replenishment_id

        warehouse_id = self.warehouse_id

        product_id = self.product_id

        from_bin = self.from_bin.to_dict()

        to_bin = self.to_bin.to_dict()

        quantity = self.quantity.to_dict()

        replenishment_type = self.replenishment_type.value

        priority = self.priority

        status = self.status.value

        world_ref = self.world_ref.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        sku = self.sku

        due_date: Union[None, Unset, str]
        if isinstance(self.due_date, Unset):
            due_date = UNSET
        elif isinstance(self.due_date, datetime.datetime):
            due_date = self.due_date.isoformat()
        else:
            due_date = self.due_date

        task_id: Union[None, Unset, str]
        if isinstance(self.task_id, Unset):
            task_id = UNSET
        else:
            task_id = self.task_id

        approved_by: Union[None, Unset, str]
        if isinstance(self.approved_by, Unset):
            approved_by = UNSET
        else:
            approved_by = self.approved_by

        approved_date: Union[None, Unset, str]
        if isinstance(self.approved_date, Unset):
            approved_date = UNSET
        elif isinstance(self.approved_date, datetime.datetime):
            approved_date = self.approved_date.isoformat()
        else:
            approved_date = self.approved_date

        completed_by: Union[None, Unset, str]
        if isinstance(self.completed_by, Unset):
            completed_by = UNSET
        else:
            completed_by = self.completed_by

        completed_date: Union[None, Unset, str]
        if isinstance(self.completed_date, Unset):
            completed_date = UNSET
        elif isinstance(self.completed_date, datetime.datetime):
            completed_date = self.completed_date.isoformat()
        else:
            completed_date = self.completed_date

        cancel_reason: Union[None, Unset, str]
        if isinstance(self.cancel_reason, Unset):
            cancel_reason = UNSET
        else:
            cancel_reason = self.cancel_reason

        cancelled_by: Union[None, Unset, str]
        if isinstance(self.cancelled_by, Unset):
            cancelled_by = UNSET
        else:
            cancelled_by = self.cancelled_by

        cancelled_date: Union[None, Unset, str]
        if isinstance(self.cancelled_date, Unset):
            cancelled_date = UNSET
        elif isinstance(self.cancelled_date, datetime.datetime):
            cancelled_date = self.cancelled_date.isoformat()
        else:
            cancelled_date = self.cancelled_date

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "replenishmentId": replenishment_id,
                "warehouseId": warehouse_id,
                "productId": product_id,
                "fromBin": from_bin,
                "toBin": to_bin,
                "quantity": quantity,
                "replenishmentType": replenishment_type,
                "priority": priority,
                "status": status,
                "worldRef": world_ref,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )
        if sku is not UNSET:
            field_dict["sku"] = sku
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if approved_by is not UNSET:
            field_dict["approvedBy"] = approved_by
        if approved_date is not UNSET:
            field_dict["approvedDate"] = approved_date
        if completed_by is not UNSET:
            field_dict["completedBy"] = completed_by
        if completed_date is not UNSET:
            field_dict["completedDate"] = completed_date
        if cancel_reason is not UNSET:
            field_dict["cancelReason"] = cancel_reason
        if cancelled_by is not UNSET:
            field_dict["cancelledBy"] = cancelled_by
        if cancelled_date is not UNSET:
            field_dict["cancelledDate"] = cancelled_date
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.wms_replenishment_custom_fields import WMSReplenishmentCustomFields
        from ..models.wms_replenishment_from_bin import WMSReplenishmentFromBin
        from ..models.wms_replenishment_quantity import WMSReplenishmentQuantity
        from ..models.wms_replenishment_to_bin import WMSReplenishmentToBin
        from ..models.wms_replenishment_world_ref import WMSReplenishmentWorldRef

        d = dict(src_dict)
        field_id = d.pop("_id")

        replenishment_id = d.pop("replenishmentId")

        warehouse_id = d.pop("warehouseId")

        product_id = d.pop("productId")

        from_bin = WMSReplenishmentFromBin.from_dict(d.pop("fromBin"))

        to_bin = WMSReplenishmentToBin.from_dict(d.pop("toBin"))

        quantity = WMSReplenishmentQuantity.from_dict(d.pop("quantity"))

        replenishment_type = WMSReplenishmentReplenishmentType(d.pop("replenishmentType"))

        priority = d.pop("priority")

        status = WMSReplenishmentStatus(d.pop("status"))

        world_ref = WMSReplenishmentWorldRef.from_dict(d.pop("worldRef"))

        created_at = isoparse(d.pop("createdAt"))

        updated_at = isoparse(d.pop("updatedAt"))

        sku = d.pop("sku", UNSET)

        def _parse_due_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_date_type_0 = isoparse(data)

                return due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        due_date = _parse_due_date(d.pop("dueDate", UNSET))

        def _parse_task_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        task_id = _parse_task_id(d.pop("taskId", UNSET))

        def _parse_approved_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        approved_by = _parse_approved_by(d.pop("approvedBy", UNSET))

        def _parse_approved_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                approved_date_type_0 = isoparse(data)

                return approved_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        approved_date = _parse_approved_date(d.pop("approvedDate", UNSET))

        def _parse_completed_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        completed_by = _parse_completed_by(d.pop("completedBy", UNSET))

        def _parse_completed_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_date_type_0 = isoparse(data)

                return completed_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        completed_date = _parse_completed_date(d.pop("completedDate", UNSET))

        def _parse_cancel_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancel_reason = _parse_cancel_reason(d.pop("cancelReason", UNSET))

        def _parse_cancelled_by(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cancelled_by = _parse_cancelled_by(d.pop("cancelledBy", UNSET))

        def _parse_cancelled_date(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cancelled_date_type_0 = isoparse(data)

                return cancelled_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        cancelled_date = _parse_cancelled_date(d.pop("cancelledDate", UNSET))

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSReplenishmentCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSReplenishmentCustomFields.from_dict(_custom_fields)

        wms_replenishment = cls(
            field_id=field_id,
            replenishment_id=replenishment_id,
            warehouse_id=warehouse_id,
            product_id=product_id,
            from_bin=from_bin,
            to_bin=to_bin,
            quantity=quantity,
            replenishment_type=replenishment_type,
            priority=priority,
            status=status,
            world_ref=world_ref,
            created_at=created_at,
            updated_at=updated_at,
            sku=sku,
            due_date=due_date,
            task_id=task_id,
            approved_by=approved_by,
            approved_date=approved_date,
            completed_by=completed_by,
            completed_date=completed_date,
            cancel_reason=cancel_reason,
            cancelled_by=cancelled_by,
            cancelled_date=cancelled_date,
            notes=notes,
            custom_fields=custom_fields,
        )

        wms_replenishment.additional_properties = d
        return wms_replenishment

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
