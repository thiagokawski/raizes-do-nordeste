from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.user import User

class UserRepository(ABC):

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        pass