from enum import Enum


class CreateERPPaymentBodyMethod(str, Enum):
    ACH = "ACH"
    CHECK = "CHECK"
    CREDIT_CARD = "CREDIT_CARD"
    OTHER = "OTHER"
    WIRE = "WIRE"

    def __str__(self) -> str:
        return str(self.value)
