from enum import Enum


class CreateODBodyScheduleType(str, Enum):
    ONCE = "once"
    RECURRING = "recurring"

    def __str__(self) -> str:
        return str(self.value)
