from enum import Enum


class GetKnowledgeGraphResponse200DataEdgesItemType(str, Enum):
    CAN_PERFORM = "can_perform"
    EXPOSED_BY = "exposed_by"
    IMPLEMENTED_BY = "implemented_by"
    MODIFIES = "modifies"
    PRODUCES = "produces"
    REQUIRES = "requires"
    USES = "uses"

    def __str__(self) -> str:
        return str(self.value)
