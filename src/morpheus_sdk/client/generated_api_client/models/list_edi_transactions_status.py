from enum import Enum


class ListEdiTransactionsStatus(str, Enum):
    ARCHIVED = "ARCHIVED"
    DELIVERED = "DELIVERED"
    ERRORED = "ERRORED"
    PROCESSING = "PROCESSING"
    QUEUED = "QUEUED"
    RECEIVED = "RECEIVED"

    def __str__(self) -> str:
        return str(self.value)
