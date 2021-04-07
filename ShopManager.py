from Fish import Fish
from Enum_types import Order
from Enum_types import Type

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
