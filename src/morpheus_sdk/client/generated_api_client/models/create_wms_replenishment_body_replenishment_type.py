from enum import Enum


class CreateWMSReplenishmentBodyReplenishmentType(str, Enum):
    CYCLE = "CYCLE"
    DEMAND = "DEMAND"
    MANUAL = "MANUAL"
    MIN_MAX = "MIN_MAX"

    def __str__(self) -> str:
        return str(self.value)
