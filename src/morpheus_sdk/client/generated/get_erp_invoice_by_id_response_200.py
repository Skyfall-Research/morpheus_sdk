from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.erp_invoice import ERPInvoice


T = TypeVar("T", bound="GetERPInvoiceByIdResponse200")


@_attrs_define
class GetERPInvoiceByIdResponse200:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        status (Union[Unset, int]):  Example: 200.
        message (Union[Unset, str]):  Example: Invoice retrieved successfully.
        data (Union[Unset, ERPInvoice]): ERP invoice with comprehensive billing information and line item details
    """

    success: Union[Unset, bool] = UNSET
    status: Union[Unset, int] = UNSET
    message: Union[Unset, str] = UNSET
    data: Union[Unset, "ERPInvoice"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        message = self.message

        data: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if status is not UNSET:
            field_dict["status"] = status
        if message is not UNSET:
            field_dict["message"] = message
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.erp_invoice import ERPInvoice

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        status = d.pop("status", UNSET)

        message = d.pop("message", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, ERPInvoice]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = ERPInvoice.from_dict(_data)

        get_erp_invoice_by_id_response_200 = cls(
            success=success,
            status=status,
            message=message,
            data=data,
        )

        get_erp_invoice_by_id_response_200.additional_properties = d
        return get_erp_invoice_by_id_response_200

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
