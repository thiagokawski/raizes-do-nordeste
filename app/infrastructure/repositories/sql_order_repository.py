from decimal import Decimal
from typing import Optional

from sqlalchemy.orm import Session, joinedload

from app.domain.entities.order import Order
from app.domain.entities.order_item import OrderItem
from app.domain.repositories.order_repository import OrderRepository
from app.infrastructure.database.models import MenuItemModel, OrderItemModel, OrderModel
from app.infrastructure.database.models.enums import SourceOrders, StatusOrders


class SqlOrderRepository(OrderRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, id_user: int, items: list[tuple[int, int]]) -> Order:
        ids_items = [id_item for id_item, _ in items]
        menu_items = (
            self.db.query(MenuItemModel)
            .filter(MenuItemModel.id_item.in_(ids_items))
            .all()
        )
        menu_items_by_id = {
            menu_item.id_item: menu_item
            for menu_item in menu_items
        }

        order_model = OrderModel(
            id_user=id_user,
            price=Decimal("0.00"),
            status=StatusOrders.AGUARDANDO_PAGAMENTO,
            source=SourceOrders.APP,
        )

        self.db.add(order_model)
        self.db.flush()

        order_total = Decimal("0.00")

        for id_item, amount in items:
            menu_item = menu_items_by_id[id_item]
            price_unit = Decimal(menu_item.price)
            price_total = price_unit * amount
            order_total += price_total

            self.db.add(
                OrderItemModel(
                    id_order=order_model.id_order,
                    id_item=id_item,
                    amount=amount,
                    price_unit=price_unit,
                    price_total=price_total,
                )
            )

        order_model.price = order_total
        self.db.commit()
        self.db.refresh(order_model)

        return self._to_entity(order_model)

    def find_by_id_order_and_user(
        self,
        id_order: int,
        id_user: int
    ) -> Optional[Order]:
        order_model = (
            self.db.query(OrderModel)
            .options(joinedload(OrderModel.items))
            .filter(
                OrderModel.id_order == id_order,
                OrderModel.id_user == id_user,
            )
            .first()
        )

        if not order_model:
            return None

        return self._to_entity(order_model)

    def update_status(
        self,
        id_order: int,
        status: str
    ) -> Order:
        order_model = (
            self.db.query(OrderModel)
            .filter(OrderModel.id_order == id_order)
            .first()
        )

        order_model.status = status
        self.db.commit()
        self.db.refresh(order_model)

        return self._to_entity(order_model)

    def exists_menu_items(self, ids_items: list[int]) -> bool:
        total_items = (
            self.db.query(MenuItemModel)
            .filter(MenuItemModel.id_item.in_(ids_items))
            .count()
        )

        return total_items == len(set(ids_items))

    def _to_entity(self, order_model: OrderModel) -> Order:
        return Order(
            id_order=order_model.id_order,
            id_user=order_model.id_user,
            price=float(order_model.price),
            status=self._enum_value(order_model.status),
            source=self._enum_value(order_model.source),
            items=[
                OrderItem(
                    id_order_item=item.id_order_item,
                    id_order=item.id_order,
                    id_item=item.id_item,
                    amount=item.amount,
                    price_unit=float(item.price_unit),
                    price_total=float(item.price_total),
                )
                for item in order_model.items
            ],
        )

    def _enum_value(self, value: str) -> str:
        if hasattr(value, "value"):
            return value.value

        return value
