from enum import Enum


class CreateWMSBinBodyBinType(str, Enum):
    CASE_FLOW = "CASE_FLOW"
    FLOOR = "FLOOR"
    PALLET = "PALLET"
    PICK_FACE = "PICK_FACE"
    RESERVE = "RESERVE"
    SHELF = "SHELF"

    def __str__(self) -> str:
        return str(self.value)
