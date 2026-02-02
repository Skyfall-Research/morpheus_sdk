import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.update_erp_order_body_status import UpdateERPOrderBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_erp_order_body_custom_fields import UpdateERPOrderBodyCustomFields
    from ..models.update_erp_order_body_lines_item import UpdateERPOrderBodyLinesItem


T = TypeVar("T", bound="UpdateERPOrderBody")


@_attrs_define
class UpdateERPOrderBody:
    """
    Attributes:
        requested_date (Union[Unset, datetime.date]): Updated requested delivery date Example: 2024-02-01.
        due_date (Union[Unset, datetime.date]): Updated due date Example: 2024-02-05.
        subtotal (Union[Unset, float]): Updated subtotal amount Example: 1350.
        total_amount (Union[Unset, float]): Updated total amount Example: 1450.
        status (Union[Unset, UpdateERPOrderBodyStatus]): Updated order status Example: IN_PROGRESS.
        lines (Union[Unset, list['UpdateERPOrderBodyLinesItem']]): Updated order line items
        notes (Union[Unset, str]): Updated order notes Example: Delivery instructions updated.
        custom_fields (Union[Unset, UpdateERPOrderBodyCustomFields]): Updated custom fields
    """

    requested_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    subtotal: Union[Unset, float] = UNSET
    total_amount: Union[Unset, float] = UNSET
    status: Union[Unset, UpdateERPOrderBodyStatus] = UNSET
    lines: Union[Unset, list["UpdateERPOrderBodyLinesItem"]] = UNSET
    notes: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "UpdateERPOrderBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        requested_date: Union[Unset, str] = UNSET
        if not isinstance(self.requested_date, Unset):
            requested_date = self.requested_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        subtotal = self.subtotal

        total_amount = self.total_amount

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        lines: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.lines, Unset):
            lines = []
            for lines_item_data in self.lines:
                lines_item = lines_item_data.to_dict()
                lines.append(lines_item)

        notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if requested_date is not UNSET:
            field_dict["requestedDate"] = requested_date
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if subtotal is not UNSET:
            field_dict["subtotal"] = subtotal
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if status is not UNSET:
            field_dict["status"] = status
        if lines is not UNSET:
            field_dict["lines"] = lines
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_erp_order_body_custom_fields import UpdateERPOrderBodyCustomFields
        from ..models.update_erp_order_body_lines_item import UpdateERPOrderBodyLinesItem

        d = dict(src_dict)
        _requested_date = d.pop("requestedDate", UNSET)
        requested_date: Union[Unset, datetime.date]
        if isinstance(_requested_date, Unset):
            requested_date = UNSET
        else:
            requested_date = isoparse(_requested_date).date()

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        subtotal = d.pop("subtotal", UNSET)

        total_amount = d.pop("totalAmount", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateERPOrderBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateERPOrderBodyStatus(_status)

        lines = []
        _lines = d.pop("lines", UNSET)
        for lines_item_data in _lines or []:
            lines_item = UpdateERPOrderBodyLinesItem.from_dict(lines_item_data)

            lines.append(lines_item)

        notes = d.pop("notes", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateERPOrderBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateERPOrderBodyCustomFields.from_dict(_custom_fields)

        update_erp_order_body = cls(
            requested_date=requested_date,
            due_date=due_date,
            subtotal=subtotal,
            total_amount=total_amount,
            status=status,
            lines=lines,
            notes=notes,
            custom_fields=custom_fields,
        )

        update_erp_order_body.additional_properties = d
        return update_erp_order_body

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
