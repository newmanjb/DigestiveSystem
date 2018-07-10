from abc import ABC, abstractmethod
import time
from enum import Enum
from com.noomtech.building_blocks import Transportable

"""Higher level objects used to define the consumables i.e. anything that can be eaten
"""

class Consumable(ABC):

    """Anything that can be eaten"""

    @abstractmethod
    def digest(self):
        pass

class Drink(Consumable, Transportable):

    """Any liquid consumable"""

    def onMove(self):
        pass

class Food(Consumable, Transportable, ABC) :

    """Any solid consumable.  Subclasses must define how long it takes to chew and digest the food"""

    def __init__(self):
        self.state = FoodState.UNTOUCHED

    def chew(self):
        time.sleep(self.chewTime)
        self.state = FoodState.CHEWED

    def digest(self):
        time.sleep(self.digestTime)
        self.state = FoodState.DIGESTED

    def onMove(self):
        pass

    @abstractmethod
    def preDigest(self):
        pass

    @abstractmethod
    def postDigest(self):
        pass

class FoodState(Enum):

    """Defines the current state of a food"""

    UNTOUCHED = 1
    CHEWED = 2
    BROKEN_DOWN = 3
