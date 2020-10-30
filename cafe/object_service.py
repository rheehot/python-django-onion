import abc
from typing import NoReturn

from cafe.models import Cafe


class Repository(abc.ABC):
    # cafe interface
    @abc.abstractmethod
    def get(self, cafe_id: int):
        pass

    @abc.abstractmethod
    def save(self, cafe: Cafe):
        pass


class CafeRepository(Repository):
    def get(self, cafe_id: int) -> Cafe:
        return Cafe.objects.get(pk=cafe_id)

    def save(self, cafe: Cafe) -> NoReturn:
        cafe.save()
