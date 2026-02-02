from enum import Enum


class WMSTaskDetailsItemDetailStatus(str, Enum):
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    PENDING = "PENDING"
    SHORT = "SHORT"
    SKIPPED = "SKIPPED"

    def __str__(self) -> str:
        return str(self.value)
