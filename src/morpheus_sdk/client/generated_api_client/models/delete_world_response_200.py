from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.delete_world_response_200_data import DeleteWorldResponse200Data
    from ..models.delete_world_response_200_meta import DeleteWorldResponse200Meta


T = TypeVar("T", bound="DeleteWorldResponse200")


@_attrs_define
class DeleteWorldResponse200:
    """
    Attributes:
        success (bool):  Example: True.
        status (int):  Example: 200.
        data (DeleteWorldResponse200Data):
        meta (DeleteWorldResponse200Meta):
    """

    success: bool
    status: int
    data: "DeleteWorldResponse200Data"
    meta: "DeleteWorldResponse200Meta"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        data = self.data.to_dict()

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
                "data": data,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.delete_world_response_200_data import DeleteWorldResponse200Data
        from ..models.delete_world_response_200_meta import DeleteWorldResponse200Meta

        d = dict(src_dict)
        success = d.pop("success")

        status = d.pop("status")

        data = DeleteWorldResponse200Data.from_dict(d.pop("data"))

        meta = DeleteWorldResponse200Meta.from_dict(d.pop("meta"))

        delete_world_response_200 = cls(
            success=success,
            status=status,
            data=data,
            meta=meta,
        )

        delete_world_response_200.additional_properties = d
        return delete_world_response_200

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
