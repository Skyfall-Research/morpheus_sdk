from enum import Enum


class SamplingStrategyType3Type(str, Enum):
    SEEDED = "seeded"

    def __str__(self) -> str:
        return str(self.value)
