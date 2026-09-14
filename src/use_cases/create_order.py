from typing import List, Dict, Any
from src.domain.models import Order, OrderItem
from src.use_cases.interfaces import IOrderRepository


class CreateOrderUseCase:


    def __init__(self, order_repo: IOrderRepository):
        self._order_repo = order_repo

    def execute(self, order_id: str, raw_items: List[Dict[str, Any]]) -> Dict[str, Any]:
        items = [
            OrderItem(
                item_id=i["id"],
                title=i["title"],
                price=float(i["price"]),
                quantity=int(i["quantity"])
            )
            for i in raw_items
        ]
        order = Order(order_id=order_id, items=items)
        self._order_repo.save(order)
        return {
            "order_id": order.order_id,
            "subtotal": order.calculate_subtotal(),
            "final_amount": order.calculate_final_amount(),
            "items_count": len(order.items),
            "status": "CREATED"
        }