from fastapi import status

from app.core.handler.exception_app_exception import AppException
from app.domain.repositories.order_repository import OrderRepository


class UpdateStatusOrderUseCase:

    def __init__(self, order_repository: OrderRepository):
        self.order_repository = order_repository

    def execute(
        self,
        id_order: int,
        id_user: int,
        new_status: str
    ) -> str:
        order = self.order_repository.find_by_id_order_and_user(
            id_order=id_order,
            id_user=id_user
        )

        if not order:
            raise AppException(
                status_code=status.HTTP_404_NOT_FOUND,
                message="Pedido não encontrado"
            )

        order = self.order_repository.update_status(
            id_order=id_order,
            status=new_status
        )

        return order.status
