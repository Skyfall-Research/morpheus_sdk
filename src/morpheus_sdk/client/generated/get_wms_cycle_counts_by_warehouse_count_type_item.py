from enum import Enum


class GetWMSCycleCountsByWarehouseCountTypeItem(str, Enum):
    ABC = "ABC"
    BLIND = "BLIND"
    DAILY = "DAILY"
    FULL = "FULL"
    MONTHLY = "MONTHLY"
    SPOT = "SPOT"
    WEEKLY = "WEEKLY"

    def __str__(self) -> str:
        return str(self.value)
