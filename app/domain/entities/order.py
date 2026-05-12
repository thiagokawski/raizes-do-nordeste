from dataclasses import dataclass, field

from app.domain.entities.order_item import OrderItem

@dataclass
class Order:
    id_order: int
    id_user: int
    price: float
    status: str
    source: str
    items: list[OrderItem] = field(default_factory=list)
