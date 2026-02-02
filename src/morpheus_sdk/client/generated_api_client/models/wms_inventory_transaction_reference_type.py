from enum import Enum


class WMSInventoryTransactionReferenceType(str, Enum):
    CYCLE_COUNT = "CYCLE_COUNT"
    ORDER = "ORDER"
    PO = "PO"
    TASK = "TASK"

    def __str__(self) -> str:
        return str(self.value)
