from enum import Enum


class CreateWMSCycleCountBodyAssignmentsItemStatus(str, Enum):
    ASSIGNED = "ASSIGNED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"

    def __str__(self) -> str:
        return str(self.value)
