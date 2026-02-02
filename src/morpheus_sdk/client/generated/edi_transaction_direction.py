from enum import Enum


class EdiTransactionDirection(str, Enum):
    IN = "IN"
    OUT = "OUT"

    def __str__(self) -> str:
        return str(self.value)
