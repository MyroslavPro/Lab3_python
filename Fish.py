from ClassItems import Items
from Enum_types import Type
from Date import Date

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