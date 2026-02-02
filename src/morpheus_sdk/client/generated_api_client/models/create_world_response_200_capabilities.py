from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_world_response_200_capabilities_validation_warnings_item import (
        CreateWorldResponse200CapabilitiesValidationWarningsItem,
    )


T = TypeVar("T", bound="CreateWorldResponse200Capabilities")


@_attrs_define
class CreateWorldResponse200Capabilities:
    """Capability sampling results (only present when samplingStrategy is provided)

    Attributes:
        sampling_type (Union[Unset, str]): Type of sampling used Example: random.
        count (Union[Unset, int]): Number of capabilities sampled Example: 10.
        ids (Union[Unset, list[str]]): IDs of sampled capabilities
        validation_warnings (Union[Unset, list['CreateWorldResponse200CapabilitiesValidationWarningsItem']]): Any
            validation warnings from capability validation
    """

    sampling_type: Union[Unset, str] = UNSET
    count: Union[Unset, int] = UNSET
    ids: Union[Unset, list[str]] = UNSET
    validation_warnings: Union[Unset, list["CreateWorldResponse200CapabilitiesValidationWarningsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sampling_type = self.sampling_type

        count = self.count

        ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.ids, Unset):
            ids = self.ids

        validation_warnings: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.validation_warnings, Unset):
            validation_warnings = []
            for validation_warnings_item_data in self.validation_warnings:
                validation_warnings_item = validation_warnings_item_data.to_dict()
                validation_warnings.append(validation_warnings_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sampling_type is not UNSET:
            field_dict["samplingType"] = sampling_type
        if count is not UNSET:
            field_dict["count"] = count
        if ids is not UNSET:
            field_dict["ids"] = ids
        if validation_warnings is not UNSET:
            field_dict["validationWarnings"] = validation_warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_world_response_200_capabilities_validation_warnings_item import (
            CreateWorldResponse200CapabilitiesValidationWarningsItem,
        )

        d = dict(src_dict)
        sampling_type = d.pop("samplingType", UNSET)

        count = d.pop("count", UNSET)

        ids = cast(list[str], d.pop("ids", UNSET))

        validation_warnings = []
        _validation_warnings = d.pop("validationWarnings", UNSET)
        for validation_warnings_item_data in _validation_warnings or []:
            validation_warnings_item = CreateWorldResponse200CapabilitiesValidationWarningsItem.from_dict(
                validation_warnings_item_data
            )

            validation_warnings.append(validation_warnings_item)

        create_world_response_200_capabilities = cls(
            sampling_type=sampling_type,
            count=count,
            ids=ids,
            validation_warnings=validation_warnings,
        )

        create_world_response_200_capabilities.additional_properties = d
        return create_world_response_200_capabilities

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
