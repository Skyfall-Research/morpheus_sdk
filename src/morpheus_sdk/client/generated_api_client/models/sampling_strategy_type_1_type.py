from enum import Enum


class SamplingStrategyType1Type(str, Enum):
    FILTER = "filter"

    def __str__(self) -> str:
        return str(self.value)
