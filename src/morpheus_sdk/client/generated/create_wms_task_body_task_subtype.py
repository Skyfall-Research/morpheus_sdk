from enum import Enum


class CreateWMSTaskBodyTaskSubtype(str, Enum):
    BATCH = "BATCH"
    CLUSTER = "CLUSTER"
    DISCRETE = "DISCRETE"
    ZONE = "ZONE"

    def __str__(self) -> str:
        return str(self.value)
