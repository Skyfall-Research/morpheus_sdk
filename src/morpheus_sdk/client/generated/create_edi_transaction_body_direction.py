from enum import Enum


class CreateEdiTransactionBodyDirection(str, Enum):
    INBOUND = "INBOUND"
    OUTBOUND = "OUTBOUND"

    def __str__(self) -> str:
        return str(self.value)
