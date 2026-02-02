from enum import Enum


class WMSInboundOrderLinesItemLineStatus(str, Enum):
    CLOSED = "CLOSED"
    EXPECTED = "EXPECTED"
    RECEIVED = "RECEIVED"
    RECEIVING = "RECEIVING"

    def __str__(self) -> str:
        return str(self.value)
