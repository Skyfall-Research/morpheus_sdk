from enum import Enum


class BulkScheduleODsBodySchedulesItemType(str, Enum):
    ONCE = "once"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
