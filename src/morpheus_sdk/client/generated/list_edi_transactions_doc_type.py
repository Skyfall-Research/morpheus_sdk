from enum import Enum


class ListEdiTransactionsDocType(str, Enum):
    VALUE_0 = "850"
    VALUE_1 = "855"
    VALUE_2 = "856"
    VALUE_3 = "810"
    VALUE_4 = "820"
    VALUE_5 = "997"
    VALUE_6 = "999"

    def __str__(self) -> str:
        return str(self.value)
