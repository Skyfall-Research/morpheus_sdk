from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.world import World


T = TypeVar("T", bound="ListWorldsResponse200Data")


@_attrs_define
class ListWorldsResponse200Data:
    """
    Attributes:
        worlds (list['World']): Array of world objects
        next_cursor (Union[None, Unset, str]): Cursor for next page of results Example: 507f1f77bcf86cd799439012.
    """

    worlds: list["World"]
    next_cursor: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        worlds = []
        for worlds_item_data in self.worlds:
            worlds_item = worlds_item_data.to_dict()
            worlds.append(worlds_item)

        next_cursor: Union[None, Unset, str]
        if isinstance(self.next_cursor, Unset):
            next_cursor = UNSET
        else:
            next_cursor = self.next_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "worlds": worlds,
            }
        )
        if next_cursor is not UNSET:
            field_dict["nextCursor"] = next_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.world import World

        d = dict(src_dict)
        worlds = []
        _worlds = d.pop("worlds")
        for worlds_item_data in _worlds:
            worlds_item = World.from_dict(worlds_item_data)

            worlds.append(worlds_item)

        def _parse_next_cursor(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_cursor = _parse_next_cursor(d.pop("nextCursor", UNSET))

        list_worlds_response_200_data = cls(
            worlds=worlds,
            next_cursor=next_cursor,
        )

        list_worlds_response_200_data.additional_properties = d
        return list_worlds_response_200_data

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
