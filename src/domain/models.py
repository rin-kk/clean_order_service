from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class OrderItem:
    item_id: str
    title: str
    price: float
    quantity: int

    @property
    def total_price(self) -> float:
        return self.price * self.quantity


class Order:
    def __init__(self, order_id: str, items: List[OrderItem]):
        if not items:
            raise ValueError("Заказ не может быть пустым.")
        self.order_id = order_id
        self._items = items

    @property
    def items(self) -> List[OrderItem]:
        return list(self._items)

    def calculate_subtotal(self) -> float:
        return sum(item.total_price for item in self._items)

    def calculate_final_amount(self) -> float:

        subtotal = self.calculate_subtotal()
        if subtotal >= 5000.0:
            return round(subtotal * 0.90, 2)
        return round(subtotal, 2)