from typing import Dict, Optional
from src.domain.models import Order
from src.use_cases.interfaces import IOrderRepository


class InMemoryOrderRepository(IOrderRepository):

    def __init__(self):
        self._storage: Dict[str, Order] = {}

    def save(self, order: Order) -> None:
        self._storage[order.order_id] = order

    def get_by_id(self, order_id: str) -> Optional[Order]:
        return self._storage.get(order_id)