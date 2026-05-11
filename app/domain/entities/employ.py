from dataclasses import dataclass

@dataclass
class Employ:
    id_employ: int
    id_user: int
    id_company: int
    position: str