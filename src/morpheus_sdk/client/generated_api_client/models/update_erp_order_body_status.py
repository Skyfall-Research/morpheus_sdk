from enum import Enum


class UpdateERPOrderBodyStatus(str, Enum):
    ACKED = "ACKED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    PARTIALLY_SHIPPED = "PARTIALLY_SHIPPED"
    RECEIVED = "RECEIVED"

    def __str__(self) -> str:
        return str(self.value)
