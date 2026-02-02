import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWMSInboundOrderReceivingProgressBody")


@_attrs_define
class UpdateWMSInboundOrderReceivingProgressBody:
    """
    Example:
        {'lineNumber': 1, 'receivedQuantity': 150, 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}

    Attributes:
        line_number (float): Line number within the order for specific product Example: 1.
        received_quantity (float): Quantity received in this receiving session Example: 150.
        lot_number (Union[Unset, str]): Lot number for batch tracking and traceability Example: LOT-2024-W47.
        expiration_date (Union[Unset, datetime.datetime]): Product expiration date for perishable items Example:
            2025-11-27T00:00:00Z.
    """

    line_number: float
    received_quantity: float
    lot_number: Union[Unset, str] = UNSET
    expiration_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        line_number = self.line_number

        received_quantity = self.received_quantity

        lot_number = self.lot_number

        expiration_date: Union[Unset, str] = UNSET
        if not isinstance(self.expiration_date, Unset):
            expiration_date = self.expiration_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lineNumber": line_number,
                "receivedQuantity": received_quantity,
            }
        )
        if lot_number is not UNSET:
            field_dict["lotNumber"] = lot_number
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        line_number = d.pop("lineNumber")

        received_quantity = d.pop("receivedQuantity")

        lot_number = d.pop("lotNumber", UNSET)

        _expiration_date = d.pop("expirationDate", UNSET)
        expiration_date: Union[Unset, datetime.datetime]
        if isinstance(_expiration_date, Unset):
            expiration_date = UNSET
        else:
            expiration_date = isoparse(_expiration_date)

        update_wms_inbound_order_receiving_progress_body = cls(
            line_number=line_number,
            received_quantity=received_quantity,
            lot_number=lot_number,
            expiration_date=expiration_date,
        )

        update_wms_inbound_order_receiving_progress_body.additional_properties = d
        return update_wms_inbound_order_receiving_progress_body

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
