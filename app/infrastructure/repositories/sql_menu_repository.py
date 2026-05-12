from typing import Optional
from sqlalchemy.orm import Session, joinedload

from app.domain.entities.menu import Menu
from app.domain.entities.menu_items import MenuItem
from app.domain.repositories.menu_repository import MenuRepository
from app.infrastructure.database.models import MenuModel

class SqlMenuRepository(MenuRepository):

    def __init__(self, db: Session):
        self.db = db

    def find_by_id_menu(self, id_menu: int) -> Optional[Menu]:
        menu_model = (
            self.db.query(MenuModel)
            .options(joinedload(MenuModel.items))
            .filter(MenuModel.id_menu == id_menu)
            .first()
        )

        if not menu_model:
            return None

        return self._to_entity(menu_model)

    def _to_entity(self, menu_model: MenuModel) -> Menu:
        return Menu(
            id_menu=menu_model.id_menu,
            name=menu_model.name,
            active=menu_model.active,
            items=[
                MenuItem(
                    id_item=item.id_item,
                    name=item.name,
                    ingredients=item.ingredients,
                    amount=item.amount,
                    price=float(item.price),
                )
                for item in menu_model.items
            ],
        )
