import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.create_wms_replenishment_body_replenishment_type import CreateWMSReplenishmentBodyReplenishmentType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_wms_replenishment_body_from_bin import CreateWMSReplenishmentBodyFromBin
    from ..models.create_wms_replenishment_body_quantity import CreateWMSReplenishmentBodyQuantity
    from ..models.create_wms_replenishment_body_to_bin import CreateWMSReplenishmentBodyToBin


T = TypeVar("T", bound="CreateWMSReplenishmentBody")


@_attrs_define
class CreateWMSReplenishmentBody:
    """
    Attributes:
        replenishment_id (str): Unique identifier for the replenishment request Example: REPL-001-WH001-20241127.
        warehouse_id (str): Source warehouse identifier Example: WH001.
        product_id (str): Product being replenished Example: PROD-12345.
        from_bin (CreateWMSReplenishmentBodyFromBin): Source bin details with availability
        to_bin (CreateWMSReplenishmentBodyToBin): Destination bin details with capacity
        quantity (CreateWMSReplenishmentBodyQuantity): Quantity information for replenishment
        sku (Union[Unset, str]): Product SKU for reference Example: ABC-XYZ-001.
        replenishment_type (Union[Unset, CreateWMSReplenishmentBodyReplenishmentType]):  Example: MIN_MAX.
        priority (Union[Unset, float]): Priority level (1-10, 10 being highest) Example: 5.
        due_date (Union[Unset, datetime.datetime]): When replenishment should be completed Example:
            2024-11-28T10:00:00Z.
    """

    replenishment_id: str
    warehouse_id: str
    product_id: str
    from_bin: "CreateWMSReplenishmentBodyFromBin"
    to_bin: "CreateWMSReplenishmentBodyToBin"
    quantity: "CreateWMSReplenishmentBodyQuantity"
    sku: Union[Unset, str] = UNSET
    replenishment_type: Union[Unset, CreateWMSReplenishmentBodyReplenishmentType] = UNSET
    priority: Union[Unset, float] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        replenishment_id = self.replenishment_id

        warehouse_id = self.warehouse_id

        product_id = self.product_id

        from_bin = self.from_bin.to_dict()

        to_bin = self.to_bin.to_dict()

        quantity = self.quantity.to_dict()

        sku = self.sku

        replenishment_type: Union[Unset, str] = UNSET
        if not isinstance(self.replenishment_type, Unset):
            replenishment_type = self.replenishment_type.value

        priority = self.priority

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "replenishmentId": replenishment_id,
                "warehouseId": warehouse_id,
                "productId": product_id,
                "fromBin": from_bin,
                "toBin": to_bin,
                "quantity": quantity,
            }
        )
        if sku is not UNSET:
            field_dict["sku"] = sku
        if replenishment_type is not UNSET:
            field_dict["replenishmentType"] = replenishment_type
        if priority is not UNSET:
            field_dict["priority"] = priority
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_wms_replenishment_body_from_bin import CreateWMSReplenishmentBodyFromBin
        from ..models.create_wms_replenishment_body_quantity import CreateWMSReplenishmentBodyQuantity
        from ..models.create_wms_replenishment_body_to_bin import CreateWMSReplenishmentBodyToBin

        d = dict(src_dict)
        replenishment_id = d.pop("replenishmentId")

        warehouse_id = d.pop("warehouseId")

        product_id = d.pop("productId")

        from_bin = CreateWMSReplenishmentBodyFromBin.from_dict(d.pop("fromBin"))

        to_bin = CreateWMSReplenishmentBodyToBin.from_dict(d.pop("toBin"))

        quantity = CreateWMSReplenishmentBodyQuantity.from_dict(d.pop("quantity"))

        sku = d.pop("sku", UNSET)

        _replenishment_type = d.pop("replenishmentType", UNSET)
        replenishment_type: Union[Unset, CreateWMSReplenishmentBodyReplenishmentType]
        if isinstance(_replenishment_type, Unset):
            replenishment_type = UNSET
        else:
            replenishment_type = CreateWMSReplenishmentBodyReplenishmentType(_replenishment_type)

        priority = d.pop("priority", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        create_wms_replenishment_body = cls(
            replenishment_id=replenishment_id,
            warehouse_id=warehouse_id,
            product_id=product_id,
            from_bin=from_bin,
            to_bin=to_bin,
            quantity=quantity,
            sku=sku,
            replenishment_type=replenishment_type,
            priority=priority,
            due_date=due_date,
        )

        create_wms_replenishment_body.additional_properties = d
        return create_wms_replenishment_body

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
