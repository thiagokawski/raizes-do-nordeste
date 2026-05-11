from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, true
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base


class MenuModel(Base):
    __tablename__ = "menus"

    id_menu = Column(Integer, primary_key=True, autoincrement=True)
    id_company = Column(
        Integer,
        ForeignKey(
            "companies.id_company",
            name="fk_menus_companies",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    name = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False, server_default=true())

    company = relationship("CompanyModel", back_populates="menus")
    items = relationship(
        "MenuItemModel",
        back_populates="menu",
        cascade="all, delete-orphan",
    )
