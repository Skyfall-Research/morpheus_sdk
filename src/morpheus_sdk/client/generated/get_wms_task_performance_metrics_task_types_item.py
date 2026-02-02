from enum import Enum


class GetWMSTaskPerformanceMetricsTaskTypesItem(str, Enum):
    CYCLE_COUNT = "CYCLE_COUNT"
    LOAD = "LOAD"
    MOVE = "MOVE"
    PACK = "PACK"
    PICK = "PICK"
    PUTAWAY = "PUTAWAY"
    REPLENISHMENT = "REPLENISHMENT"
    SORT = "SORT"
    UNLOAD = "UNLOAD"

    def __str__(self) -> str:
        return str(self.value)
