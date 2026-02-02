from enum import Enum


class GetAllERPPaymentsStatus(str, Enum):
    APPLIED = "APPLIED"
    RECEIVED = "RECEIVED"
    REVERSAL = "REVERSAL"
    UNMATCHED = "UNMATCHED"

    def __str__(self) -> str:
        return str(self.value)
