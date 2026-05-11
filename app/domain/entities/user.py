from dataclasses import dataclass

@dataclass
class User:
    id_user: int
    name: str
    email: str
    password: str
    active: bool