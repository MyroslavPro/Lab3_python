from Fish import Fish
from Enum_types import Order,Type,Kind,Freezing
from Date import Date
from ShopManager import ShopManager
import unittest

class TestShopManager(unittest.TestCase):
    def setUp(self):
        self.salmon = Fish("Salmon", 15.0, "China", "ChinaFish", Type.FreshWater)
        self.ocynb = Fish("Okynb",12.0,"China", "ChinaTown",Type.FreshWater)
        self.fugu = Fish("Fugu",6.0,"Japan", "JapanFishInc",Type.Sea)

        list_of_fishes = [self.salmon,self.ocynb,self.fugu]

        self.price_max = 55
        self.price_min = 10
        self.type_of_tested_fish = Type.FreshWater

        self.tested_manager= ShopManager(list_of_fishes)
    
    def test_sort_by_name(self):
        res = self.tested_manager.sort_by_name()
        self.assertEqual(res,[self.fugu,self.ocynb,self.salmon])
    
    def test_sort_by_price(self):
        result= self.tested_manager.sort_by_price(Order.ASC)
        self.assertEqual(result,[self.salmon,self.ocynb,self.fugu])
    
    def test_search_by_price(self):
        result= self.tested_manager.search_fish_by_price(self.price_min,self.price_max)
        self.assertEqual(result,[self.salmon,self.ocynb])
    
    def test_search_by_type(self):
        result= self.tested_manager.search_fish_by_type(self.type_of_tested_fish)
        self.assertEqual(result,[self.salmon,self.ocynb])
    
    def tearDown(self):
        print("Done")


if __name__ == "__main__":
    unittest.main()
