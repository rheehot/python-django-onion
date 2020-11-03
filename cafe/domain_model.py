from dataclasses import dataclass

from cafe.models import Order


@dataclass
class Cafe:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


@dataclass
class Customer:
    id: int
    name: str

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


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
