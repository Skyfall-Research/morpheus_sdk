from enum import Enum


class VerifyEntityBodyEntityType(str, Enum):
    INVENTORY = "INVENTORY"
    ORDER = "ORDER"
    SHIPMENT = "SHIPMENT"
    TASK = "TASK"
    WAVE = "WAVE"

    def __str__(self) -> str:
        return str(self.value)
