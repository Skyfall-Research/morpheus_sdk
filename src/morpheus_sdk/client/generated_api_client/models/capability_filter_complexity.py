from enum import Enum


class CapabilityFilterComplexity(str, Enum):
    COMPLEX = "complex"
    MEDIUM = "medium"
    SIMPLE = "simple"

    def __str__(self) -> str:
        return str(self.value)
