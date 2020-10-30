from cafe.models import Cafe, Order


class OrderCoffeeService:
    # same as usecase
    def order_coffee(self, cafe_id: int, customer_id: int):
        cafe = Cafe.objects.get(pk=cafe_id)
        order = Order.objects.create(cafe_id=cafe.id, customer_id=customer_id)
        order.save()
