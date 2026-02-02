from enum import Enum


class GetODsOdType(str, Enum):
    BACKGROUND_JOB = "background_job"
    STANDARD = "standard"
    WORKFLOW = "workflow"

    def __str__(self) -> str:
        return str(self.value)
