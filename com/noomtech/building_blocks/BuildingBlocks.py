from abc import ABC, abstractmethod
from time import sleep
import threading

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
    def onMove(self):
        pass

class Receiver(ABC):
    """
    Anything that can receive a transportable object e.g. a pipe
    """
    @abstractmethod
    def receive(self, transportable):
        pass


class Pipe(Receiver,Producer):
    """
    Moves transportable instances from one end to the other in a configured time.  Once items have been moved along the
    pipe they are delivered to a receiver instance
    """

    def __init__(self, transportTime):
        self.transportTime = transportTime
        self.content = []

    def start(self):
        self.isAlive = True
        threading.Thread(target=self.move,daemon=False,name="Pipe content mover").start()

    def stop(self):
        self.isAlive = False

    def receive(self, transportableList):
        #Add a pair to the pipe content which consists of the object to be transported and how long it has got left until
        #it has been moved through the pipe
        [self.content.append([self.transportTime, x]) for x in transportableList]

    def deliverProduce(self,transportableList):
        [print("Delivering " + str(x)) for x in transportableList]
        self.receiverA.receive(transportableList)

    def move(self):

        #Every second, check how long each object to be transported has been in the pipe.  If it has reached the required
        # time then it can be delivered to the other end
        while self.isAlive:
            toBeDelivered = []
            sleep(1)
            for idx, transportingList in enumerate(self.content):
                time = transportingList[0]
                transportable = transportingList[1]
                transportable.onMove
                if time == 1:
                    toBeDelivered.append(transportable)
                    self.content.remove(transportingList)
                else :
                    transportingList[0] = time - 1

            if len(toBeDelivered) > 0:
                self.deliverProduce(toBeDelivered)
