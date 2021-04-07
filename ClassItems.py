class Items:
    def __init__(self, name: str = "NoName", price: float = 0.0, country: str = None, provider: str = None):
        self.name = name
        self.price = price
        self.country = country
        self.provider = provider