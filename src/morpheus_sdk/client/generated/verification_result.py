import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constraint_check_result import ConstraintCheckResult
    from ..models.entity_state_check_result import EntityStateCheckResult
    from ..models.invariant_check_result import InvariantCheckResult
    from ..models.verification_result_failure_details_type_0 import VerificationResultFailureDetailsType0


T = TypeVar("T", bound="VerificationResult")


@_attrs_define
class VerificationResult:
    """Comprehensive result of the verification process

    Attributes:
        passed (bool): Overall pass/fail status of the verification
        ticket_id (str): ID of the ticket being verified Example: 507f1f77bcf86cd799439011.
        world_id (UUID): ID of the world where verification ran Example: 550e8400-e29b-41d4-a716-446655440000.
        timestamp (datetime.datetime): When the verification was performed Example: 2024-01-15T10:30:00.000Z.
        total_checks (int): Total number of checks performed Example: 10.
        passed_checks (int): Number of passed checks Example: 8.
        failed_checks (int): Number of failed checks Example: 2.
        verification_duration_ms (float): Duration of verification in milliseconds Example: 150.5.
        invariant_checks (Union[Unset, list['InvariantCheckResult']]): Results of invariant checks
        entity_state_checks (Union[Unset, list['EntityStateCheckResult']]): Results of entity state checks
        constraint_checks (Union[Unset, list['ConstraintCheckResult']]): Results of constraint checks
        failure_reason (Union[None, Unset, str]): High-level reason for failure if applicable Example: Entity state
            mismatch.
        failure_details (Union['VerificationResultFailureDetailsType0', None, Unset]): Detailed failure information
    """

    passed: bool
    ticket_id: str
    world_id: UUID
    timestamp: datetime.datetime
    total_checks: int
    passed_checks: int
    failed_checks: int
    verification_duration_ms: float
    invariant_checks: Union[Unset, list["InvariantCheckResult"]] = UNSET
    entity_state_checks: Union[Unset, list["EntityStateCheckResult"]] = UNSET
    constraint_checks: Union[Unset, list["ConstraintCheckResult"]] = UNSET
    failure_reason: Union[None, Unset, str] = UNSET
    failure_details: Union["VerificationResultFailureDetailsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.verification_result_failure_details_type_0 import VerificationResultFailureDetailsType0

        passed = self.passed

        ticket_id = self.ticket_id

        world_id = str(self.world_id)

        timestamp = self.timestamp.isoformat()

        total_checks = self.total_checks

        passed_checks = self.passed_checks

        failed_checks = self.failed_checks

        verification_duration_ms = self.verification_duration_ms

        invariant_checks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.invariant_checks, Unset):
            invariant_checks = []
            for invariant_checks_item_data in self.invariant_checks:
                invariant_checks_item = invariant_checks_item_data.to_dict()
                invariant_checks.append(invariant_checks_item)

        entity_state_checks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.entity_state_checks, Unset):
            entity_state_checks = []
            for entity_state_checks_item_data in self.entity_state_checks:
                entity_state_checks_item = entity_state_checks_item_data.to_dict()
                entity_state_checks.append(entity_state_checks_item)

        constraint_checks: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.constraint_checks, Unset):
            constraint_checks = []
            for constraint_checks_item_data in self.constraint_checks:
                constraint_checks_item = constraint_checks_item_data.to_dict()
                constraint_checks.append(constraint_checks_item)

        failure_reason: Union[None, Unset, str]
        if isinstance(self.failure_reason, Unset):
            failure_reason = UNSET
        else:
            failure_reason = self.failure_reason

        failure_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.failure_details, Unset):
            failure_details = UNSET
        elif isinstance(self.failure_details, VerificationResultFailureDetailsType0):
            failure_details = self.failure_details.to_dict()
        else:
            failure_details = self.failure_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "passed": passed,
                "ticketId": ticket_id,
                "worldId": world_id,
                "timestamp": timestamp,
                "totalChecks": total_checks,
                "passedChecks": passed_checks,
                "failedChecks": failed_checks,
                "verificationDurationMs": verification_duration_ms,
            }
        )
        if invariant_checks is not UNSET:
            field_dict["invariantChecks"] = invariant_checks
        if entity_state_checks is not UNSET:
            field_dict["entityStateChecks"] = entity_state_checks
        if constraint_checks is not UNSET:
            field_dict["constraintChecks"] = constraint_checks
        if failure_reason is not UNSET:
            field_dict["failureReason"] = failure_reason
        if failure_details is not UNSET:
            field_dict["failureDetails"] = failure_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constraint_check_result import ConstraintCheckResult
        from ..models.entity_state_check_result import EntityStateCheckResult
        from ..models.invariant_check_result import InvariantCheckResult
        from ..models.verification_result_failure_details_type_0 import VerificationResultFailureDetailsType0

        d = dict(src_dict)
        passed = d.pop("passed")

        ticket_id = d.pop("ticketId")

        world_id = UUID(d.pop("worldId"))

        timestamp = isoparse(d.pop("timestamp"))

        total_checks = d.pop("totalChecks")

        passed_checks = d.pop("passedChecks")

        failed_checks = d.pop("failedChecks")

        verification_duration_ms = d.pop("verificationDurationMs")

        invariant_checks = []
        _invariant_checks = d.pop("invariantChecks", UNSET)
        for invariant_checks_item_data in _invariant_checks or []:
            invariant_checks_item = InvariantCheckResult.from_dict(invariant_checks_item_data)

            invariant_checks.append(invariant_checks_item)

        entity_state_checks = []
        _entity_state_checks = d.pop("entityStateChecks", UNSET)
        for entity_state_checks_item_data in _entity_state_checks or []:
            entity_state_checks_item = EntityStateCheckResult.from_dict(entity_state_checks_item_data)

            entity_state_checks.append(entity_state_checks_item)

        constraint_checks = []
        _constraint_checks = d.pop("constraintChecks", UNSET)
        for constraint_checks_item_data in _constraint_checks or []:
            constraint_checks_item = ConstraintCheckResult.from_dict(constraint_checks_item_data)

            constraint_checks.append(constraint_checks_item)

        def _parse_failure_reason(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        failure_reason = _parse_failure_reason(d.pop("failureReason", UNSET))

        def _parse_failure_details(data: object) -> Union["VerificationResultFailureDetailsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_details_type_0 = VerificationResultFailureDetailsType0.from_dict(data)

                return failure_details_type_0
            except:  # noqa: E722
                pass
            return cast(Union["VerificationResultFailureDetailsType0", None, Unset], data)

        failure_details = _parse_failure_details(d.pop("failureDetails", UNSET))

        verification_result = cls(
            passed=passed,
            ticket_id=ticket_id,
            world_id=world_id,
            timestamp=timestamp,
            total_checks=total_checks,
            passed_checks=passed_checks,
            failed_checks=failed_checks,
            verification_duration_ms=verification_duration_ms,
            invariant_checks=invariant_checks,
            entity_state_checks=entity_state_checks,
            constraint_checks=constraint_checks,
            failure_reason=failure_reason,
            failure_details=failure_details,
        )

        verification_result.additional_properties = d
        return verification_result

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
