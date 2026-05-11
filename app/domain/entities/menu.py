from dataclasses import dataclass

@dataclass
class Menu:
    id_menu: int
    name: str
    active: bool