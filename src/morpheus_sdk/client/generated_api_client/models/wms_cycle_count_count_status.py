from enum import Enum


class WMSCycleCountCountStatus(str, Enum):
    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    REJECTED = "REJECTED"
    SCHEDULED = "SCHEDULED"

    def __str__(self) -> str:
        return str(self.value)
