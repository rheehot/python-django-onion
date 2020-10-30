import inject

from cafe.models import Cafe, Order


# class OrderCoffeeService:
#     # same as usecase
#     def order_coffee(self, cafe_id: int, customer_id: int):
#         cafe = Cafe.objects.get(pk=cafe_id)
#         order = Order.objects.create(cafe_id=cafe.id, customer_id=customer_id)
#         order.save()
from cafe.object_service import CafeRepository


class OrderCoffeeService:
    # same as usecase
    @inject.autoparams('cafe_repository')
    def __init__(self, cafe_repository: CafeRepository):
        self._cafe_repository = cafe_repository

    def order_coffee(self, cafe_id: int, customer_id: int):
        cafe = Cafe.objects.get(pk=cafe_id)
        order = Order.objects.create(cafe_id=cafe.id, customer_id=customer_id)
        order.save()


order_coffee_service = OrderCoffeeService()
