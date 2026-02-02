from enum import Enum


class ERPInvoiceInvoiceType(str, Enum):
    CORRECTION = "CORRECTION"
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"
    STANDARD = "STANDARD"

    def __str__(self) -> str:
        return str(self.value)
