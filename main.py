from Fish import Fish
from Enum_types import Order,Type,Kind,Freezing
from Date import Date
from ShopManager import ShopManager


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

