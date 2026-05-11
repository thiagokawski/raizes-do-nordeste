from typing import Optional
from sqlalchemy.orm import Session

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.database.models import UserModel

class SqlUserRepository(UserRepository):

    def __init__(self, db: Session):
        self.db = db

    def find_by_email(self, email: str) -> Optional[User]:
        user_model = (
            self.db.query(UserModel)
            .join(UserModel.roles)
            .filter(UserModel.email == email)
            .first()
        )

        if not user_model:
            return None

        return User(
            id_user=user_model.id_user,
            name=user_model.name,
            email=user_model.email,
            password=user_model.password,
            active=user_model.active
        )