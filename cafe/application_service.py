from cafe.domain_model import OrderDomainModel
from cafe.models import Order
from cafe.object_service import CafeObjectService, OrderObjectService, order_object_service


class OrderCoffeeService:
    def __init__(self, cafe_object_service: CafeObjectService = None):
        self.cafe_object_service = cafe_object_service

    def order_coffee(self, cafe_id: int, customer_id: int):
        order = Order.objects.create(cafe_id=cafe_id, customer_id=customer_id)
        order.save()


class OrderService:
    def __init__(self, order_object_service: OrderObjectService = None):
        self.order_object_service = order_object_service

    def get_order(self, order_id: int) -> OrderDomainModel:
        order = self.order_object_service.get(order_id)
        return OrderDomainModel.of(order)


order_coffee_service = OrderCoffeeService()
order_service = OrderService(order_object_service=order_object_service)
