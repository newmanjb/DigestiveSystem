from abc import ABC, abstractmethod

"""The higher level objects used to form the components of the body"""


class Producer(ABC):

    """Producer is anything that produces an object that can be transported or moved e.g. the mouth
    producing chewed food or the stomach producing digested food.
    """

    @abstractmethod
    def deliverProduce(self,transportable):
        pass

class Transportable(ABC) :

    """Transportable represents an object that can be moved e.g chewed or digested food from the above
    example"""


    @abstractmethod
    def move(self):
        pass
