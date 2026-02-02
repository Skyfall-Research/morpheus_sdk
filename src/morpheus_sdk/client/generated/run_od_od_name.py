from enum import Enum


class RunOdOdName(str, Enum):
    SIMPLE_EDI = "simple-edi"
    SIMPLE_WMS = "simple-wms"

    def __str__(self) -> str:
        return str(self.value)
