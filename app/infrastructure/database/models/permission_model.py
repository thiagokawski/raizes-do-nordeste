from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.infrastructure.database.base import Base
from app.infrastructure.database.models.associations import roles_permissions


class PermissionModel(Base):
    __tablename__ = "permissions"

    id_permission = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=True)

    roles = relationship(
        "RoleModel",
        secondary=roles_permissions,
        back_populates="permissions"
    )
