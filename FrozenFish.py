from Fish import Fish
from Enum_types import Freezing

class FrozenFish(Fish):
    def __init__(self, type_of_freezing: Freezing):
        self.type_of_freezing = type_of_freezing