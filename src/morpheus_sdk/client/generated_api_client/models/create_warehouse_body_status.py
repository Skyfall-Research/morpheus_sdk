from enum import Enum


class CreateWarehouseBodyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DISABLED = "DISABLED"

    def __str__(self) -> str:
        return str(self.value)
