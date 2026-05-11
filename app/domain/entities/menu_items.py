from dataclasses import dataclass

@dataclass
class MenuItem:
    id_item: int
    name: str
    ingredients: str
    amount: int
    price: float