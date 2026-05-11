from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base


class MenuItemModel(Base):
    __tablename__ = "menuitems"

    id_item = Column(Integer, primary_key=True, autoincrement=True)
    id_menu = Column(
        Integer,
        ForeignKey(
            "menus.id_menu",
            name="fk_menuitems_menus",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    name = Column(String(255), nullable=False)
    ingredients = Column(Text, nullable=True)
    amount = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2), nullable=False)

    menu = relationship("MenuModel", back_populates="items")
    order_items = relationship("OrderItemModel", back_populates="menu_item")
