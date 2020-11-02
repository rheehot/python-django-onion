from dataclasses import dataclass


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
