from sqlalchemy import Column, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, Table

from app.infrastructure.database.base import Base

users_roles = Table(
    "users_roles",
    Base.metadata,
    Column("id_user", Integer, nullable=False),
    Column("id_role", Integer, nullable=False),
    PrimaryKeyConstraint("id_user", "id_role"),
    ForeignKeyConstraint(
        ["id_user"],
        ["users.id_user"],
        name="fk_users_roles_users",
        ondelete="CASCADE",
    ),
    ForeignKeyConstraint(
        ["id_role"],
        ["roles.id_role"],
        name="fk_users_roles_roles",
        ondelete="CASCADE",
    ),
)

roles_permissions = Table(
    "roles_permissions",
    Base.metadata,
    Column("id_role", Integer, nullable=False),
    Column("id_permission", Integer, nullable=False),
    PrimaryKeyConstraint("id_role", "id_permission"),
    ForeignKeyConstraint(
        ["id_role"],
        ["roles.id_role"],
        name="fk_roles_permissions_roles",
        ondelete="CASCADE",
    ),
    ForeignKeyConstraint(
        ["id_permission"],
        ["permissions.id_permission"],
        name="fk_roles_permissions_permissions",
        ondelete="CASCADE",
    ),
)
