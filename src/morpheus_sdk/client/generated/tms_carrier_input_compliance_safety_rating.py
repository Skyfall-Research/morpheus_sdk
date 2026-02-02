from enum import Enum


class TMSCarrierInputComplianceSafetyRating(str, Enum):
    CONDITIONAL = "CONDITIONAL"
    NOT_RATED = "NOT_RATED"
    SATISFACTORY = "SATISFACTORY"
    UNSATISFACTORY = "UNSATISFACTORY"

    def __str__(self) -> str:
        return str(self.value)
