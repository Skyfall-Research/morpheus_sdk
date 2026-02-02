from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_wms_task_body_task_subtype import CreateWMSTaskBodyTaskSubtype
from ..models.create_wms_task_body_task_type import CreateWMSTaskBodyTaskType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_task_body_assignment import CreateWMSTaskBodyAssignment
    from ..models.create_wms_task_body_from import CreateWMSTaskBodyFrom
    from ..models.create_wms_task_body_product import CreateWMSTaskBodyProduct
    from ..models.create_wms_task_body_quantity import CreateWMSTaskBodyQuantity
    from ..models.create_wms_task_body_reference import CreateWMSTaskBodyReference
    from ..models.create_wms_task_body_timing import CreateWMSTaskBodyTiming
    from ..models.create_wms_task_body_to import CreateWMSTaskBodyTo


T = TypeVar("T", bound="CreateWMSTaskBody")


@_attrs_define
class CreateWMSTaskBody:
    """
    Attributes:
        warehouse_id (str): Warehouse identifier where task occurs Example: WH001.
        task_type (CreateWMSTaskBodyTaskType): Type of warehouse operation Example: PICK.
        task_id (Union[Unset, str]): Unique task identifier (auto-generated if not provided) Example:
            wms_task_674565c1234567890abcdef.
        task_subtype (Union[Unset, CreateWMSTaskBodyTaskSubtype]): Task execution methodology Example: DISCRETE.
        priority (Union[Unset, float]): Task priority level (higher values = higher priority) Default: 50.0. Example:
            75.
        reference (Union[Unset, CreateWMSTaskBodyReference]): Reference to originating document
        product (Union[Unset, CreateWMSTaskBodyProduct]): Product information for the task
        from_ (Union[Unset, CreateWMSTaskBodyFrom]): Source location details
        to (Union[Unset, CreateWMSTaskBodyTo]): Destination location details
        quantity (Union[Unset, CreateWMSTaskBodyQuantity]): Quantity requirements
        assignment (Union[Unset, CreateWMSTaskBodyAssignment]): Task assignment information
        timing (Union[Unset, CreateWMSTaskBodyTiming]): Task timing estimates
    """

    warehouse_id: str
    task_type: CreateWMSTaskBodyTaskType
    task_id: Union[Unset, str] = UNSET
    task_subtype: Union[Unset, CreateWMSTaskBodyTaskSubtype] = UNSET
    priority: Union[Unset, float] = 50.0
    reference: Union[Unset, "CreateWMSTaskBodyReference"] = UNSET
    product: Union[Unset, "CreateWMSTaskBodyProduct"] = UNSET
    from_: Union[Unset, "CreateWMSTaskBodyFrom"] = UNSET
    to: Union[Unset, "CreateWMSTaskBodyTo"] = UNSET
    quantity: Union[Unset, "CreateWMSTaskBodyQuantity"] = UNSET
    assignment: Union[Unset, "CreateWMSTaskBodyAssignment"] = UNSET
    timing: Union[Unset, "CreateWMSTaskBodyTiming"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        warehouse_id = self.warehouse_id

        task_type = self.task_type.value

        task_id = self.task_id

        task_subtype: Union[Unset, str] = UNSET
        if not isinstance(self.task_subtype, Unset):
            task_subtype = self.task_subtype.value

        priority = self.priority

        reference: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.reference, Unset):
            reference = self.reference.to_dict()

        product: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        from_: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.from_, Unset):
            from_ = self.from_.to_dict()

        to: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()

        quantity: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.quantity, Unset):
            quantity = self.quantity.to_dict()

        assignment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.assignment, Unset):
            assignment = self.assignment.to_dict()

        timing: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timing, Unset):
            timing = self.timing.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouseId": warehouse_id,
                "taskType": task_type,
            }
        )
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if task_subtype is not UNSET:
            field_dict["taskSubtype"] = task_subtype
        if priority is not UNSET:
            field_dict["priority"] = priority
        if reference is not UNSET:
            field_dict["reference"] = reference
        if product is not UNSET:
            field_dict["product"] = product
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if assignment is not UNSET:
            field_dict["assignment"] = assignment
        if timing is not UNSET:
            field_dict["timing"] = timing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_task_body_assignment import CreateWMSTaskBodyAssignment
        from ..models.create_wms_task_body_from import CreateWMSTaskBodyFrom
        from ..models.create_wms_task_body_product import CreateWMSTaskBodyProduct
        from ..models.create_wms_task_body_quantity import CreateWMSTaskBodyQuantity
        from ..models.create_wms_task_body_reference import CreateWMSTaskBodyReference
        from ..models.create_wms_task_body_timing import CreateWMSTaskBodyTiming
        from ..models.create_wms_task_body_to import CreateWMSTaskBodyTo

        d = dict(src_dict)
        warehouse_id = d.pop("warehouseId")

        task_type = CreateWMSTaskBodyTaskType(d.pop("taskType"))

        task_id = d.pop("taskId", UNSET)

        _task_subtype = d.pop("taskSubtype", UNSET)
        task_subtype: Union[Unset, CreateWMSTaskBodyTaskSubtype]
        if isinstance(_task_subtype, Unset):
            task_subtype = UNSET
        else:
            task_subtype = CreateWMSTaskBodyTaskSubtype(_task_subtype)

        priority = d.pop("priority", UNSET)

        _reference = d.pop("reference", UNSET)
        reference: Union[Unset, CreateWMSTaskBodyReference]
        if isinstance(_reference, Unset):
            reference = UNSET
        else:
            reference = CreateWMSTaskBodyReference.from_dict(_reference)

        _product = d.pop("product", UNSET)
        product: Union[Unset, CreateWMSTaskBodyProduct]
        if isinstance(_product, Unset):
            product = UNSET
        else:
            product = CreateWMSTaskBodyProduct.from_dict(_product)

        _from_ = d.pop("from", UNSET)
        from_: Union[Unset, CreateWMSTaskBodyFrom]
        if isinstance(_from_, Unset):
            from_ = UNSET
        else:
            from_ = CreateWMSTaskBodyFrom.from_dict(_from_)

        _to = d.pop("to", UNSET)
        to: Union[Unset, CreateWMSTaskBodyTo]
        if isinstance(_to, Unset):
            to = UNSET
        else:
            to = CreateWMSTaskBodyTo.from_dict(_to)

        _quantity = d.pop("quantity", UNSET)
        quantity: Union[Unset, CreateWMSTaskBodyQuantity]
        if isinstance(_quantity, Unset):
            quantity = UNSET
        else:
            quantity = CreateWMSTaskBodyQuantity.from_dict(_quantity)

        _assignment = d.pop("assignment", UNSET)
        assignment: Union[Unset, CreateWMSTaskBodyAssignment]
        if isinstance(_assignment, Unset):
            assignment = UNSET
        else:
            assignment = CreateWMSTaskBodyAssignment.from_dict(_assignment)

        _timing = d.pop("timing", UNSET)
        timing: Union[Unset, CreateWMSTaskBodyTiming]
        if isinstance(_timing, Unset):
            timing = UNSET
        else:
            timing = CreateWMSTaskBodyTiming.from_dict(_timing)

        create_wms_task_body = cls(
            warehouse_id=warehouse_id,
            task_type=task_type,
            task_id=task_id,
            task_subtype=task_subtype,
            priority=priority,
            reference=reference,
            product=product,
            from_=from_,
            to=to,
            quantity=quantity,
            assignment=assignment,
            timing=timing,
        )

        create_wms_task_body.additional_properties = d
        return create_wms_task_body

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
