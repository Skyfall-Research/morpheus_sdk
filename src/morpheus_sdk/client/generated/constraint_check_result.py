from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constraint_check_result_details_type_0 import ConstraintCheckResultDetailsType0


T = TypeVar("T", bound="ConstraintCheckResult")


@_attrs_define
class ConstraintCheckResult:
    """Result of a constraint check

    Attributes:
        constraint_id (str): Unique identifier for the constraint Example: CONST_001.
        description (str): Description of the constraint Example: Total weight must not exceed limit.
        passed (bool): Whether the check passed Example: True.
        details (Union['ConstraintCheckResultDetailsType0', None, Unset]): Additional details about the check
    """

    constraint_id: str
    description: str
    passed: bool
    details: Union["ConstraintCheckResultDetailsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.constraint_check_result_details_type_0 import ConstraintCheckResultDetailsType0

        constraint_id = self.constraint_id

        description = self.description

        passed = self.passed

        details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.details, Unset):
            details = UNSET
        elif isinstance(self.details, ConstraintCheckResultDetailsType0):
            details = self.details.to_dict()
        else:
            details = self.details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "constraintId": constraint_id,
                "description": description,
                "passed": passed,
            }
        )
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraint_check_result_details_type_0 import ConstraintCheckResultDetailsType0

        d = dict(src_dict)
        constraint_id = d.pop("constraintId")

        description = d.pop("description")

        passed = d.pop("passed")

        def _parse_details(data: object) -> Union["ConstraintCheckResultDetailsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                details_type_0 = ConstraintCheckResultDetailsType0.from_dict(data)

                return details_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ConstraintCheckResultDetailsType0", None, Unset], data)

        details = _parse_details(d.pop("details", UNSET))

        constraint_check_result = cls(
            constraint_id=constraint_id,
            description=description,
            passed=passed,
            details=details,
        )

        constraint_check_result.additional_properties = d
        return constraint_check_result

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
