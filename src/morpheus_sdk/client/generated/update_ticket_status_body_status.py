from enum import Enum


class UpdateTicketStatusBodyStatus(str, Enum):
    CLOSED = "closed"
    IN_PROGRESS = "in_progress"
    NEW = "new"
    ON_HOLD = "on_hold"
    OPEN = "open"
    RESOLVED = "resolved"

    def __str__(self) -> str:
        return str(self.value)
