from src.infrastructure.memory_repo import InMemoryOrderRepository
from src.use_cases.create_order import CreateOrderUseCase


def main():
    repository = InMemoryOrderRepository()
    use_case = CreateOrderUseCase(order_repo=repository)

    cart = [
        {"id": "A101", "title": "Клавиатура механическая", "price": 3200.0, "quantity": 1},
        {"id": "A102", "title": "Мышь оптическая", "price": 2400.0, "quantity": 1}
    ]

    result = use_case.execute(order_id="ORD-2026-001", raw_items=cart)

    print("=== Результат выполнения Use Case ===")
    print(f"ID Заказа: {result['order_id']}")
    print(f"Количество позиций: {result['items_count']}")
    print(f"Сумма без скидки: {result['subtotal']} руб.")
    print(f"Итого к оплате: {result['final_amount']} руб. (скидка 10% при заказе >= 5000)")
    print(f"Статус: {result['status']}")


if __name__ == "__main__":
    main()