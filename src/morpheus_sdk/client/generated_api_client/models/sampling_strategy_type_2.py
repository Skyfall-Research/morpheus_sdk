from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sampling_strategy_type_2_type import SamplingStrategyType2Type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SamplingStrategyType2")


@_attrs_define
class SamplingStrategyType2:
    """
    Attributes:
        type_ (SamplingStrategyType2Type): Randomly select a number of capabilities
        count (int): Number of capabilities to randomly select Example: 10.
        seed (Union[Unset, int]): Optional seed for reproducible random selection
    """

    type_: SamplingStrategyType2Type
    count: int
    seed: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        count = self.count

        seed = self.seed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "count": count,
            }
        )
        if seed is not UNSET:
            field_dict["seed"] = seed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = SamplingStrategyType2Type(d.pop("type"))

        count = d.pop("count")

        seed = d.pop("seed", UNSET)

        sampling_strategy_type_2 = cls(
            type_=type_,
            count=count,
            seed=seed,
        )

        sampling_strategy_type_2.additional_properties = d
        return sampling_strategy_type_2

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
