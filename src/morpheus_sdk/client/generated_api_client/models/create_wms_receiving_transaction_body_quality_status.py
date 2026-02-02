from enum import Enum


class CreateWMSReceivingTransactionBodyQualityStatus(str, Enum):
    FAIL = "FAIL"
    PASS = "PASS"
    PENDING = "PENDING"

    def __str__(self) -> str:
        return str(self.value)
