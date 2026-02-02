from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateERPPaymentBodyAllocationsItem")


@_attrs_define
class CreateERPPaymentBodyAllocationsItem:
    """
    Attributes:
        invoice_number (str): Invoice number for allocation Example: INV_507f1f77bcf86cd799439016.
        applied_amount (float): Amount applied to invoice Example: 750.
        discount_taken (Union[Unset, float]): Early payment discount taken Example: 15.
        unapplied_amount (Union[Unset, float]): Unapplied amount remaining
        allocation_method (Union[Unset, str]): Method used for allocation Example: FIFO.
    """

    invoice_number: str
    applied_amount: float
    discount_taken: Union[Unset, float] = UNSET
    unapplied_amount: Union[Unset, float] = UNSET
    allocation_method: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        invoice_number = self.invoice_number

        applied_amount = self.applied_amount

        discount_taken = self.discount_taken

        unapplied_amount = self.unapplied_amount

        allocation_method = self.allocation_method

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invoiceNumber": invoice_number,
                "appliedAmount": applied_amount,
            }
        )
        if discount_taken is not UNSET:
            field_dict["discountTaken"] = discount_taken
        if unapplied_amount is not UNSET:
            field_dict["unappliedAmount"] = unapplied_amount
        if allocation_method is not UNSET:
            field_dict["allocationMethod"] = allocation_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        invoice_number = d.pop("invoiceNumber")

        applied_amount = d.pop("appliedAmount")

        discount_taken = d.pop("discountTaken", UNSET)

        unapplied_amount = d.pop("unappliedAmount", UNSET)

        allocation_method = d.pop("allocationMethod", UNSET)

        create_erp_payment_body_allocations_item = cls(
            invoice_number=invoice_number,
            applied_amount=applied_amount,
            discount_taken=discount_taken,
            unapplied_amount=unapplied_amount,
            allocation_method=allocation_method,
        )

        create_erp_payment_body_allocations_item.additional_properties = d
        return create_erp_payment_body_allocations_item

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
