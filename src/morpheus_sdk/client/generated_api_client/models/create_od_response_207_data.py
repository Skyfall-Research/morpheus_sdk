from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_od_response_207_data_od import CreateODResponse207DataOd


T = TypeVar("T", bound="CreateODResponse207Data")


@_attrs_define
class CreateODResponse207Data:
    """
    Attributes:
        od (Union[Unset, CreateODResponse207DataOd]):
        schedule_error (Union[Unset, str]):
        message (Union[Unset, str]):
    """

    od: Union[Unset, "CreateODResponse207DataOd"] = UNSET
    schedule_error: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        od: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.od, Unset):
            od = self.od.to_dict()

        schedule_error = self.schedule_error

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if od is not UNSET:
            field_dict["od"] = od
        if schedule_error is not UNSET:
            field_dict["scheduleError"] = schedule_error
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_od_response_207_data_od import CreateODResponse207DataOd

        d = dict(src_dict)
        _od = d.pop("od", UNSET)
        od: Union[Unset, CreateODResponse207DataOd]
        if isinstance(_od, Unset):
            od = UNSET
        else:
            od = CreateODResponse207DataOd.from_dict(_od)

        schedule_error = d.pop("scheduleError", UNSET)

        message = d.pop("message", UNSET)

        create_od_response_207_data = cls(
            od=od,
            schedule_error=schedule_error,
            message=message,
        )

        create_od_response_207_data.additional_properties = d
        return create_od_response_207_data

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
