from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base


class CompanyModel(Base):
    __tablename__ = "companies"

    id_company = Column(Integer, primary_key=True, autoincrement=True)
    serial_branch = Column(Integer, nullable=False)

    address = relationship(
        "AddressModel",
        back_populates="company",
        cascade="all, delete-orphan",
        uselist=False,
    )
    employees = relationship(
        "EmployeeModel",
        back_populates="company",
        cascade="all, delete-orphan",
    )
    menus = relationship(
        "MenuModel",
        back_populates="company",
        cascade="all, delete-orphan",
    )
