from Fish import Fish 
from Date import Date

class FreshFish(Fish):
    def __init__(self, when_it_was_delivered: Date = None):
        self.when_it_was_delivered = when_it_was_delivered