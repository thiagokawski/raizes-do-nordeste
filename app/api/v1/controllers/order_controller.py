from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.api.v1.dependencies.auth_dependencies import get_current_user
from app.api.v1.schemas.api_default_schema import ResponseDefault
from app.api.v1.schemas.order_schema import CreateOrderReq, OrderResponse
from app.application.use_cases.order.create_order_use_case import CreateOrderUseCase
from app.application.use_cases.order.get_status_order_use_case import GetStatusOrderUseCase
from app.application.use_cases.order.update_status_order_use_case import UpdateStatusOrderUseCase
from app.domain.entities.user import User
from app.infrastructure.database.database_connection import get_db
from app.infrastructure.database.models.enums import StatusOrders
from app.infrastructure.repositories.sql_order_repository import SqlOrderRepository

router = APIRouter(
    prefix="/orders",
    tags=["ORDER"]
)

@router.post(
        "", 
        response_model=ResponseDefault[OrderResponse],
        status_code=status.HTTP_201_CREATED,
    )
def create_order(
    order: list[CreateOrderReq],
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    use_case = CreateOrderUseCase(
        order_repository=SqlOrderRepository(db)
    )

    return ResponseDefault.created(
        data=use_case.execute(
            id_user=current_user.id_user,
            items=order
        ),
        message="Pedido criado com sucesso!"
    )


@router.put(
        "/{id_order}/status", 
        response_model=ResponseDefault[StatusOrders],
    )
def update_status_order(
    id_order: int,
    new_status: StatusOrders = Query(alias="status"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    use_case = UpdateStatusOrderUseCase(
        order_repository=SqlOrderRepository(db)
    )

    return ResponseDefault.success(
        data=use_case.execute(
            id_order=id_order,
            id_user=current_user.id_user,
            new_status=new_status
        ),
        message="Status do pedido atualizado com sucesso!"
    )


@router.get(
        "/{id_order}/status", 
        response_model=ResponseDefault[StatusOrders],
    )
def get_status_order(
    id_order: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    use_case = GetStatusOrderUseCase(
        order_repository=SqlOrderRepository(db)
    )

    return ResponseDefault.success(
        data=use_case.execute(
            id_order=id_order,
            id_user=current_user.id_user
        ),
        message="Status do pedido retornado com sucesso!"
    )
