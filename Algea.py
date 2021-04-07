from ClassItems import Items
from Enum_types import Kind

class Algea(Items):
    def __init__(self, proteins_in_grams: float, kind_of_algae: Kind):
        self.proteins_in_grams = proteins_in_grams
        self.kind_of_algae = kind_of_algae
