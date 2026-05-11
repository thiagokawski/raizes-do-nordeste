from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.menu import Menu

class MenuRepository(ABC):

    @abstractmethod
    def find_all(self) -> list[Menu]:
        pass
    
    @abstractmethod
    def find_by_id_menu(self, id_menu: int) -> Optional[Menu]:
        pass

    @abstractmethod
    def find_by_id_company(self, id_company: int) -> list[Menu]:
        pass
