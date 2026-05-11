from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.associations import users_roles, roles_permissions


class RoleModel(Base):
    __tablename__ = "roles"

    id_role = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)

    users = relationship(
        "UserModel",
        secondary=users_roles,
        back_populates="roles"
    )

    permissions = relationship(
        "PermissionModel",
        secondary=roles_permissions,
        back_populates="roles"
    )
