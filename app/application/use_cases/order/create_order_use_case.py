from fastapi import status

from app.api.v1.schemas.order_schema import CreateOrderReq, OrderResponse
from app.core.handler.exception_app_exception import AppException
from app.domain.repositories.order_repository import OrderRepository


class CreateOrderUseCase:

    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(self, id_user: int, items: list[CreateOrderReq]) -> OrderResponse:
        if not items:
            raise AppException(
                status_code=status.HTTP_400_BAD_REQUEST,
                message="Pedido inválido, informe pelo menos um item"
            )

        ids_items = [item.id_item for item in items]

        if not self.order_repository.exists_menu_items(ids_items):
            raise AppException(
                status_code=status.HTTP_404_NOT_FOUND,
                message="Um ou mais itens do cardápio não foram encontrados"
            )

        order = self.order_repository.create(
            id_user=id_user,
            items=[
                (item.id_item, item.amount)
                for item in items
            ],
        )

        return OrderResponse(
            id_order=order.id_order,
            price=order.price,
            status=order.status,
            source=order.source,
        )
