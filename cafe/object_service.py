import abc
from typing import NoReturn

from cafe.models import Cafe, Order


class ObjectService(abc.ABC):
    @abc.abstractmethod
    def get(self, cafe_id: int):
        pass

    @abc.abstractmethod
    def save(self, cafe: Cafe):
        pass


class CafeObjectService(ObjectService):
    def get(self, cafe_id: int) -> Cafe:
        return Cafe.objects.get(pk=cafe_id)

    def save(self, cafe: Cafe) -> NoReturn:
        cafe.save()


class OrderObjectService(ObjectService):
    def get(self, order_id: int) -> Cafe:
        return Order.objects.get(pk=order_id)

    def save(self, order: Order) -> NoReturn:
        order.save()
