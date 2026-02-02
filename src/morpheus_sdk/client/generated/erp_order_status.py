from enum import Enum


class ERPOrderStatus(str, Enum):
    ACKED = "ACKED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    MANUFACTURING_COMPLETE = "MANUFACTURING_COMPLETE"
    MATERIALS_PICKED = "MATERIALS_PICKED"
    PARTIALLY_SHIPPED = "PARTIALLY_SHIPPED"
    RECEIVED = "RECEIVED"

    def __str__(self) -> str:
        return str(self.value)
