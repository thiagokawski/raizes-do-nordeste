from dataclasses import dataclass

@dataclass
class MenuItem:
    id_item: int
    name: str
    ingredients: str | None
    amount: int
    price: float
