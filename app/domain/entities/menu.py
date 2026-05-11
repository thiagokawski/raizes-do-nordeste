from dataclasses import dataclass, field

from app.domain.entities.menu_items import MenuItem

@dataclass
class Menu:
    id_menu: int
    name: str
    active: bool
    items: list[MenuItem] = field(default_factory=list)
