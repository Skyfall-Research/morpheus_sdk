from enum import Enum


class BulkInsertFinanceTransactionsBodyTransactionsItemType(str, Enum):
    PAYMENT_IN = "payment_in"
    PAYMENT_OUT = "payment_out"

    def __str__(self) -> str:
        return str(self.value)
