from enum import Enum


class PaymentAllocationAllocationMethod(str, Enum):
    AUTOMATIC = "AUTOMATIC"
    FIFO = "FIFO"
    LIFO = "LIFO"
    MANUAL = "MANUAL"

    def __str__(self) -> str:
        return str(self.value)
