from enum import Enum


class ERPOrderPoType(str, Enum):
    BLANKET = "BLANKET"
    CONTRACT = "CONTRACT"
    DROP_SHIP = "DROP_SHIP"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
