from dataclasses import dataclass 
from typing import Literal

@dataclass
class ClientDeps:
    name: str 
    goal: str
    experience_lvl: Literal["beginner", "intermediate", "advances"] = "beginner"
    weekly_hours: int = 8
    current_role: str | None = None
