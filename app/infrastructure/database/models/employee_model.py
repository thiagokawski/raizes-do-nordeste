from sqlalchemy import Column, Enum as SQLEnum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.enums import PositionEmploy


class EmployeeModel(Base):
    __tablename__ = "employees"

    id_employ = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(
        Integer,
        ForeignKey(
            "users.id_user",
            name="fk_employees_users",
            ondelete="CASCADE",
        ),
        nullable=False,
        unique=True,
    )
    id_company = Column(
        Integer,
        ForeignKey(
            "companies.id_company",
            name="fk_employees_companies",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    position = Column(SQLEnum(PositionEmploy, name="position_employ"), nullable=False)

    user = relationship("UserModel", back_populates="employee")
    company = relationship("CompanyModel", back_populates="employees")
