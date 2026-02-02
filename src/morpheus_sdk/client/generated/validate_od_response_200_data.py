from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidateODResponse200Data")


@_attrs_define
class ValidateODResponse200Data:
    """
    Attributes:
        is_valid (Union[Unset, bool]):
        errors (Union[Unset, list[str]]):
        warnings (Union[Unset, list[str]]):
    """

    is_valid: Union[Unset, bool] = UNSET
    errors: Union[Unset, list[str]] = UNSET
    warnings: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_valid = self.is_valid

        errors: Union[Unset, list[str]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = self.errors

        warnings: Union[Unset, list[str]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_valid is not UNSET:
            field_dict["isValid"] = is_valid
        if errors is not UNSET:
            field_dict["errors"] = errors
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_valid = d.pop("isValid", UNSET)

        errors = cast(list[str], d.pop("errors", UNSET))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        validate_od_response_200_data = cls(
            is_valid=is_valid,
            errors=errors,
            warnings=warnings,
        )

        validate_od_response_200_data.additional_properties = d
        return validate_od_response_200_data

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
