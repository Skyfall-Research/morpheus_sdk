from enum import Enum


class GetWorldScheduleStatusResponse200DataStatus(str, Enum):
    OPERATIONAL = "operational"
    PARTIAL = "partial"
    PAUSED = "paused"

    def __str__(self) -> str:
        return str(self.value)
