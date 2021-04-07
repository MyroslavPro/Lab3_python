from enum import Enum, auto


class Type(Enum):
    Sea = auto()
    FreshWater = auto()
    Ocean = auto()


class Freezing(Enum):
    Natural = auto()
    Unnatural = auto()


class Kind(Enum):
    Red = auto()
    Green = auto()
    Brown = auto()


class Order(Enum):
    ASC = auto()
    DESC = auto()
