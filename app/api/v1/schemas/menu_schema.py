from pydantic import BaseModel

class MenuResponseBasic(BaseModel):
    id_menu: int
    name: str
    active: bool

class MenuItemResponse(BaseModel):
    id_item: int
    name: str
    ingredients: str | None
    amount: int
    price: float

class MenuResponse(BaseModel):
    id_menu: int
    name: str
    active: bool
    items: list[MenuItemResponse]
