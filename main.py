from enum import Enum, auto


class Items:
    def __init__(self, name: str = "NoName", price: float = 0.0, country: str = None, provider: str = None):
        self.name = name
        self.price = price
        self.country = country
        self.provider = provider


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


class Date:
    def __init__(self, date_of_expiration_in_days: int):
        self.date_of_expiration_in_days = date_of_expiration_in_days


class Fish(Items):
    def __init__(self, name: str = "NoName", price: float = 0.0, country: str = None, provider: str = None, type_of_fish: Type = None, origin: str = None, date_of_expiration: Date = None):
        self.name = name
        self.price = price
        self.country = country
        self.provider = provider
        self.type_of_fish = type_of_fish
        self.origin = origin
        self.date_of_expiration = date_of_expiration

    def __str__(self):
        res_items = f"\nName_of_Item: {self.name}\nPrice: {self.price}\nCountry: {self.country}\nOrigin: {self.origin} \nType of Fish: {self.type_of_fish}"
        return res_items


class FrozenFish(Fish):
    def __init__(self, type_of_freezing: Freezing):
        self.type_of_freezing = type_of_freezing


class FreshFish(Fish):
    def __init__(self, when_it_was_delivered: Date = None):
        self.when_it_was_delivered = when_it_was_delivered


class Algea(Items):
    def __init__(self, proteins_in_grams: float, kind_of_algae: Kind):
        self.proteins_in_grams = proteins_in_grams
        self.kind_of_algae = kind_of_algae


class ShopManager:
    def __init__(self, fish: list):
        self.__fish = fish

    def sort_by_price(self, order: Order):
        self.__fish.sort(key=lambda fish: fish.price, reverse=order.value)
        return self.__fish

    def search_fish_by_type(self, type_of_fish: Type):
        found_fish = [fish for fish in self.__fish if fish.type_of_fish == type_of_fish]
        return found_fish

    def search_fish_by_price(self, min_price: float, max_price: float):
        found_fish = [fish for fish in self.__fish if (fish.price <= max_price) and (fish.price >= min_price)]
        return found_fish

    def sort_by_name(self):
        self.__fish.sort(key=lambda fish: fish.name)
        return self.__fish


def main():
    salmon = Fish(name="Salmon", price=15.0, country=None, provider=None, type_of_fish=Type.FreshWater)

    print(salmon)

    list_of_fish = []
    list_of_fish.append(salmon)

    cyprinys = Fish()
    print(cyprinys)

    carassius = Fish(name="second fish", price=999.0, country=None, provider=None, type_of_fish=Type.FreshWater)
    print(carassius)

    list_of_fish.append(cyprinys)
    list_of_fish.append(carassius)

    assistant = ShopManager(list_of_fish)
    print('\nSorted by price:\n\n' + '\n'.join([str(x) for x in assistant.sort_by_price(Order.ASC)]), '\n\n')
    print('\nSorted by name:\n\n' + '\n'.join([str(x) for x in assistant.sort_by_name()]), '\n\n')
    print('Find Fish by required Type:\n\n' + '\n'.join([str(x) for x in assistant.search_fish_by_type(Type.FreshWater)]), '\n\n')
    print('Find Fish by required Price:\n\n' + '\n'.join([str(x) for x in assistant.search_fish_by_price(10, 500)]), '\n\n')


if __name__ == '__main__':
    main()
