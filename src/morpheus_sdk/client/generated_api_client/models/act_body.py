from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.act_body_body import ActBodyBody
    from ..models.act_body_params import ActBodyParams
    from ..models.act_body_query import ActBodyQuery


T = TypeVar("T", bound="ActBody")


@_attrs_define
class ActBody:
    """
    Attributes:
        path (str): Target URL path (can include params like :id) Example: /:worldId/erp/orders.
        method (Union[Unset, str]): HTTP method to use (default: GET) Example: GET.
        params (Union[Unset, ActBodyParams]): Path parameters to substitute in the path Example: {'worldId': '123'}.
        query (Union[Unset, ActBodyQuery]): Query parameters to append to the URL Example: {'status': 'open'}.
        body (Union[Unset, ActBodyBody]): Request body for POST/PUT/PATCH methods Example: {'customerId': 'abc'}.
    """

    path: str
    method: Union[Unset, str] = UNSET
    params: Union[Unset, "ActBodyParams"] = UNSET
    query: Union[Unset, "ActBodyQuery"] = UNSET
    body: Union[Unset, "ActBodyBody"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        path = self.path

        method = self.method

        params: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.params, Unset):
            params = self.params.to_dict()

        query: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "path": path,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if params is not UNSET:
            field_dict["params"] = params
        if query is not UNSET:
            field_dict["query"] = query
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.act_body_body import ActBodyBody
        from ..models.act_body_params import ActBodyParams
        from ..models.act_body_query import ActBodyQuery

        d = dict(src_dict)
        path = d.pop("path")

        method = d.pop("method", UNSET)

        _params = d.pop("params", UNSET)
        params: Union[Unset, ActBodyParams]
        if isinstance(_params, Unset):
            params = UNSET
        else:
            params = ActBodyParams.from_dict(_params)

        _query = d.pop("query", UNSET)
        query: Union[Unset, ActBodyQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = ActBodyQuery.from_dict(_query)

        _body = d.pop("body", UNSET)
        body: Union[Unset, ActBodyBody]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = ActBodyBody.from_dict(_body)

        act_body = cls(
            path=path,
            method=method,
            params=params,
            query=query,
            body=body,
        )

        act_body.additional_properties = d
        return act_body

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
