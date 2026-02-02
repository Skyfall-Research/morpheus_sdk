from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.wms_task_details_item_detail_status import WMSTaskDetailsItemDetailStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="WMSTaskDetailsItem")


@_attrs_define
class WMSTaskDetailsItem:
    """
    Attributes:
        detail_id (Union[Unset, str]): Unique detail line identifier Example: DTL-001.
        product_id (Union[Unset, str]): Product identifier for this detail line Example: PROD-12345.
        sku (Union[Unset, str]): SKU for this detail line Example: ABC-XYZ-001.
        bin_id (Union[Unset, str]): Bin identifier for this detail line Example: BIN-A001.
        lot_number (Union[None, Unset, str]): Lot number for this detail line Example: LOT-20241127-001.
        quantity (Union[Unset, float]): Required quantity for this detail line Example: 24.
        picked_quantity (Union[None, Unset, float]): Actual picked quantity Example: 22.
        uom (Union[Unset, str]): Unit of measure Example: EA.
        sequence_number (Union[None, Unset, float]): Execution sequence number Example: 1.
        detail_status (Union[Unset, WMSTaskDetailsItemDetailStatus]): Status of this detail line Example: COMPLETED.
    """

    detail_id: Union[Unset, str] = UNSET
    product_id: Union[Unset, str] = UNSET
    sku: Union[Unset, str] = UNSET
    bin_id: Union[Unset, str] = UNSET
    lot_number: Union[None, Unset, str] = UNSET
    quantity: Union[Unset, float] = UNSET
    picked_quantity: Union[None, Unset, float] = UNSET
    uom: Union[Unset, str] = UNSET
    sequence_number: Union[None, Unset, float] = UNSET
    detail_status: Union[Unset, WMSTaskDetailsItemDetailStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail_id = self.detail_id

        product_id = self.product_id

        sku = self.sku

        bin_id = self.bin_id

        lot_number: Union[None, Unset, str]
        if isinstance(self.lot_number, Unset):
            lot_number = UNSET
        else:
            lot_number = self.lot_number

        quantity = self.quantity

        picked_quantity: Union[None, Unset, float]
        if isinstance(self.picked_quantity, Unset):
            picked_quantity = UNSET
        else:
            picked_quantity = self.picked_quantity

        uom = self.uom

        sequence_number: Union[None, Unset, float]
        if isinstance(self.sequence_number, Unset):
            sequence_number = UNSET
        else:
            sequence_number = self.sequence_number

        detail_status: Union[Unset, str] = UNSET
        if not isinstance(self.detail_status, Unset):
            detail_status = self.detail_status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if detail_id is not UNSET:
            field_dict["detailId"] = detail_id
        if product_id is not UNSET:
            field_dict["productId"] = product_id
        if sku is not UNSET:
            field_dict["sku"] = sku
        if bin_id is not UNSET:
            field_dict["binId"] = bin_id
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if picked_quantity is not UNSET:
            field_dict["pickedQuantity"] = picked_quantity
        if uom is not UNSET:
            field_dict["uom"] = uom
        if sequence_number is not UNSET:
            field_dict["sequenceNumber"] = sequence_number
        if detail_status is not UNSET:
            field_dict["detailStatus"] = detail_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail_id = d.pop("detailId", UNSET)

        product_id = d.pop("productId", UNSET)

        sku = d.pop("sku", UNSET)

        bin_id = d.pop("binId", UNSET)

        def _parse_lot_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        lot_number = _parse_lot_number(d.pop("lotNumber", UNSET))

        quantity = d.pop("quantity", UNSET)

        def _parse_picked_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        picked_quantity = _parse_picked_quantity(d.pop("pickedQuantity", UNSET))

        uom = d.pop("uom", UNSET)

        def _parse_sequence_number(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sequence_number = _parse_sequence_number(d.pop("sequenceNumber", UNSET))

        _detail_status = d.pop("detailStatus", UNSET)
        detail_status: Union[Unset, WMSTaskDetailsItemDetailStatus]
        if isinstance(_detail_status, Unset):
            detail_status = UNSET
        else:
            detail_status = WMSTaskDetailsItemDetailStatus(_detail_status)

        wms_task_details_item = cls(
            detail_id=detail_id,
            product_id=product_id,
            sku=sku,
            bin_id=bin_id,
            lot_number=lot_number,
            quantity=quantity,
            picked_quantity=picked_quantity,
            uom=uom,
            sequence_number=sequence_number,
            detail_status=detail_status,
        )

        wms_task_details_item.additional_properties = d
        return wms_task_details_item

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
