from enum import Enum


class GetWMSInventoryMovementReportTransactionTypeItem(str, Enum):
    ADJUST = "ADJUST"
    CYCLE_COUNT = "CYCLE_COUNT"
    DAMAGE = "DAMAGE"
    MOVE = "MOVE"
    PICK = "PICK"
    PUTAWAY = "PUTAWAY"
    RECEIVE = "RECEIVE"
    RETURN = "RETURN"
    SHIP = "SHIP"

    def __str__(self) -> str:
        return str(self.value)
