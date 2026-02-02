from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sampling_strategy_type_1_type import SamplingStrategyType1Type

if TYPE_CHECKING:
    from ..models.capability_filter import CapabilityFilter


T = TypeVar("T", bound="SamplingStrategyType1")


@_attrs_define
class SamplingStrategyType1:
    """
    Attributes:
        type_ (SamplingStrategyType1Type): Filter capabilities by criteria
        filter_ (CapabilityFilter): Filter criteria for capability sampling
    """

    type_: SamplingStrategyType1Type
    filter_: "CapabilityFilter"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        filter_ = self.filter_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "filter": filter_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.capability_filter import CapabilityFilter

        d = dict(src_dict)
        type_ = SamplingStrategyType1Type(d.pop("type"))

        filter_ = CapabilityFilter.from_dict(d.pop("filter"))

        sampling_strategy_type_1 = cls(
            type_=type_,
            filter_=filter_,
        )

        sampling_strategy_type_1.additional_properties = d
        return sampling_strategy_type_1

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
