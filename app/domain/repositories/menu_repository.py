from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.user import User

class MenuRepository(ABC):

    @abstractmethod
    def find_all(self) -> Optional[User]:
        pass
    
    @abstractmethod
    def find_by_id_menu(self, id_menu: int) -> Optional[User]:
        pass

    @abstractmethod
    def find_by_id_company(self, id_company: int) -> Optional[User]:
        pass