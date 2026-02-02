from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.invariant_check_result_actual_type_0 import InvariantCheckResultActualType0
    from ..models.invariant_check_result_expected_type_0 import InvariantCheckResultExpectedType0


T = TypeVar("T", bound="InvariantCheckResult")


@_attrs_define
class InvariantCheckResult:
    """Result of an invariant check

    Attributes:
        invariant_id (str): Unique identifier for the invariant Example: INV_001.
        description (str): Description of the invariant Example: Shipment must belong to the correct warehouse.
        passed (bool): Whether the check passed Example: True.
        actual (Union['InvariantCheckResultActualType0', None, Unset]): Actual value found
        expected (Union['InvariantCheckResultExpectedType0', None, Unset]): Expected value
        error (Union[None, Unset, str]): Error message if applicable Example: Mismatch in warehouse ID.
    """

    invariant_id: str
    description: str
    passed: bool
    actual: Union["InvariantCheckResultActualType0", None, Unset] = UNSET
    expected: Union["InvariantCheckResultExpectedType0", None, Unset] = UNSET
    error: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.invariant_check_result_actual_type_0 import InvariantCheckResultActualType0
        from ..models.invariant_check_result_expected_type_0 import InvariantCheckResultExpectedType0

        invariant_id = self.invariant_id

        description = self.description

        passed = self.passed

        actual: Union[None, Unset, dict[str, Any]]
        if isinstance(self.actual, Unset):
            actual = UNSET
        elif isinstance(self.actual, InvariantCheckResultActualType0):
            actual = self.actual.to_dict()
        else:
            actual = self.actual

        expected: Union[None, Unset, dict[str, Any]]
        if isinstance(self.expected, Unset):
            expected = UNSET
        elif isinstance(self.expected, InvariantCheckResultExpectedType0):
            expected = self.expected.to_dict()
        else:
            expected = self.expected

        error: Union[None, Unset, str]
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "invariantId": invariant_id,
                "description": description,
                "passed": passed,
            }
        )
        if actual is not UNSET:
            field_dict["actual"] = actual
        if expected is not UNSET:
            field_dict["expected"] = expected
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.invariant_check_result_actual_type_0 import InvariantCheckResultActualType0
        from ..models.invariant_check_result_expected_type_0 import InvariantCheckResultExpectedType0

        d = dict(src_dict)
        invariant_id = d.pop("invariantId")

        description = d.pop("description")

        passed = d.pop("passed")

        def _parse_actual(data: object) -> Union["InvariantCheckResultActualType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actual_type_0 = InvariantCheckResultActualType0.from_dict(data)

                return actual_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InvariantCheckResultActualType0", None, Unset], data)

        actual = _parse_actual(d.pop("actual", UNSET))

        def _parse_expected(data: object) -> Union["InvariantCheckResultExpectedType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                expected_type_0 = InvariantCheckResultExpectedType0.from_dict(data)

                return expected_type_0
            except:  # noqa: E722
                pass
            return cast(Union["InvariantCheckResultExpectedType0", None, Unset], data)

        expected = _parse_expected(d.pop("expected", UNSET))

        def _parse_error(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        error = _parse_error(d.pop("error", UNSET))

        invariant_check_result = cls(
            invariant_id=invariant_id,
            description=description,
            passed=passed,
            actual=actual,
            expected=expected,
            error=error,
        )

        invariant_check_result.additional_properties = d
        return invariant_check_result

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
