from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.wms_outbound_shipment_lines_item_custom_fields import WMSOutboundShipmentLinesItemCustomFields


T = TypeVar("T", bound="WMSOutboundShipmentLinesItem")


@_attrs_define
class WMSOutboundShipmentLinesItem:
    """Individual line item with order and product details

    Attributes:
        line_number (float): Sequential line identifier within shipment Example: 1.
        sku (str): Product SKU/item code Example: SKU-WIDGET-001.
        quantity_shipped (float): Quantity included in this shipment Example: 25.
        order_id (Union[Unset, str]): Source order identifier Example: ORD-2024-001234.
        order_line_id (Union[Unset, str]): Source order line identifier Example: LINE-001.
        product_name (Union[Unset, str]): Product display name Example: Premium Widget Assembly.
        quantity_ordered (Union[Unset, float]): Originally ordered quantity Example: 25.
        unit_of_measure (Union[Unset, str]): Unit of measure code Example: EA.
        lot_number (Union[Unset, str]): Lot/batch number for traceability Example: LOT-20241201-A.
        serial_numbers (Union[Unset, list[str]]): Serial numbers for serialized items Example: ['SN123456', 'SN123457'].
        pallet_id (Union[Unset, str]): Pallet identifier for logistics Example: PLT-001.
        package_count (Union[Unset, float]): Number of packages for this line Example: 2.
        weight (Union[Unset, float]): Line weight contribution Example: 15.5.
        custom_fields (Union[Unset, WMSOutboundShipmentLinesItemCustomFields]): Line-specific custom attributes
    """

    line_number: float
    sku: str
    quantity_shipped: float
    order_id: Union[Unset, str] = UNSET
    order_line_id: Union[Unset, str] = UNSET
    product_name: Union[Unset, str] = UNSET
    quantity_ordered: Union[Unset, float] = UNSET
    unit_of_measure: Union[Unset, str] = UNSET
    lot_number: Union[Unset, str] = UNSET
    serial_numbers: Union[Unset, list[str]] = UNSET
    pallet_id: Union[Unset, str] = UNSET
    package_count: Union[Unset, float] = UNSET
    weight: Union[Unset, float] = UNSET
    custom_fields: Union[Unset, "WMSOutboundShipmentLinesItemCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        sku = self.sku

        quantity_shipped = self.quantity_shipped

        order_id = self.order_id

        order_line_id = self.order_line_id

        product_name = self.product_name

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
        if order_id is not UNSET:
            field_dict["orderId"] = order_id
        if order_line_id is not UNSET:
            field_dict["orderLineId"] = order_line_id
        if product_name is not UNSET:
            field_dict["productName"] = product_name
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
        from ..models.wms_outbound_shipment_lines_item_custom_fields import WMSOutboundShipmentLinesItemCustomFields

        d = dict(src_dict)
        line_number = d.pop("lineNumber")

        sku = d.pop("sku")

        quantity_shipped = d.pop("quantityShipped")

        order_id = d.pop("orderId", UNSET)

        order_line_id = d.pop("orderLineId", UNSET)

        product_name = d.pop("productName", UNSET)

        quantity_ordered = d.pop("quantityOrdered", UNSET)

        unit_of_measure = d.pop("unitOfMeasure", UNSET)

        lot_number = d.pop("lotNumber", UNSET)

        serial_numbers = cast(list[str], d.pop("serialNumbers", UNSET))

        pallet_id = d.pop("palletId", UNSET)

        package_count = d.pop("packageCount", UNSET)

        weight = d.pop("weight", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, WMSOutboundShipmentLinesItemCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = WMSOutboundShipmentLinesItemCustomFields.from_dict(_custom_fields)

        wms_outbound_shipment_lines_item = cls(
            line_number=line_number,
            sku=sku,
            quantity_shipped=quantity_shipped,
            order_id=order_id,
            order_line_id=order_line_id,
            product_name=product_name,
            quantity_ordered=quantity_ordered,
            unit_of_measure=unit_of_measure,
            lot_number=lot_number,
            serial_numbers=serial_numbers,
            pallet_id=pallet_id,
            package_count=package_count,
            weight=weight,
            custom_fields=custom_fields,
        )

        wms_outbound_shipment_lines_item.additional_properties = d
        return wms_outbound_shipment_lines_item

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
