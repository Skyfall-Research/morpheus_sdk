from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_erp_shipment_lines_body_lines_item_custom_fields import (
        UpdateERPShipmentLinesBodyLinesItemCustomFields,
    )


T = TypeVar("T", bound="UpdateERPShipmentLinesBodyLinesItem")


@_attrs_define
class UpdateERPShipmentLinesBodyLinesItem:
    """
    Attributes:
        line_number (float): Line item sequence number Example: 1.
        sku (str): Product SKU identifier Example: PROD_WIDGET_001.
        quantity_shipped (float): Quantity being shipped Example: 8.
        quantity_ordered (Union[Unset, float]): Original quantity ordered Example: 10.
        unit_of_measure (Union[Unset, str]): Unit of measure Example: EA.
        lot_number (Union[Unset, str]): Lot or batch number Example: LOT_2024_002.
        serial_numbers (Union[Unset, list[str]]): Serial numbers for tracked items Example: ['SN003', 'SN004', 'SN005'].
        pallet_id (Union[Unset, str]): Pallet identifier Example: PALLET_002.
        package_count (Union[Unset, float]): Number of packages Example: 1.
        weight (Union[Unset, float]): Total weight for line Example: 20.4.
        custom_fields (Union[Unset, UpdateERPShipmentLinesBodyLinesItemCustomFields]): Line-specific custom fields
    """

    line_number: float
    sku: str
    quantity_shipped: float
    quantity_ordered: Union[Unset, float] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    serial_numbers: Union[Unset, list[str]] = UNSET
    pallet_id: Union[Unset, str] = UNSET
    package_count: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    custom_fields: Union[Unset, "UpdateERPShipmentLinesBodyLinesItemCustomFields"] = UNSET
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

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNumber": line_number,
                "sku": sku,
                "quantityShipped": quantity_shipped,
            }
        )
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
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_erp_shipment_lines_body_lines_item_custom_fields import (
            UpdateERPShipmentLinesBodyLinesItemCustomFields,
        )

        d = dict(src_dict)
        line_number = d.pop("lineNumber")

        sku = d.pop("sku")

        quantity_shipped = d.pop("quantityShipped")

        quantity_ordered = d.pop("quantityOrdered", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        serial_numbers = cast(list[str], d.pop("serialNumbers", UNSET))

        pallet_id = d.pop("palletId", UNSET)

        package_count = d.pop("packageCount", UNSET)

        weight = d.pop("weight", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateERPShipmentLinesBodyLinesItemCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateERPShipmentLinesBodyLinesItemCustomFields.from_dict(_custom_fields)

        update_erp_shipment_lines_body_lines_item = cls(
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
            custom_fields=custom_fields,
        )

        update_erp_shipment_lines_body_lines_item.additional_properties = d
        return update_erp_shipment_lines_body_lines_item

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
