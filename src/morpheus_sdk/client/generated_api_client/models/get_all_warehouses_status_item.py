from enum import Enum


class GetAllWarehousesStatusItem(str, Enum):
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    DISABLED = "DISABLED"

    def __str__(self) -> str:
        return str(self.value)
