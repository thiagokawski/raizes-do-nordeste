from dataclasses import dataclass

@dataclass
class Order:
    id_order: int
    price: float
    status: int