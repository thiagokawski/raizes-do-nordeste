from sqlalchemy import Boolean, Column, Date, Integer, String, true
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.associations import users_roles


class UserModel(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    active = Column(Boolean, nullable=False, server_default=true())
    create_at = Column(Date, nullable=False, server_default=func.current_date())
    update_at = Column(Date, nullable=True)

    roles = relationship(
        "RoleModel",
        secondary=users_roles,
        back_populates="users"
    )
    employee = relationship(
        "EmployeeModel",
        back_populates="user",
        cascade="all, delete-orphan",
        uselist=False,
    )
    orders = relationship(
        "OrderModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )
    refresh_tokens = relationship(
        "RefreshTokenModel",
        back_populates="user",
        cascade="all, delete-orphan",
    )
