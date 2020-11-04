from cafe.domain_model import OrderDomainModel
from cafe.domain_service import OrderDomainService, CafeDomainService, order_domain_service
from cafe.models import Order


class OrderCoffeeService:
    def __init__(self, cafe_domain_service: CafeDomainService = None):
        self.cafe_domain_service = cafe_domain_service

    def order_coffee(self, cafe_id: int, customer_id: int):
        order = Order.objects.create(cafe_id=cafe_id, customer_id=customer_id)
        order.save()


class OrderService:
    def __init__(self, order_domain_service: OrderDomainService = None):
        self.order_domain_service = order_domain_service

    def get_order(self, order_id: int) -> OrderDomainModel:
        order = self.order_domain_service.get(order_id)
        return OrderDomainModel.of(order)


order_coffee_service = OrderCoffeeService()
order_service = OrderService(order_domain_service=order_domain_service)
