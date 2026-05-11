from sqlalchemy import Column, Enum as SQLEnum, ForeignKey, Integer, Numeric
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.enums import StatusOrders


class OrderModel(Base):
    __tablename__ = "orders"

    id_order = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(
        Integer,
        ForeignKey(
            "users.id_user",
            name="fk_orders_users",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    price = Column(Numeric(10, 2), nullable=False)
    status = Column(
        SQLEnum(StatusOrders, name="status_orders"),
        nullable=False,
        server_default=StatusOrders.AGUARDANDO_PAGAMENTO.value,
    )

    user = relationship("UserModel", back_populates="orders")
    items = relationship(
        "OrderItemModel",
        back_populates="order",
        cascade="all, delete-orphan",
    )
