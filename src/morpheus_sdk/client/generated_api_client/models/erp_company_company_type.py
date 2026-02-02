from enum import Enum


class ERPCompanyCompanyType(str, Enum):
    CUSTOMER = "CUSTOMER"
    INTERNAL = "INTERNAL"
    PARTNER = "PARTNER"
    SUPPLIER = "SUPPLIER"

    def __str__(self) -> str:
        return str(self.value)
