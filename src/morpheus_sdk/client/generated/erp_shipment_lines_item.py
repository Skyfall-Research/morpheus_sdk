from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_shipment_lines_item_custom_fields import ERPShipmentLinesItemCustomFields
    from ..models.erp_shipment_lines_item_customs import ERPShipmentLinesItemCustoms


T = TypeVar("T", bound="ERPShipmentLinesItem")


@_attrs_define
class ERPShipmentLinesItem:
    """
    Attributes:
        line_number (Union[Unset, float]):  Example: 1.
        sku (Union[Unset, str]):  Example: PROD_WIDGET_001.
        quantity_shipped (Union[Unset, float]):  Example: 10.
        quantity_ordered (Union[Unset, float]):  Example: 15.
        unit_of_measure (Union[Unset, str]):  Example: EA.
        lot_number (Union[Unset, str]):  Example: LOT_2024_001.
        serial_numbers (Union[Unset, list[str]]):  Example: ['SN001', 'SN002'].
        pallet_id (Union[Unset, str]):  Example: PALLET_001.
        package_count (Union[Unset, float]):  Example: 2.
        weight (Union[Unset, float]):  Example: 25.5.
        customs (Union[Unset, ERPShipmentLinesItemCustoms]): Customs information
        custom_fields (Union[Unset, ERPShipmentLinesItemCustomFields]): Line-specific custom fields
    """

    line_number: Union[Unset, float] = UNSET
    sku: Union[Unset, str] = UNSET
    quantity_shipped: Union[Unset, float] = UNSET
    quantity_ordered: Union[Unset, float] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    serial_numbers: Union[Unset, list[str]] = UNSET
    pallet_id: Union[Unset, str] = UNSET
    package_count: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    customs: Union[Unset, "ERPShipmentLinesItemCustoms"] = UNSET
    custom_fields: Union[Unset, "ERPShipmentLinesItemCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        sku = self.sku

        quantity_shipped = self.quantity_shipped

        quantity_ordered = self.quantity_ordered

        unit_of_measure = self.unit_of_measure

        lot_number = self.lot_number

        serial_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.serial_numbers, Unset):
            serial_numbers = self.serial_numbers

        pallet_id = self.pallet_id

        package_count = self.package_count

        weight = self.weight

        customs: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customs, Unset):
            customs = self.customs.to_dict()

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if line_number is not UNSET:
            field_dict["lineNumber"] = line_number
        if sku is not UNSET:
            field_dict["sku"] = sku
        if quantity_shipped is not UNSET:
            field_dict["quantityShipped"] = quantity_shipped
        if quantity_ordered is not UNSET:
            field_dict["quantityOrdered"] = quantity_ordered
        if unit_of_measure is not UNSET:
            field_dict["unitOfMeasure"] = unit_of_measure
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if serial_numbers is not UNSET:
            field_dict["serialNumbers"] = serial_numbers
        if pallet_id is not UNSET:
            field_dict["palletId"] = pallet_id
        if package_count is not UNSET:
            field_dict["packageCount"] = package_count
        if weight is not UNSET:
            field_dict["weight"] = weight
        if customs is not UNSET:
            field_dict["customs"] = customs
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_shipment_lines_item_custom_fields import ERPShipmentLinesItemCustomFields
        from ..models.erp_shipment_lines_item_customs import ERPShipmentLinesItemCustoms

        d = dict(src_dict)
        line_number = d.pop("lineNumber", UNSET)

        sku = d.pop("sku", UNSET)

        quantity_shipped = d.pop("quantityShipped", UNSET)

        quantity_ordered = d.pop("quantityOrdered", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        serial_numbers = cast(list[str], d.pop("serialNumbers", UNSET))

        pallet_id = d.pop("palletId", UNSET)

        package_count = d.pop("packageCount", UNSET)

        weight = d.pop("weight", UNSET)

        _customs = d.pop("customs", UNSET)
        customs: Union[Unset, ERPShipmentLinesItemCustoms]
        if isinstance(_customs, Unset):
            customs = UNSET
        else:
            customs = ERPShipmentLinesItemCustoms.from_dict(_customs)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, ERPShipmentLinesItemCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = ERPShipmentLinesItemCustomFields.from_dict(_custom_fields)

        erp_shipment_lines_item = cls(
            line_number=line_number,
            sku=sku,
            quantity_shipped=quantity_shipped,
            quantity_ordered=quantity_ordered,
            unit_of_measure=unit_of_measure,
            lot_number=lot_number,
            serial_numbers=serial_numbers,
            pallet_id=pallet_id,
            package_count=package_count,
            weight=weight,
            customs=customs,
            custom_fields=custom_fields,
        )

        erp_shipment_lines_item.additional_properties = d
        return erp_shipment_lines_item

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
