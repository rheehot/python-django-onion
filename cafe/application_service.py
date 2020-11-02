import inject

from cafe.models import Order
from cafe.object_service import CafeObjectService


class OrderCoffeeService:
    @inject.autoparams('cafe_repository')
    def __init__(self, cafe_object_service: CafeObjectService):
        self._cafe_object_service = cafe_object_service

    def order_coffee(self, cafe_id: int, customer_id: int):
        order = Order.objects.create(cafe_id=cafe_id, customer_id=customer_id)
        order.save()


order_coffee_service = OrderCoffeeService()
