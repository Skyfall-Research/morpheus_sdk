from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_erp_payment_body_method import UpdateERPPaymentBodyMethod
from ..models.update_erp_payment_body_status import UpdateERPPaymentBodyStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_erp_payment_body_bank_details import UpdateERPPaymentBodyBankDetails
    from ..models.update_erp_payment_body_custom_fields import UpdateERPPaymentBodyCustomFields


T = TypeVar("T", bound="UpdateERPPaymentBody")


@_attrs_define
class UpdateERPPaymentBody:
    """
    Attributes:
        total_amount (Union[Unset, float]): Updated payment amount Example: 1650.
        method (Union[Unset, UpdateERPPaymentBodyMethod]): Updated payment method Example: WIRE.
        bank_details (Union[Unset, UpdateERPPaymentBodyBankDetails]): Updated banking information
        status (Union[Unset, UpdateERPPaymentBodyStatus]): Updated payment status Example: APPLIED.
        reference_numbers (Union[Unset, list[str]]): Updated reference numbers Example: ['REF002', 'WIRE98765'].
        notes (Union[Unset, str]): Updated payment notes Example: Payment updated per customer request.
        custom_fields (Union[Unset, UpdateERPPaymentBodyCustomFields]): Updated custom fields
    """

    total_amount: Union[Unset, float] = UNSET
    method: Union[Unset, UpdateERPPaymentBodyMethod] = UNSET
    bank_details: Union[Unset, "UpdateERPPaymentBodyBankDetails"] = UNSET
    status: Union[Unset, UpdateERPPaymentBodyStatus] = UNSET
    reference_numbers: Union[Unset, list[str]] = UNSET
    notes: Union[Unset, str] = UNSET
    custom_fields: Union[Unset, "UpdateERPPaymentBodyCustomFields"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_amount = self.total_amount

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        bank_details: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.bank_details, Unset):
            bank_details = self.bank_details.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        reference_numbers: Union[Unset, list[str]] = UNSET
        if not isinstance(self.reference_numbers, Unset):
            reference_numbers = self.reference_numbers

        notes = self.notes

        custom_fields: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.custom_fields, Unset):
            custom_fields = self.custom_fields.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_amount is not UNSET:
            field_dict["totalAmount"] = total_amount
        if method is not UNSET:
            field_dict["method"] = method
        if bank_details is not UNSET:
            field_dict["bankDetails"] = bank_details
        if status is not UNSET:
            field_dict["status"] = status
        if reference_numbers is not UNSET:
            field_dict["referenceNumbers"] = reference_numbers
        if notes is not UNSET:
            field_dict["notes"] = notes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_erp_payment_body_bank_details import UpdateERPPaymentBodyBankDetails
        from ..models.update_erp_payment_body_custom_fields import UpdateERPPaymentBodyCustomFields

        d = dict(src_dict)
        total_amount = d.pop("totalAmount", UNSET)

        _method = d.pop("method", UNSET)
        method: Union[Unset, UpdateERPPaymentBodyMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = UpdateERPPaymentBodyMethod(_method)

        _bank_details = d.pop("bankDetails", UNSET)
        bank_details: Union[Unset, UpdateERPPaymentBodyBankDetails]
        if isinstance(_bank_details, Unset):
            bank_details = UNSET
        else:
            bank_details = UpdateERPPaymentBodyBankDetails.from_dict(_bank_details)

        _status = d.pop("status", UNSET)
        status: Union[Unset, UpdateERPPaymentBodyStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = UpdateERPPaymentBodyStatus(_status)

        reference_numbers = cast(list[str], d.pop("referenceNumbers", UNSET))

        notes = d.pop("notes", UNSET)

        _custom_fields = d.pop("customFields", UNSET)
        custom_fields: Union[Unset, UpdateERPPaymentBodyCustomFields]
        if isinstance(_custom_fields, Unset):
            custom_fields = UNSET
        else:
            custom_fields = UpdateERPPaymentBodyCustomFields.from_dict(_custom_fields)

        update_erp_payment_body = cls(
            total_amount=total_amount,
            method=method,
            bank_details=bank_details,
            status=status,
            reference_numbers=reference_numbers,
            notes=notes,
            custom_fields=custom_fields,
        )

        update_erp_payment_body.additional_properties = d
        return update_erp_payment_body

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
