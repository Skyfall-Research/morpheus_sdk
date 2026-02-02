from enum import Enum


class GetRandomERPCompanyType(str, Enum):
    MPC = "mpc"
    NPC = "npc"

    def __str__(self) -> str:
        return str(self.value)
