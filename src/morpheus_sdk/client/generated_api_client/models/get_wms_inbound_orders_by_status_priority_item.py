from enum import Enum


class GetWMSInboundOrdersByStatusPriorityItem(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    NORMAL = "NORMAL"
    URGENT = "URGENT"

    def __str__(self) -> str:
        return str(self.value)
