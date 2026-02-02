from enum import Enum


class UpdateERPInvoiceStatusBodyStatus(str, Enum):
    DRAFT = "DRAFT"
    PAID = "PAID"
    PARTIALLY_PAID = "PARTIALLY_PAID"
    REJECTED = "REJECTED"
    SENT = "SENT"
    VALIDATED = "VALIDATED"

    def __str__(self) -> str:
        return str(self.value)
