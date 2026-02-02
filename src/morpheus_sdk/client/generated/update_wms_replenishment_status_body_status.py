from enum import Enum


class UpdateWMSReplenishmentStatusBodyStatus(str, Enum):
    APPROVED = "APPROVED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    SUGGESTED = "SUGGESTED"
    TASK_CREATED = "TASK_CREATED"

    def __str__(self) -> str:
        return str(self.value)
