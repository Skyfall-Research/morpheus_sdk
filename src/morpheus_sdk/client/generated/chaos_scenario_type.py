from enum import Enum


class ChaosScenarioType(str, Enum):
    DATA_CORRUPTION = "data_corruption"
    DEPENDENCY_FAILURE = "dependency_failure"
    DUPLICATE_DATA = "duplicate_data"
    FORMAT_CHANGE = "format_change"
    INVALID_STATE = "invalid_state"
    MISSING_DATA = "missing_data"
    PARTIAL_DATA = "partial_data"
    PERMISSION_DENIED = "permission_denied"
    RATE_LIMIT = "rate_limit"
    STALE_DATA = "stale_data"
    TIMING_ISSUE = "timing_issue"

    def __str__(self) -> str:
        return str(self.value)
