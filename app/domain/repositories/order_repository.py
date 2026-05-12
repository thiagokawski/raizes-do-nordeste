from abc import ABC, abstractmethod
from typing import Optional

from app.domain.entities.order import Order


class OrderRepository(ABC):

    @abstractmethod
    def create(self, id_user: int, items: list[tuple[int, int]]) -> Order:
        pass

    @abstractmethod
    def find_by_id_order_and_user(
        self,
        id_order: int,
        id_user: int
    ) -> Optional[Order]:
        pass

    @abstractmethod
    def update_status(
        self,
        id_order: int,
        status: str
    ) -> Order:
        pass

    @abstractmethod
    def exists_menu_items(self, ids_items: list[int]) -> bool:
        pass
