from enum import Enum


class GetAllERPProductsStatus(str, Enum):
    ACTIVE = "ACTIVE"
    DISCONTINUED = "DISCONTINUED"

    def __str__(self) -> str:
        return str(self.value)
