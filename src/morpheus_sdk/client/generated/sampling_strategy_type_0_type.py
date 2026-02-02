from enum import Enum


class SamplingStrategyType0Type(str, Enum):
    ALL = "all"

    def __str__(self) -> str:
        return str(self.value)
