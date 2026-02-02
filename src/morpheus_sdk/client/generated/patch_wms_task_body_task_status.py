from enum import Enum


class PatchWMSTaskBodyTaskStatus(str, Enum):
    ASSIGNED = "ASSIGNED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    CREATED = "CREATED"
    IN_PROGRESS = "IN_PROGRESS"
    RELEASED = "RELEASED"
    SUSPENDED = "SUSPENDED"

    def __str__(self) -> str:
        return str(self.value)
