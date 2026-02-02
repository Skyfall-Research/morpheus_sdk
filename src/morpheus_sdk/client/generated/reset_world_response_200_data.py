from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reset_world_response_200_data_seed_result import ResetWorldResponse200DataSeedResult


T = TypeVar("T", bound="ResetWorldResponse200Data")


@_attrs_define
class ResetWorldResponse200Data:
    """
    Attributes:
        success (Union[Unset, bool]):  Example: True.
        message (Union[Unset, str]):  Example: World reset and re-seeded.
        seed_result (Union[Unset, ResetWorldResponse200DataSeedResult]): Result of the re-seeding process
    """

    success: Union[Unset, bool] = UNSET
    message: Union[Unset, str] = UNSET
    seed_result: Union[Unset, "ResetWorldResponse200DataSeedResult"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        seed_result: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.seed_result, Unset):
            seed_result = self.seed_result.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if success is not UNSET:
            field_dict["success"] = success
        if message is not UNSET:
            field_dict["message"] = message
        if seed_result is not UNSET:
            field_dict["seedResult"] = seed_result

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reset_world_response_200_data_seed_result import ResetWorldResponse200DataSeedResult

        d = dict(src_dict)
        success = d.pop("success", UNSET)

        message = d.pop("message", UNSET)

        _seed_result = d.pop("seedResult", UNSET)
        seed_result: Union[Unset, ResetWorldResponse200DataSeedResult]
        if isinstance(_seed_result, Unset):
            seed_result = UNSET
        else:
            seed_result = ResetWorldResponse200DataSeedResult.from_dict(_seed_result)

        reset_world_response_200_data = cls(
            success=success,
            message=message,
            seed_result=seed_result,
        )

        reset_world_response_200_data.additional_properties = d
        return reset_world_response_200_data

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
