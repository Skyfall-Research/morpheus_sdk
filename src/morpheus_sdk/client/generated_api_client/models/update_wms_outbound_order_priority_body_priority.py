from enum import Enum


class UpdateWMSOutboundOrderPriorityBodyPriority(str, Enum):
    NORMAL = "NORMAL"
    RUSH = "RUSH"
    STANDARD = "STANDARD"
    URGENT = "URGENT"

    def __str__(self) -> str:
        return str(self.value)
