from enum import Enum


class GetAllFinanceTransactionsSourceType(str, Enum):
    BILL = "bill"
    INTEREST = "interest"
    INVOICE = "invoice"
    MANUAL = "manual"
    PAYMENT = "payment"

    def __str__(self) -> str:
        return str(self.value)
