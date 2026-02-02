from enum import Enum


class PatchWMSInboundOrderBodyPriority(str, Enum):
    NORMAL = "NORMAL"
    RUSH = "RUSH"
    STANDARD = "STANDARD"
    URGENT = "URGENT"

    def __str__(self) -> str:
        return str(self.value)
