from enum import Enum


class GetKnowledgeGraphResponse200DataNodesItemType(str, Enum):
    CAPABILITY = "CAPABILITY"
    ENTITY = "ENTITY"
    OD = "OD"
    PERSONA = "PERSONA"
    SERVICE = "SERVICE"
    TOOL = "TOOL"

    def __str__(self) -> str:
        return str(self.value)
