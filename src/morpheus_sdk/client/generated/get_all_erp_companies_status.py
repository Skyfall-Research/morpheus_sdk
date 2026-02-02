from enum import Enum


class GetAllERPCompaniesStatus(str, Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    INACTIVE = "INACTIVE"
    PROSPECT = "PROSPECT"

    def __str__(self) -> str:
        return str(self.value)
