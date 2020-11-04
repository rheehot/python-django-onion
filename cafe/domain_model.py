from dataclasses import dataclass

from cafe.models import Order, Cafe, Customer


@dataclass
class CafeDomainModel:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @classmethod
    def of(cls, cafe: Cafe):
        return cls(id=cafe.id, name=cafe.name)


@dataclass
class CustomerDomainModel:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    @classmethod
    def of(cls, customer: Customer):
        return cls(id=customer.id, name=customer.name)


@dataclass
class OrderDomainModel:
    id: int
    cafe_id: int
    customer_id: int

    def __init__(self, id: int, cafe_id: int, customer_id: int):
        self.id = id
        self.cafe_id = cafe_id
        self.customer_id = customer_id

    @classmethod
    def of(cls, order: Order):
        return cls(id=order.id, customer_id=order.customer_id, cafe_id=order.cafe_id)
