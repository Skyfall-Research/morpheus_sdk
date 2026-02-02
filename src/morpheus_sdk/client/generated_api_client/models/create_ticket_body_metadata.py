from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_ticket_body_metadata_context_snapshots_item import CreateTicketBodyMetadataContextSnapshotsItem


T = TypeVar("T", bound="CreateTicketBodyMetadata")


@_attrs_define
class CreateTicketBodyMetadata:
    """Additional context and system metadata

    Attributes:
        od_id (Union[Unset, str]):
        od_name (Union[Unset, str]):
        run_id (Union[Unset, str]):
        failed_step_id (Union[Unset, str]):
        failure_type (Union[Unset, str]):
        context_snapshots (Union[Unset, list['CreateTicketBodyMetadataContextSnapshotsItem']]):
    """

    od_id: Union[Unset, str] = UNSET
    od_name: Union[Unset, str] = UNSET
    run_id: Union[Unset, str] = UNSET
    failed_step_id: Union[Unset, str] = UNSET
    failure_type: Union[Unset, str] = UNSET
    context_snapshots: Union[Unset, list["CreateTicketBodyMetadataContextSnapshotsItem"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        od_id = self.od_id

        od_name = self.od_name

        run_id = self.run_id

        failed_step_id = self.failed_step_id

        failure_type = self.failure_type

        context_snapshots: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.context_snapshots, Unset):
            context_snapshots = []
            for context_snapshots_item_data in self.context_snapshots:
                context_snapshots_item = context_snapshots_item_data.to_dict()
                context_snapshots.append(context_snapshots_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if od_id is not UNSET:
            field_dict["odId"] = od_id
        if od_name is not UNSET:
            field_dict["odName"] = od_name
        if run_id is not UNSET:
            field_dict["runId"] = run_id
        if failed_step_id is not UNSET:
            field_dict["failedStepId"] = failed_step_id
        if failure_type is not UNSET:
            field_dict["failureType"] = failure_type
        if context_snapshots is not UNSET:
            field_dict["contextSnapshots"] = context_snapshots

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_ticket_body_metadata_context_snapshots_item import (
            CreateTicketBodyMetadataContextSnapshotsItem,
        )

        d = dict(src_dict)
        od_id = d.pop("odId", UNSET)

        od_name = d.pop("odName", UNSET)

        run_id = d.pop("runId", UNSET)

        failed_step_id = d.pop("failedStepId", UNSET)

        failure_type = d.pop("failureType", UNSET)

        context_snapshots = []
        _context_snapshots = d.pop("contextSnapshots", UNSET)
        for context_snapshots_item_data in _context_snapshots or []:
            context_snapshots_item = CreateTicketBodyMetadataContextSnapshotsItem.from_dict(context_snapshots_item_data)

            context_snapshots.append(context_snapshots_item)

        create_ticket_body_metadata = cls(
            od_id=od_id,
            od_name=od_name,
            run_id=run_id,
            failed_step_id=failed_step_id,
            failure_type=failure_type,
            context_snapshots=context_snapshots,
        )

        create_ticket_body_metadata.additional_properties = d
        return create_ticket_body_metadata

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
