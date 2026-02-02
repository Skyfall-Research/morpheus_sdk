from enum import Enum


class GetAllWMSReceivingTransactionsStatusItem(str, Enum):
    COMPLETED = "COMPLETED"
    PUTAWAY_PENDING = "PUTAWAY_PENDING"
    QC_HOLD = "QC_HOLD"
    RECEIVED = "RECEIVED"
    REJECTED = "REJECTED"

    def __str__(self) -> str:
        return str(self.value)
