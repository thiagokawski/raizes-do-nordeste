from sqlalchemy import Column, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base


class OrderItemModel(Base):
    __tablename__ = "orderitems"

    id_order_item = Column(Integer, primary_key=True, autoincrement=True)
    id_order = Column(
        Integer,
        ForeignKey(
            "orders.id_order",
            name="fk_orderitems_orders",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    id_item = Column(
        Integer,
        ForeignKey("menuitems.id_item", name="fk_orderitems_menuitems"),
        nullable=False,
    )
    amount = Column(Integer, nullable=False)
    price_unit = Column(Numeric(10, 2), nullable=False)
    price_total = Column(Numeric(10, 2), nullable=False)

    order = relationship("OrderModel", back_populates="items")
    menu_item = relationship("MenuItemModel", back_populates="order_items")
