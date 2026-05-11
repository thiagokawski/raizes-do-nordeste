from sqlalchemy import Boolean, Column, ForeignKey, Integer, Text, Time, false
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.infrastructure.database.base import Base


class RefreshTokenModel(Base):
    __tablename__ = "refreshtokens"

    id_refresh = Column(Integer, primary_key=True, autoincrement=True)
    id_user = Column(
        Integer,
        ForeignKey(
            "users.id_user",
            name="fk_refreshtokens_users",
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    refresh_token = Column(Text, nullable=False, unique=True)
    expires_at = Column(Time, nullable=False)
    revoked = Column(Boolean, nullable=False, server_default=false())
    created_at = Column(Time, nullable=False, server_default=func.current_time())

    user = relationship("UserModel", back_populates="refresh_tokens")
