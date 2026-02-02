from enum import Enum


class SamplingStrategyType2Type(str, Enum):
    RANDOM = "random"

    def __str__(self) -> str:
        return str(self.value)
