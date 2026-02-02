from enum import Enum


class UpdateERPProductBodyStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISCONTINUED = "DISCONTINUED"

    def __str__(self) -> str:
        return str(self.value)
