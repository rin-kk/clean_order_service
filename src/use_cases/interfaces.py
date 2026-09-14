from abc import ABC, abstractmethod
from typing import Optional
from src.domain.models import Order


class IOrderRepository(ABC):


    @abstractmethod
    def save(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Optional[Order]:
        pass