import abc
from typing import NoReturn

from cafe.models import Cafe, Order


class DomainService(abc.ABC):
    @abc.abstractmethod
    def get(self, pk: int):
        pass

    @abc.abstractmethod
    def save(self, arg):
        pass


class CafeDomainService(DomainService):
    def get(self, pk: int) -> Cafe:
        return Cafe.objects.get(pk=pk)

    def save(self, cafe: Cafe) -> NoReturn:
        cafe.save()


class OrderDomainService(DomainService):
    def get(self, order_id: int) -> Order:
        try:
            return Order.objects.get(pk=order_id)
        except Order.DoesNotExist:
            raise Exception('Order Does not exist')

    def save(self, order: Order) -> NoReturn:
        order.save()


cafe_domain_service = CafeDomainService()
order_domain_service = OrderDomainService()
