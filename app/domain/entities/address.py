from dataclasses import dataclass

@dataclass
class Address:
    id_address: int
    id_company: int
    country: str
    state: str
    city: str
    address: str