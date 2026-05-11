from fastapi import status

from app.api.v1.schemas.menu_schema import MenuItemResponse, MenuResponse
from app.core.handler.exception_app_exception import AppException
from app.domain.repositories.menu_repository import MenuRepository


class GetMenuByIdUseCase:

    def __init__(self, menu_repository: MenuRepository):
        self.menu_repository = menu_repository

    def execute(self, id_menu: int) -> MenuResponse:
        menu = self.menu_repository.find_by_id_menu(id_menu)

        if not menu:
            raise AppException(
                status_code=status.HTTP_404_NOT_FOUND,
                message="Cardápio não encontrado"
            )

        return MenuResponse(
            id_menu=menu.id_menu,
            name=menu.name,
            active=menu.active,
            items=[
                MenuItemResponse(
                    id_item=item.id_item,
                    name=item.name,
                    ingredients=item.ingredients,
                    amount=item.amount,
                    price=item.price,
                )
                for item in menu.items
            ],
        )
