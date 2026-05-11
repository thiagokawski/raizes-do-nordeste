from dataclasses import dataclass

@dataclass
class Menu:
    id_order_item: int
    id_order: int
    id_item: int
    amount: int
    price_unit: float
    price_total: float