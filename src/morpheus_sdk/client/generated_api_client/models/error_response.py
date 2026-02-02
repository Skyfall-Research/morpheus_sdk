from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.error_response_meta import ErrorResponseMeta


T = TypeVar("T", bound="ErrorResponse")


@_attrs_define
class ErrorResponse:
    """Standard error response format

    Attributes:
        success (bool): Always false for error responses
        status (int): HTTP status code Example: 400.
        error (str): Human-readable error message Example: worldId is required.
        meta (ErrorResponseMeta):
    """

    success: bool
    status: int
    error: str
    meta: "ErrorResponseMeta"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        status = self.status

        error = self.error

        meta = self.meta.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
                "status": status,
                "error": error,
                "meta": meta,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_response_meta import ErrorResponseMeta

        d = dict(src_dict)
        success = d.pop("success")

        status = d.pop("status")

        error = d.pop("error")

        meta = ErrorResponseMeta.from_dict(d.pop("meta"))

        error_response = cls(
            success=success,
            status=status,
            error=error,
            meta=meta,
        )

        error_response.additional_properties = d
        return error_response

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
