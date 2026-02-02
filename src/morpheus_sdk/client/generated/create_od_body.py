from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_od_body_data import CreateODBodyData
    from ..models.create_od_body_schedule import CreateODBodySchedule


T = TypeVar("T", bound="CreateODBody")


@_attrs_define
class CreateODBody:
    """
    Attributes:
        data (CreateODBodyData): The Operational Descriptor definition Example: {'id': 'edi-process-850', 'name': 'EDI
            850 Processing', 'version': '1.0.0', 'type': 'workflow', 'steps': [{'id': 'validate', 'name': 'Validate EDI',
            'type': 'mcp', 'service': 'edi-validator', 'tool': 'validate_document', 'input': {'type': 'literal', 'value':
            {'docType': '850'}}}]}.
        schedule (Union[Unset, CreateODBodySchedule]): Optional scheduling configuration
    """

    data: "CreateODBodyData"
    schedule: Union[Unset, "CreateODBodySchedule"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        schedule: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if schedule is not UNSET:
            field_dict["schedule"] = schedule

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_od_body_data import CreateODBodyData
        from ..models.create_od_body_schedule import CreateODBodySchedule

        d = dict(src_dict)
        data = CreateODBodyData.from_dict(d.pop("data"))

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, CreateODBodySchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = CreateODBodySchedule.from_dict(_schedule)

        create_od_body = cls(
            data=data,
            schedule=schedule,
        )

        create_od_body.additional_properties = d
        return create_od_body

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
